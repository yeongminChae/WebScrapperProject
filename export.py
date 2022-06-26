import csv

def save_job_file(job_list):
    file = open("job_list.csv", mode="w", encoding='utf-8-sig')
    writer = csv.writer(file)
    writer.writerow(["Title", "Company", "Link"])
    for i in job_list:
        writer.writerow(list(i.values()))
    return
