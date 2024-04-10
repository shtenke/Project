#Импорт
import flask
from flask import Flask, render_template, request
import python_weather
import asyncio
import os
import requests
from datetime import datetime
from datetime import timedelta
import pandas
import geopy
import meteostat
from meteostat import Point, Daily
from geopy.geocoders import Nominatim
from geopy.geocoders import get_geocoder_for_service
app = Flask(__name__)

#Основная функция
def pos(name):
  loc = Nominatim(user_agent="GetLoc")
  getLoc = loc.geocode(name)

  #Получение координат введенного города
  Latitude = getLoc.latitude
  Longitude = getLoc.longitude

  day = timedelta(days=1)
  year = timedelta(days=365)
  hours =  timedelta(hours=24)

  #Время прогноза температуры
  start = datetime.today()
  start = start - hours
  end = start + day
  start_back = start - year
  end_back = end - year

  #Задаем город
  city = Point(Latitude, Longitude, 70)

  #Температура в прошлом году
  data_back = Daily(city,start_back,end_back)
  data_back = data_back.fetch()
  data_back = data_back.iloc[[0],[0]]
  data_back = data_back.values.tolist()
  for j in data_back:
    data_back = str(j)
  data_back = data_back[1:-1]
  data_back = float(data_back)

  #Нынешняя температура
  data = Daily(city, start, end)
  data = data.fetch()
  data = data.iloc[[0],[0]]
  data = data.values.tolist()
  for i in data:
    data = str(i)
  data = data[1:-1]
  data = float(data)

  #Сравнение температур
  data_end = data - data_back
  data_end = data_end // 1

  return data,data_end,data_back
#Первая страница
@app.route('/')
def index():
    return render_template('index.html')

#Вторая страница
@app.route('/submit',methods=['POST'])
def submit_form():
    #Переменные
    name = request.form['name']
    try:
      data = pos([0])
      data_back = pos([2])
      data_end = pos([1])
    except:
      data = 'error'
      data_back = 'error'
      data_end = 'error'
    return render_template(
                            'lights.html', 
                            name=name,
                            data = data,
                            data_back = data_back,
                            data_end = data_end
                           )
app.run(debug=True)
