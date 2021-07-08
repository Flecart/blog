# Here will be implemented all the stuff for the calls for the API
# 07-07-2021 Huang Xuanqiang for Matteo's BLOG (a friend)


import requests
import os
import json


# set environment variables and catch errors meanwhile
try:
    DATABASE = os.getenv("NOTION_DATABASE_ID")
    API_KEY = os.getenv("NOTION_KEY")
    VERSION = os.getenv("NOTION_VERSION")
except Exception as e:
    print(e)
    exit(1)


# just watching the return code, exits with internal server error code
def check_res_code(code, text):
    if code != 200:
        print(code, text)
        print(" C' `e stato l'errorino qui presente, cerca di capire cosa dice!")
        return 500 
    elif code == 429:
        # https://developers.notion.com/reference-link/request-limits
        print(" Too many requests ", text)
        return 500
    else:
        # everything went fine
        return 200


# gets the notion DATABASE with id=page
# https://developers.notion.com/reference/get-database
def get_database(page):
    url = f"https://api.notion.com/v1/databases/{page}"
    headers = {'Authorization': f'Bearer {API_KEY}', 'Notion-Version' : VERSION}
    res = requests.get(url, headers=headers)

    # checking if request went just fine
    check_res_code(res.status_code, res.text)
    
    # keeping only the JSON text
    res = json.loads(res.text)
    print(res) # debugging stuff here on
    for key in res:
        print(key)
    return


# queries the database based on id (see response structure with this link)
# https://developers.notion.com/reference/post-database-query
def query(id, data={}):
    # TODO make queries work

    url = f"https://api.notion.com/v1/databases/{id}/query"
    headers = {'Authorization': f'Bearer {API_KEY}', 'Notion-Version' : VERSION}
    res = requests.post(url, headers=headers, data=data)

    # checking if request went just fine
    check_res_code(res.status_code, res.text)

    # keeping only the JSON text
    res = json.loads(res.text)

    # creates array of wanted stuff
    # page_ids = []
    # for page in res['results']:
    #     page_ids.append(page)

    # print(page_ids)
    return res


# see https://developers.notion.com/reference/get-page
# only gets page properties and not content
def get_page_properties(id):
    url = f"https://api.notion.com/v1/pages/{id}"
    headers = {'Authorization': f'Bearer {API_KEY}', 'Notion-Version' : VERSION}
    res = requests.get(url, headers=headers)

    # checking if request went just fine
    check_res_code(res.status_code, res.text)
    
    # keeping only the JSON text
    res = json.loads(res.text)
    print(res) # debugging stuff here on
    for key in res:
        print(key)

    return res


# see here, every page is a block with notion!
# https://developers.notion.com/reference/get-block-children
def get_page_content(id):
    url = f"https://api.notion.com/v1/blocks/{id}/children"
    headers = {'Authorization': f'Bearer {API_KEY}', 'Notion-Version' : VERSION}
    res = requests.get(url, headers=headers)

    # checking if request went just fine
    check_res_code(res.status_code, res.text)

    # keeping only the JSON text
    res = json.loads(res.text)
    # print(res) # debugging stuff here on

    return res

def date_parser(date):
    # le date dovrebbero sempre restare nel formato di Notion, quindi faccio soluzioone ez...

    return date[:10]

# debuggin stuff here
if __name__ == "__main__":
    # getting the stuff to fetch
    data = {"page_size": 5}
    pages = query(DATABASE, data)

    # mi creo una lista di pagine, che saranno delle cards dopo
    scrapped_pages = []

    for page in pages['results']:
        # sono le proprieta del database che ho deciso io!
        # quindi sono abbastanza sicuro che ci siano
        # quindi le tengo cosi
        tmp_dict = page['properties']
        tmp_dict['id'] = page['id']
        scrapped_pages.append(tmp_dict)

    tmp = scrapped_pages[0]['Nome articolo']['type']
    print()
    print(scrapped_pages[0]['Nome articolo'][ tmp ][0]['plain_text'])
    # print(scrapped_pages)