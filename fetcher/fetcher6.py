#!/bin/bash
# midday_national
import BeautifulSoup
import curl
crl = curl.Curl()
print "Fetching Rss Feed.. "
data = crl.get("http://www.mid-day.com/feed_api/rss/articles.php?section=news/national")
doc = BeautifulSoup.BeautifulStoneSoup(data)
i = 0
for link in doc.findAll('link')[2:4]:
	url = str(link.findAll(text=True)[0])
	print "Fetching data " + str(i) + " " + url
	data = crl.get(url)
	data = BeautifulSoup.BeautifulSoup(data)
	content = data.find("div",{"id":"ar_fulltext.pt15.content_articel_body"})
	print "Writing File"
	fp = open("temp-middaynatnl-" + str(i),'w')
	for pdata in content.findAll("p"):
		temp = pdata.findAll(text=True)
		if len(temp) > 0 :
			fp.write(temp[0].encode("ascii","ignore"))
	i = i + 1

