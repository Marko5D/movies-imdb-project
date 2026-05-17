import MetaTrader5 as mt5
import pandas as pd
import time
from ta.trend import EMAIndicator
from ta.volatility import AverageTrueRange

symbols = ["XAUUSD", "BTCUSD"]

timeframes = {
    "M1": mt5.TIMEFRAME_M1,
    "M5": mt5.TIMEFRAME_M5,
    "M15": mt5.TIMEFRAME_M15
}

risk_percent = 0.2
check_interval = 60  # sekundi

if not mt5.initialize():
    print("Greška:", mt5.last_error())
    quit()


def get_account_risk():
    account_info = mt5.account_info()

    if account_info is None:
        print("Ne mogu da pročitam account info:", mt5.last_error())
        return None, None, None

    balance = account_info.balance
    risk_amount = balance * (risk_percent / 100)

    return balance, risk_percent, risk_amount


def get_signal(symbol, timeframe):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, 100)

    if rates is None:
        return None

    df = pd.DataFrame(rates)

    df["EMA20"] = EMAIndicator(close=df["close"], window=20).ema_indicator()
    df["EMA50"] = EMAIndicator(close=df["close"], window=50).ema_indicator()

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


while True:
    balance, risk_percent_value, risk_amount = get_account_risk()

    if balance is None:
        break

    print("\n==============================")
    print("NOVA PROVERA")
    print("Account balance:", round(balance, 2))
    print("Risk percent:", risk_percent_value, "%")
    print("Risk amount:", round(risk_amount, 2))

    for symbol in symbols:
        mt5.symbol_select(symbol, True)

        print(f"\n========== {symbol} ==========")

        positions = mt5.positions_get(symbol=symbol)

        if positions is not None and len(positions) > 0:
            print("Već postoji otvorena pozicija za ovaj simbol. Preskačem.")
            continue

        symbol_info = mt5.symbol_info(symbol)

        if symbol_info is None:
            print(f"Ne mogu da pročitam info za {symbol}")
            continue

        tick = mt5.symbol_info_tick(symbol)

        if tick is None or tick.bid <= 0 or tick.ask <= 0:
            print("Market je zatvoren ili nema aktivne bid/ask cene. Preskačem.")
            continue

        print("SYMBOL INFO")
        print("Trade contract size:", symbol_info.trade_contract_size)
        print("Volume min:", symbol_info.volume_min)
        print("Volume max:", symbol_info.volume_max)
        print("Volume step:", symbol_info.volume_step)
        print("Bid:", tick.bid)
        print("Ask:", tick.ask)

        m1 = get_signal(symbol, timeframes["M1"])
        m5 = get_signal(symbol, timeframes["M5"])
        m15 = get_signal(symbol, timeframes["M15"])

        if m1 is None or m5 is None or m15 is None:
            print("Nema dovoljno podataka za signal.")
            continue

        print("\nM1:", m1["signal"])
        print("M5:", m5["signal"])
        print("M15:", m15["signal"])

        final_signal = "NO TRADE"

        if m1["signal"] == "BUY" and m5["signal"] == "BUY" and m15["signal"] == "BUY":
            final_signal = "BUY"
        elif m1["signal"] == "SELL" and m5["signal"] == "SELL" and m15["signal"] == "SELL":
            final_signal = "SELL"

        print("\nFINAL SIGNAL:", final_signal)

        if final_signal != "NO TRADE":
            atr = m1["atr"]

            if final_signal == "BUY":
                order_type = mt5.ORDER_TYPE_BUY
                entry_price = tick.ask
                sl = entry_price - atr * 1.5
                tp = entry_price + atr * 2
            else:
                order_type = mt5.ORDER_TYPE_SELL
                entry_price = tick.bid
                sl = entry_price + atr * 1.5
                tp = entry_price - atr * 2

            print("Entry:", round(entry_price, 2))
            print("Stop Loss:", round(sl, 2))
            print("Take Profit:", round(tp, 2))

            sl_distance = abs(entry_price - sl)

            print("SL distance:", round(sl_distance, 2))
            print("Risk amount:", round(risk_amount, 2))

            contract_size = symbol_info.trade_contract_size
            raw_lot = risk_amount / (sl_distance * contract_size)

            volume_step = symbol_info.volume_step
            min_volume = symbol_info.volume_min
            max_volume = symbol_info.volume_max

            lot = round(raw_lot / volume_step) * volume_step
            lot = max(min_volume, min(lot, max_volume))

            print("Suggested lot:", round(lot, 2))

            confirm = input("Da li želiš da pošalješ DEMO order? Ukucaj YES: ")

            if confirm == "YES":
                request = {
                    "action": mt5.TRADE_ACTION_DEAL,
                    "symbol": symbol,
                    "volume": lot,
                    "type": order_type,
                    "price": entry_price,
                    "sl": sl,
                    "tp": tp,
                    "deviation": 20,
                    "magic": 123456,
                    "comment": "AI Trading Bot",
                    "type_time": mt5.ORDER_TIME_GTC,
                    "type_filling": mt5.ORDER_FILLING_IOC,
                }

                result = mt5.order_send(request)

                print("\nORDER RESULT:")
                print(result)
            else:
                print("Order nije poslat.")

    print(f"\nČekam {check_interval} sekundi do sledeće provere...")
    time.sleep(check_interval)