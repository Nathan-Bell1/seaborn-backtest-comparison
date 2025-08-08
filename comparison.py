import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import talib
import yfinance as yf
from backtesting import Backtest, Strategy
from backtesting.lib import crossover

class SMAcrossover(Strategy):
    display_name = "SMAcrossover"
    short = 5
    long = 10

    def init(self):
        close = self.data.Close
        self.sma_short = self.I(talib.SMA, close, self.short)
        self.sma_long = self.I(talib.SMA, close, self.long)

    def next(self):
        cross_up = crossover(self.sma_short, self.sma_long)
        cross_down = crossover(self.sma_long, self.sma_short)
        if cross_up:
            if self.position:
                self.position.close()
            self.buy()
        elif cross_down:
            if self.position:
                self.position.close()

class RSI(Strategy):
    display_name = "RSI"
    timeperiod = 7
    
    def init(self):
        self.rsi = self.I(talib.RSI, self.data.Close, self.timeperiod)
    
    def next(self):
        if self.rsi[-2] < 35 and self.rsi[-1] >= 35:
            if self.position:
                self.position.close()
            self.buy()
        elif self.rsi[-2] > 65 and self.rsi[-1] <= 65:
            if self.position:
                self.position.close()

class Momentum(Strategy):
    display_name = "Momentum"
    timeperiod = 20
    
    def init(self):
        close = self.data.Close
        self.momentum = self.I(talib.MOM, close, timeperiod=self.timeperiod)
        
    def next(self):
        if self.momentum[-1] > 0 and self.momentum[-2] <= 0:
            if self.position:
                self.position.close()
            self.buy()
        elif self.momentum[-1] < 0 and self.momentum[-2] >= 0:
            if self.position:
                self.position.close()

strategies = {
    'smacrossover': SMAcrossover,
    'rsi': RSI,
    'momentum': Momentum
}

while True:
    try:
        n = int(input("How many strategies would you like to compare? "))
        if n < 1:
            print("Please enter a positive integer.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

print("\nAvailable strategies:")
for strat in strategies.values():
    print(f" - {strat.display_name}")

chosen_strategies = []
for i in range(n):
    while True:
        strategy_input = input(f"\nStrategy {i + 1}: ").strip().lower()
        if strategy_input in strategies and strategy_input not in chosen_strategies:
            chosen_strategies.append(strategy_input)
            print(f"{strategies[strategy_input].display_name} added.")
            break
        else:
            print("Invalid or duplicate strategy. Try again.")

df = yf.download('AAPL', period='2y', auto_adjust=True)
df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']

cash, commission, margin = 1000000, 0.001, 1.0

results = {}
for strat in chosen_strategies:
    bt = Backtest(df, strategies[strat], cash=cash, commission=commission, margin=margin)
    results[strat] = bt.run()
    print(f"Results for {strategies[strat].display_name}:\n{results[strat]}\n\n")
    print(f"Number of trades: {len(results[strat]._trades)}")

buy_and_hold_equity = (df['Close'] / df['Close'].iloc[0]) * cash

sns.set_theme(style="darkgrid")

plt.figure(figsize=(12, 6))

for name, result in results.items():
    sns.lineplot(x=result._equity_curve.index, y=result._equity_curve['Equity'], label=strategies[name].display_name)
sns.lineplot(x=buy_and_hold_equity.index, y=buy_and_hold_equity.values, linestyle='--', label=f"Buy and Hold")

plt.title("Equity Curve Comparison with Buy and Hold")
plt.xlabel("Time")
plt.ylabel("Equity ($)")
plt.legend()
plt.show()
