def is_psp(candle1, candle2):
    return (candle1['Close'] > candle1['Open']) != (candle2['Close'] > candle2['Open'])

def is_tpd(candle1, candle2, candle3):
    return (candle3['Close'] < candle1['Close']) != (candle3['Close'] > candle1['Close'])