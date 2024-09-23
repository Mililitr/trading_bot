import asyncio
from data_fetching.yfinance_fetcher import YFinanceDataFetcher
from analysis.quarters import get_current_quarter
from analysis.psp_tpd import is_psp, is_tpd
from analysis.true_open import get_true_open
from notifications.telegram import TelegramNotifier

async def main():
    # Инициализация
    yf_fetcher = YFinanceDataFetcher()
    notifier = TelegramNotifier(token='2120119987:AAH6XMiLeOwu14cRv8fcraw4LjzsjDSeHEc', chat_id='932236582')

    # Получение данных
    data = yf_fetcher.get_data(symbol='EURUSD=X', interval='1h', period='5d')

    # Проверка наличия данных
    if data.empty:
        print("No data fetched.")
        return

    # Вывод структуры данных
    print(data.head())

    # Анализ данных
    current_quarter = get_current_quarter()
    print(f"Current Quarter: {current_quarter}")

    # Проверка наличия достаточного количества данных для анализа
    if len(data) < 3:
        print("Not enough data for PSP and TPD analysis.")
        return

    # Пример анализа PSP
    candle1 = data.iloc[-3]
    candle2 = data.iloc[-2]
    candle3 = data.iloc[-1]
    if is_psp(candle1, candle2):
        await notifier.send_message("PSP detected!")

    # Пример анализа TPD
    if is_tpd(candle1, candle2, candle3):
        await notifier.send_message("TPD detected!")

    # Проверка истинной цены открытия
    true_open = get_true_open(data, 'daily')
    print(f"True Open: {true_open}")

if __name__ == "__main__":
    asyncio.run(main())