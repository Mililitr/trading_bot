def get_true_open(candles, timeframe):
    if timeframe == 'weekly':
        return candles.iloc[0]['Open']
    elif timeframe == 'daily':
        return candles.iloc[0]['Open']
    else:
        raise ValueError(f"Unsupported timeframe: {timeframe}")