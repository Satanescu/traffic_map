"""
app.py — punct de intrare.
Rulează: python app.py
Produce: traffic_map.html
"""
from map_builder import build_map,insert_legend
import logging

from providers import check,change_values_env

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

if __name__ == "__main__":
    main()
    log()
    logging.info('Codul a rulat corect')
    #logging.warning('s-a detectar o probblema')
    #logging.error('S-aa detectat o erroare')
    check()
    change_values_env()
    insert_legend()

