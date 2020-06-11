from pymongo import MongoClient
from datetime import datetime


class Model:

    def __init__(self, dbUser, dbPass, dbCluster, dbCollection):
        self.cluster = MongoClient(
            f"mongodb+srv://{dbUser}:{dbPass}@cluster0-7sgza.mongodb.net/{dbCluster}?retryWrites=true&w=majority"
        )
        self.db = self.cluster[dbCluster]
        self.collection = self.db[dbCollection]

    def findData(self, data):
        result = self.collection.find_one(data)
        return result

    def addData(self, data):
        self.collection.insert_one(data)

    def usernameCheck(self, username):
        if self.findData({"username": username}):
            return True
        else:
            return False

    def passwordCheck(self, username, password):
        result = self.findData({"username": username})
        if result["password"] == password:
            return True
        else:
            return False

    def signup(self, username, password):
        data = {
            "username": username,
            "password": password,
            "Insert Date": datetime.utcnow()
        }
        self.addData(data)
