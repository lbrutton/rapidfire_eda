## Rapidfire_eda

This Python package will help data scientists quickly pull information about the dataset they are looking at, prior to actually starting CRISP-DM. 

It lets users:
- Figures out whether the dataset is time based or not
- Handles strange date formats
- If the dataset is time based, then:
    - look at the evolution of each numerical value over time
    - sum each numerical column over time and look at its distribution
    - pull a histogram of each categorical column
    - look at the correlation between each of the numerical columns
    - draw scatterplot for the 5 most highly correlated variables
- If the dataset has no date column:
    - Look at the distribution of each numerical column
    - Pull a histogram of each of the categorical columns (for the top 50 categories)
    - Look at the correlation between each of the numerical variables
    - Draw scatterplots for the 5 most highly correlated variables
    
It should be super lightweight and easy to run, mostly aimed at providing some quick visualisations for time series data, and not competing with the many quick eda solutions already out there (autoviz, sweetviz, etc)