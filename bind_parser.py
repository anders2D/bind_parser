from datetime import datetime


def load(file: str) -> list:
    """ Load log file and return beauty queries dict list"""

    log_queries: list = []

    with open(file, 'r') as queries_log:
        for query in queries_log:
            log_queries.append(get_query(query))
    
    return log_queries


def get_query(query: str) -> dict:
    """ Return a usefull query informatión from the following format

    date time headers hexadecimal ip_from host_queried query_class ...

    18-May-2021 16:34:13.003 queries: info: client @0x55adcc672cc0 45.231.61.2#80
    (pizzaseo.com): query: pizzaseo.com IN ANY +E(0) (172.20.101.44)

    return: dict : timestamp,name,client_ip,client_name,type
    """
    template: dict = {}

    words_to_clean = ["query:", "info:",
                      "client", "view", "standard:", "queries:"]
    data = [i for i in query.split() if i not in words_to_clean]

    # Usefull columns, you can see more about usefull columns here:
    # https://docs.lumu.io/portal/en/kb/articles/cc-api-specifications#Send_DNS_Queries

    # Column, name
    # 0,1   , timestamp
    # 2     , client_name <-- it is client hexadecimal id, but we are going to take it as client_name
    # 3     , client_ip
    # 5     , name
    # 7     , type

    # 0,1
    timestamp_str = f"{data[0]} {data[1]}"
    timestamp = datetime.strptime(timestamp_str, "%d-%B-%Y %H:%M:%S.%f")

    # 2
    client_name = data[2]

    # 3
    client_ip = data[3].split('#')[0] # we need ip only

    # 5
    name = data[5]

    # 7
    query_type = data[7]    

    result =  {
        "timestamp": timestamp.strftime('%Y-%m-%dT%H:%M:%SZ'),
        "name": name,
        "client_ip": client_ip,
        "client_name": client_name, 
        "type": query_type
    }
    return result


