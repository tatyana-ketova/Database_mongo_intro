
import pymongo
from bson import ObjectId

# Replace these with your MongoDB connection details
host = 'localhost'  # MongoDB server address
port = 27017        # MongoDB server port
database_name = 'mydatabase'  # Name of the database you want to connect to
collection_name = 'mycollection'  # Name of the collection you want to use

# Create a connection to the MongoDB server
client = pymongo.MongoClient(host, port)

# Create or access a specific database
db = client['database_tasks']

# Create or access a specific collection within the database
collection = db['tasks']




def add_task(title, description, status = "ToDo"):
    data = {"title": title, "description": description,"status":status}
    insert_result = collection.insert_one(data)
    print(f"Inserted document ID: {insert_result.inserted_id}")

def list_tasks():
    tasks = collection.find()
    for task in tasks:
        print(task)

def update_task_status(task_id, new_status):
    query = {'_id': ObjectId(task_id)}
    new_values = {"$set": {"status": new_status}}
    collection.update_one(query, new_values)
    print("Task {} status updated to {}".format(task_id, new_status))

def delete_task(task_id):
    query = {'_id': ObjectId(task_id)}
    collection.delete_one(query)
    print("Task {} deleted".format(task_id))


add_task("FigmaTask","Solve 789 task")
list_tasks()
update_task_status("654cbd0ec000a658b3d98c01", "Done")
delete_task("654cb7e81efe9f782de68214")
list_tasks()
