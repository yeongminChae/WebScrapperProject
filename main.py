from flask import Flask

"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

app = Flask("SuperScrapper")

@app.route("/")
def home():
    return "Hello! welcome to mi casa"

@app.route("/contact")
def contact() :
  return "Contact me!"

app.run(host="0.0.0.0")
