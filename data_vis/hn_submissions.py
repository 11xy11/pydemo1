import requests
from operator import itemgetter

url="https://hacker-news.firebaseio.com/v0/topstories.json"
res=requests.get(url)
print("Status Code:",res.status_code)
data=res.json()
dicts=[]
for row in data[:10]:
    url="https://hacker-news.firebaseio.com/v0/item/"+str(row)+".json"
    res_row=requests.get(url)
    print(res_row.status_code)
    response_dict=res_row.json()
    submission_dict={
        "title":response_dict["title"],
        "link":'http://news.ycombinator.com/item?id='+str(row),
        "comments":response_dict.get("descendants",0)
    }
    dicts.append(submission_dict)

dicts=sorted(dicts,key=itemgetter('comments'),reverse=True)
for dict in dicts:
    print("\nTitle:",dict["title"])
    print("Link:",dict["link"])
    print("Comments:",dict["comments"])