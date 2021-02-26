from lxml import html
import requests
import threading
import time





def getName(txCno):

    
    s=requests.Session()
    data = {"cboOpt": 1,
    "txCno": txCno,
    "cbSdiv": 28,
    "txKno": "Input+K.+No",
    "txMno": "Input+Mobile+No",
    "txBno": "Input+Bill+No"}

    url = "http://secure.urjamitra.in/urjamitra/onlinepay/index.php"

    r = s.post(url)

    header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Length": "91",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "secure.urjamitra.in",
    "Origin": "https://secure.urjamitra.in",
    "Referer": "https://secure.urjamitra.in/urjamitra/onlinepay/index.php",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Sec-GPC": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    }


    r = s.post(url, data=data, headers=header)

    if r.url=="http://secure.urjamitra.in/urjamitra/onlinepay/home.php" :


        tree = html.fromstring(str(r.text))

        tableData = tree.xpath("//tr//text()")

        i=0
        for i in range(len(tableData)):
            if tableData[i] != 'Consumer Name :':
                continue
            else:
                # print (tableData[i+1])
                break
        s.close()
        # print(tableData[i+1])
        f.write(txCno + "," + tableData[i+1] + "\n")
    else:
        s.close()
        # print ("No Record Found!")
        f.write(txCno + "," + "No Record Found!" + "\n")




currentPercent = 0
prefix = input('Enter Prefix here[eg.:PTT]: ')
start = int(input('Enter Starting Point: '))
end = int(input('Enter Ending Point: '))
noOfThreads = 11
initialThreads = threading.activeCount()
f = open("data.csv", 'a')
print ( str(threading.activeCount()))
print ("%03d" %currentPercent+"%", end='')
for i in range(start,end+1):
    currentPercent+=1
    # getName(prefix+str(i))
    print ("\b\b\b\b" + "%03d"%currentPercent + "%", end='')
    while (threading.activeCount() >= noOfThreads):
        time.sleep(1)
    threading.Thread(target=getName, args=(prefix+str(i),)).start()

while (threading.activeCount() != initialThreads):
    time.sleep(2)
time.sleep(2)
f.close()