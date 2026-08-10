from pathlib import Path
import shutil
import urllib.request

ROOT = Path(__file__).parent
DIST = ROOT / "dist"
ASSETS = DIST / "assets"
PINNED_INVESTOR_COMMIT = "fa67a659478f9ab883c06544bb7fbb99d8af0db0"
RAW = f"https://raw.githubusercontent.com/castefeudal/stimul-food-investor/{PINNED_INVESTOR_COMMIT}"

shutil.rmtree(DIST, ignore_errors=True)
ASSETS.mkdir(parents=True, exist_ok=True)

for name in ("index.html", "menu.html", "privacy.html"):
    shutil.copy2(ROOT / name, DIST / name)

for name in ("menu.js", "config.js"):
    shutil.copy2(ROOT / "assets" / name, ASSETS / name)

shared_assets = ("site.css", "site.js", "favicon.svg", "mark.svg", "hero.jpg", "packaging.jpg")
for name in shared_assets:
    urllib.request.urlretrieve(f"{RAW}/assets/{name}", ASSETS / name)

urllib.request.urlretrieve(f"{RAW}/data.json", DIST / "data.json")
(DIST / ".nojekyll").write_text("", encoding="utf-8")

print("Готово: dist собран для GitHub Pages")
