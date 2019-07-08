# warsztaty_5_1
Twitter-like application

A) The aim of this project is to write a full and functional twitter-like application.
The application implements the following functions:

1) Users: As a user you can create an account, modify some personal information and delete your account.
Users are identifiable by their email (it must be unique).

2) Posts: Every user can create an arbitrary number of posts.

3) Comments: beneath each post other users can leave their comments

4) Messages: Every user can send a message to any other user. 

B) Installation Guide:

1. Go to the directory with the program:
cd path/to/the program
2. create a virtual environment:
virtualenv -p python3 env
3. install dependencies:
python3 install -r requirements.py
4. create database ‘warsztaty_5_1’
>> sudo su - postgres
>> psql
>> CREATE DATABASE warsztaty_5_1;
5. Open the file settings.py.
Find the dictionary 'DATABASES' and change the values of the keys 'USER' and 'PASSWORD' adequately.