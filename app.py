"""
app.py — punct de intrare.
Rulează: python app.py
Produce: traffic_map.html
"""
from dotenv import load_dotenv

from map_builder import build_map
import logging
import dotenv
import os
import requests

def main():
    m = build_map()
    m.save("traffic_map.html")
    print("Generat: traffic_map.html")
    log()
    logging.info('Harta s-a generat')

def log(log_file='app.log'):

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def check():
    load_dotenv()

    api_key=os.getenv('TOMTOM_API_KEY')
    if not api_key:
        msg="The key is missing"
        logging.error(msg)
        return False,None

    url=f"https://api.tomtom.com/maps/orbis/traffic/tile/flow/{{z}}/{{x}}/{{y}}.png?{{qs}}"
    # url = f"https://api.tomtom.com/maps/orbis/traffic/tile/flow/0/0/0.png?key={api_key}"

    resp=requests.get(url)
    code=resp.status_code

    if code == 200:
        msg="OK"
        logging.info(msg)
        return True
    elif code == 401:
        msg="Unauthorized: API key invalidă sau lipsă."
        logging.error(msg)
    elif code == 403:
        msg="Forbidden: cheia este valida dar nu are permisiuni pentru acest endpoint."
        logging.error(msg)
    elif code == 404:
        msg = "Not Found: verifică URL-ul de test."
        logging.error(msg)
    else:
        msg="Unhandled error"
        logging.error(msg)
    return 'ok'







if __name__ == "__main__":
    main()
    log()
    logging.info('Codul a rulat corect')
    #logging.warning('s-a detectar o probblema')
    #logging.error('S-aa detectat o erroare')
    check()

