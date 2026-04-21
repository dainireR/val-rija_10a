import json



datne=open("uzd1.json",encoding="utf-8")
dati=json.load(datne)
datne.close()

valstis=[]
lauksaimniecibas_ipatsvars=[]

for vardnica in dati:
    valstis.append(vardnica["nosaukums"])
print(valstis)




for vardnica in dati:
    proc=(100/vardnica["nosaukums"]["lauksaimniecibas_zeme"])*(vardnica["nosaukums"]["lauksaimniecibas_zeme"]+vardnica["nosaukums"]["mezs"]+vardnica["nosaukums"]["cita_veida_zeme"])
    lauksaimniecibas_ipatsvars.append(proc)
    print(f"{proc}%")

a={}
a.update(valstis)
a.update(lauksaimniecibas_ipatsvars)
import csv


with open("rezultati.csv","w",encoding="utf-8")as f:
    i=csv.writer(f)
    i.writerow(a)





