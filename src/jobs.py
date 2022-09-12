from functools import lru_cache
import csv


@lru_cache
def read(path: str):
    jobs_list = []
    with open(path, encoding="utf8") as file:
        content = csv.DictReader(file, delimiter=",", quotechar='"')
        for job in content:
            jobs_list.append(job)

    return jobs_list


print(read("src/jobs.csv"))
