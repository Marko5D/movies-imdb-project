import MetaTrader5 as mt5
import pandas as pd
from ta.trend import EMAIndicator
from ta.volatility import AverageTrueRange

symbols = ["XAUUSD", "BTCUSD"]

timeframes = {
    "M1": mt5.TIMEFRAME_M1,
    "M5": mt5.TIMEFRAME_M5,
    "M15": mt5.TIMEFRAME_M15
}

if not mt5.initialize():
    print("Greška:", mt5.last_error())
    quit()

account_info = mt5.account_info()

if account_info is None:
    print("Ne mogu da pročitam account info:", mt5.last_error())
    mt5.shutdown()
    quit()

balance = account_info.balance
risk_percent = 1
risk_amount = balance * (risk_percent / 100)

print("Account balance:", round(balance, 2))
print("Risk percent:", risk_percent, "%")
print("Risk amount:", round(risk_amount, 2))

def get_signal(symbol, timeframe):

    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, 100)

    if rates is None:
        return None

    df = pd.DataFrame(rates)

    df["EMA20"] = EMAIndicator(
        close=df["close"],
        window=20
    ).ema_indicator()

    df["EMA50"] = EMAIndicator(
        close=df["close"],
        window=50
    ).ema_indicator()

    df["ATR14"] = AverageTrueRange(
        high=df["high"],
        low=df["low"],
        close=df["close"],
        window=14
    ).average_true_range()

    last = df.iloc[-1]

    if last["close"] > last["EMA20"] > last["EMA50"]:
        signal = "BUY"

    elif last["close"] < last["EMA20"] < last["EMA50"]:
        signal = "SELL"

    else:
        signal = "NO TRADE"

    return {
        "signal": signal,
        "close": last["close"],
        "atr": last["ATR14"]
    }


for symbol in symbols:

    symbol_info = mt5.symbol_info(symbol)

    if symbol_info is None:
        print(f"Ne mogu da pročitam info za {symbol}")
        continue

    print("\nSYMBOL INFO")

    print("Trade contract size:", symbol_info.trade_contract_size)
    print("Volume min:", symbol_info.volume_min)
    print("Volume max:", symbol_info.volume_max)
    print("Volume step:", symbol_info.volume_step)

    print(f"\n========== {symbol} ==========")

    m1 = get_signal(symbol, timeframes["M1"])
    m5 = get_signal(symbol, timeframes["M5"])
    m15 = get_signal(symbol, timeframes["M15"])

    print("M1:", m1["signal"])
    print("M5:", m5["signal"])
    print("M15:", m15["signal"])

    final_signal = "NO TRADE"

    if (
        m1["signal"] == "BUY"
        and m5["signal"] == "BUY"
        and m15["signal"] == "BUY"
    ):
        final_signal = "BUY"

    elif (
        m1["signal"] == "SELL"
        and m5["signal"] == "SELL"
        and m15["signal"] == "SELL"
    ):
        final_signal = "SELL"

    print("\nFINAL SIGNAL:", final_signal)

    if final_signal != "NO TRADE":

        close_price = m1["close"]
        atr = m1["atr"]

        if final_signal == "BUY":
            sl = close_price - atr * 1.5
            tp = close_price + atr * 2

        else:
            sl = close_price + atr * 1.5
            tp = close_price - atr * 2

        print("Entry:", round(close_price, 2))
        print("Stop Loss:", round(sl, 2))
        print("Take Profit:", round(tp, 2))

mt5.shutdown()