#Brandon Lo
#Backend for the Novel Tracking App

#For futute funtionality.Currently unsued
import praw,traceback

#crontab settings
from crontab import CronTab

def cronUpdate():
    print "VoHiYo I'm checking VoHiYo..."
    cron = CronTab(user=True)
    job = cron.new(command='python updatenovel.py')
    job.minute.every(0)
    cron.write()

#sets up the database
import sqlite3
sqlite_file = 'novel.sqlite'

conn = sqlite3.connect(sqlite_file)
conn.text_factory = str
c = conn.cursor()

#Creates the data if it does not exist.
#Online novels for the web novels
#Real novels for physical books
#Search is temporary table that gets cleared after every use
def createTable():
    c.execute("""CREATE TABLE IF NOT EXISTS ONLINE_NOVELS
        (ID INTEGER PRIMARY KEY AUTOINCREMENT   NOT NULL,
        NOVEL_NAME      TEXT   NOT NULL,
        NOVEL_CURRENT   INT    NOT NULL,
        NOVEL_LATEST    INT    NOT NULL,
        NOVEL_LANG      CHAR(2)   NOT NULL,
        CURRENT_WEBSITE        TEXT   NOT NULL,
        LATEST_WEBSITE         TEXT);""")

    c.execute("""CREATE TABLE IF NOT EXISTS REAL_NOVELS
        (ID INTEGER PRIMARY KEY AUTOINCREMENT   NOT NULL,
        NOVEL_NAME      TEXT   NOT NULL,
        NOVEL_CURRENT   INT    NOT NULL,
        NOVEL_LATEST    INT    NOT NULL,
        NOVEL_LANG      CHAR(2)   NOT NULL);""")

    c.execute("""CREATE TABLE IF NOT EXISTS SEARCH
        (ID INTEGER PRIMARY KEY AUTOINCREMENT   NOT NULL,
        NOVEL_NAME      TEXT   NOT NULL,
        NOVEL_CURRENT   INT    NOT NULL,
        NOVEL_LATEST    INT    NOT NULL,
        NOVEL_LANG      CHAR(2)   NOT NULL,
        CURRENT_WEBSITE        TEXT   NOT NULL,
        LATEST_WEBSITE         TEXT NOT NULL);""")
    conn.commit()

#Inserts novel into Online novels table
from prettytable import PrettyTable

def setOnlineNovel(name, chapter, latest, lang, urlCurrent, latestUrl):
    c.execute("""INSERT INTO ONLINE_NOVELS (NOVEL_NAME, NOVEL_CURRENT, NOVEL_LATEST, NOVEL_LANG, CURRENT_WEBSITE, LATEST_WEBSITE) VALUES (?, ?, ?, ? ,?, ?)""", (name.upper(),chapter,latest,lang,urlCurrent, latestUrl))
    conn.commit()

#Inserts novel into real novels table
def setRealNovel(name, chapter, latest, lang):
    c.execute("""INSERT INTO REAL_NOVELS (NOVEL_NAME, NOVEL_CURRENT, NOVEL_LATEST, NOVEL_LANG) VALUES (?, ?, ?, ? )""", (name.upper(),chapter,latest,lang))
    conn.commit()

#Inserts novel into search table
def setSearchNovel(name, chapter, latest, lang, urlCurrent, urlLatest):
    c.execute("""INSERT INTO SEARCH (NOVEL_NAME, NOVEL_CURRENT, NOVEL_LATEST, NOVEL_LANG, CURRENT_WEBSITE, LATEST_WEBSITE) VALUES (?, ?, ?, ? ,?, ?)""", (name.upper(),chapter,latest,lang,urlCurrent,urlLatest))
    conn.commit()

#Updates a Real Novel when called
def updateCurrentRealNovel(name, chapter):
    c.execute(""" UPDATE REAL_NOVELS
        SET NOVEL_CURRENT = ?
        WHERE NOVEL_NAME = ?""",(chapter,name.upper()))
    conn.commit()

#Updates an online novel latest chapter. Automatically called
def updateLatestOnlineNovel(name,chapter,url):
    c.execute("""UPDATE ONLINE_NOVELS
        SET NOVEL_LATEST = ?, LATEST_WEBSITE = ?
        WHERE NOVEL_NAME = ? """,(chapter,url,name.upper()))
    conn.commit()

