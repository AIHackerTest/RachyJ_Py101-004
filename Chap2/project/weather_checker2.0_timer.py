
import requests
import json
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import configparser

def get_city():
    config = configparser.ConfigParser()
    config.read('weather_checker2.0_timer.ini')
    city = config['location']['city']
    return city

def talk_with_api():
    key = "dfde3e873b7b4b3690aefd2d139fea91"  # heweather key
    city = get_city()  # "hangzhou"
    # city = input("请输入城市名查询天气情况>")
    url = "https://free-api.heweather.com/v5/now?city=%s&key=%s" % (
        city, key)  # url for checking real-time weather
    r = requests.get(url)
    return r.json()

def retrive_data():
    print('This job is to run every weekday at specified time:'+
        str(datetime.datetime.now()))

    try:
        parse_data(talk_with_api())
    except ValueError:
        print("Fail to query the weather data.")


def parse_data(source_data):
    data = json.loads(
        json.dumps(source_data)
    )  # json.dumps take a dictionary as input and returns a string as output; loads reverts
    weather_result = (
        "hangzhou" + "天气" + data['HeWeather5'][0]['now']['cond']['txt'] +
        ","  # print the weather
        + "风向为" + data['HeWeather5'][0]['now']['wind']['dir']
        + ","  # print the wind direction
        + "气温为" + data['HeWeather5'][0]['now']['tmp']
        + "。"  # print the temperature
        + "更新时间" + data['HeWeather5'][0]['basic']['update']['loc']+ "。"
    )  # print the update time
    print(weather_result)


sched = BlockingScheduler()
#  check the weather each week day at sepecified time till 2018-05-05
sched.add_job(
    retrive_data,'cron',
    day_of_week = 'mon-fri',
    hour = 21,
    minute = 1,
    end_date = '2018-05-05'
)

sched.start()
