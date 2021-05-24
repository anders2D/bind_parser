import requests

API_BASE = "https://api.lumu.io:443"

LUMU_CLIENT_KEY = "d39a0f19-7278-4a64-a255-b7646d1ace80"
COLLECTOR_ID = "5ab55d08-ae72-4017-a41c-d9d735360288"

HEADERS = {"Content-Type": "application/json"}

LIMIT_OBJECTS_PER_REQ = 500

def send_dns_queries(queries: any):
    """ send request to put queries into lumu api """
    url = f"{API_BASE}/collectors/{COLLECTOR_ID}/dns/queries?key={LUMU_CLIENT_KEY}"
    chunked_queries = get_chunked_list(queries, LIMIT_OBJECTS_PER_REQ)

    for chunk in chunked_queries:
        requests.post(url, headers=HEADERS, json=chunk)

def get_chunked_list(objects:list, chunk_limit:int):
    """ return a generator of lists that contain chunks """
    for i in range(0, len(objects), chunk_limit):
        yield objects[i:i+chunk_limit]