#Updates the current online chapter. Manually called
def updateCurrentOnlineChapter(name,chapter,url):
    c.execute("""UPDATE ONLINE_NOVELS
        SET NOVEL_CURRENT = ?, CURRENT_WEBSITE = ?
        WHERE NOVEL_NAME = ?""",(chapter,url,name.upper()))
    conn.commit()

#Moves a search novel to the online novel table
def transferSearchToOnline(name):
    c.execute("""INSERT INTO ONLINE_NOVELS (NOVEL_NAME, NOVEL_CURRENT, NOVEL_LATEST, NOVEL_LANG, CURRENT_WEBSITE, LATEST_WEBSITE)
        SELECT NOVEL_NAME, NOVEL_CURRENT, NOVEL_LATEST, NOVEL_LANG, CURRENT_WEBSITE, LATEST_WEBSITE FROM SEARCH
        WHERE NOVEL_NAME = ?""",(name.upper(),))
    deleteSearchCache()
    conn.commit()

#displays what is currently in the SQL table
def showOnlineTable():
    c.execute("""SELECT * FROM ONLINE_NOVELS""")
    result = c.fetchall()
    novelNames = [novels for novels in result]
    showTable = PrettyTable()
    showTable.padding_width = 1
    showTable.field_names = ["ID","Web Novel Name", "Current Chapter", "Latest Chapter","Language", "Current Chapter URL", "Latest Chapter URL"]
    for rows in novelNames:
        showTable.add_row([rows[0],rows[1],rows[2],rows[3],rows[4],rows[5],rows[6]])
    print (showTable)

#displays what is currently in the SQL table
def showRealTable():
    c.execute("""SELECT * FROM REAL_NOVELS""")
    result = c.fetchall()
    novelNames = [novels for novels in result]
    showTable = PrettyTable()
    showTable.align = "l"
    showTable.padding_width = 1
    showTable.field_names = ["ID","Web Novel Name", "Current Chapter", "Latest Chapter","Language"]
    for rows in novelNames:
        showTable.add_row([rows[0],rows[1],rows[2],rows[3],rows[4]])
    print (showTable)

#displays what is currently in the SQL table
def showSearchTable():
    c.execute("""SELECT * FROM SEARCH""")
    result = c.fetchall()
    novelNames = [novels for novels in result]
    for rows in novelNames:
        print rows

#Used for debugging the novels, currently unsued
def gatherOnlineNovelNames():
    c.execute("""SELECT NOVEL_NAME FROM ONLINE_NOVELS""")
    result = c.fetchall()
    novelNames = [novels[0] for novels in result]
    return novelNames

#Gathers the chapter numbers only
def gatherOnlineChapters(name):
    c.execute("""SELECT NOVEL_LATEST FROM ONLINE_NOVELS WHERE NOVEL_NAME = ?""", (name.upper(),))
    result = c.fetchall()
    novelChaps = [novels[0] for novels in result]
    return novelChaps

#Deletes a certain novel from the online table
def deleteOnlineRow(idNovel):
    c.execute("""DELETE FROM ONLINE_NOVELS WHERE id = ?""", (idNovel,))
    conn.commit()

#Deletes a certain novel from the real table
def deleteRealRow(idNovel):
    c.execute("""DELETE FROM REAL_NOVELS WHERE id = ?""", (idNovel,))
    conn.commit()

#clears the search table
def deleteSearchCache():
    c.execute("""DELETE FROM SEARCH""")
    c.execute("""VACUUM""")
    conn.commit()

#clears the real novel table
def deleteRealTable():
    c.execute("""DELETE FROM REAL_NOVELS""")
    c.execute("""VACUUM""")
    conn.commit()

#clears the online novel table
def deleteOnlineTable():
    c.execute("""DELETE FROM ONLINE_NOVELS""")
    c.execute("""VACUUM""")
    conn.commit()

#for the email
import smtplib

#clears the sends an email with a subject and content
def emailMessage(messageContent,subject):
    fromaddress = "kenshin421@yahoo.com"
    toaddress = "brandonklo94@gmail.com"
    msg = "Subject: %s \n\n%s" % (subject,messageContent)
    server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
    server.ehlo()
    server.starttls()
    server.login("kenshin421","ctfbhsgpqibquoxw")
    try:
        server.sendmail(fromaddress, toaddress, msg)
    except SMTPException:
        print "NotLikeThis. Your email has failed to send! Please notify the admin."
    server.quit()

