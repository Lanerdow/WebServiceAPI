from flask import Flask, jsonify
import calendar

app = Flask(__name__)


# Route qui se fait appeler par l'application
@app.route('/calendar/<int:year>/<int:month>', methods=['GET'])
def get_calendar(year, month):
    # Vérification de la validité de la saisie du mois
    if month < 1 or month > 12:
        return jsonify({"error": "Month should be between 1 and 12"}), 400

    # Génération du calendrier HTML
    html_cal = calendar.HTMLCalendar(firstweekday=0)

    # Renvoie du calendrier en json
    return jsonify({"calendar": html_cal.formatmonth(year, month)})


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)