> 📝 **Template Note:** This is a template, please be sure to adapt it the following way before publishing the new WaterBench:
> - All text inside Template Notes gives some indication of the content that should be included in the final README. Please adapt all of these fields and remove the Template Notes before publishing.
> - The `output/` folder contains its own `README.md` that is uploaded to Zenodo together with the output data. This file must also be adapted before publishing.
> - Don't forget to add the WaterBench to https://github.com/DHI/WaterBench so it is included in https://dhi.github.io/WaterBench/
> - Please make sure that you specify the timezone format of your data.

# MIKE3 Hydrodynamic model of Øresund

> 📝 **Template Note:** Replace `XXXXXXXX` with the Zenodo DOI. Use the HTML format below (not Markdown image syntax) — Pandoc skips raw HTML in PDF output, which prevents the badge from breaking LaTeX rendering.

<a href="https://doi.org/10.5281/zenodo.XXXXXXXX"><img src="https://img.shields.io/badge/DOI-10.5281%2Fzenodo.XXXXXXXX-blue" alt="DOI"></a>

This repository contains practical and background information for the WaterBench case "MIKE3 HD model of Øresund".

The dataset can be cited as:

> 📝 **Template Note:** Replace the citation below with the correct author, year, title, version, and DOI.

> \[DHI\]. (YEAR). *\[Case Name: Short Description\]*
> (Version X.X) \[Data set\]. Zenodo. https://doi.org/XXXX

See the [LICENSE](LICENSE) file for usage conditions.

⚠️ Disclaimer

The included MIKE21 model setup is designed as a simple demonstration for educational and research purposes. It is not optimized for precision or exhaustive calibration and should not be regarded as a benchmark for best practices in hydrodynamic modeling. The results should not be used for operational or decision-making purposes.

> This model setup and dataset are provided for educational,
> benchmarking, and research purposes only.\
> The model configuration is simplified and may not be fully calibrated
> or validated for operational use.\
> Results must not be used for real-time forecasting, infrastructure
> design, safety-critical decisions, or regulatory purposes.\
> The dataset does not represent best-practice modelling standards at DHI and
> should be treated as a controlled benchmark case.

# Intended Use

The dataset is aimed at supporting educational, research, and exploratory activities, such as:

-   Development and benchmarking of hydrodynamic or hydrological models
-   Testing model calibration and validation workflows
-   Machine learning and surrogate modelling
-   Extreme event forecasting studies
-   Uncertainty quantification experiments

# Folder Structure

> 📝 **Template Note:** The WaterBench cases should follow a folder structure that is standardized between them. If you are using a model for data creation, please stick to the following structure. If you are not using a model you might rename or remove the model and input folders.


    - README.md
    - LICENSE
    - .github/
        + workflows/           # GitHub Actions workflow files. This renders the README.md to PDF
    - .publish/                # Folder for rendered outputs (e.g., README.pdf)
    - .preprocessing/          # Notebooks for preprocessing of raw data (if applicable)
    - model/
        + model setup files
        + simulation logs 
    - input/
        + boundary conditions
        + meteorological forcing
        + mesh file 
        + parameters such as bed roughness
    - observations/
        + in-situ observations
        + satellite data (if applicable)
    - code/
        + notebooks for data exploration
        + validation scripts
    - figures/
        + generated plots
    - output_sample/
        + reduced model outputs for testing
    - output/
        + full simulation results (only on Zenodo)


> 📝 **Template Note:**
> Choose the software you have used to create your data. If you did not use specific software, describe the method you followed to create the data. Example snippets for common software and methods are provided below as collapsible sections (click to expand/collapse) for clarity in the template.
>
> For your final README:
> - Delete all unused software or method snippets, i.e. remove everything from `<details>` to `</details>` (inclusive) for each snippet you do not use.
> - For the snippet you keep, remove the wrapping `<details>`, `<summary>...</summary>`, and `</details>` tags so that only the `#` heading and body text remain.
> - If your software or method is not listed, you have to create a new snippet following a similar format as the examples below.


<details>
<summary><strong>MIKE 21 Flow Model FM</strong></summary>

# MIKE 21 Flow Model FM

