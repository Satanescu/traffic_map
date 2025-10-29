"""
map_builder.py — construiește harta:
- OSM ca bază
- Overlay raster trafic TomTom (ready-made)
- Overlay vector “Traffic (din cache)” desenat din Flow Segment
"""
import folium
from providers import tomtom_flow_tiles_template, osm_basemap_template
from config import MAP_CENTER, MAP_ZOOM

def build_map() -> folium.Map:
    """Construiește obiectul hartă Folium și atașează straturile."""
    m = folium.Map(
        location=MAP_CENTER,
        zoom_start=MAP_ZOOM,
        tiles=osm_basemap_template(),
        attr='&copy; OpenStreetMap contributors'
    )
    # Overlay raster oficial TomTom, pentru referință vizuală.  :contentReference[oaicite:6]{index=6}
    folium.TileLayer(
        tiles=tomtom_flow_tiles_template(),
        name="Traffic Flow (TomTom raster)",
        attr="Traffic © TomTom",
        overlay=True,
        control=True,
        opacity=0.75,
        max_zoom=22
    ).add_to(m)

    folium.LayerControl(collapsed=False).add_to(m)

    return m
