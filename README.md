## JobOffers_DataExtraction
Data extraction part of Job offer aggregation project.
- Data Extraction (you are here)
- [Data Transformation](https://github.com/tomoicki/JobOffers_DataTransformation)
- [Data Load](https://github.com/tomoicki/JobOffers_DataLoad)
- [REST API](https://github.com/tomoicki/JobOffers_API)


On this branch we only used requests library to gather data. Other branches utilize different approach.

Main functionality lies inside get_job_offers function (job_offers_data_extraction.extraction_functions). It automatically gathers all job offers from either nofluffjobs.com or justjoin.it.
To specify which site to get data from provide either 'nofluff' or 'justjoin' as a value of kwarg site=

If in need of more details see example_use.py file.

To install use
>py -m pip install job_offers_data_extraction@git+https://github.com/tomoicki/JobOffers_DataExtraction@using_requests


