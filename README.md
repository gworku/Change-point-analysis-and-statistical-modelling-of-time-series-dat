# 📊 Brent Oil Price Analysis: Change Point Detection and Statistical Modeling

A comprehensive analysis of Brent Crude Oil Prices, focusing on change point detection, time series modeling, and the impact of geopolitical events and economic indicators.

## 🌟 Features

- **Time Series Analysis**: Historical price trends and patterns
- **Change Point Detection**: Identify significant shifts in price behavior
- **Statistical Modeling**: Advanced models for price prediction
- **Interactive Dashboard**: Visual exploration of data and insights
- **CI/CD Pipeline**: Automated testing and deployment

## 📁 Project Structure

```
.
├── Brent-dashboard/           # Interactive dashboard for data visualization
├── github/                    # GitHub Actions workflows
│   └── workflows/
│       └── ci.yml            # CI/CD pipeline configuration
├── notebook/                 # Jupyter notebooks for analysis
│   ├── brent_change_point_analysis.ipynb
│   └── data_preprocessing.ipynb
├── src/                      # Source code
│   ├── brent_change_point_analysis.py
│   ├── data_eda.py
│   ├── utils.py
│   └── __init__.py
├── test/                     # Test files
│   └── __init__.py
├── .gitignore
├── README.md
└── requirements.txt
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/gworku/Change-point-analysis-and-statistical-modelling-of-time-series-dat.git
   cd Change-point-analysis-and-statistical-modelling-of-time-series-dat
   ```

2. **Create and activate a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

### Running the Analysis

1. **Data Preprocessing**
   ```bash
   python -m notebook.data_preprocessing
   ```

2. **Change Point Analysis**
   ```bash
   python -m notebook.brent_change_point_analysis
   ```

3. **Start the Dashboard**
   ```bash
   cd Brent-dashboard/brent-dashboard
   npm install
   npm start
   ```

## 📊 Data Sources

- Historical Brent Crude Oil Prices
- Geopolitical Event Data
- Economic Indicators

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [10x Academy](https://www.10xacademy.org/) for the project opportunity
- Open-source contributors and maintainers of the libraries used in this project
