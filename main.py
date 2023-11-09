import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
"""
database = client['Tasks_db']
collection = database["tasks"]

def add_task(title, description, status = "ToDo"):
    pass

def list_tasks():
    pass

def update_task_status(task_id,new_status):
    pass

def delete_task(task_id):
    pass
"""