# Traffic Map Starter (Python + Folium)

## Setup
1. `python -m venv .venv && . .venv/bin/activate` (Windows: `.venv\Scripts\activate`)
2. `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and set `TOMTOM_API_KEY`.

## Run
`python app.py` → open `traffic_map.html`.

## How it works
- We overlay TomTom **Raster Flow Tiles** on top of OSM tiles using Folium’s `TileLayer`. URL template and params follow TomTom docs. :contentReference[oaicite:4]{index=4}
- Documentation: https://python-visualization.github.io/folium/latest/

## Tasks

#### 1) Light/Dark nu functioneaza corespunzator
- Daca setez in `.env` variabila `TOMTOM_STYLE` sa fie dark, mapa nu devine dark, doar drumurile
- Un inginer a observat ca mapa nu poate avea stiluri, dar putem sa schimbam harta folosita pe una dark.
  Citind documentatia de la folium, a gasit ca putem sa folosim acest url pentru OSM tiles (https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}.png)
- Scopul final este sa putem schimba in `.env` o singura variabila in dark si sa se updateaza si drumurile si harta pe dark.
- Bonus, light/dark se poate schimba direct din harta, cu un toggle sau buton

#### 2) Adauga print si logging
- Avem clienti care se plang ca nu isi dau seama din terminal ce se intampla, daca codul a rulat corect sau nu
- De asemenea, se plang ca nu au un fisier `.log` unde sa vada jurnalul de executie
- Adauga un `Logger` si adauga `log.info()` si `log.error()` unde consideri ca si aplicatia sa transmita clar ce face

#### 3) Fallback cand API KEY-ul lui TOMTOM expira
- Luna trecuta toti clientii ni s-au plans ca aplicatia nu mai merge si nu stiau de ce.
- Creeaza un check daca cheia este valida (daca requesturile dau fail din motivul asta) si afiseaza mesaj si log
care sa le zica clar clientiilor ca cheia a expirat si de unde sa isi genereze alta (link spre tomtom dashboard)

#### 4) Adauga max_zoom si opacitatea ca valori configurabile in `.env`
- Diferiti clienti au nevoie sa genereze hartile cu alt zoom si cu opacitati diferite
- Momentan, aceste valori sunt 'hardcoded' in codul sursa
- Modifica in asa fel incat valorile astea sa fie setate in `.env` si folosite de acolo

#### 5) Adauga legenda pe harta in html
- Adauga o legenda de culori care sa explice clientilor cat de rau e traficul in functie de culoare
- Legenda sa fie vizibila, dar sa nu acopere alte butoane
- Un inginer cu foarte mult timp liber a fost destul de politicos sa scrie un cod html (un div) pentru
o astfel de legenda

```html
<div style="position: fixed; bottom: 50px; left: 50px; z-index:9999;
 background: white; border:2px solid #666; padding:8px; font-size:14px;">
 <b>Legendă trafic</b><br>
 <i style="background:#2ecc71;width:12px;height:12px;display:inline-block;"></i> liber<br>
 <i style="background:#f1c40f;width:12px;height:12px;display:inline-block;"></i> moderat<br>
 <i style="background:#e67e22;width:12px;height:12px;display:inline-block;"></i> aglomerat<br>
 <i style="background:#e74c3c;width:12px;height:12px;display:inline-block;"></i> blocaj
</div>
```



## Notes
- Folium tile layers require attribution and allow overlays via `overlay=True` and `LayerControl`.

