import streamlit as st
import os
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client["cloud_storage"]
users_collection = db["users"]

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

st.title("☁️ Cloud Storage System")


username = st.text_input("Enter Username")

uploaded_file = st.file_uploader("Upload a file")

if uploaded_file and username:
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)

    
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    
    users_collection.update_one(
        {"name": username},
        {
            "$push": {
                "files": {
                    "name": uploaded_file.name,
                    "size": uploaded_file.size
                }
            }
        },
        upsert=True
    )

    st.success("File uploaded successfully!")

if username:
    user = users_collection.find_one({"name": username})
    
    if user and "files" in user:
        st.subheader("Your Files")
        for file in user["files"]:
            st.write(file["name"], "-", file["size"], "bytes")