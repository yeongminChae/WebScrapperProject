import requests
from bs4 import BeautifulSoup

def search_job(html):
    title = html.find("div", {"class": "post-list-info"}).find("a")["title"]
    company = html.find("div", {"class": "post-list-corp"}).find("a").get_text()
    link = html.find("div", {"class": "post-list-info"}).find("a")["href"]
    return {"company": company, "title": title, "link": f"https://www.jobkorea.co.kr{link}"}
    

def indeed_jobs(word):
    url = f"https://www.jobkorea.co.kr/search/?stext={word}"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find("div", {"class": "list-default"}).find_all("li")
    
    jobs = []
    for i in results:
        jobs.append(search_job(i))
    return jobs

