from flask import Flask, render_template, json, request, abort
import requests

app = Flask(__name__)
history = []

@app.route("/")
def main():
    return render_template('home.html')


@app.route('/queryCity', methods=['GET','POST'])
def queryCity():

    _city = request.form['city']

    key = "dfde3e873b7b4b3690aefd2d139fea91"  # heweather key
    url = "https://free-api.heweather.com/v5/now?city=%s&key=%s" % (
        _city, key)  # url for checking real-time weather

    try:

        r = requests.get(url)
        data = json.loads(json.dumps(r.json()))

        weather_result = (
            _city + "天气" + data['HeWeather5'][0]['now']['cond']['txt'] +
            ","  # print the weather
            + "风向为" + data['HeWeather5'][0]['now']['wind']['dir'] +
            ","  # print the wind direction
            + "气温为" + data['HeWeather5'][0]['now']['tmp'] +
            "摄氏度,"  # print the temperature
            + "更新时间为" + data['HeWeather5'][0]['basic']['update']['loc'] + "。"
        )  # print the update time

        history.append('\n' + weather_result)
        return weather_result
    except:
        abort(500)

@app.route('/showHistory', methods = ['GET'])
def showHistory():
    return json.dumps(history)


@app.route('/showHelp')
def showHelp():
    return render_template('help.html')


if __name__ == "__main__":
    app.run(debug=True)
