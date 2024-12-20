Here is your updated `app.py` file with the added route for the root URL and the optional favicon:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Notentexte
sehrgut = "Sehr gut! Du hast eine"
gut = "Gut gemacht, du hast eine"
befriedigend = "Deine Leistungen sind befriedigend du hast eine"
ausreichend = "Deine Leistungen sind grade so ausreichend"
mangelhaft = "Deine Leistungen sind mangelhaft du hast eine"
ungenügend = "Leider ist deine Note sehr schlecht, du hast eine"

# Funktion zum Berechnen der Note
def ausrechnen(notenpunkte):
    if notenpunkte == 15:
        return f"{sehrgut} 1+"
    elif notenpunkte == 14:
        return f"{sehrgut} 1"
    elif notenpunkte == 13:
        return f"{sehrgut} 1-"
    elif notenpunkte == 12:
        return f"{gut} 2+"
    elif notenpunkte == 11:
        return f"{gut} 2"
    elif notenpunkte == 10:
        return f"{gut} 2-"
    elif notenpunkte == 9:
        return f"{befriedigend} 3+"
    elif notenpunkte == 8:
        return f"{befriedigend} 3"
    elif notenpunkte == 7:
        return f"{befriedigend} 3-"
    elif notenpunkte == 6:
        return f"{ausreichend} 4+"
    elif notenpunkte == 5:
        return f"{ausreichend} 4"
    elif notenpunkte == 4:
        return f"{ausreichend} 4-"
    elif notenpunkte == 3:
        return f"{mangelhaft} 5+"
    elif notenpunkte == 2:
        return f"{mangelhaft} 5"
    elif notenpunkte == 1:
        return f"{mangelhaft} 5-"
    elif notenpunkte == 0:
        return f"{ungenügend} 6"
    else:
        return "Diese Notenpunktzahl gibt es nicht!"

# Flask-Route
@app.route('/')
def home():
    return "Welcome to the Notenumrechner API!"

@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route('/berechne_note', methods=['POST'])
def berechne_note():
    data = request.get_json()
    notenpunkte = data.get('notenpunkte', None)
    if not isinstance(notenpunkte, int) or not (0 <= notenpunkte <= 15):
        return jsonify({"error": "Ungültige Eingabe. Punkte müssen zwischen 0 und 15 liegen."}), 400

    result = ausrechnen(notenpunkte)
    return jsonify({"notenpunkte": notenpunkte, "note": result})

if __name__ == "__main__":
    app.run(debug=True)
```
