#Made by :- Aayush Gupta 2017002
from urllib.request import urlopen
import datetime
i=datetime.datetime.now()
y=int("  %d"%i.year)
m=int("  %d"%i.month)
d=int("  %d"%i.day)
date=str(datetime.date(y,m,d))

def weather_response(location, API_key):
	url='http://api.openweathermap.org/data/2.5/forecast?q='+location+'&APPID='+API_key
	f=urlopen(url)
	json=str(f.read().decode())
	return(json)

def has_error(location,json):
	error=json.find(name)
	error_s=json.index('"',(error+6)) #error stats from (if any);
	error_e=json.index('"',(error_s)) #error ends at (if any)
	a=json[error_s:error_e]
	if a==location:
		return False
	else:
		return True

def get_temperature (json, time, n=0):
	import datetime
	i=datetime.datetime.now()
	date=str(datetime.date(y,m,d+n))
	#checking for errors in the entery of time
	if (time=='00:00:00' or time=='03:00:00' or time=='06:00:00' or time=='09:00:00' or time=='12:00:00' or time=='15:00:00' or time=='18:00:00' or time=='21:00:00'):
		t=str(time)
	else:
		exit()
	dt='"'+date+' '+t+'"'
	z=json.index(dt)
	#searching for tempurature
	temp=json.rfind('"temp"',z)
	temp_s=json.index(":",temp);	temp_e=json.index(",",temp)
	p1=float(json[temp_s+1:temp_e])
	return(p1)


def get_humidity(json, time, n=0):
	import datetime
	i=datetime.datetime.now()
	date=str(datetime.date(y,m,d+n))
	#checking for errors in the entery of time
	if (time=='00:00:00' or time=='03:00:00' or time=='06:00:00' or time=='09:00:00' or time=='12:00:00' or time=='15:00:00' or time=='18:00:00' or time=='21:00:00'):
		t=str(time)
	else:
		exit()
	dt='"'+date+' '+t+'"'
	z=json.index(dt)
	#searching for humidity
	humidity=json.rfind("humidity",z)
	humidity_s=json.index(":",humidity);	humidity_e=json.index(",",humidity)
	p2=float(json[humidity_s+1:humidity_e])
	return(p2)


def get_pressure(json, time, n=0):
	import datetime
	i=datetime.datetime.now()
	date=str(datetime.date(y,m,d+n))
	#checking for errors in the entery of time
	if (time=='00:00:00' or time=='03:00:00' or time=='06:00:00' or time=='09:00:00' or time=='12:00:00' or time=='15:00:00' or time=='18:00:00' or time=='21:00:00'):
		t=str(time)
	else:
		exit()
	dt='"'+date+' '+t+'"'
	z=json.index(dt)
	#searching for pressure
	pressure=json.rfind("pressure",z)
	pressure_s=json.index(":",pressure);	pressure_e=json.index(",",pressure)
	p3=float(json[pressure_s+1:pressure_e])
	return(p3)


def get_wind(json,  time, n=0):
	import datetime
	i=datetime.datetime.now()
	date=str(datetime.date(y,m,d+n))
	#checking for errors in the entery of time
	if (time=='00:00:00' or time=='03:00:00' or time=='06:00:00' or time=='09:00:00' or time=='12:00:00' or time=='15:00:00' or time=='18:00:00' or time=='21:00:00'):
		t=str(time)
	else:
		exit()
	dt='"'+date+' '+t+'"'
	z=json.index(dt)
	#searching for wind speed
	wind=json.rfind("speed",z)
	wind_s=json.index(":",wind);	wind_e=json.index(",",wind)
	p4=float(json[wind_s+1:wind_e])
	return(p4)


def get_sealevel(json, time, n=0):
	import datetime
	i=datetime.datetime.now()
	date=str(datetime.date(y,m,d+n))
	#checking for errors in the entery of time
	if (time=='00:00:00' or time=='03:00:00' or time=='06:00:00' or time=='09:00:00' or time=='12:00:00' or time=='15:00:00' or time=='18:00:00' or time=='21:00:00'):
		t=str(time)
	else:
		exit()
	dt='"'+date+' '+t+'"'
	z=json.index(dt)
	#searching for sea level
	sea=json.rfind("sea_level",z)
	sea_s=json.index(":",sea);	sea_e=json.index(",",sea)
	p5=float(json[sea_s+1:sea_e])
	return(p5)