## LIBRARY MANAGEMENT SYSTEM

[![OpenFaaS](https://img.shields.io/badge/Database-Mongodb-darkblue.svg)](https://www.openfaas.com)
[![OpenFaaS](https://img.shields.io/badge/API-FastAPI-darkgreen.svg)](https://www.openfaas.com)
[![OpenFaaS](https://img.shields.io/badge/Language-Python-purple.svg)](https://www.openfaas.com)
[![OpenFaaS](https://img.shields.io/badge/Cloud-MongodbAtlas-brown.svg)](https://www.openfaas.com)


# Description
     This is a backend app created to perform certain basic CRUD operations which are specified below 
     using mongodb(document based database where information is stored in key-value pairs) and fastapi.
       
# Operations
      C - create a new book
      R - Get books,get book by id
      U - update info of the book by id ( update info like user who borrowed, his/her contact info etc.)
      D - delete book by id
 # Project structure
      app 
       |
       |_ _ __init__.py------>This file is an empty file but it tells the project folder with all its 
                              python files is a package.
       |
       |_ _ database.py --> In this file ,the database url is created and db connection is made.
       |
       |_ _ schemas.py -->This file includes pydantic models which is used for data validation.
       |
       |_ _ crud.py -->CRUD stands for Create,Read,Update and Delete.This file contains reusable 
                       functions through which interaction with the data in db is performed.
       |
       |_ _ main.py --> This file is used for integrating all other python files.
       
       
   # Pre requisite
     - FastAPI
     - Python
     - MongoDB
     - MongoDBAtlas
     
   # Working
   
   - Run the following command in the terminal to check how the app works

      ```
          uvicorn main:app --reload
      ```
   - The server will be running at
 
      ```
            http://127.0.0.1:8000
      ```
   - Create an account,create free tier cluster,add user and whitelist IP address to connect mongodb atlas with your application.
   
   # Results 
   
   # Endpoints
   
   ![Alt Text](https://github.com/heera0410/Dummy/blob/master/app/screenshots/endpoints.png)
   
   # swagger UI --> Post
   
   ![Alt Text](https://github.com/heera0410/Dummy/blob/master/app/screenshots/post.png)
 
   # Atlas Dashboard -->Post
   
   ![Alt Text](https://github.com/heera0410/Dummy/blob/master/app/screenshots/post1.png)
   
   # swagger UI ---> Retrieve all the books
   
   ![Alt Text](https://github.com/heera0410/Dummy/blob/master/app/screenshots/retrieve_all1.png)
   
   # Atlas Dashboard --> Retrieve all the books
   
   ![Alt Text](https://github.com/heera0410/Dummy/blob/master/app/screenshots/retrieve_all.png)
   
   # swagger UI ---> Retrieve book by ID
   
   ![Alt Text](https://github.com/heera0410/Dummy/blob/master/app/screenshots/retrieve_by_id.png)
   
   # Atlas Dashboard --> Retrieve book by ID
   
   ![Alt Text](https://github.com/heera0410/Dummy/blob/master/app/screenshots/retrieve_by_id1.png)
   
   # swagger UI ---> Update book by ID
   
   ![Alt Text](https://github.com/heera0410/Dummy/blob/master/app/screenshots/update.png)
   
   # Atlas Dashboard --> Update book by ID
   
   ![Alt Text](https://github.com/heera0410/Dummy/blob/master/app/screenshots/update1.png)
   
   # swagger UI ---> Delete book by ID
   
   ![Alt Text](https://github.com/heera0410/Dummy/blob/master/app/screenshots/delete.png)
   
   # Atlas Dashboard --> Delete book by ID
   
   ![Alt Text](https://github.com/heera0410/Dummy/blob/master/app/screenshots/delete1.png)
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
       
   
       


