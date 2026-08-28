import sys
from app.services.tmdb import tmdb_buscador

query = sys.argv[1] if len(sys.argv) > 1 else "matrix"

for peli in tmdb_buscador(query):
    print(peli["id"], "-", peli["title"], f"({peli.get('release_date', '')[:4]})")