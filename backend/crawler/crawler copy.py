from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from xml.dom import minidom
import requests
import json
import time
from datetime import datetime
from pathlib import Path
items = [] # The Projects in JSON format
jsonItems = {}
wrongItems = []

max_download_space_bytes = 100 * 1024 * 1024 * 1024
page_name = "https://cordis.europa.eu/search?q=(%2Farticle%2Frelations%2Fcategories%2Fcollection%2Fcode%3D%27resultsPack%27%2C%27projectsInfoPack%27%2C%27brief%27%20OR%20(%2Fresult%2Frelations%2Fcategories%2Fcollection%2Fcode%3D%27deliverable%27%2C%27publication%27%20OR%20contenttype%3D%27project%27))%20AND%20(%27SUSTAINABILITY%27%20OR%20%27INNOVATION%27%20OR%20%27MULTI-CRITERIA%27)&p="

def download_xml(page_beg, page_end):
    page = page_beg
    total_file_size = 0
    while page <= page_end:
        print("--- Downloading Page " + str(page) + " ---")
        try:
            r = requests.get(page_name + str(page) + "&num=50&srt=Relevance:decreasing&format=xml", timeout=120)
            open("./downloads/cordis_" + str(page) + ".xml", 'wb').write(r.content)
            total_file_size += Path("./downloads/cordis_" + str(page) + ".xml").stat().st_size
            print(total_file_size)
            page += 1
        except Exception as e:
            print(e)
            print("Timed Out. Retrying in 10 sec")
            time.sleep(10)
            continue
        if total_file_size > max_download_space_bytes:
            break


def converter(page_beg, page_end):
    print("--- Converting Files to Json  ---")
    for file_num in range(page_beg, page_end + 1):
        print(" -- Page " + str(file_num)) 
        # parse an xml ile by name
        file_name = './downloads/cordis_' + str(file_num) +  '.xml'
        try:
            file = minidom.parse(file_name)
        except:
            wrongItems.append(file_num)
            continue
        projects = file.getElementsByTagName('project')
        for proj in projects:
            projId = proj.getElementsByTagName('id')[0].firstChild.nodeValue
            try:    # If the title or the summary does not exists, then skip this project
                title = proj.getElementsByTagName('title')[0].firstChild.nodeValue
                summary = proj.getElementsByTagName('objective')[0].firstChild.nodeValue
            except IndexError:
                continue

            try:    # If the keywords do not exits, then leave them empty
                keywords = proj.getElementsByTagName('keywords')[0].firstChild.nodeValue
            except IndexError:
                keywords = ""
            
            try:    # If the lang does not exits, then leave it empty
                language = proj.getElementsByTagName('language')[0].firstChild.nodeValue
            except IndexError:
                language = ""
            
            try:    # If the lang does not exits, then leave it empty
                totalCost = proj.getElementsByTagName('totalCost')[0].firstChild.nodeValue
            except IndexError:
                totalCost = ""
            
            try:    # If the lang does not exits, then leave it empty
                ecMaxContribution = proj.getElementsByTagName('ecMaxContribution')[0].firstChild.nodeValue
            except IndexError:
                ecMaxContribution = ""
            
            try:    # If the lang does not exits, then leave it empty
                duration = proj.getElementsByTagName('duration')[0].firstChild.nodeValue
            except IndexError:
                duration = ""
                
            try:    # If the lang does not exits, then leave it empty
                endDate = proj.getElementsByTagName('endDate')[0].firstChild.nodeValue
            except IndexError:
                endDate = ""
                
            source = "https://cordis.europa.eu/project/id/" + proj.getElementsByTagName("id")[0].firstChild.nodeValue
            items.append({\
                "_id": "cor-"+projId, \
                "title": title, \
                "summary": summary, \
                "keywords": keywords, \
                "source": source, \
                "language": language, \
                "totalCost": totalCost, \
                "ecMaxContribution": ecMaxContribution, \
                "duration": duration, \
                "pdfLink": source+"?format=pdf", \
                "database": "CORDIS",\
                "endDate": endDate\
                })

def outputJson(filename):
    # Write to json file
    with open(filename, "w") as f:
        json.dump(items, f)
    print("--- Done ---")
    
