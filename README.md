# Compare Backtesting Trading Strategies with Seaborn

## Overview

This Python script allows you to **compare multiple trading strategies** against a Buy-and-Hold benchmark using historical stock price data.  
It uses [yfinance](https://pypi.org/project/yfinance/) for data retrieval, [TA-Lib](https://mrjbq7.github.io/ta-lib/) for technical indicators, and the [Backtesting.py](https://kernc.github.io/backtesting.py/) framework for simulating trades.

You can select from built-in strategies:

- **SMA Crossover** – Trades based on short and long moving averages
- **RSI** – Trades based on overbought/oversold RSI thresholds
- **Momentum** – Trades based on momentum shifts

After running, the script outputs:
- Strategy performance statistics
- Number of trades executed
- Equity curve plots comparing chosen strategies with Buy-and-Hold

---

## Features
- Interactive selection of strategies to test
- Equity curve visualization with Seaborn
- Adjustable backtest parameters (cash, commission, margin)
- Works with any stock ticker

---

## Installation

## Conda Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/strategy-comparison-backtester.git
cd strategy-comparison-backtester
```

### 2. Create the conda environment from the environment.yml file:

```bash 
conda env create -f environment.yml  
```

### 3. Activate the environment:

```bash
conda activate venv 
```

---


## Pip Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/strategy-comparison-backtester.git
cd strategy-comparison-backtester
```

### 2. Install Python (Recommended: Python 3.10)
Make sure you have Python 3.10 installed to ensure library compatibility.

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## Usage

Run the script:

```bash
python comparison.py
```
