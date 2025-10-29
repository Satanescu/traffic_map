"""
app.py — punct de intrare.
Rulează: python app.py
Produce: traffic_map.html
"""
from map_builder import build_map

def main():
    m = build_map()
    m.save("traffic_map.html")
    print("Generat: traffic_map.html")

if __name__ == "__main__":
    main()
