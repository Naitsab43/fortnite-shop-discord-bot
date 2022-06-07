from datetime import date, datetime

def get_actual_date_formatted():

	date = datetime.now()
	day = date.strftime("%A")
	day_number = date.strftime("%d")
	month = date.strftime("%B")
	year = date.strftime("%Y")

	if day == "Monday":
		day = "Lunes"
	elif day == "Tuesday":
		day = "Martes"
	elif day == "Wednesday":
		day = "Miércoles"
	elif day == "Thursday":
		day = "Jueves"
	elif day == "Friday":
		day = "Viernes"
	elif day == "Saturday":
		day = "Sábado"
	elif day == "Sunday":
		day = "Domingo"

	if month == "January":
		month = "Enero"
	elif month == "February":
		month = "Febrero"
	elif month == "March":
		month = "Marzo"
	elif month == "April":
		month = "Abril"
	elif month == "May":
		month = "Mayo"
	elif month == "June":
		month = "Junio"
	elif month == "July":
		month = "Julio"
	elif month == "August":
		month = "Agosto"
	elif month == "September":
		month = "Septiembre"
	elif month == "October":
		month = "Octubre"
	elif month == "November":
		month = "Noviembre"
	elif month == "December":
		month = "Diciembre"

	return {
		"day": day,
		"day_number": day_number,
		"month": month,
		"year": year
	}
