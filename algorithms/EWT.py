#! /usr/bin/env python
# Authors: Christiana Ade, Erik Bolch, Dana Chadwick
# Note: This Python version is fully independent of the original source code.
#
#####################################################################################

# Import Packages
import os
# Some cells may generate warnings that we can ignore. Comment below lines to see.
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import xarray as xr
from osgeo import gdal
import rasterio as rio
import rioxarray as rxr
from matplotlib import pyplot as plt
import hvplot.xarray
import hvplot.pandas
import pandas as pd
import earthaccess

#from modules.emit_tools import emit_xarray
#from modules.ewt_calc import calc_ewt
from scipy.optimize import least_squares 



# https://github.com/isofit/isofit/blob/main/isofit/inversion/inverse_simple.py#L514C1-L532C17
# Function: beer_lambert_model
def beer_lambert_model(x, y, wl, alpha_lw):
    """Function, which computes the vector of residuals between measured and modeled surface reflectance optimizing
    for path length of surface liquid water based on the Beer-Lambert attenuation law.

    Args:
        x:        state vector (liquid water path length, intercept, slope)
        y:        measurement (surface reflectance spectrum)
        wl:       instrument wavelengths
        alpha_lw: wavelength dependent absorption coefficients of liquid water

    Returns:
        resid: residual between modeled and measured surface reflectance
    """

    attenuation = np.exp(-x[0] * 1e7 * alpha_lw)
    rho = (x[1] + x[2] * wl) * attenuation
    resid = rho - y

    return resid



## function to get desired data from csv file 
# https://github.com/isofit/isofit/blob/dev/isofit/core/common.py#L461C1-L488C26
def get_refractive_index(k_wi, a, b, col_wvl, col_k):
    """Convert refractive index table entries to numpy array.

    Args:
        k_wi:    variable
        a:       start line
        b:       end line
        col_wvl: wavelength column in pandas table
        col_k:   k column in pandas table

    Returns:
        wvl_arr: array of wavelengths
        k_arr:   array of imaginary parts of refractive index
    """

    wvl_ = []
    k_ = []

    for ii in range(a, b):
        wvl = k_wi.at[ii, col_wvl]
        k = k_wi.at[ii, col_k]
        wvl_.append(wvl)
        k_.append(k)

    wvl_arr = np.asarray(wvl_)
    k_arr = np.asarray(k_)
 


# Lastly, to calculate CWC we define a function that uses least squares optimization to minimize the residuals of our Beer-Lambert Model and find a likely path length of liquid water. 
 # https://github.com/isofit/isofit/blob/main/isofit/inversion/inverse_simple.py#L443C1-L511C24
def invert_liquid_water(
    rfl_meas: np.array,
    wl: np.array,
    l_shoulder: float = 850,
    r_shoulder: float = 1100,
    lw_init: tuple = (0.02, 0.3, 0.0002),
    lw_bounds: tuple = ([0, 0.5], [0, 1.0], [-0.0004, 0.0004]),
    ewt_detection_limit: float = 0.5,
    return_abs_co: bool = False,
):
    """Given a reflectance estimate, fit a state vector including liquid water path length
    based on a simple Beer-Lambert surface model.

    Args:
        rfl_meas:            surface reflectance spectrum
        wl:                  instrument wavelengths, must be same size as rfl_meas
        l_shoulder:          wavelength of left absorption feature shoulder
        r_shoulder:          wavelength of right absorption feature shoulder
        lw_init:             initial guess for liquid water path length, intercept, and slope
        lw_bounds:           lower and upper bounds for liquid water path length, intercept, and slope
        ewt_detection_limit: upper detection limit for ewt
        return_abs_co:       if True, returns absorption coefficients of liquid water

    Returns:
        solution: estimated liquid water path length, intercept, and slope based on a given surface reflectance
    """
    
    # Ensure least squares is done with float64 datatype (added)
    wl = np.float64(wl)
    
    # params needed for liquid water fitting
    lw_feature_left = np.argmin(abs(l_shoulder - wl))
    lw_feature_right = np.argmin(abs(r_shoulder - wl))
    wl_sel = wl[lw_feature_left : lw_feature_right + 1]

    # adjust upper detection limit for ewt if specified
    if ewt_detection_limit != 0.5:
        lw_bounds[0][1] = ewt_detection_limit

    # load imaginary part of liquid water refractive index and calculate wavelength dependent absorption coefficient
    # __file__ should live at isofit/isofit/inversion/
    
    
    data_dir_path = "../data/"
    path_k = os.path.join(data_dir_path,"k_liquid_water_ice.csv")
    
    #isofit_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    #path_k = os.path.join(isofit_path, "data", "iop", "k_liquid_water_ice.xlsx")

    # k_wi = pd.read_excel(io=path_k, sheet_name="Sheet1", engine="openpyxl")
    # wl_water, k_water = get_refractive_index(
    #     k_wi=k_wi, a=0, b=982, col_wvl="wvl_6", col_k="T = 20°C"
    # )
    k_wi = pd.read_csv(path_k)
    wl_water, k_water = get_refractive_index(
        k_wi=k_wi, a=0, b=982, col_wvl="wvl_6", col_k="T = 20°C"
    )
    kw = np.interp(x=wl_sel, xp=wl_water, fp=k_water)
    abs_co_w = 4 * np.pi * kw / wl_sel

    rfl_meas_sel = rfl_meas[lw_feature_left : lw_feature_right + 1]

    x_opt = least_squares(
        fun=beer_lambert_model,
        x0=lw_init,
        jac="2-point",
        method="trf",
        bounds=(
            np.array([lw_bounds[ii][0] for ii in range(3)]),
            np.array([lw_bounds[ii][1] for ii in range(3)]),
        ),
        max_nfev=15,
        args=(rfl_meas_sel, wl_sel, abs_co_w),
    )

    solution = x_opt.x

    if return_abs_co:
        return solution, abs_co_w
    else:
        return solution