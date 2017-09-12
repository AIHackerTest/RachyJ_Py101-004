# create a list for storing history query
history = []

# create a dict for holding the whether info
weather_dict = {}


# source_data = open("weather_info.txt")
with open("weather_info.txt", "r") as source_data:  # optimize using with..as, not need to call close file

	for item in source_data.readlines():
		pair = item.split(',')
		#print(pair)
		city_item = pair.pop(0)
		whether_item = pair.pop(-1)
		# insert the data into the dict
		weather_dict.update({city_item:whether_item})


def check_weather(query):
	try:
		print(weather_dict[query])
		history.append(query)

	except:
		print("City or command not found")


def program_help():
	print("""
	 输入城市，获得天气信息；
	 输入help或h，获得帮助提示；
	 输入history，获取历史查询信息；
	 输入exit，退出程序；
	""")


def get_history():
	#print("history query info")
	print(history)


while True:
	query = input("请输入指令或您要查询的城市名：")
	# print(query)
	# history.append(query)

	if query =='help' or query =='h':
		program_help()
	elif query == 'history':
		get_history()
	elif query == 'exit':
		exit(0)
	else:
		check_weather(query)
