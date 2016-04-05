#bklo Webscraper For Slickdeals
import httplib2, re

#Grabs the title and links from slick deals
def grabTags(webpage):
    count = 0
    grabHtmlTags = re.compile('<title>(.{0,200})</title>|<link>(.{0,200})</link>',re.IGNORECASE)
    allTags=re.findall(grabHtmlTags,webpage)

#prints outs the title and links. Cleans title with replace
    for i in allTags:
        print(i[0].replace("\\","").replace("<","").replace("!","").replace("[","").replace("]","").replace(">","") + i[1])
#Has a count to insert a new line
        count = count + 1
        if(count%2 == 0):
            print("\n")
        
#Downloads the webpage
def getArticle(webpage):
    if webpage:
        i =httplib2.Http('cache')
        content = i.request(webpage)
        content = str(content)
        
#Selects the URL And runs
def main():
    url = "http://slickdeals.net/newsearch.php?mode=frontpage&searcharea=deals&searchin=first&rss=1"
    h = httplib2.Http('.cache')
    content = h.request(url)
    grabTags(str(content))


if __name__ == "__main__": main()
