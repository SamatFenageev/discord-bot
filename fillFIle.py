import datetime
with open('pidorDate.txt', 'w') as file:
	file.write(datetime.datetime.strftime(datetime.datetime.today(), "%d/%m/%y %H:%M"))