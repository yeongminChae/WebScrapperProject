import requests
from bs4 import BeautifulSoup

def search_job(html):
    title = html.a.h2.string.strip()
    company = html.span.h3.string.strip()
    link = "https://remoteok.com/" + html.a['href']
    return {'title' : title, 'company' : company, 'link' : link}

def remoteok_jobs(word):
    url = f"https://remoteok.com/remote-{word}-jobs?hide_closed=true"
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
    result = requests.get(url, headers = header)
    soup = BeautifulSoup(result.text, "html.parser" )
    results = soup.table.find_all('tr', {'class' : 'job'})
  
    jobs_li = []
    for i in results:
        detail_info = i.find('td', {'class' : 'company'})
        jobs_li.append(search_job(detail_info))
    return jobs_li

