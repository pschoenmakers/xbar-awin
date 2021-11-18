#!/usr/bin/python
# <bitbar.title>Awin Sales Summary</bitbar.title>
# <bitbar.version>1.0</bitbar.version>
# <bitbar.author>Paul Schoenmakers</bitbar.author>
# <bitbar.author.github>pschoenmakers</bitbar.author.github>
# <bitbar.desc>Displays your sales for today on the AWIN platform. Perfect for AWIN publishers.</bitbar.desc>
# <bitbar.dependencies>python</bitbar.dependencies>
# <bitbar.image>https://github.com/pschoenmakers/xbar-awin/blob/main/awin-sales-xbar-screenshot.jpg?raw=true</bitbar.image>
# <bitbar.abouturl>https://github.com/pschoenmakers</bitbar.abouturl>
import urllib2
import json

# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from datetime import datetime, time
today = datetime.today().strftime('%Y-%m-%d')

# Insert your publisherid and accesstoken below.
# See https://wiki.awin.com/index.php/API_authentication
# with info how to obtain your API accessToken.

pubid = "YOUR-PUBLISHER-ID"
accessToken = "YOUR-API-ACCESSTOKEN"
region = "de"
timezone = "Europe/Berlin"

response = urllib2.urlopen("https://api.awin.com/publishers/" + pubid + "/reports/advertiser?startDate=" + today +"&endDate=" + today + "&timezone=" + timezone + "&region=" + region + "&accessToken=" + accessToken)
json_data = json.loads(response.read())

clicks = 0
commission = 0
salesnumber = 0


for item in json_data:
    clicks = clicks + item['clicks']
    commission = commission + item['totalComm']
    salesnumber = salesnumber + item['totalNo']

print ("{} {} - {} clicks - {} sales".format(commission,item['currency'],clicks,salesnumber))

# Disable these lines below to only show the stats summary
# if you have a long list of advertisers the dropdown wouldn't make sense.

print("---")

for item in json_data:
    print("{}: {} {} - {} clicks - {} sales".format(item['advertiserName'],item['totalComm'],item['currency'],item['clicks'],item['totalNo']))
