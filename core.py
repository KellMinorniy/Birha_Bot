from bs4 import BeautifulSoup
from selenium import webdriver
import mysql.connector
from config import TOKEN, HOST_DATABASE_HOST, HOST_DATABASE_USERNAME, HOST_DATABASE_PASSWORD, HOST_DATABASE_NAME

# Запросы к базе данных

def dataBaseRequest(query):
    connection = mysql.connector.connect(
        host = HOST_DATABASE_HOST,
        user = HOST_DATABASE_USERNAME,
        password = HOST_DATABASE_PASSWORD,
        database = HOST_DATABASE_NAME
    )

    cursor = connection.cursor()
    cursor.execute(query)
    if 'INSERT' in query or 'UPDATE' in query:
        connection.commit()
    
    
    return cursor.fetchall()

# Верификация через LolzTeam

def Verif(usr , url):
    dr = webdriver.Chrome()
    dr.get(url)
    bs = BeautifulSoup(dr.page_source,"lxml")

    try:
        quotes = bs.find('span', class_='displayIfLanguage displayIfLanguage--1').find('a')['href'].split("=")[1]
        print(quotes)
        if quotes.lower() == usr.lower():
            return True
        else:
            return False
    except:
        print('Ошибка! Нету телеграмма')

    

    





