from src.jobs import read


def get_unique_job_types(path):
    jobs_data = read(path)
    jobs_types_collection = []
    for job in jobs_data:
        if job["job_type"] not in jobs_types_collection:
            jobs_types_collection.append(job["job_type"])
    return jobs_types_collection


# print(get_unique_job_types('src/jobs.py'))


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    jobs_data = read(path)
    industries_collection = set()
    for job in jobs_data:
        if job["industry"] != "":
            industries_collection.add(job["industry"])
    return industries_collection


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    jobs_data = read(path)
    max_salary = []
    for job in jobs_data:
        if job["max_salary"].isdigit() and job["max_salary"] != "":
            max_salary.append(int(job["max_salary"]))
    print(max_salary)
    return max(max_salary)


def get_min_salary(path):
    jobs_data = read(path)
    min_salary = []
    for job in jobs_data:
        if job["min_salary"].isdigit() and job["min_salary"] != "":
            min_salary.append(int(job["min_salary"]))
    print(min_salary)
    return min(min_salary)


def matches_salary_range(job: dict, salary: int):
    if "min_salary" not in job.keys() or "max_salary" not in job.keys():
        raise ValueError("doesn't exists")
    elif (
        type(job["min_salary"])
        and type(job["max_salary"])
        and type(salary) != int
    ):
        raise ValueError("aren't valid integers")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary can't be greather than max_salary")
    return job["min_salary"] <= salary and job["max_salary"] >= salary


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
