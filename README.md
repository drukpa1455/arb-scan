# Arbitrage Scanner Documentation

This project is an arbitrage scanner that analyzes stock price data and calculates potential arbitrage opportunities. It fetches historical stock data from Yahoo Finance, calculates financial ratios, and visualizes the data in a web dashboard.

## Getting Started

1. Clone the repository: `git clone https://github.com/your-username/arb-scan.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the web dashboard: `streamlit run web_dashboard.py`

## Codebase Index

- `calculate_profit.py`: Contains functions for calculating the potential profit from arbitrage opportunities.
- `calculate_ratios.py`: Contains functions for calculating financial ratios from stock data.
- `fetch_data.py`: Contains functions for fetching historical stock data from Yahoo Finance.
- `main.py`: The main entry point of the application.
- `visualizations.py`: Contains functions for visualizing data using Matplotlib and Seaborn.
- `web_dashboard.py`: Implements the Streamlit web dashboard.

## Usage

1. Run the `main.py` script to fetch data, calculate ratios, and calculate profits.
2. Access the web dashboard by running `streamlit run web_dashboard.py` and open the provided URL in a browser.
3. Select the desired date range and view the visualizations of financial ratios and potential profits.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Make your changes and commit them: `git commit -m "Add your feature description"`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Create a pull request with a detailed description of your changes.

## License

This project is licensed under the [MIT License](LICENSE).