import requests
from bs4 import BeautifulSoup

def search_job(html):
    title = html.find('span', {'class' : 'title'}).string.strip()
    company = html.find('span', {'class' : 'company'}).string.strip()
    link = "https://weworkremotely.com/" + html.a['href']
    return {'title' : title, 'company' : company, 'link' : link}

def weworkremotely_jobs(word):
    url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser" )
    results = soup.find_all("section", {'class' : 'jobs'})
  
    jobs_li = []
    for i in results:
        ul = i.find_all('ul')
        for j in ul:
            class_1 = j.find_all('li', {'class' : ""}, recursive = False) 
            class_2 = j.find_all('li', {'class' : 'feature'})            
            li = class_1 + class_2
            for k in li:
                jobs_li.append(search_job(k))
    return jobs_li

