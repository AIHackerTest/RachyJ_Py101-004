import requests
import json


# create a list for storing history query
history = []


def retrive_data(query):
    key = "dfde3e873b7b4b3690aefd2d139fea91"  # heweather key
    # city = input("请输入城市名查询天气情况>")
    url = "https://free-api.heweather.com/v5/now?city=%s&key=%s" % (
        query, key) # url for checking real-time weather

    try:
        r = requests.get(url)
        #history.append(query)
    except ValueError:
        print("Fail to query the weather data.")

    parse_data(r.json())


def parse_data(source_data):
    data = json.loads(
        json.dumps(source_data)
    )  # json.dumps take a dictionary as input and returns a string as output; loads reverts
    weather_result = (
        query + "天气" + data['HeWeather5'][0]['now']['cond']['txt'] +
        ","  # print the weather
        + "风向为" + data['HeWeather5'][0]['now']['wind']['dir'] +
        ","  # print the wind direction
        + "气温为" + data['HeWeather5'][0]['now']['tmp'] +
        "。"  # print the temperature
        + "更新时间" + data['HeWeather5'][0]['basic']['update']['loc'] + "。"
    )  # print the update time
    print(weather_result)
    history.append(weather_result)


def program_help():
    print("""
        输入城市，获得天气信息；
        输入help或h，获得帮助提示；
        输入history，获取历史查询信息；
        输入exit，退出程序；
        """)


def get_history():
    print(history)


while True:
    query = input("请输入指令或您要查询的城市名：")

    if query in ['help', 'h']:
    	program_help()
    elif query == 'history':
    	get_history()
    elif query == 'exit':
    	exit(0)
    else:
    	try:
    		retrive_data(query)
    	except:
    		print(
                "Invalid command. Type 'help' to check the available commands."
            )
