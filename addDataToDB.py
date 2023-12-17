import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://online-attendance-14b7d-default-rtdb.firebaseio.com/"
})
ref = db.reference('Students')

data = {
    "101":
        {
            "name": "Ayush Raj",
            "major": "CSE",
            "starting": 2021,
            "total_attendance": 6,
            "standing": "A",
            "year": 3,
            "last_time_Attendance": "2023-12-07 00:54:34"
        },
    "102":
        {
            "name": "Shubham Singh",
            "major": "CSE",
            "starting": 2021,
            "total_attendance": 5,
            "standing": "B+",
            "year": 3,
            "last_time_Attendance": "2023-12-07 00:54:10"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
