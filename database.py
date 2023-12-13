from typing import Any
from pymongo import MongoClient

my_client = MongoClient(
    host="mongodb+srv://dp950810:Vxxtzwwh91WZ2aZw@cluster0.hlhsyvo.mongodb.net/?retryWrites=true&w=majority")
my_db = my_client["link_extractor_db"]  # selecting the database

def addUser(user_id: int, first_name: str, last_name: str, user_name: str) -> None:
    my_col = my_db["users"]
    #Finding if the user_id of the user is in the collection (Table), if found, assigning it to user variable.
    user = my_col.find_one({"user_id": user_id}) 
    #Checking if the user_id matches with the one from the Collection (Table).
    #If the user_id is not in the Collection (Table), the below statement adds the user to the Collection (Table).
    if user is None:
        my_dict = {
        "user_id": user_id,
        "first_name": first_name,
        "last_name": last_name,
        "user_name": user_name,
    }
        my_col.insert_one(my_dict)
    elif user["user_id"] == user_id:
        updateUser(user_id, first_name, last_name, user_name)
        

def updateUser(user_id: int, first_name: str, last_name: str, user_name: str) -> None:
    """
    Update a User in the collection (Table).
    """
    my_col = my_db["users"]
    to_update = {
        "user_name": user_name,
        "first_name": first_name,
        "last_name": last_name,
    }
    my_col.update_one({"user_id": user_id}, {"$set": to_update})
