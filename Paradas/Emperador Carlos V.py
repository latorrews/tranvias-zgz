import requests
import json

r1 = requests.get(url = "https://www.zaragoza.es/api/recurso/urbanismo-infraestructuras/tranvia/1701.json?srsname=wgs84")
data1 = r1.json()

r2 = requests.get(url = "https://www.zaragoza.es/api/recurso/urbanismo-infraestructuras/tranvia/1702.json?srsname=wgs84")
data2 = r2.json()

destino11 = data1["destinos"][0]["destino"]
tiempo11 = data1["destinos"][0]["minutos"]
destino12 = data1["destinos"][1]["destino"]
tiempo12 = data1["destinos"][1]["minutos"]

destino21 = data2["destinos"][0]["destino"]
tiempo21 = data2["destinos"][0]["minutos"]
destino22 = data2["destinos"][1]["destino"]
tiempo22 = data2["destinos"][1]["minutos"]

if tiempo11 == 0:
  print("El primer tranvía con destino a ", destino11, " ya está en la parada.")
else:
  print("El primer tranvía con destino a ", destino11, " tarda ", tiempo11, " minutos.")

if tiempo12 == 0:
  print("El segundo tranvía con destino a ", destino12, " ya está en la parada.")
else:
  print("El segundo tranvía con destino a ", destino12, " tarda ", tiempo12, " minutos.")


if tiempo21 == 0:
  print("El tercer tranvía con destino a ", destino21, " ya está en la parada.")
else:
  print("El tercer tranvía con destino a ", destino21, " tarda ", tiempo21, " minutos.")

if tiempo22 == 0:
  print("El cuarto tranvía con destino a ", destino22, "ya está en la parada.")
else:
  print("El cuarto tranvía con destino a ", destino22, " tarda ", tiempo22, " minutos.")