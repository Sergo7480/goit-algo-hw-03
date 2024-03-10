from datetime import datetime
def get_days_from_today(date: int) -> int:
    input_date = datetime.strptime(date, '%Y-%m-%d')
    current_date = datetime.today()
    days_delta = (current_date - input_date).days
    return days_delta
input_date = "1980-04-07"
result = get_days_from_today(input_date)
print(f"Количество дней от {input_date} до текущей даты: {result}")
    
