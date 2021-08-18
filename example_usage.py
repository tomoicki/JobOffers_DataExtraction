from utilities.extraction_functions import get_job_offers


if __name__ == "__main__":

    #  incorrect use of function, we need to specify site= kwarg to 'nofluff' or 'justjoin'
    get_job_offers()

    #  calls get_job_offers for nofluffjobs.com without saving to .json file
    data_from_nofluffjobs = get_job_offers(site='nofluff', save_json=False)
    #  calls get_job_offers for nofluffjobs.com with saving to .json file
    data_from_nofluffjobs_json = get_job_offers(site='nofluff', save_json=True)

    #  calls get_job_offers for justjoin.it without saving to .json file
    data_from_justjoin = get_job_offers(site='justjoin', save_json=False)
    #  calls get_job_offers for justjoin.it with saving to .json file
    data_from_justjoin_json = get_job_offers(site='justjoin', save_json=True)

