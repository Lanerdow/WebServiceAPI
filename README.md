# WebServiceAPI

Input :
# Générer un URL pour joindre l'API
api_url = 'http://localhost:8080/calendar?year=' + year + '&month=' + month

Output :
# Le retour est un calendrier sous forme de tableau HTML
return jsonify({"calendar": html_cal.formatmonth(year, month)})

# Route utilisé par l'API
/calendar
