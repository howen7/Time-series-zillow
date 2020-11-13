# Time-series-zillow
Modeling ZIP codes that show promise for realestate firms. 


# Table of Contents

<!--ts-->
 * [General Setup Instructions](https://github.com/howen7/Time-series-zillow#general-setup-instructions)
 * [Context of Project](https://github.com/howen7/Time-series-zillow)
 * [Definitions](https://github.com/howen7/Time-series-zillow)
 * [Data](https://github.com/howen7/Time-series-zillow)
 * [Process](https://github.com/howen7/Time-series-zillow)
 * [Results](https://github.com/howen7/Time-series-zillow)
 * [Next Steps](https://github.com/howen7/Time-series-zillow)
<!--te-->

```
.
├── README.md     
├── environment.yml
├── notebooks
│   ├── exploratory
│   │   ├── 
│   │   ├── 
│   │   ├── 
│   │   ├── 
│   │   ├── 
│   │   ├── 
│   │   ├──  
│   │   ├──  
│   │   ├──
│   │   ├── 
│   │   ├──
│   │   ├──
│   │   └──
│   │     
│   └── report
│       ├── figures
│       │   ├── 
│       │   ├── 
│       │   ├── 
│       │   ├── 
│       │   ├── 
│       │   ├── 
│       │   ├── 
│       │   └── 
│       └── finalnotebook.ipynb
├── reports
│   └── Presentation_deck
└── src
    ├── data
    │   ├── 
    │   ├── 
    │   ├── 
    │   └── 
    └── mymods.py
    

```
#### Repo Navigation Links
 - [final summary notebook](https://github.com/howen7/Time-series-zillow/master/notebooks/report/final_notebook.ipynb)
 - [exploratory notebooks folder](https://github.com/howen7/Time-series-zillow)
 - [src folder](https://github.com/howen7/Time-series-zillow)
 - [presentation.pdf](https://github.com/howen7/Time-series-zillow)
 
# General Setup Instructions 

Ensure that you have installed [Anaconda](https://docs.anaconda.com/anaconda/install/) 

### `housing` conda Environment

This project relies on you using the [`environment.yml`](environment.yml) file to recreate the `housing` conda environment. To do so, please run the following commands *in your terminal*:
```bash
# create the housing conda environment
conda env create -f environment.yml
# activate the housing conda environment
conda activate housing
# if needed, make housing available to you as a kernel in jupyter
python -m ipykernel install --user --name churn --display-name "Python 3 (housing)"
```
# Context:

This projects goal was to provide a real estate firm with 5 ZIP codes within the United States that would be good investments. Along with are suggestions we would also provide them with a time series model for each ZIP code to predict how well the ZIP codes would perform 5 years into the future (2018 - 2023). Todays housing market is less predictable because of the recent pandemic and the ability to work from homes. There has been reports of a lot of people moving out of more expensive/ high tax states. [Here](https://losangeles.cbslocal.com/2020/09/23/residents-moving-out-of-california-on-the-rise/) is an article explaning why people are leaving California. 

## Aims:

This project aims to:

    - Investigate the area codes that would be good mid to long term investments(5+ years)
    - Provide inferential statistics and visualisations based on this data.
    - Create predictive, supervised learning models from the data to predict future housing prices in select ZIP codes
    
# Definitions:

    - House: A 1-5 bedroom single family home, Condo, or Co-op
    - MAPE: Mean absolute percentage error. A measure of how well our model did when predicting on our hold out test. 

# Data:

This project uses dataset from Zillow.
The dataset compomises of nearly every ZIP code and the average price of home value from 1996-04 to 2018-04.


# Models used + Methodology:

This project tests several Time series models:

    - Facebooks Prophet model
    - ARIMA model 
    - SARIMAX model

    
# Results, Future Investigations and Recommendations:

#### Best model:


#### Future Investigations and Recommendations:
