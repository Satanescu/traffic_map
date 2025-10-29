from urllib.parse import urlencode
from config import TOMTOM_API_KEY, TOMTOM_STYLE

def tomtom_flow_tiles_template() -> str:
    # Spec per TomTom Orbis Raster Flow Tiles:
    # https://api.tomtom.com/maps/orbis/traffic/tile/flow/{zoom}/{x}/{y}.png?apiVersion=1&key=...&style=light
    if not TOMTOM_API_KEY:
        raise RuntimeError("Missing TOMTOM_API_KEY")
    qs = urlencode({"apiVersion": 1, "key": TOMTOM_API_KEY, "style": TOMTOM_STYLE})
    return f"https://api.tomtom.com/maps/orbis/traffic/tile/flow/{{z}}/{{x}}/{{y}}.png?{qs}"

def osm_basemap_template() -> str:
    # OSM raster tiles, attribution handled in folium
    return "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
