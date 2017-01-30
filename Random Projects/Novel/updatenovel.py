#Brandon Lo
#File that continiously runs and updates

#used for time tracking
import praw,time,traceback

#sets up the database
import sqlite3
sqlite_file = 'novel.sqlite'

conn = sqlite3.connect(sqlite_file)
conn.text_factory = str
c = conn.cursor()

#Inserts novel into online novels table
def setOnlineNovel(name, chapter, latest, lang, urlCurrent, latestUrl):
    c.execute("""INSERT INTO ONLINE_NOVELS (NOVEL_NAME, NOVEL_CURRENT, NOVEL_LATEST, NOVEL_LANG, CURRENT_WEBSITE, LATEST_WEBSITE) VALUES (?, ?, ?, ? ,?, ?)""", (name.upper(),chapter,latest,lang,urlCurrent, latestUrl))
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

#Used for gathering all the novel
def gatherOnlineNovelNames():
    c.execute("""SELECT NOVEL_NAME FROM ONLINE_NOVELS""")
    result = c.fetchall()
    novelNames = [novels[0] for novels in result]
    return novelNames

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
    server.login("kenshin421","sircadgon2.")
    try:
        server.sendmail(fromaddress, toaddress, msg)
        print "Everything went well! Email sent!"
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

#Updates the novel if it appears on the front page of novel updates
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

            subject = "Your novel " + Title.upper() + " has been updated!"
            messageContent = "Your novel "+ Title.upper() +" has been updated! \nThe new chapter is on " + str(finalChapterNumber) + ".\nAt this link "+ finalWebLink +"\nI am your faithful servent. You fucking weeb. \n~SneakyWeeb."
            emailMessage(messageContent, subject)

#Main function. Has a commented out area for debugging.
def main():
    try:
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        novelList = gatherOnlineNovelNames()
        subject = "Update Running"
        messageContent = "VoHiYo I'm checking VoHiYo..."
        emailMessage(messageContent, subject)
        for items in novelList:
            novelUpdate(items)
        conn.close()
    except KeyError:
        print "KeyError!"
    except AttributeError:
        print "Novel Attritube Note Found!"
    except UnicodeEncodeError:
        print "Unicode encountered!"

if __name__ == "__main__": main()
