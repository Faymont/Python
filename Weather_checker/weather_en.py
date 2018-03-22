import re
import urllib.request
import json
from tkinter import *


class Weather(object):
    def get_ip(self):
        data = str(urllib.request.urlopen('http://checkip.dyndns.com/').read())
        return data[data.rfind(' '):-19]

    def get_location(self):
        json_data = urllib.request.urlopen('https://ipinfo.io/json')
        data = json.loads(json_data.read())
        return data['city']

    def get_weather(self):
        key = '0d9724aa4c7bee359a3ca1b7b520c4d0'
        response = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/forecast?q='
                                          + self.get_location() + '&appid=' + key)
        data = json.loads(response.read())
        return data['list'][0]['main']


def main_menu():
    W = Weather()
    root = Tk()
    root.title("Weather")
    root.geometry('360x190')
    root.resizable(False, False)
    ip_label = Label(root, text="Your ip address" + W.get_ip(), width=27, font=15)
    city_label = Label(root, text="Your city " + W.get_location(), width=27, font=15)
    weather_label = Label(root, text="Weather: ", width=500, font=100, bg='white')
    weather_temp = Label(root, text='Temp now:  %0.1f' % (W.get_weather()['temp'] - 273) + 'C',
                         width=500, font=100, bg='white')
    weather_temp_max = Label(root, text='Temp min: %0.1f' % (
    W.get_weather()['temp_max'] - 273) + 'C', width=500, font=100, bg='white')
    weather_temp_min = Label(root, text='Temp max: %0.1f' % (
    W.get_weather()['temp_min'] - 273) + 'C', width=500, font=100, bg='white')
    weather_pressure = Label(root, text='Pressure: %0.1f' % (W.get_weather()['pressure']),
                             width=500, font=100, bg='white')
    weather_humidity = Label(root, text='Humidity: %0.1f' % (W.get_weather()['humidity']),
                             width=500, font=100, bg='white')
    ip_label.pack()
    city_label.pack()
    weather_label.pack()
    weather_temp.pack()
    weather_temp_max.pack()
    weather_temp_min.pack()
    weather_pressure.pack()
    weather_humidity.pack()
    mainloop()


main_menu()
