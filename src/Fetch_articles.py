import sys
import backoff
import urllib.request
import requests
import re
from bs4 import BeautifulSoup as BS
from Bio import SeqIO
import random
import string
import time
import pandas as pd
import logging

# The on_exception decorator is used to retry when a specified exception is raised. Using exponential backoff retries when any kind of requests exception is raised.
# The keyword argument max_time specifies the maximum amount of total time in seconds that can elapse before giving up.


def get_genes_ids_from_file(file_input):
    """From txt file obtain gene ids

    Arguments:
        file_input {[file]} -- .txt file with genes separeted by new line

    Returns:
        [list] -- List of genes identificators
    """

    return open(file_input, "r").read().split("\n")


@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_time=120)
def get_text_from_gene(gene):
    '''This function obtains a list of articles associated with the query gene. Use the PaperBLAST API in order to obtain for the query gene (and their homologues) the list of articles where they are mentioned.

    Arguments:
        gene {[string]} -- id of a gene. It can  be from UniProt, RefSeq, or MicrobesOnline

    Returns:
        [list] -- List of XML results. Each element is an homologue result.
    '''

    try:
        logging.info("Searching %s in paperblast!" % (gene))
        url = 'http://papers.genomics.lbl.gov/cgi-bin/litSearch.cgi?query=' + gene
        response = urllib.request.urlopen(url)
        data = response.read()      # a `bytes` object
        text = data.decode('utf-8')  # transform byte to txt
        primarylist = []  # create empty list
        for x in str(text).split("\n"):  # parse response
            if "showAlign" in x:
                # if it has showAlign has the info we want.
                primarylist.append(x)
        logging.info("For %s PaperBLAST detected %i homologues" %
                     (gene, len(primarylist)))
        return primarylist
    except:
        return False


def create_fasta_db(fastafile):
    """Convert a fasta file into a dictionary.

    Arguments:
        fastafile {[string]} -- Multifasta file of query protein. Must be in fasta format.

    Returns:
        [dict] -- Dictionary with ID as a key and sequence as a value.
    """
    fastadict = {}
    record_dict = SeqIO.to_dict(SeqIO.parse(fastafile, "fasta"))
    for key in record_dict:
        fastadict[key] = record_dict[key].seq._data
    return fastadict


@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_time=120)
def get_text_from_fasta(gene, seq):
    """This function obtains a list of articles associated with the query sequence. Use the PaperBLAST API in order to obtain for the query sequence (and their homologues) the list of articles where they are mentioned.

    Arguments:
        gene {[string]} -- id of a gene.
        seq {[string]} -- aminoacidic sequence of the gene (protein).

    Returns:
        [list] -- List of XML results. Each element is an homologue result.
    """
    try:
        logging.info("Searching %s in paperblast!" % (gene))
        url = 'http://papers.genomics.lbl.gov/cgi-bin/litSearch.cgi?query=' + seq
        response = urllib.request.urlopen(url)
        data = response.read()      # a `bytes` object
        text = data.decode('utf-8')
        primarylist = []
        for x in str(text).split("\n"):
            if "showAlign" in x:
                primarylist.append(x)
        logging.info("For %s PaperBLAST detected %i homologues" %
                     (gene, len(primarylist)))
        return primarylist
    except:
        return False


def get_info_hit(xml_list, pcov=30, pident=30):
    """Parse the xml of the search made in Paper Blast to get a summary of it.

    Arguments:
        xml_list {[list]} -- List of XML results. Each element is an homologue result.

    Keyword Arguments:
        pcov {int} --  Minimum percentage of coverage for a homologous to be accepted.  (default: {30})
        pident {int} -- Minimum percentage of identity for a homologous to be accepted. (default: {30})

    Returns:
        [dict] -- Dictionary of accepted homologs. The values ​​of the dictionary are: Database from where the hit {string} was obtained, identifier of the hit {string}, p-value of the search of BLAST {float}, bitscore of the search of BLAST {integer},% of coverage of the query protein and its respective hit {integer},% identity of the query protein and its respective hit {integer} and publications associated with the homologue {list}
    """

    regex = "title=.*?(.+?)</a>"  # Expresion regular para obtener los ids.
    hit = {}  # Diccionario de hits.
    count = 0  # Inicio contador
    for x in xml_list:
        # Obtengo todos los sitios donde aparece la expresión regex
        results = re.findall(regex, x)
        for n, y in enumerate(results):
            if n == 0:
                # Obtiene la base de datos.
                db = y.split(">")[0].split(" ")[0].replace('"', "")
                # Obtiene el nombre del hit.
                gene = y.split(">")[1].split(" ")[-1]
            else:
                if "% identity, " in y:  # Contiene la informacion del alineamiento.
                    values = y
                    evalue, score = values[values.find(
                        "(")+1:values.find(")")].replace("E =", "").replace(" bits", "").split(",")
                    score = score.lstrip()  # Obtengo valores de evalue y bitscore
                    identity, coverage = values.split(">")[-1].split(",")
                    identity = identity.split("%")[0].strip()
                    # obtengo valores de cobertura e identidad.
                    coverage = coverage.split("%")[0].strip()
                    continue
        if pcov <= int(coverage) and pident <= int(identity):
            # Transformo el XML en un objeto de la clase bs4.BeautifulSoup para poder parsearlo.
            soup = BS(x, "lxml")
            primarylist = []  # Creo una lista vacia para poner los identificadores
            # Me quedo con todos los tags href.
            for a in soup.findAll('a', href=True):
                # Dentro de ellos me quedo con los que mencionen pmc or pubmed.
                if re.findall('pmc|pubmed', a['href']):
                    primarylist.append(a['href'])  # Agrego a la lista.
            # Si la lista no esta vacia actualizo el contador y agrego un hit al diccionario.
            if primarylist != []:
                count += 1
                key = "Hit_" + str(count)
                hit[key] = db, gene, evalue, score, identity, coverage, primarylist
        else:
            pass
    logging.info('There were %i homologues, with at least %s %i coverage and %s %i  identity' % (
        len(hit), "%", pcov, "%", pident))
    return hit