def outputWrong(filename):
    # Write to json file
    with open(filename, "w") as f:
        json.dump(wrongItems, f)
    print("--- Done ---")

def crawlByKeyword(jsonItems, keyword):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        url = "https://search.trdizin.gov.tr/tr/yayin/ara?q="+keyword+"&order=publicationYear-DESC&page=1&limit=100&facet-documentType=PROJECT"
        page.goto(url)
        page.wait_for_load_state("networkidle")
        htmlStr = page.content()
        soup = BeautifulSoup(htmlStr, 'html.parser')
        records = soup.find_all('div', class_='latex mb-2 ps-1 pe-4 pt-4 pb-4 search-result ng-star-inserted')
        

        for record in records:
            link = record.find('a')["href"]
            newUrl = "https://search.trdizin.gov.tr/"+link
            page.goto(newUrl)
            page.wait_for_load_state("networkidle")
            htmlStr = page.content()
            soup = BeautifulSoup(htmlStr, 'html.parser')
            f = open("dummy.txt","w", encoding='utf-8')
            f.write(htmlStr)
            f.close()
            item = {}
            _id = "tub-"+ soup.find_all('strong', class_='dark-blue')[2].find_next('label').text.strip()
            if _id not in jsonItems:
                item["_id"] = _id
                item["title"] = soup.find('h4', class_='title').text.strip()
                item["summary"] = soup.find('div', class_='mt-2 font-noto-light').find('p').text.strip()
                if "Projede öz verilmemiştir" in item["summary"]:
                    continue
                item["endDate"] = soup.find_all('strong', class_='dark-blue')[3].find_next('label').text.strip()
                item["keywords"] = []
                keywords = soup.find('div', class_='cards').find_all('button', class_='card-button zoom-05')
                for keyword in keywords:
                    item["keywords"].append(keyword.text.strip())
                item["language"] = soup.find_all('strong', class_='dark-blue')[4].find_next('label').text.strip()
                item["source"] = newUrl
                item["totalCost"] = ""
                item["ecMaxContribution"] = ""
                item["duration"] = ""
                item["database"] = "TUBITAK"
                if(record["pdfLink"] != ""):
                    item["pdfLink"] = record["pdfLink"]
                else:
                    item["pdfLink"] = ""
                jsonItems[_id] = item

        browser.close()
#download_xml(0, 0)

for i in range(0,0):
    items = []
    wrongItems = []
    converter(i*1000+1,(i+1)*1000)
    outputJson("./output/output_"+str(i+1)+".json")

items = []
crawlByKeyword(jsonItems, "mcda")
print("mcda bitti")
crawlByKeyword(jsonItems, "mcdm")
print("mcdm bitti")
crawlByKeyword(jsonItems, "çkkv")
print("çkkv bitti")
crawlByKeyword(jsonItems, "innovation")
print("innovation bitti")
crawlByKeyword(jsonItems, "inovasyon")
print("inovasyon bitti")
crawlByKeyword(jsonItems, "sürdürülebilirlik")
print("sürdürülebilirlik bitti")
crawlByKeyword(jsonItems, "sustainability")
print("sustainability bitti")
crawlByKeyword(jsonItems, "çok kriterli")
print("çok kriterli bitti")
crawlByKeyword(jsonItems, "multicriteria")
print("multicriteria bitti")
crawlByKeyword(jsonItems, "multi-criteria")
print("multi-criteria bitti")
crawlByKeyword(jsonItems, "multi criteria")
print("multi criteria bitti")
crawlByKeyword(jsonItems, "topsis")
print("topsis bitti")
crawlByKeyword(jsonItems, "ahd")
print("ahd bitti")
items.extend(jsonItems.values())

outputJson("./output/output_trdizin.json")

items = []

def outputJson(filename):
    # Write to json file
    with open(filename, "w") as f:
        json.dump(items, f)
    print("--- Done ---")
def inputJson(filename):
    # Write to json file
    with open(filename, "r") as f:
        items.extend(json.load(f))
    print("--- Done ---")

for i in range(47):
    inputJson("./output/output_"+str(i+1)+".json")
inputJson("./output/output_trdizin.json")
outputJson("publishes.json")