MIKE 21 Flow Model FM is a modelling system based on a flexible mesh approach. The modelling system has been developed for applications within oceanographic, coastal and estuarine environments. The model is based on the numerical solution of the two-dimensional shallow water equations - the depth-integrated incompressible Reynolds averaged Navier-Stokes equations. More information can be found [in the documentation](https://manuals.mikepoweredbydhi.help/latest/Coast_and_Sea/MIKE_FM_HD_2D.pdf).

Since all data, including output from a simulation, is given, it is not necessary to run the MIKE simulation. However, it is possible, since a setup file is supplied as well as all of the input data. Running the MIKE software requires a license. Read more about obtaining a [license](https://www.dhigroup.com/technologies/mikepoweredbydhi/pricing) and about [academic licensing](https://www.dhigroup.com/technologies/mikepoweredbydhi/pricing/academic-licenses). If you already have a license, read the [step-by-step guide](https://manuals.mikepoweredbydhi.help/latest/Coast_and_Sea/MIKE_FM_HD_Step_By_Step.pdf) to learn how to run simulations.

</details>

<details>
<summary><strong>MIKE 21 Spectral Wave Model</strong></summary>

# MIKE 21 Spectral Wave Model

MIKE 21 SW is a modelling system based on a flexible mesh approach. The modelling system has been developed for applications within oceanographic, coastal and estuarine environments. The governing equation is the wave action balance equation formulated in either Cartesian or spherical coordinates. More information can be found [in the documentation](https://manuals.mikepoweredbydhi.help/latest/Coast_and_Sea/M21SW_Scientific_Doc.pdf).

Since all data, including output from a simulation, is given, it is not necessary to run the MIKE simulation. However, it is possible, since a setup file is supplied as well as all of the input data. Running the MIKE software requires a license. Read more about obtaining a [license](https://www.dhigroup.com/technologies/mikepoweredbydhi/pricing) and about [academic licensing](https://www.dhigroup.com/technologies/mikepoweredbydhi/pricing/academic-licenses). If you already have a license, read the [user guide](https://manuals.mikepoweredbydhi.help/latest/Coast_and_Sea/MIKE21SW.pdf) to learn how to run simulations.
</details>

<details>
<summary><strong>MIKE SHE Integrated Hydrological Model</strong></summary>

# MIKE SHE Integrated Hydrological Model
MIKE SHE is an integrated hydrological modeling system that emerged in the 1980s to represent the physical processes of water flow through the hydrological cycle in a modular way and with relevant scale. The available process modules - evapotranspiration, overland flow, unsaturated zone flow, groundwater flow, channel flow - are each governed by their relevant partial differential equations describing the movement of water through their system. Modules can be represented with more conceptual or lumped alternatives, giving the user the ability to tailor model complexity and compute time for their application. The model also has flexibility in the spatial and temporal discretization, allowing process modules to have the grid size and time step appropriate for the modeling goals and data availability. Typical applications (among many others) for a MIKE SHE model include:
 
- Water resource management for a river basin
- Flood modeling and prediction
- Wetland restoration and management
- Surface and groundwater interaction analyses
- Land change effects on basin hydrology
- Climate change effects on basin hydrology
- Groundwater withdrawal management
- Agriculture impact
- Irrigation management

A MIKE simulation can be run using the [MIKE modeling software](https://www.dhigroup.com/technologies/mikepoweredbydhi), provided that the appropriate input data and setup files are included. Although input and setup files depend on which modules are included and what numerical engines for these models are chosen, basic inputs include:

- Model domain 
- Topography (DEM)
- Precipitation time series

Detailed information on what inputs are required when different modules are added can be found in the [MIKE SHE user guide and reference manual](https://userdoc.mikeshe.mikepoweredbydhi.com/).

</details>

# Case Description

> 📝 **Template Note:** Answer why this specific case is part of the WaterBench series:
> - What makes this case unique?
> - Geographic location
> - Type of system (river basin, estuary, urban catchment, coastal strait, etc.)
> - Approximate spatial extent
> - Hydrodynamic or hydrological characteristics
> - Tidal range (if coastal)
> - Flood characteristics

# Model Setup

> 📝 **Template Note:** Describe all of the following to define a complete model setup. If you are not using a model, describe your workflow for data creation and rename the section to "Workflow"
> - Model Domain and Mesh
>   - Model extent
>   - Bathymetry
>   - Grid/mesh resolution
> - Model Forcing
>   - Initial condition
>   - Boundary conditions
>   - River inflows
>   - Rainfall
>   - Wind / pressure
>   - Tide
>   - ...
> - Model Parameters
>   - Bed roughness
>   - Eddy viscosity
>   - Wetting and drying threshold
>   - ...
> - Model Outputs
>   - Variables available
>   - Spatial resolution
>   - Temporal resolution
>   - Start and end date

# Validation

> 📝 **Template Note:** Describe the validation process for the model, including:
> - Observation Coverage
> - Validation approach
> - Skill metrics used
> - Comparison to operational model (if applicable)
>
> Validation scripts or notebooks should be located in: `code/model_validation_*.ipynb`

# Data Sources

> 📝 **Template Note:** Describe the edits that have been made to the original data. This could, for example, include outlier analysis and imputation. 
> In the following table adapt the columns to fit the data sources you have used. Add rows as needed.

| Data | Source | Citation | License |
|------|--------|----------|--------|
| e.g. Bathymetry  | Provider + URL | How to cite the data | License type of license link |
| e.g. Forcing | Provider + URL |  How to cite the data | License type of license link |
