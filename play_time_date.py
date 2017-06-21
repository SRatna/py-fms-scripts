import datetime
start_date = '2017-06-17'
end_date = '2017-06-27'
fmt = '%Y-%m-%d'
start_date_obj = datetime.datetime.strptime(start_date, fmt)
end_date_obj = datetime.datetime.strptime(end_date, fmt)
date = start_date_obj
while date != end_date_obj:
    date += datetime.timedelta(days=1)
    print(date.date())
