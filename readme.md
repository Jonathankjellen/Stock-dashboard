# Django Stock Analysis Dashboard

A Django-based web application for stock analysis and prediction. This dashboard allows users to view stock history, compare different stocks, and visualize stock data with dynamic and interactive charts.

## Features

- Display stock history with interactive charts
- Compare different stocks on the same graph
- Search for stocks with an autocomplete dropdown
- Display a list of the most valuable stocks
- Fetch and update stock data using the `yfinance` library

## Requirements

- Python 3.x
- Django 3.x or higher
- yfinance
- AmCharts for data visualization

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Jonathankjellen/Stock-dashboard.git
    cd stock_dashboard
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Configure your database settings in `stock_dashboard/settings.py`.

## Usage

### To Run the Project

1. Apply migrations to set up the database:
    ```sh
    python manage.py migrate
    ```

2. Run the development server:
    ```sh
    python manage.py runserver
    ```

3. Open your web browser and navigate to `http://127.0.0.1:8000` to view the dashboard.

### To Create a New Migration of the Model

1. Make migrations for your model changes:
    ```sh
    python manage.py makemigrations
    ```

2. Apply the migrations to update the database schema:
    ```sh
    python manage.py migrate
    ```
    
### To fetch stock data

1. Run the management command:
    ```sh
    python manage.py populate_stock_data
    ```

# Acknowledgements

- [Django](https://www.djangoproject.com/) - The web framework used
- [yfinance](https://pypi.org/project/yfinance/) - For fetching stock data
- [AmCharts](https://www.amcharts.com/) - For data visualization