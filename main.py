from flask import Flask , render_template

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
    return render_template("home.html")
    
app.run(host="0.0.0.0")

