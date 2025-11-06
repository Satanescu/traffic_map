from urllib.parse import urlencode
from config import TOMTOM_API_KEY, TOMTOM_STYLE
import requests
import os
from dotenv import load_dotenv, set_key
import logging

def tomtom_flow_tiles_template() -> str:
    # Spec per TomTom Orbis Raster Flow Tiles:
    # https://api.tomtom.com/maps/orbis/traffic/tile/flow/{zoom}/{x}/{y}.png?apiVersion=1&key=...&style=light
    if not TOMTOM_API_KEY:
        raise RuntimeError("Missing TOMTOM_API_KEY")
    qs = urlencode({"apiVersion": 1, "key": TOMTOM_API_KEY, "style": TOMTOM_STYLE})
    return f"https://api.tomtom.com/maps/orbis/traffic/tile/flow/{{z}}/{{x}}/{{y}}.png?{qs}"

def osm_basemap_template() -> str:
    # OSM raster tiles, attribution handled in folium
    if TOMTOM_STYLE == 'light':
        return "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
    else:
        return "https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png"
    # return "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"



def change_values_env():
    load_dotenv()

    current_zoom=os.getenv('MAP_MAX_ZOOM')
    current_opacity=os.getenv('MAP_OPACITY')

    new_max_zoom=input(f'Zoom-ul maxim actual este {current_zoom}: ')
    new_opacity=input(f'Opacitatea actual este {current_opacity}: ')

    try:
        if new_max_zoom is not None:
            new_max_zoom=str(int(new_max_zoom))
        if new_opacity is not None:
            new_opacity=str(float(new_opacity))
    except ValueError:
        print("Va rog introduceti o valoare corecta")
        return #???????????

    env_file=".env"

    if new_max_zoom:
        set_key(env_file,"MAP_MAX_ZOOM",new_max_zoom)
    if new_opacity:
        set_key(env_file,"MAP_OPACITY",new_opacity)

    logging.info(f"Valorile s-au updatat new_zoom: {new_max_zoom} & new_opacity: {new_opacity} ")

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
        msg="Unauthorized: API key invalidă sau lipsă. Incearca sa iei o cheie de aici --> https://developer.tomtom.com/knowledgebase/platform/articles/how-to-get-an-tomtom-api-key/"
        logging.error(msg)
    elif code == 403:
        msg="Forbidden: cheia este valida dar nu are permisiuni pentru acest endpoint. Incearca sa iei o cheie de aici --> https://developer.tomtom.com/knowledgebase/platform/articles/how-to-get-an-tomtom-api-key/"
        logging.error(msg)
    elif code == 404:
        msg = "Not Found: verifică URL-ul de test."
        logging.error(msg)
    else:
        msg="Unhandled error"
        logging.error(msg)
    return 'ok'