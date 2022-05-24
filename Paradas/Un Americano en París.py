import requests
import json

r = requests.get(url = "https://www.zaragoza.es/api/recurso/urbanismo-infraestructuras/tranvia/2422.json?srsname=wgs84")
data = r.json()

destino1 = data["destinos"][0]["destino"]
tiempo1 = data["destinos"][0]["minutos"]
destino2 = data["destinos"][1]["destino"]
tiempo2 = data["destinos"][1]["minutos"]

print("El primer tranvía con destino a ", destino1, " tarda ", tiempo1, " minutos.")
print("El segundo tranvía con destino a ", destino2, " tarda ", tiempo2, " minutos.")