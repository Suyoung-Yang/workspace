import requests
res = requests.get("http://google.com")
res1 = requests.get("http://nadocoding.tistory.com")
print("response: ",res.status_code) #200이면 정상

print("response: ",res1.status_code) #200아니면 비정상

if res.status_code ==requests.codes.ok:
    print("ok")
else:print("problem",res.status_code)

res.raise_for_status() # 문제가 생긴 경우에는 문제를 발생시킨다.
print("stat scrapping")

with open("mygoogle.html","w",encoding="utf8") as f:
    f.write(res.text)
