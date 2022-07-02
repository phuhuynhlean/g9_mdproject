from flask import Flask, render_template, request
from models import *

app = Flask(__name__)


@app.route("/")
def home():
    sensor_list = ['node2', 'node6']
    my_sensor_data = []
    pm25 = []
    temp = []
    hum = []

    # default node is 'node2'

    sensor_name = request.args.get("choose_node")
    if request.args.get("choose_node") == []:
        sensor_name = 'node2'

    for sensor in sensor_list:
        my_sensor = MyNode(sensor)
        my_sensor.get_last_data()

        my_sensor_data.append(my_sensor.node_data)

        #get data for graphing chosen sensor
        if sensor == sensor_name:
            my_sensor.get_data_for_graph()
            pm25 = my_sensor.node_data_pm25
            temp = my_sensor.node_data_temp
            hum = my_sensor.node_data_hum

    return render_template("index.html", data=my_sensor_data, pm25=pm25, hum=hum, temp=temp, name=sensor_name, date_time=my_sensor.date_time)


@app.route("/ourteam")
def ourteam():
    return render_template("team.html", members=members)


if __name__ == "__main__":
    app.run(debug=True)
