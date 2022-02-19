from youtube_search import YoutubeSearch
import json
import csv
import pandas as pd
import time
def like(video_url):
    from requests_html import HTMLSession 
    from bs4 import BeautifulSoup as bs # importing BeautifulSoup
    import re,json
    # sample youtube video url
    # init an HTML Session
    session = HTMLSession()
    # get the html content
    response = session.get(video_url)
    # execute Java-script
    response.html.render(sleep=1)
    # create bs object to parse HTML
    soup = bs(response.html.html, "html.parser")
    result = {}
    # Additional video and channel information (with help from: https://stackoverflow.com/a/68262735)
    data = re.search(r"var ytInitialData = ({.*?});", soup.prettify()).group(1)
    data_json = json.loads(data)
    videoPrimaryInfoRenderer = data_json['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']
    # videoSecondaryInfoRenderer = data_json['contents']['twoColumnWatchNextResults']['results']['results']['contents'][1]['videoSecondaryInfoRenderer']
        # number of likes
    likes_label = videoPrimaryInfoRenderer['videoActions']['menuRenderer']['topLevelButtons'][0]['toggleButtonRenderer']['defaultText']['accessibility']['accessibilityData']['label'] # "No likes" or "###,### likes"
    likes_str = likes_label.split(' ')[0].replace(',','')
    return likes_str

def searcher():
    i = 200
    res = YoutubeSearch('kek', max_results=i).to_dict()
    print(res)
    # for k in range(i):
    #     # likes = like('https://www.youtube.com/' + res[k]['url_suffix'])
    #     # res[k]['likes'] = likes
        
    #     with open('C:/GIT/NCFUcarddecoding/file.csv','a',newline='',encoding='utf-8') as f:
    #         w = csv.DictWriter(f,res[k].keys())
    #         # w.writeheader()
    #         w.writerow(res[k])
    #         time.sleep(0.5)
        

searcher()



