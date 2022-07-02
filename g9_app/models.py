import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from math import floor

cred = credentials.Certificate("zzz_key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://aqimonitoringsystem-default-rtdb.firebaseio.com/'
})


class MyNode():
    def __init__(self, name):
        self.node_name = name
        self.date_time = 0
        self.node_data = []
        self.node_data_pm25 = []
        self.node_data_temp = []
        self.node_data_hum = []

    def get_last_data(self):
        snapshot = db.reference(self.node_name).order_by_key().limit_to_last(1).get()
        print('Snapshot:')
        print(snapshot)
        for key, val in snapshot.items():
            self.date_time = key
            self.node_data.append(self.node_name)
            self.node_data.append(int(val['pm25']))
            self.node_data.append(int(val['temp']))
            self.node_data.append(int(val['hum']))
            self.node_data.append(int(val['alt']))
            self.node_data.append(val['lati'][:5])
            self.node_data.append(val['longi'][:5])
    def get_data_for_graph(self):
        snapshot = db.reference(self.node_name).order_by_key().limit_to_last(60).get()
        for key, val in snapshot.items():
            #limit the maximum pm25 value
            for key, val in snapshot.items():
                if int(val['pm25']) < 1000:
                    self.node_data_pm25.append(int(val['pm25']))
                    last_pm25 = int(val['pm25'])
                else:
                    self.node_data_pm25.append(last_pm25)
            self.node_data_temp.append(int(val['temp']))
            self.node_data_hum.append(int(val['hum']))

# Group 9
g9_nhu = {
    'name': 'Phan Tâm Như',
    'id': '10421122',
    'dob': '15/08/2003',
    'address': 'district 8'
}
g9_thuan = {
    'name': 'Nguyễn Minh Thuận',
    'id': '10421057',
    'dob': '22/10/2003',
    'address': 'Binh Thanh district'
}
g9_tien = {
    'name': 'Nguyễn Xuân Tiến',
    'id': '10421058',
    'dob': '22/10/2003',
    'address': 'Binh Thanh district'
}
g9_phu = {
    'name': 'Huỳnh Lê An Phú',
    'id': '10421100',
    'dob': '22/10/2003',
    'address': 'Binh Thanh district'
}

g9_phuc = {
    'name': 'Hồ Duy Phúc',
    'id': '10421048',
    'dob': '07/02/2003',
    'address': 'Tien Giang'
}

members = [g9_phu, g9_phuc, g9_nhu, g9_thuan, g9_tien]
