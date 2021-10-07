import requests
import pandas
from joblib import Parallel, delayed
from requests.exceptions import ConnectionError
import datetime
import os
import json

list_of_failures = []


def parse_api(url: str):
    """Initial parse. This one returns json data."""
    global list_of_failures
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except ConnectionError:
        print(f"Url: {url} did not work.")
        list_of_failures.append(url)
        return None


def get_job_offers(site: str = 'nofluff' or 'justjoin', save_json: bool = False) -> list or None:
    """Returns either list of all job offers as list of dict or saves it to .json file.
    You need to provide kwarg site='justjoin' or site='nofluff'."""
    if site == 'nofluff':
        url = 'https://nofluffjobs.com/api/posting/'
        filename = os.getcwd() + f'/json/nofluff_{datetime.date.today()}.json'
        func = get_job_offer_details_nofluff
        data = parse_api(url)
        data = data['postings']
    elif site == 'justjoin':
        url = 'https://justjoin.it/api/offers/'
        filename = os.getcwd() + f'/json/justjoin_{datetime.date.today()}.json'
        func = get_job_offer_details_justjoin
        data = parse_api(url)
    else:
        return print("Function needs to have either site='nofluff' or site='justjoin'")
    df = pandas.DataFrame(data)
    id_df = pandas.DataFrame(list(set(df['id'].tolist())), columns=['id'])
    id_df['id'] = id_df['id'].map(lambda x: url + x)
    url_list = id_df['id'].to_list()
    job_offers_list = Parallel(n_jobs=-1)(delayed(func)(url) for url in url_list)
    if save_json:
        with open(filename, "w", encoding="utf-8") as dumpfile:
            dumpfile.write(json.dumps(job_offers_list, default=str))
    print(f"Data from {site} scraped successfully.")
    return job_offers_list


def get_job_offer_details_nofluff(job_url: str) -> dict:
    """Function that gets details about job offer for nofluff."""
    job_data = parse_api(job_url)
    if job_data is not None and job_data["status"] != "DOES_NOT_EXIST":
        job_offer_details_dictionary = {"title": job_data["title"],
                                        "company": job_data["company"]["name"],
                                        "location": job_data["location"]["places"],
                                        "company_size": job_data["company"]["size"],
                                        "offer_url": job_data["postingUrl"],
                                        "employment_types": job_data["essentials"]["originalSalary"],
                                        "experience": job_data["basics"]["seniority"],
                                        "skills_must": job_data["requirements"]["musts"],
                                        "skills_nice": job_data["requirements"]["nices"],
                                        "scraped_at": datetime.datetime.now(),
                                        "expired": 'false',
                                        "expired_at": " ",
                                        "jobsite": "nofluff"
                                        }
        return job_offer_details_dictionary


def get_job_offer_details_justjoin(job_url: str) -> dict:
    """Function that gets details about job offer for justjoin."""
    job_data = parse_api(job_url)
    if job_data is not None:
        job_offer_details_dictionary = {"title": job_data["title"],
                                        "company": job_data["company_name"],
                                        "location": job_data["city"],
                                        "company_size": job_data["company_size"],
                                        "offer_url": job_data["id"],
                                        "employment_types": job_data["employment_types"],
                                        "experience": job_data["experience_level"],
                                        "skills": job_data["skills"],
                                        "scraped_at": datetime.datetime.now(),
                                        "expired": 'false',
                                        "expired_at": " ",
                                        "jobsite": "justjoin",
                                        "remote": job_data["remote"]
                                        }
        return job_offer_details_dictionary
