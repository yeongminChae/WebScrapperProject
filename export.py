import csv

def save_to_file(job_lists):
    file = open("job_lists.csv", mode="w") 
    writer = csv.writer(file)
    writer.writerow(["Title", "Company", "Link"])
    for i in job_lists:
        writer.writerow(list(i.values()))
    return