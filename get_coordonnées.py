import xml.etree.ElementTree as ET

# Charger le fichier SVG
tree = ET.parse("G-100_path.svg")
root = tree.getroot()

# Namespace pour SVG (nécessaire pour parser correctement)
namespace = {"svg": "http://www.w3.org/2000/svg"}

# Récupérer les cercles
points = []
for ellipse in root.findall(".//svg:ellipse", namespace):
    id_point = ellipse.get("id")
    cx = ellipse.get("cx")
    cy = ellipse.get("cy")
    points.append({"id": id_point, "x": float(cx), "y": float(cy)})

# Récupérer les dimensions depuis la balise <svg>
svg_tag = root.find("svg:svg", namespace)
if svg_tag is None:  # Si le namespace n'est pas utilisé
    svg_tag = root

width = svg_tag.get("width")
height = svg_tag.get("height")

# Si les dimensions ne sont pas spécifiées, utiliser le viewBox
if not width or not height:
    viewBox = svg_tag.get("viewBox")
    if viewBox:
        _, _, width, height = map(float, viewBox.split())

def parse_dimension(value):
    if value.endswith("mm"):
        value = value.replace("mm", "")
    return float(value)

# Extraire et nettoyer les dimensions
width = parse_dimension(svg_tag.get("width", "0"))
height = parse_dimension(svg_tag.get("height", "0"))

# Calcul des coordonnées relatives
for point in points:
    relative_x = point["x"] / width
    relative_y = point["y"] / height
    print(f"Point {point['id']} : ({relative_x:.2f}, {relative_y:.2f})")

