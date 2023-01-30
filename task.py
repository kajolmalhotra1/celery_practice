import json
import pymongo
from celery import Celery

app = Celery("task",
             broker="redis://localhost:6379/0",
             backend="mongodb://localhost:27017/celery_table"
             )

@app.task
def data_push(json_data):
    try:
        connection = pymongo.MongoClient('mongodb://localhost:27017/')
        print("connecestablish")
        db = connection.student
        collection = db.Table1
        print(type(json_data))
        data = json.loads(json_data)
        print(data)
        collection.insert_many(data)
    except Exception as err:
        print(err)


