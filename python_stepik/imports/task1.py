import datetime
year, month, day = map(int, input().split())
current_date = datetime.date(year, month, day)
answer = current_date + datetime.timedelta(days=int(input()))
print(answer.year, answer.month, answer.day)