# NYC-Airbnb-Data-Analysis
The goal of this data analysis is to find the lowest priced Airbnb listings of 2019 based on the Airbnb dataset features.

The dataset is presented in csv format and is read using Pandas. It contains information such as id, name, host id, host name, neighbourhood group, neighbourhood, latitude, longitude, room type, price, minimum nights, number of reviews, last review, reviews per month, calculated host list, availability 365.The dataset can be found [here](https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data#AB_NYC_2019.csv).

# Setup Instructions
1. Download Python 3.7 [here](https://www.python.org/downloads/). This will download your Python global environment onto your computer. This is necessary in order to create the Python virtual environment in the next step.
1. Go to the project directory through the command line and create a Python virtual environment with all of the necessary libraries imported.
    1. To create the virtual environment, run the following command:
    ```
    python3 -m venv venv
    ```

    1. To activate the virtual environment, run the following command:
    ```
    source venv/bin/activate
    ```

    1. To install the required imports needed for your Python code, run the following commands:

    ```
    pip install -r app/requirements.txt
    ```