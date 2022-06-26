from indeed import indeed_jobs as get_indeed
from weworkremotely import weworkremotely_jobs as get_weworkremotely
from remoteok import remoteok_jobs as get_remoteok

def get_jobs(word):
  indeed = get_indeed(word)
  weworkremotely = get_weworkremotely(word)
  remoteok = get_remoteok(word)  
  
  all_jobs = weworkremotely + remoteok + indeed
  return all_jobs
