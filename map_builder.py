"""
map_builder.py — construiește harta:
- OSM ca bază
- Overlay raster trafic TomTom (ready-made)
- Overlay vector “Traffic (din cache)” desenat din Flow Segment
"""
import folium
from providers import tomtom_flow_tiles_template, osm_basemap_template
from config import MAP_CENTER, MAP_ZOOM
from pathlib import Path

def build_map() -> folium.Map:
    """Construiește obiectul hartă Folium și atașează straturile."""
    m = folium.Map(
        location=MAP_CENTER,
        zoom_start=MAP_ZOOM,
        tiles=osm_basemap_template(),
        attr='&copy; OpenStreetMap contributors'

    )
    # Overlay raster oficial TomTom, pentru referință vizuală.
    folium.TileLayer(
        tiles=tomtom_flow_tiles_template(),
        name="Traffic Flow (TomTom raster)",
        attr="Traffic © TomTom",
        overlay=True,
        control=True,
        opacity=0.75,
        max_zoom=22
    ).add_to(m)

    folium.LayerControl(collapsed=True).add_to(m)

    return m

def insert_legend():
    legend="""
    <div style="position: fixed; bottom: 50px; left: 50px; z-index:9999;
 background: white; border:2px solid #666; padding:8px; font-size:14px;">
 <b>Legendă trafic</b><br>
 <i style="background:#2ecc71;width:12px;height:12px;display:inline-block;"></i> liber<br>
 <i style="background:#f1c40f;width:12px;height:12px;display:inline-block;"></i> moderat<br>
 <i style="background:#e67e22;width:12px;height:12px;display:inline-block;"></i> aglomerat<br>
 <i style="background:#e74c3c;width:12px;height:12px;display:inline-block;"></i> blocaj
</div>
    """

    p=Path('traffic_map.html')
    html=p.read_text(encoding='utf-8')

    if "Legenda trafic" in html:
        print("Legenda deja exista")
        return

    i = html.lower().rfind("</body>")
    if i == -1:
        i=len(html)

    new_html=html[:i]+legend+html[i:]
    p.write_text(new_html, encoding='utf-8')
    print("Legenda a fost inserata")