#for web scrapping
import httplib2
from bs4 import BeautifulSoup
from collections import OrderedDict
from operator import itemgetter

#gets a cache file of the requested webpage
def getArticle(webpage):
    if webpage:
        h = httplib2.Http(".cache")
        content = h.request(webpage)
        return content

#Main function that is run that runs all the others. Honestly could be the the main function
def novelInsert():
    print "1: Online Novels"
    print "2: Real Novels"
    print "3: Search for your novel"
    tableOptions = raw_input("Which table number do you want to add to:")
    if tableOptions == "1" or tableOptions == "2":
        name = raw_input("Input the novel name:")
        chapter = int(raw_input("Input current chapter:"))
        latest = int(raw_input("Input latest chapter:"))
        lang = raw_input("Input Language Symbol:")
        if tableOptions == "1":
            urlCurrent = raw_input("Input current chapter URL:")
            latestURL = raw_input("Input current latest URL:")
            setOnlineNovel(name.upper(),chapter,latest,lang,urlCurrent,latestURL)
            subject = "Your novel " + name.upper() + " has been inserted!"
            messageContent = "Your novel "+ name.upper() +" has been inserted! \nYou are on chapter " + str(chapter) + ". \nAt this link " + urlCurrent + "\nThe latest chapter is " + str(latest) + ".\nAt this link" + latestURL + "\nYou are " + str((latest-chapter)) + " chapters behind.\nI am your faithful servent. You fucking " + lang + "weeb. \n~SneakyWeeb."
            emailMessage(messageContent, subject)
        elif tableOptions == "2":
            setRealNovel(name, chapter, latest, lang)
            subject = "Your novel " + name.upper() + " has been inserted!"
            messageContent = "Your novel "+ name.upper() +" has been inserted! \nYou are on chapter " + str(chapter) + "\nThe latest chapter is " + str(latest) + ".\nYou are " + str((latest-chapter)) + " chapters behind.\nI am your faithful servent. You fucking " + lang + "weeb. \n~SneakyWeeb."
            emailMessage(messageContent, subject)
    elif tableOptions == "3":
        searchTerm = raw_input("What do you want to search for?:")
        novelSearch(searchTerm)

#Updates the novel if it appears on the front page of novel updates
def novelUpdate(searchItem):
    table = "ONLINE_NOVELS"
    url = "http://www.novelupdates.com/"
    content = getArticle(url)
    grabContent = BeautifulSoup(str(content), "html.parser")
    output = grabContent.find_all("td")
    count = 0
    inputNovel = searchItem

    subject = "Update Running"
    messageContent = "VoHiYo I'm checking VoHiYo..."
    emailMessage(messageContent, subject)

    for chapter in output:
        Title = chapter.get_text()
        count = count + 1
        if Title.upper() == inputNovel:
            chapterNumber = output[count].get_text().split("c")
            #reads the outputted list to get the chapter number
            finalChapterNumber = chapterNumber[1]
            currentFinalChapterNumber = gatherOnlineChapters(Title)[0]
            if (int(finalChapterNumber[0]) > int(currentFinalChapterNumber)):
                webLink = output[count].find_all("a")

                #reads the outputted list to get the web link
                finalWebLink = webLink[1]['href']
                updateLatestOnlineNovel(Title.upper(),finalChapterNumber,finalWebLink)

                subject = "Your novel " + Title.upper() + " has been updated!"
                messageContent = "Your novel "+ Title.upper() +" has been updated! \nThe new chapter is on " + str(finalChapterNumber) + ".\nAt this link "+ finalWebLink +"\nI am your faithful servent. You fucking weeb. \n~SneakyWeeb."
                emailMessage(messageContent, subject)
            else:
                pass

