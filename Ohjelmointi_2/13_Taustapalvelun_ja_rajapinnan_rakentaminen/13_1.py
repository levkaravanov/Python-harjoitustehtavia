from flask import Flask, Response
import json

app = Flask(__name__)

@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    try:
        tilakoodi = 200
        luku = int(luku)
        if luku < 2:
            vastaus = {
                "Number":luku,
                "isPrime":False
            }
        else:
            alkuluku = True
            for i in range(2, int(luku ** 0.5) + 1):
                if luku % i == 0:
                    alkuluku = False
                    break

            if alkuluku:
                vastaus = {
                    "Number": luku,
                    "isPrime": True
                }
            else:
                vastaus = {
                    "Number": luku,
                    "isPrime": False
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