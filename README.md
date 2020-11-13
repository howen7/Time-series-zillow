# Time-series-zillow

# Table of Contents

<!--ts-->
 * [General Setup Instructions](https://github.com/howen7/Time-series-zillow/Time-series-zillow#general-setup-instructions)
 * [Context of Project](https://github.com/howen7/Time-series-zillow)
 * [Definitions](https://github.com/)
 * [Data](https://github.com/chum46/<>#data)
 * [Process](https://github.com/howen7/Time-series-zillow/#models-used--methodology)
 * [Results](https://github.com/chum46/<>#results-future-investigations-and-recommendations)
 * [Next Steps](https://github.com/chum46/<>#future-investigations-and-recommendations)
<!--te-->
.
├── README.md
├── data
│   ├── expanded_dataset_cm
│   ├── initial_clean_lc
│   └── raw
│       └── telecom_churn_data
├── environment.yml
├── notebooks
│   ├── exploratory
│   │   ├── 01_cm_data_exploration.ipynb
│   │   ├── 02_cm_eda_modeling.ipynb
│   │   ├── 05_cm_modeling.ipynb
│   │   ├── 06_cm_modeling.ipynb
│   │   ├── 07_cm_final_models.ipynb
│   │   ├── lmc_exploratory_nb
│   │   │   ├── 01_explore_lc.ipynb
│   │   │   ├── 02_codealong_lc.ipynb
│   │   │   ├── 03_eda_lc.ipynb
│   │   │   ├── 04_m2_lc.ipynb
│   │   │   ├── 05_state_vis_lc.ipynb
│   │   │   ├── 06_m3_lc.ipynb
│   │   │   ├── 07_clean_df_lc.ipynb
│   │   │   ├── 08_m4_lc.ipynb
│   │   │   ├── 09_notebookstats_lc.ipynb
│   │   │   ├── state_files_500
│   │   │   └── y_lc
│   │   └── model_iterations
│   │       ├── 01_cm_data_exploration.ipynb
│   │       ├── 02_cm_eda_modeling.ipynb
│   │       ├── 04_m2_lc.ipynb
│   │       ├── 05_cm_modeling.ipynb
│   │       ├── 06_cm_modeling.ipynb
│   │       ├── 06_m3_lc.ipynb
│   │       ├── 07_cm_final_models.ipynb
│   │       └── 08_m4_lc.ipynb
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
│       └── final_notebook.ipynb
├── reports
│   ├── Group\ 3\ Customer\ Churn\ Presentation\ Deck.pdf
│   └── figures
└── src
    ├── cm_class_KNN.py
    ├── cm_class_LRM.py
    ├── cm_functions_balancing.py
    ├── cm_functions_preprocessing.py
    ├── cm_functions_tuning.py
    ├── data_cleaning_lc.py
    └── modelling_lc.py
    
#### Repo Navigation Links
 - [presentation.pdf](https://github.com/chum46/mod-3-project-group-3-chi-sea-ds/blob/master/reports/Group%203%20Customer%20Churn%20Presentation%20Deck.pdf)
 - [final summary notebook](https://github.com/chum46/mod-3-project-group-3-chi-sea-ds/blob/master/notebooks/report/final_notebook.ipynb)
 - [exploratory notebooks folder](https://github.com/chum46/mod-3-project-group-3-chi-sea-ds/tree/master/notebooks/exploratory)
 - [src folder](https://github.com/chum46/mod-3-project-group-3-chi-sea-ds/tree/master/src)
 
# General Setup Instructions 

Ensure that you have installed [Anaconda](https://docs.anaconda.com/anaconda/install/) 

### `churn` conda Environment

This project relies on you using the [`environment.yml`](environment.yml) file to recreate the `housing` conda environment. To do so, please run the following commands *in your terminal*:
```bash
# create the housing conda environment
conda env create -f environment.yml
# activate the housing conda environment
conda activate housing
# if needed, make housing available to you as a kernel in jupyter
python -m ipykernel install --user --name churn --display-name "Python 3 (housing)"
```