def generate_random_emails():
    """Generates random emails.

    Returns:
        [string] -- Random email.
    """

    return ''.join(random.choice(string.ascii_lowercase[:12]) for i in range(7)) + '@' + random.choice(["hotmail.com", "gmail.com", "aol.com", "mail.com", "mail.kz", "yahoo.com"])


@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_time=120)
def convert_pmc(pmc):
    """Transforms identifiers from PMC to Pubmed. To achieve this, the NCBI API is used (https://www.ncbi.nlm.nih.gov/pmc/tools/id-converter-api/).

    Arguments:
        pmc {[list]} -- List of PMC ids

    Returns:
        [list] -- List of Pubmed ids
    """

    pubmedlist = []
    url = "https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?tool=genomepaper&" + \
        "email="+generate_random_emails()+"&ids=" + pmc
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        soup = BS(data, "lxml")
        for a in soup.findAll('record', pmid=True):
            pubmedlist.append(a['pmid'])
    except:
        logging.warning("Ignoring PMC articles. There was a problem")
    return pubmedlist


def get_list(hits, gene):
    """ Get a list of articles associated with a gene


    Arguments:
        hits {[dict]} -- Dictionary of hit generated in get_info_hit function
        gene {[string]} -- gene id

    Returns:
        [string] -- comma separeted pubmedid articles
    """

    primarylist = []
    for hit in hits:
        primarylist += hits[hit][-1]
    pmc = ",".join([article.split("/")[-1]
                    for article in primarylist if "PMC" in article])  # articulos de PMC
    pubmed = ",".join([article.split(
        "/")[-1] for article in primarylist if "pubmed" in article])  # articulos de pubmed
    if pmc != "":
        pmc = ",".join(convert_pmc(pmc))
    pmids = pmc + pubmed
    logging.info("For %s PaperBLAST recovered %i articles" %
                 (gene, pmids.count(",")+1))
    return pmids


def check_format(input_file, format_file):
    """ Check format and return gene list or fasta dict

    Arguments:
        input_file {[file]} -- Input file. Could be fasta format or text format of genes separated by new lines
        format_file {[string]} -- Format name. fasta or text.

    Raises:
        ValueError -- Fasta wrong format
        ValueError -- Text wrong format

    Returns:
        [list]/[dict] -- List of genes (text format) or dictionary of sequence (fasta format)
    """

    if format_file == "fasta":
        genes = create_fasta_db(input_file)
        if not genes:
            raise ValueError(
                "There was an error with your fasta file. Please check if it is a valid format")
    else:
        genes = get_genes_ids_from_file(input_file)
        if not genes:
            logging.error(
                "There was an error with your txt file. Please check if it is a valid format. Remember genes id must be separeted by new lines")
            raise ValueError(
                "There was an error with your txt file. Please check if it is a valid format. Remember genes id must be separeted by new lines")
    return genes


def ids_by_gene(run_name, input_file, format_file, pcov=30, pident=30):
    """ Create a table (tsv format) of genes and their associated articles

    Arguments:
        run_name {[string]} -- Run name for output files
        input_file {[file]} -- Input file in either fasat or text format
        format_file {[string]} -- Format of input file, either fasta or text.

    Keyword Arguments:
        pcov {int} --  Minimum percentage of coverage for a homologous to be accepted.  (default: {30})
        pident {int} -- Minimum percentage of identity for a homologous to be accepted. (default: {30})

    Raises:
        ValueError -- Rise an error if there was not results.
    """

    articles = []
    # Check format and return genes name (and if fasta sequence)
    genes = check_format(input_file, format_file)
    for gene in genes:
        if format_file == "fasta":
            xml_list = get_text_from_fasta(
                gene, genes[gene])  # get blastpaper result
        else:
            xml_list = get_text_from_gene(gene)  # get blastpaper result
        hits = get_info_hit(xml_list, pcov, pident)  # obtain hit information
        if not hits == {}:  # if not empty. Ther was at least one gene which pass the filter.
            pmids = get_list(hits, gene)
            tmpart = [gene] + [pmids]
            articles += [tmpart]
    if articles == []:  # If ther was not results. Error
        logging.error("There was non results on your search")
        raise ValueError("There was non results on your search")
    dfarticles = pd.DataFrame(articles, columns=["id", "article"])
    dfarticles.to_csv(run_name + ".tsv", sep="\t", header=True, index=False)


# In order to run....

# Need to load form dash app:

    # Input_file: txt or fasta file.
    # Format_file: selection of text or fasta (radio button in app)
    # Run_name: name of output files (text box in app)

# Example of run:

# Input_file = "Test_fasta.fasta"
# Format_file = "fasta"
# Run_name = "Test_fasta"


# start_time = time.time()
# logging.basicConfig(format='%(asctime)s - IdMiner - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',filename= Run_name + '.log',level=logging.DEBUG)
# ids_by_gene(Run_name,Input_file,Format_file)
# elapsed_time = time.time() - start_time
# logging.info("Duration %i seconds" %(elapsed_time))
