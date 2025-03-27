from flask import Flask, Response
import json
from db_connection import get_connection

app = Flask(__name__)

@app.route('/kenttä/<icao>')
def kenttä(icao):
    try:
        icao = icao.upper()
        tilakoodi = 200
        conn = get_connection()
        cursor = conn.cursor()

        sql = ("SELECT name, municipality "
               "FROM airport "
               "WHERE ident = %s")

        cursor.execute(sql, (icao, ))
        airport = cursor.fetchone()

        cursor.close()
        conn.close()

        if airport:
            airport_name = airport[0]
            municipality = airport[1]
            vastaus = {
                "ICAO": icao,
                "Name": airport_name,
                "Municipality": municipality
            }
        else:
            tilakoodi = 404
            vastaus = {
                "status": tilakoodi,
                "teksti": "Kenttää ei löytynyt"
            }
    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen lukuparametri"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status": "404",
        "teksti": "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)