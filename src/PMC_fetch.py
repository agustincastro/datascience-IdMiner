import os 
import urllib.request
import json
import logging
import requests
import backoff
 
@backoff.on_exception(backoff.expo,requests.exceptions.RequestException,max_time=120)
def get_pmc_query(query,mark,pubmed=[]):
    url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=gene_protein:"'+query+'"+and+LANG:eng+and+has_abstract:y&resultType=lite&synonym=TRUE&cursorMark='+mark+'&pageSize=1000&format=JSON'
    response = urllib.request.urlopen(url)
    data = response.read()      # a `bytes` object
    my_json = data.decode('utf8')
    data = json.loads(my_json)
    if data["resultList"]["result"] and len(pubmed) < 10000:
        results = data["resultList"]["result"]
        pubmed += [x["pmid"] for x in results if "pmid" in x]
        pubmed = get_pmc_query(query, data["nextCursorMark"],pubmed)
        return pubmed
    else:
        logging.info(" -- Via pmc annotation API IdMiner recover %i articles for %s" %(len(pubmed),query))
        return pubmed