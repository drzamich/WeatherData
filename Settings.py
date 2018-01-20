import datetime
from Helping import *


year = 2016
lat = 52.93
lon = 8.23


use_recent_data= 0
use_offline_data = 0
testing_mode = 1

observedCharacteristics = [
    ['air_temperature', 'TU',[3,4]],                #0
    ['cloudiness', 'N',[4]],                        #1
    ['precipitation', 'RR',[3]],                    #2
    ['pressure', 'P0',[3,4]],                       #3
    ['soil_temperature', 'EB',[3,4,5,6,7,8]],       #4
    ['solar', 'ST',[3,4,5,6,7]],                    #5
    ['sun', 'SD',[3]],                              #6
    ['wind', 'FF',[3,4]]                            #7
]
observations_number = len(observedCharacteristics)

dirpath_offline = 'E:\\DOKUMENTY\\WeatherData\\'
dirpath_ftp = '/pub/CDC/observations_germany/climate/hourly/'
dirpath_downloaded = 'data/download/'

current_date_ts = datetime.datetime.now()

current_date = current_date_ts.strftime('%Y%m%d - %H%M%S')
current_year = current_date_ts.strftime('%Y')
past_year = str(int(current_year)-1)

fmt = '%Y%m%d%H'  # format of the timestamp



