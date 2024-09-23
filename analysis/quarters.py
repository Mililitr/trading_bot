from datetime import datetime, timedelta

def get_current_quarter():
    now = datetime.now() - timedelta(hours=4)  # UTC-4
    hour = now.hour
    if 18 <= hour < 24:
        return 'Q1'
    elif 0 <= hour < 6:
        return 'Q2'
    elif 6 <= hour < 12:
        return 'Q3'
    else:
        return 'Q4'