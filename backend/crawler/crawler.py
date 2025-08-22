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
    pageNum = 1
    while True:
        url = "https://search.trdizin.gov.tr/api/defaultSearch/publication/?q="+keyword+"&order=publicationYear-DESC&page="+str(pageNum)+"&limit=100&facet-documentType=PROJECT"
        x = requests.get(url)
        resultsJson = json.loads(x.text)
        if "error" not in resultsJson:
            records = resultsJson["hits"]["hits"]
            if len(records) <= 0:
                break
            pageNum+=1;

            for record in records:
                item = {}
                _id = "tub-"+record["_id"]
                if _id not in jsonItems:
                    item["_id"] = _id
                    if len(record["_source"]["abstracts"]) > 1:
                        item["title"] = record["_source"]["abstracts"][1]["title"]
                        if "abstract" in record["_source"]["abstracts"][1]:
                            item["summary"] = record["_source"]["abstracts"][1]["abstract"]
                        elif "abstract" in record["_source"]["abstracts"][0]:
                            item["summary"] = record["_source"]["abstracts"][0]["abstract"]
                        else:
                            item["summary"] = ""
                        if "keywords" in record["_source"]["abstracts"][1]:
                            item["keywords"] = record["_source"]["abstracts"][1]["keywords"]
                            if item["keywords"] is None or any("Projede anahtar kelime verilmemiştir" in s for s in item["keywords"]):
                                item["keywords"] = []
                        elif "keywords" in record["_source"]["abstracts"][0]:
                            item["keywords"] = record["_source"]["abstracts"][0]["keywords"]
                            if item["keywords"] is None or any("Projede anahtar kelime verilmemiştir" in s for s in item["keywords"]):
                                item["keywords"] = []
                        else:
                            item["keywords"] = []
                    else:
                        item["title"] = record["_source"]["abstracts"][0]["title"]
                        if "abstract" in record["_source"]["abstracts"][0]:
                            item["summary"] = record["_source"]["abstracts"][0]["abstract"]
                        else:
                            item["summary"] = ""
                        if "keywords" in record["_source"]["abstracts"][0]:
                            item["keywords"] = record["_source"]["abstracts"][0]["keywords"]
                            if item["keywords"] is None or any("Projede anahtar kelime verilmemiştir" in s for s in item["keywords"]):
                                item["keywords"] = []
                        else:
                            item["keywords"] = []
                    if "Projede öz verilmemiştir" in item["summary"]:
                        continue
                    item["endDate"] = datetime.strptime(record["_source"]["endDate"].split("T")[0], "%Y-%m-%d").strftime("%Y-%m-%d")
                    
                    item["language"] = record["_source"]["language"]
                    item["source"] = "https://search.trdizin.gov.tr/tr/yayin/detay/"+str(record["_id"])
                    item["totalCost"] = ""
                    item["ecMaxContribution"] = ""
                    item["duration"] = ""
                    item["database"] = "TUBITAK"
                    item["pdfLink"] = ""
                    jsonItems[_id] = item
        else:
            break

# download_xml(550, 4000)

# for i in range(0,4):
#     items = []
#     wrongItems = []
#     converter(i*1000+1,(i+1)*1000)
#     outputJson("./output/output_"+str(i+1)+".json")
# print(jsonItems)
# items = []
# crawlByKeyword(jsonItems, "mcda")
# print("mcda bitti")
# crawlByKeyword(jsonItems, "mcdm")
# print("mcdm bitti")
# crawlByKeyword(jsonItems, "çkkv")
# print("çkkv bitti")
# crawlByKeyword(jsonItems, "innovation")
# print("innovation bitti")
# crawlByKeyword(jsonItems, "inovasyon")
# print("inovasyon bitti")
# crawlByKeyword(jsonItems, "sürdürülebilirlik")
# print("sürdürülebilirlik bitti")
# crawlByKeyword(jsonItems, "sustainability")
# print("sustainability bitti")
# crawlByKeyword(jsonItems, "çok kriterli")
# print("çok kriterli bitti")
# crawlByKeyword(jsonItems, "multicriteria")
# print("multicriteria bitti")
# crawlByKeyword(jsonItems, "multi-criteria")
# print("multi-criteria bitti")
# crawlByKeyword(jsonItems, "multi criteria")
# print("multi criteria bitti")
# crawlByKeyword(jsonItems, "topsis")
# print("topsis bitti")
# crawlByKeyword(jsonItems, "ahd")
# print("ahd bitti")
# items.extend(jsonItems.values())

# outputJson("./output/output_trdizin.json")

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

for i in range(4):
    print(i)
    inputJson("./output/output_"+str(i+1)+".json")
inputJson("./output/output_trdizin.json")
outputJson("publishes.json")



