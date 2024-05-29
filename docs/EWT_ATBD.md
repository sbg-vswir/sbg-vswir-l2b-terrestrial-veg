# SBG VSWIR Terrestrial Vegetation Equivalent Water Thickness Product - Algorithm Theoretical Basis Document (ATBD)**

*K.D. Chadwick**<sup>1</sup>

<sup>1</sup>Jet Propulsion Laboratory, California Institute of Technology

Corresponding author: K. Dana Chadwick (dana.chadwick@jpl.nasa.gov)
K. Dana Chadwick1, Ryan Pavlick, David R. Thompson1, Philip G. Brodrick1, Niklas Bohn1, Regina Eckert1, Robert O. Green1, and others (TBD) 

**Key Points:**
    SBG-VSWIR will produce estimates of equivalent water thickness (EWT) which is often used as an estimate of canopy water content (CWC)  

**Version:** 1.0

**Release Date:** TBD

**DOI:** TBD

## Abstract

The SBG-VSWIR mission level 2+ processing for terrestrial vegetation will estimate canopy water content (CWC) via an equivalent water thickness (EWT) estimation, and vegetation traits nominally via a partial least squares regression strategy.  

## Plain Language Summary
This document describes the strategy for producing terrestrial vegetation gridded products that will be produced by the SBG-VSWIR mission.  The terrestrial vegetation products will be generated for pixels that are determined through the unmixing product (Lxx) to contain sufficient vegetation cover to warrant estimation. Error will be estimated for each product to the best ability to assess. Here we outline the strategy for scaling terrestrial vegetation products

### Keywords: hyperspectral imaging, imaging spectroscopy, atmospheric correction

## 1 Version Description

This is Version 1.0 of the SBG VSWIR terrestrial vegetation algorithm equivalent water thickness, sometimes referred to as canopy water content. 

## 2 Introduction

ollowing on recommendations by the National Academies of Science, Engineering and Medicine in their 2018 Decadal Survey on Earth Sciences, the National Aeronautics and Space Administration (NASA) selected the Surface Biology and Geology (SBG) mission for implementation as part of  its Earth System Observatory (ESO).  The ESO is a series of missions that will launch in the late 2020s and early 2030s to observe different aspects of the Earth System.  SBG in particular aims to measure properties of the Earth’s surface composition and ecology.  It is comprised of two platforms: a wide-swath thermal infrared instrument on a free-flying spacecraft in a polar orbit with an afternoon equatorial crossing time; and a separate spacecraft carrying a wide-swath solar reflectance imaging spectrometer operating in the Visible Shortwave Infrared (VSWIR), with a morning equatorial crossing time. 

This document focuses on the second platform, SBG-VSWIR.  SBG-VSWIR will measure the solar reflected range at approximately 380-2500 nm at 10 nm spectral sampling, over a 180 km swath with 30 m spatial sampling.  This measurement enables repeat coverage of any location on Earth every 16 days.  The visible-shortwave infrared range is sensitive to diverse physical processes in the Earth’s surface and atmosphere (Cawse-Nicholson 2021).  It provides Earth-system-scale measurements relevant to: aquatic ecosystems, including benthic ecosystems; and terrestrial ecology; biodiversity; water resources including predictions of snowmelt and river water quality; surface geology, including mineral composition; a wide range of societal applications, ranging from mapping of greenhouse gas point sources to agriculture and fishery management; and more.  With a few exceptions, these measurements follow a common pattern.  First, the raw instrument data is first calibrated to units of radiance at the sensor.  Second, the radiance data is used to invert a radiative transfer model in order to estimate properties of the surface and atmospheric state.  The primary product of this process is an estimate of the spectral surface reflectance in each pixel, or roughly speaking, the fraction of downwelling illumination reflected back in the direction of the observer (Schaepman-Strub 2006).  This surface reflectance spectrum is subsequently analyzed to estimate properties of the solid surface, vegetation, and water bodies (Figure 1). 

This Algorithm Theoretical Basis Document describes the algorithm used for terrestrial vegetation composition, function, and structure estimation step.    
![Nominal CWT Calc](./fig/nominal_ewt.PNG)

Figure 1: SBG-VSWIR product workflow.  The Level-2 products are created in the ”Surface and Atmosphere Modeling” step.

## 3 Context/Background

### 3.1 Historical Perspective

### 3.2 Additional Information

## 4 Algorithm Description

### 4.1 Scientific Theory

- slide with the water absorption features ( from nik)
#### 4.1.2 Scientific theory assumptions

### 4.2 Mathematical Theory

#### 4.2.1 Mathematical theory assumptions

### 4.3 Algorithm Input Variables

### 4.4 Algorithm Output Variables
The SBG-VSWIR output data products delivered to the DAAC use their formatting conventions, the system operates internally on data products stored as binary data cubes with detatched human-readable ASCII header files.   The specific output files from the L2b stage are: 



## 5 Algorithm Usage Constraints

## 6 Performance Assessment
There are currently no requirements validate terrestrial vegetation products.  
- can put as an example 
- susan ustin - destructive canopy sampling 

### 6.1 Validation Methods

### 6.2 Uncertainties

### 6.3 Validation Errors

## 7 Algorithm Implementation

** something like this 
Algorithms outputs from the partial least squares algorithm strategy (LMA, N, LWC) have the potential to be unpredictable when applied to areas and vegetation communities that have not been included in training datasets. Caution should be applied when interpreting results that are from areas not documented here to be included in training datasets [map figure].  

### 7.1 Algorithm Availability
The SBG-VSWIR mission will store the specific implementation of vegetation model development and parameters, including configuration options, training datasets, etc. at the SBG software repository (https://github.com/nasa-sbg). 

### 7.2 Input Data Access
All input data required to run the code not found in the above repositories is available at the NASA Digital Archive. 

### 7.3 Output Data Access
All output data is available at the NASA Digital Archive and searchable from NASA Earthdata Search (https://search.earthdata.nasa.gov/search). 

### 7.4 Important Related URLs
N/A 

## 8 Significance Discussion

This ATBD describes the implementation of 1) an implementation of equivalent water thickness estimation.

## 9 Open Research
All code described here is open source.  All publications sponsored by the SBG-VSWIR mission related to this code are open access. 
## 10 Acknowledgements

## 11 Contact Details

K. Dana Chadwick 

ORCID: 0000-0002-5633-4865 

URL:  

Email: dana.chadwick@jpl.nasa.gov 

Role(s) related to this ATBD: writing - original and revision, methodology, software. 

Affiliation – Jet Propulsion Laboratory, California Institute of Technology 

 

## References
