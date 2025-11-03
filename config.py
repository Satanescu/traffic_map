from dotenv import load_dotenv
import os

load_dotenv()

TOMTOM_API_KEY = os.getenv("TOMTOM_API_KEY", "")
MAP_CENTER = (float(os.getenv("MAP_CENTER_LAT", "44.4268")), float(os.getenv("MAP_CENTER_LON", "26.1025")))
MAP_ZOOM = int(os.getenv("MAP_ZOOM", "12"))
TOMTOM_STYLE = os.getenv("TOMTOM_STYLE", "light")
