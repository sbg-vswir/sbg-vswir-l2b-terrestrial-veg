# SBG VSWIR Terrestrial Vegetation Canopy Surface Trait Products - Algorithm Theoretical Basis Document (ATBD)**

*K.D. Chadwick**<sup>1</sup>

<sup>1</sup>Jet Propulsion Laboratory, California Institute of Technology

Corresponding author: K. Dana Chadwick (dana.chadwick@jpl.nasa.gov)

**Key Points:**

**Version:** 1.0

**Release Date:** TBD

**DOI:** TBD

## Abstract

## Plain Language Summary

### Keywords: 

## 1 Version Description

This is Version 1.0 of the SBG VSWIR terrestrial vegetation algorithms for top of canopy traits.

## 2 Introduction

The NAS 2017 Decadal Survey called for a new generation of satellite missions to address critical science questions related to the Earth's surface and interior. The Surface Biology and Geology (SBG) mission was one of the missions recommended in the Decadal Survey. The SBG mission is designed to address key science questions related to the Earth's surface and interior, including the carbon cycle, terrestrial vegetation dynamics, and the water cycle. The mission is comprised of two satellite projects, the visible to shortwave infrared imaging spectrometer (VSWIR) Project and the thermal infrared (TIR) Project. This document describes the algorithm theoretical basis for the VSWIR terrestrial vegetation canopy surface trait products that are tracable to satisfying the science needs outlined in the Decadal Survey. 

This ATBD will cover the product generation for all terrestrial vegetation algorithms that are generated using a partial least squares regression framework. At the time of writing, this will include the following properties estimated for the phtosyntheic vegetation canopy surface observable from the VSWIR instrument: foliar nitrogen (N), leaf mass per area (LMA), and leaf water content (LWC). These products are generalized into a single ATBD because they use a similar algorithmic framework and are generated using the same input data.
 
## 3 Context/Background

The PLSR derived terrestrial vegetation properties are situated in the larger context of the SBG VSWIR algorithm pipeline. The full algorithm pipeline can be seen in Figure 1 below.

![img.png](figs/OverallVSWIR_FlowDiagram.png)
**Figure 1.** _Map of SBG VSWIR algorithm pipeline._

This pipeline is the expected framework as of the time of writing, but is subject to change as the mission progresses.


### 3.1 Historical Perspective



### 3.2 Additional Information



## 4 Algorithm Description

![img.png](figs/TraitFlowDiagram.png)

**Figure 2.** _Map of PLSR algorithm for terrestrial vegetation demonstration products._

### 4.1 Scientific Theory



#### 4.1.2 Scientific theory assumptions

### 4.2 Mathematical Theory

#### 4.2.1 Mathematical theory assumptions

### 4.3 Algorithm Input Variables

The input variables for terrestrial vegetation PLSR products are: isofit corrected reflectance and uncertianty (L2a), fractional cover and uncertianty (L2b_FRAC).  

### 4.4 Algorithm Output Variables

Output variables for foliar nitrogen, leaf mass per area, and leaf water content are generated for each pixel in the input data with a fractional cover >= 0.XX photosynthetic vegetation. For all other pixels, the output is set to NaN. Units are as follows: foliar nitrogen (g N/g of dry foliar mass), leaf mass per area (g dry mass/m^2 of leaf area), and leaf water content (g water/g fresh foliage). Uncertianties are also generated for each output variable in the same units as the output variable.

## 5 Algorithm Usage Constraints

## 6 Performance Assessment

### 6.1 Validation Methods

### 6.2 Uncertainties

### 6.3 Validation Errors

## 7 Algorithm Implementation

### 7.1 Algorithm Availability

### 7.2 Input Data Access

### 7.3 Output Data Access

### 7.4 Important Related URLs

## 8 Significance Discussion

## 9 Open Research

## 10 Acknowledgements

## 11 Contact Details

## References