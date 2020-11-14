# Time-series-zillow
Modeling ZIP codes that show promise for realestate firms. <br>
![alt text](/notebooks/report/figures/nashville_pic.jpg)

# Table of Contents

<!--ts-->
 * [General Setup Instructions](https://github.com/howen7/Time-series-zillow#general-setup-instructions)
 * [Context of Project](https://github.com/howen7/Time-series-zillow#Context)
 * [Definitions](https://github.com/howen7/Time-series-zillow#Definitions)
 * [Data](https://github.com/howen7/Time-series-zillow#Data)
 * [Process](https://github.com/howen7/Time-series-zillow#models-used--methodology)
 * [Results](https://github.com/howen7/Time-series-zillow#Results)
 * [Next Steps](https://github.com/howen7/Time-series-zillow#Future-Investigations-and-Recommendations)
<!--te-->

```
.
├── README.md     
├── environment.yml
├── notebooks
│   ├── exploratory
│   │   ├── EDA.ipynb
│   │   ├── Jon_Mapping.ipynb
│   │   ├── Jon_Modeling.ipynb
│   │   ├── Jons_Notebook.ipynb
│   │   ├── Prophet.ipynb
│   │   ├── oz_01_preliminary_eda.ipynb
│   │   ├── oz_02_modeling.ipynb
│   │   ├── oz_03_arima_modeling_continued.ipynb
│   │   ├── oz_04_37115_final.ipynb
│   │   ├── oz_04_37148_final.ipynb
│   │   ├── oz_04_37210_final.ipynb
│   │   ├── oz_05_final_5_modeling.ipynb
│   │   ├── oz_06_map.ipynb
│   │   ├── zc_df.geojson
│   │   └── ImportData.ipynb
│   └── report
│       ├── figures
│       │   ├── 37115_Confidence.png
│       │   ├── 37115_predictions.png
│       │   ├── 37148_predictions.png
│       │   ├── 37174_predictions.png
│       │   ├── 37210_predictions.png
│       │   ├── 37221_predictions.png
│       │   ├── Model_performance.png
│       │   ├── nashville_pic.jpg
│       │   ├── top_growing_Metro.png
│       │   └── top_growing_state.png
│       └── finalnotebook.ipynb
├── reports
│   └── Presentation_deck
└── src
    ├── data
    │   ├── zillow_data_lf.csv
    │   ├── zillow_data.csv
    │   └── zip_data.npy
    └── mymods.py
    

```
#### Repo Navigation Links
 - [Getting Data to long Format](https://github.com/howen7/Time-series-zillow/tree/main/notebooks/exploratory/ImportData.ipynb)   
 - [Final summary notebook](https://github.com/howen7/Time-series-zillow/tree/main/notebooks/report/final_notebook.ipynb)
 - [Exploratory notebooks folder](https://github.com/howen7/Time-series-zillow/tree/main/notebooks/exploratory)
 - [src folder](https://github.com/howen7/Time-series-zillow/tree/main/src)
 - [Presentation.pdf](https://github.com/howen7/Time-series-zillow/tree/main/reports)
 
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

This project aims to:<br>

- Investigate the area codes that would be good mid to long term investments(5+ years)<br>
- Provide inferential statistics and visualisations based on this data.<br>
- Create predictive, supervised learning models from the data to predict future housing prices in select ZIP codes<br>
    
# Definitions:

- House: A 1-5 bedroom single family home, Condo, or Co-op<br>
- MAPE: Mean absolute percentage error. A measure of how well our model did when predicting on our hold out test. <br>

# Data:

This project uses dataset from Zillow found [here](https://www.zillow.com/research/data/).<br>
The dataset compomises of nearly every ZIP code in the USA and their average price of home value from 1996-04 to 2018-04.


# Models used + Methodology:

This project tests several Time series models:<br>

- Facebooks Prophet model<br>
- ARIMA model <br>
- SARIMAX model<br>

    
# Results:
![alt text](/notebooks/report/figures/Model_performance.png)


### Best model: Prophet Model

The Parameters for each ZIP code are shown in this table:
The all used Interval width of 0.95
![alt text](/notebooks/report/figures/Model_Parameters.png)


#### Future Investigations and Recommendations:

Our model only looks at average home prices within a ZIP code
Need to also look at what is driving prices in an area:
-Population change
-Nearby development
-Local property taxes
Our model is a good starting point for narrowing down ZIP Codes

