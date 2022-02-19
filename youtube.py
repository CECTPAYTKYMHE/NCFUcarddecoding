from textwrap import indent
from youtubesearchpython import VideosSearch
import json

res = []

videosSearch = VideosSearch('NoCopyrightSounds')
while len(res) != 5:
    videosSearch.next()
    res.append(videosSearch.result())
# for i in res[0]['result']['id']:
#     print(i)
# with open('c:/git/NCFUcarddecoding/you.json','w') as file:
#     json.dump(res,file,indent=4)
o = 0
for k in range(0,len(res)):
    for i in range(len(res[k]['result'])):
        print(res[k]['result'][i]['title'])
        o += 1
print(o)
