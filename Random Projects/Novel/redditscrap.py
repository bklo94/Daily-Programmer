#bklo94
#simple bot to look at sales thread on reddit and alert myself

import praw,time,sqlite3,traceback

#for the email
import smtplib

#for web scrapping
import httplib2
from bs4 import BeautifulSoup

def getChapter(webpage):
    grabContent = BeautifulSoup(webpage, 'html.parser')
    output = grabContent.find_all('td')
    count = 0
    for chapter in output:
        Title = chapter.get_text()
        count = count + 1
        if Title == 'Martial God Asura' :
            print Title
            chapterNumber = count
            print output[count].get_text()
    
def getArticle(webpage):
    if webpage:
        h = httplib2.Http('.cache')
        content = h.request(webpage)
        return content

def main():
    url = "http://www.novelupdates.com/"
    content = getArticle(url)
    #h = httplib2.Http('.cache')
    #content = h.request(url
    try:
        getChapter(str(content))
    except KeyError:
        print "KeyError"
    except AttributeError:
        pass
    
if __name__ == "__main__": main()

