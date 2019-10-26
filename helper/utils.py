from enum import Enum


class Constants(Enum):
    host = "ensembldb.ensembl.org"
    port = 3306
    user = "anonymous"
    database = "ensembl_website_97"
    table = 'gene_autocomplete'
    name = 'name'
    species = 'species'
    error = 'error'
    message = 'message'
    min_keyword_count=3
    limit_retries=5
    pool_size=5

