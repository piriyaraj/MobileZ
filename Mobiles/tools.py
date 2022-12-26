


from distutils.command.build import build
import os
import requests
from bs4 import BeautifulSoup

def findimgurl(soup):
    imgUrls = []
    # firstImg = soup.find("div", class_="specs-photo-main").find("img").get_attribute_list("src")[0]
    # imgUrls.append(firstImg)
    try:
        imgclass = soup.find_all('div', class_="specs-photo-main")[0]
        a_tag = imgclass.find_all('a')[0]
        imglink = "https://www.gsmarena.com/" +a_tag.get_attribute_list('href')[0]
    except:
        imgclass = soup.find_all('div', class_="specs-photo-main")[0]
        imglink = imgclass.find_all('img')[0].get_attribute_list('src')[0]
    reqs = requests.get(imglink)
    soupImg = BeautifulSoup(reqs.text, 'html.parser')

    try:
        picclass = soupImg.findAll("div", id="pictures-list")[0]
        imgtags = picclass.findAll("img")
        for i in imgtags:
            if(i.get_attribute_list("border")[0]==None):
                continue
            img_url = i.get_attribute_list("src")[0]
            if(img_url == None):
                img_url = i.get_attribute_list("data-src")[0]
            imgUrls.append(img_url)
    except Exception as e:
        print(e)
        imgUrls.append(imglink)
    return imgUrls
    
def downloadImages(imgUrlList)->None:
    for i in os.listdir(os.path.abspath("images/")):
        os.remove(os.path.abspath("images/"+i))

    for i in range(len(imgUrlList)):
        reqs = requests.get(imgUrlList[i])
        try:
            soup = BeautifulSoup(reqs.text, 'html.parser')
            picclass=soup.findAll("div",id="pictures-list")[0]
            imgtag=picclass.findAll("img")[0]
            img_url=imgtag.get_attribute_list("src")[0]
            res=requests.get(img_url)
        except:
            res=reqs
        img_title=os.path.abspath("images/"+str(i)+".jpg")
        file = open(img_title,'wb')
        for chunk in res.iter_content(10000):
            file.write(chunk)
        file.close()

def maketable(soup):
    tables=soup.findAll("table")
    dataDict={}
    for i in tables:
        tempDict={}

        for j in i.findAll("tr"):
            if(i.findAll("tr").index(j)==0):
                try:
                    th=j.findAll('th')[0].text
                except:
                    th="PRICE"
            tds = j.findAll("td")
            try:
                key=tds[0].text
                value=tds[1].text.replace("\n","").split("/")
                listvalue=tds[1].text.replace("\n","")
                value.reverse()
                value=" ||".join(value)
                value=value.split(",")
                value.reverse()
                value=", ".join(value)
                value=value.split(":")
                value.reverse()
                value=" ||".join(value)
                tempDict[key]=value
            except:
                break


        dataDict[th]=tempDict
        
    return dataDict


def run(soup):
    # link="https://www.gsmarena.com/oneplus_10_pro-11234.php"
    # reqs = requests.get(link)
    # soup = BeautifulSoup(reqs.text, 'html.parser')
    downloadImages(findimgurl(soup))
    dataDict=maketable(soup)
    phoneName = soup.title.text.split(" -")[0]
    return phoneName,dataDict

def createNewPost(postData):
    try:
        network=postData['Network']
        try:technology=network['TEchnology']
        except:pass
        try:band3g=network['3G bands']
        except:pass
        try:band4g=network['4G bands']
        except:pass
        try:band5g=network['5G bands']
        except:pass
        try:speed=network['speed']
        except:pass
    except:pass
    try:
        lunch=postData['Lunch']
        try:announced=lunch['Announced']
        except:pass
        try:status=lunch['status']
        except:pass
    except:pass
    try:
        body=postData["Body"]
        try:dimension=body['dimension']
        except:pass
        try:weight=body['Weight']
        except:pass
        try:build=body['Build']
        except:pass
        try:sim=body['SIM']
        except:pass
    except:pass
    try:
        display=postData["Display"]
        try:type=display['Type']
        except:pass
        try:size=display['Size']
        except:pass
        try:resolution=display['Resolution']
        except:pass
        try:protection=display['Protection']
        except:pass
    except:pass
    try:
        platform=postData["Platform"]
        try:os=platform['OS']
        except:pass
        try:chipset=platform['Chipset']
        except:pass
        try:cpu=platform['CPU']
        except:pass
        try:gpu=platform['GPU']
        except:pass
    except:pass
    try:
        memory=postData["Memory"]
        try:cartslot=memory['Card slot']
        except:pass
        try:internal=memory['Internal']
        except:pass
    except:pass
    try:
        main_camera=postData["Main Camera"]
        try:mc_triple=main_camera['Triple']
        except:pass
        try:mc_features=main_camera['Features']
        except:pass
        try:mc_video=main_camera['Video']
        except:pass
    except:pass
    try:
        selfie_camera=postData["Selfie camera"]
        try:sc_single=selfie_camera['Single']
        except:pass
        try:sc_features=selfie_camera['Features']
        except:pass
        try:sc_video=selfie_camera['Video']
        except:pass
    except:pass
    try:
        sound=postData["Sound"]
        try:loudspeaker=sound['Loudspeaker']
        except:pass
        try:jack=sound['3.5mm jack']
        except:pass
    except:pass
    try:
        comms=postData["Sound"]
        try:wlan=comms['WLAN']
        except:pass
        try:bluetooth=comms['Bluetooth']
        except:pass
        try:positioning=comms['Positioning']
        except:pass
        try:nfc=comms['NFC']
        except:pass
        try:radio=comms['Radio']
        except:pass
        try:usb=comms['USB']
        except:pass
    except:pass
    try:
        features=postData["Features"]
        try:sensors=features['Sensors']
        except:pass
       
    except:pass
    pass
if __name__=="__main__":
    link="https://www.gsmarena.com/oneplus_10_pro-11234.php"
    reqs = requests.get(link)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    downloadImages(findimgurl(soup))
    dataDict=maketable(soup)
