from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from export import save_job_file
"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

app = Flask("SuperScrapper")
fakeDB = {}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  if word :
    word = word.lower()
    job_DB = fakeDB.get(word)
    if job_DB :
      job_list = job_DB
    else :
      job_list = get_jobs(word)
      fakeDB[word] = job_list
  else :
    return redirect("/")
  return render_template("report.html",searchingBy=word,amount_of_jobs=len(job_list),job_list=job_list)

@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        job_list = fakeDB.get(word)
        if not job_list:
            raise Exception()
        save_job_file(job_list)
        return send_file("job_list.csv") 
    except :
        return redirect("/")

app.run(host="0.0.0.0")