#Uses novel update to search for a novel and then add it
def novelSearch(searchTerm):
    table = "SEARCH"
    url = "http://www.novelupdates.com/?s="+ searchTerm +"&post_type=seriesplans"
    content = getArticle(url)
    grabContent = BeautifulSoup(str(content), "html.parser")
    output = grabContent.find_all("h2")
    linkoutput = grabContent.find_all("a")
    inputNovel = searchTerm
    titleList = []
    linkList = []
    novelDict = {}
    count = 0
    for items in output:
        grabTitle = items.find_all('span')
        if grabTitle:
            span = '</span>'
            temp = str(grabTitle[0]).split(span)
            titleList.append(temp[1])

    for items in linkoutput:
        grabLinks = items['href']
        linkList.append(grabLinks)

    for items in range(4,29):
        novelDict[titleList[count]] = [linkList[items],count]
        count = count + 1

    novelDict = sorted(novelDict.items(), key=lambda novelDict: novelDict[1][1])
    #dictionary is 0-23
    for key, value in novelDict:
        print value[1], "\t\t\t", key
    print "25 \t\t\t Exit."
    searchValue = raw_input("Select the novel you want to add:")
    if searchValue == "25":
        exit()
    #known bug when novel name is long, thus makes a file path too long. Windows limimation. Working on Debian (tested), unknown for OSX.
    newNovelList = []
    for key, value in novelDict:
        if int(searchValue) == value[1]:
            name = key
            novelUrl = value[0]
            newNovelList = novelPageUpdate(str(novelUrl))
            chapter = raw_input("What chapter are you currently on?:")
            urlCurrent = raw_input("What is the url you currently on?:")
            setSearchNovel(name, chapter, newNovelList[0], newNovelList[1], urlCurrent, newNovelList[2])
            transferSearchToOnline(name)
            subject = "Your novel " + name.upper() + " has been inserted!"
            messageContent = "Your novel,"+ name.upper() +" , has been inserted! \nYou are on chapter," + str(chapter) + "\nThe latest chapter is," + str(newNovelList[0]) + ".\nThe link is at " + newNovelList[3] + " \nYou are " + str((newNovelList[0]-chapter)) + " chapters behind.\nI am your faithful servent. You fucking " + newNovelList[1] + "weeb. \n~SneakyWeeb."
            emailMessage(messageContent, subject)

#Used with the search function in order to update the latest novel and website
def novelPageUpdate(url):
    content = getArticle(url)
    grabContent = BeautifulSoup(str(content), "html.parser")
    output = grabContent.find_all("a")
    count = 0
    foundLink = 0
    chapterHolder = 0
    languageHolder = ""
    linkHolder = ""
    linkList = []
    returnList = []
    for items in output:
        scanner = items.get_text()
        linkList.append(items['href'])
        chapterSearch = scanner[1:]
        count = count + 1
        if chapterSearch.isdigit():
            temp = chapterSearch
            if temp > chapterHolder:
                chapterHolder = temp
                foundLink = count
        if scanner == "Japanese":
            languageHolder = "JP"
        elif scanner == "Chinese":
            languageHolder = "CN"
        elif scanner == "Korean":
            languageHolder = "KR"

    returnList.append(chapterHolder)
    returnList.append(languageHolder)
    returnList.append(linkList[foundLink])
    return returnList

#drop row function for deleting a novel
def deleteNovel():
    print "1: Online Novels"
    print "2: Real Novels"
    print "0: Exit"
    tableOptions = raw_input("Which table number do you want to delete:")
    if tableOptions == "1":
        showOnlineTable()
        novelID = raw_input("Input Novel ID to delete:")
        deleteOnlineRow(novelID)
    elif tableOptions == "2":
        showRealTable()
        novelID = raw_input("Input Novel ID to delete:")
        deleteRealRow(novelID)
    elif tableOptions == "3":
        exit

#Main function. Has a commented out area for debugging.
def main():
    try:
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        createTable()

        while True:
            print "Option 1: Edit Database"
            print "Option 2: Force Update"
            print "Option 3: Read Database"
            print "Option 0: Exit"
            option = raw_input("What would you like to do? ")
            if  (option == "1"):
                print "Option 1: Insert Novel"
                print "Option 2: Delete Novel"
                secondOption = raw_input("What would you like to do? ")
                if (secondOption == "1"):
                    novelInsert()
                elif (secondOption == "2"):
                    deleteNovel()
            elif (option == "2"):
                novelList = gatherOnlineNovelNames()
                for items in novelList:
                    novelUpdate(items)
                print "Novel update is complete!"
            elif (option == "3"):
                print "Real Novels List\n"
                showRealTable()
                print "Web Novel List\n"
                showOnlineTable()
                print "\n"
            elif (option == "0"):
                break

        conn.close()

    except KeyError:
        print "KeyError!"
    except AttributeError:
        print "Novel Attritube Not Found!"
    except UnicodeEncodeError:
        print "Unicode encountered!"

if __name__ == "__main__": main()
