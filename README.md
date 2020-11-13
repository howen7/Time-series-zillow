# Time-series-zillow

# Table of Contents

<!--ts-->
 * [General Setup Instructions](https://github.com/howen7/Time-series-zillow#general-setup-instructions)
 * [Context of Project](https://github.com/howen7/Time-series-zillow)
 * [Definitions](https://github.com/)
 * [Data](https://github.com/chum46/<>#data)
 * [Process](https://github.com/howen7/Time-series-zillow/#models-used--methodology)
 * [Results](https://github.com/chum46/<>#results-future-investigations-and-recommendations)
 * [Next Steps](https://github.com/chum46/<>#future-investigations-and-recommendations)
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
├── src
│   ├── data
│   │   ├── 
│   │   ├── 
│   │   ├── 
│   │   └── 
│   └── mymods.py
    

```
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
