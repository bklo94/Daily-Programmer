#Brandon Lo
#Backend for the Novel Tracking App

import praw,time,traceback

#sets up the database
import sqlite3
sqlite_file = 'novel.sqlite'

conn = sqlite3.connect(sqlite_file)
conn.text_factory = str
c = conn.cursor()

def createTable():
    c.execute("""CREATE TABLE IF NOT EXISTS ONLINE_NOVELS
        (ID INTEGER PRIMARY KEY AUTOINCREMENT   NOT NULL,
        NOVEL_NAME      TEXT   NOT NULL,
        NOVEL_CURRENT   INT    NOT NULL,
        NOVEL_LATEST    INT    NOT NULL,
        NOVEL_LANG      CHAR(3)   NOT NULL,
        CURRENT_WEBSITE        TEXT   NOT NULL,
        LATEST_WEBSITE         TEXT);""")
    print "Table ONLINE_NOVELS created"

    c.execute("""CREATE TABLE IF NOT EXISTS REAL_NOVELS
        (ID INTEGER PRIMARY KEY AUTOINCREMENT   NOT NULL,
        NOVEL_NAME      TEXT   NOT NULL,
        NOVEL_CURRENT   INT    NOT NULL,
        NOVEL_LATEST    INT    NOT NULL,
        NOVEL_LANG      CHAR(3)   NOT NULL);""")
    print "Table REAL_NOVELS created"

    c.execute("""CREATE TABLE IF NOT EXISTS SEARCH
        (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        NOVEL_NAME      TEXT   NOT NULL,
        NOVEL_CURRENT   INT    NOT NULL,
        NOVEL_LATEST    INT    NOT NULL,
        NOVEL_LANG      CHAR(3)   NOT NULL,
        CURRENT_WEBSITE        TEXT   NOT NULL,
        LATEST_WEBSITE         TEXT);""")
    print "Table SEARCH created"

def setOnlineNovel(name, chapter, latest, lang, urlCurrent):
    c.execute("""INSERT INTO ONLINE_NOVELS (NOVEL_NAME, NOVEL_CURRENT, NOVEL_LATEST, NOVEL_LANG, CURRENT_WEBSITE) VALUES (?, ?, ?, ? ,?)""", (name.upper(),chapter,latest,lang,urlCurrent))
    conn.commit()

def setRealNovel(name, chapter, latest, lang):
    c.execute("""INSERT INTO REAL_NOVELS (NOVEL_NAME, NOVEL_CURRENT, NOVEL_LATEST, NOVEL_LANG) VALUES (?, ?, ?, ? )""", (name.upper(),chapter,latest,lang))
    conn.commit()

def updateCurrentRealNovel(name, chapter):
    c.execute(""" UPDATE REAL_NOVELS
        SET NOVEL_CURRENT = ?
        WHERE NOVEL_NAME = ?""",(chapter,name.upper()))
    conn.commit()

def updateLatestOnlineNovel(name,chapter,url):
    c.execute("""UPDATE ONLINE_NOVELS
        SET NOVEL_LATEST = ?, LATEST_WEBSITE = ?
        WHERE NOVEL_NAME = ? """,(chapter,url,name.upper()))
    conn.commit()

def updateCurrentOnlineChapter(name,chapter,url):
    c.execute("""UPDATE (?)
        SET (NOVEL_CURRENT = ?, CURRENT_WEBSITE = ?
        WHERE NOVEL_NAME = ?""",(chapter,url,name.upper()))
    conn.commit()

def showOnlineTable():
    c.execute("""SELECT * FROM ONLINE_NOVELS""")
    result = c.fetchall()
    for rows in result:
        print rows

def showRealTable():
    c.execute("""SELECT * FROM REAL_NOVELS""")
    result = c.fetchall()
    for rows in result:
        print rows

def gatherOnlineNovelNames():
    c.execute("""SELECT NOVEL_NAME FROM ONLINE_NOVELS""")
    result = c.fetchall()
    return result

#for the email
import smtplib
def emailMessage(messageContent):
    fromaddress = "kenshin421@yahoo.com"
    toaddress = "brandonklo94@gmail.com"
    msg = messageContent
    server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
    server.ehlo()
    server.starttls()
    server.login("kenshin421","********")
    server.sendmail(fromaddress, toaddress, msg)
    print "Your mail has been sent"

#for web scrapping
import httplib2
from bs4 import BeautifulSoup

def novelInsert():
    print "1: Online Novels"
    print "2: Real Novels"
    tableOptions = raw_input("Which table do you want to add to:")
    if tableOptions == "1":
        table = "ONLINE_NOVELS"
    elif tableOptions == "2":
        table = "REAL_NOVELS"
    name = raw_input("Input the novel name:")
    chapter = int(raw_input("Input current chapter:"))
    latest = int(raw_input("Input latest chapter:"))
    lang = raw_input("Input Language Symbol:")
    urlCurrent = raw_input("Input current chapter URL:")
    if table == "ONLINE_NOVELS":
        setOnlineNovel(name.upper(),chapter,latest,lang,urlCurrent)
    else:
        pass
    conn.commit()
    showOnlineTable()

def novelUpdate(searchItem):
    table = "ONLINE_NOVELS"
    url = "http://www.novelupdates.com/"
    content = getArticle(url)
    grabContent = BeautifulSoup(str(content), "html.parser")
    output = grabContent.find_all("td")
    count = 0
    inputNovel = searchItem

    for chapter in output:
        Title = chapter.get_text()
        count = count + 1
        if Title.upper() == inputNovel:
            chapterNumber = output[count].get_text().split("c")
            #reads the outputted list to get the chapter number
            finalChapterNumber = chapterNumber[1]
            webLink = output[count].find_all("a")

            #reads the outputted list to get the web link
            finalWebLink = webLink[1]['href']
            updateLatestOnlineNovel(Title.upper(),finalChapterNumber,finalWebLink)

def getArticle(webpage):
    if webpage:
        h = httplib2.Http(".cache")
        content = h.request(webpage)
        return content

def main():
    #search = raw_input("Novel:")
    try:
        #novelUpdate(search)
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        #createTable()
        #novelInsert()
        novels = gatherOnlineNovelNames()
        for items in novels:
            temp = ''.join(items)
            novelUpdate(temp)

        showOnlineTable()
        print "Tables updated!"
        conn.close()
    except KeyError:
        print "KeyError"
    except AttributeError:
        print "Novel Attritube Note Found"




if __name__ == "__main__": main()
