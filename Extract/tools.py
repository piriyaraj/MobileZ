import requests
from bs4 import BeautifulSoup
from Extract.models import brand, post

def isPublished(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    table = soup.find("div", id="specs-list")
    if(str(soup.title).find("Too Many") > 0):
        return "Too Many Requests"
    print(soup.title.text, end=" :")
    if(table.text.find("soon") < 0):
        print("released")
        return soup
    else:
        print("Not released")
        return False

# get specific brand post links that not in database
def getAllMobilePosts( url, lastPostUrl):
    # print(url)
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    try:
        nextPages = soup.find_all("div", class_="nav-pages")[0].find_all("a")
    except:
        nextPages=[]
    # print(soup.find_all("div", class_="nav-pages"))
    pageLinks = []
    mobileNames = []
    mobileLinks = []
    pageLinks.append(url)
    for i in nextPages:
        pageLink = "https://gsmarena.com/"+i.get_attribute_list("href")[0]
        pageLinks.append(pageLink)

    for i in pageLinks:
        reqs = requests.get(i)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        mobileList = soup.find_all("div", class_="makers")[0]
        mobileListLis = mobileList.find_all("li")
        for i in mobileListLis:
            mobileName = i.text
            postUrl = "https://gsmarena.com/" + i.find("a").get_attribute_list("href")[0]
            if(postUrl == lastPostUrl):
                return mobileNames, mobileLinks
            mobileNames.append(mobileName)
            mobileLinks.append(postUrl)
    
    return mobileNames, mobileLinks

# update database with no of posts for brands
def extractModels():
    reqs = requests.get("https://www.gsmarena.com/makers.php3")
    soup = BeautifulSoup(reqs.text, 'html.parser')
    try:
        mobileList = soup.find_all("table")[0]
    except:
        print("too many request")
        return
    mobileListTds = mobileList.find_all("td")

    for i in mobileListTds:
        mobileCount = i.find("span").text.split(" ")[0]
        mobileBrand = i.find("a").text.split(mobileCount)[0].replace(".", " ")
        # print(i.find("a").get_attribute_list("href"))
        mobileBrandUrl = "https://www.gsmarena.com/" + \
            i.find("a").get_attribute_list("href")[0]

        try:
            brandObj = brand.objects.get(name=mobileBrand)
            if(int(mobileCount) != brandObj.totalpost):
                brandObj.totalpost = int(mobileCount)
                brandObj.havenewpost = True
                brandObj.save()
        except:
            brandObj = brand.objects.create(
                name=mobileBrand, totalpost=int(mobileCount), brandurl=mobileBrandUrl)
    pass

# update post table from brands data in table
# its add new post links in post table
def checkForNewPost():
    brands = brand.objects.filter(havenewpost=True)
    if(len(brands) == 0):
        print("Finding new updates..")
        extractModels()
        brands = brand.objects.filter(havenewpost=True)
        if(len(brands) == 0):
            print("NO new Posts in website")
            return 1
    for brandObj in brands[:1]:
        # print(i.find("a").get_attribute_list("href"))
        try:
            mobileNames, postLinks = getAllMobilePosts(brandObj.brandurl, brandObj.lastpost)
        except Exception as e:
            print(e)
            return

        brandObj.count
        postLinks.reverse()
        for i in postLinks:
            post.objects.create(url=i)
            
        brandObj.lastpost = postLinks[-1]
        brandObj.count = brandObj.count+len(postLinks)
        brandObj.havenewpost = False
        brandObj.save()

# check post table wether the post is released or not
def databasePostReleased():
    posts = post.objects.filter(released=False).order_by('updated')
    for i in posts:
        try:
            result = isPublished(i.url)
        except Exception as e:
            print(e)
            break
        if(result != False):
            i.released = True
            i.save()
        else:
            i.save()


def test():
    posts = post.objects.filter(released=False).order_by('updated')[0]
    posts.save()
    print(posts.url)
