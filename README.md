## LIBRARY MANAGEMENT SYSTEM

[![OpenFaaS](https://img.shields.io/badge/Database-Mongodb-darkblue.svg)](https://www.openfaas.com)
[![OpenFaaS](https://img.shields.io/badge/API-FastAPI-darkgreen.svg)](https://www.openfaas.com)
[![OpenFaaS](https://img.shields.io/badge/Language-Python-purple.svg)](https://www.openfaas.com)
[![OpenFaaS](https://img.shields.io/badge/Cloud-MongodbAtlas-brown.svg)](https://www.openfaas.com)


# Description
       This is a backend app for library management system created using mongodb and fastapi.
       
# Operations
       C - create a new book
       R - Get books,get book by id
       U - update info of the book by id ( update info like user who borrowed, his/her contact info etc.)
       D - delete book by id
 # Project structure
      app 
       |
       |_ _ __init__.py------> This file is an empty file but it tells the project folder with all its python files is a package.
       |
       |_ _ database.py --> In this file ,the database url is created and db connection is made.
       |
       |_ _ schemas.py -->This file includes pydantic models which is used for data validation.
       |
       |_ _ crud.py -->CRUD stands for Create,Read,Update and Delete.This file contains reusable functions through which interaction with the data in db is performed.
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
       
   
       


