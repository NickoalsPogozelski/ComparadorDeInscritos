import urllib.request
import json

adversario = urllib.request.urlopen('https://www.googleapis.com/youtube/v3/channels?part=statistics&id={}&key={}').read() #id do adversario e sua key
eu = urllib.request.urlopen('https://www.googleapis.com/youtube/v3/channels?part=statistics&id={}&key={}').read()#seu id e sua key

advsubs = (json.loads(adversario)["items"][0]["statistics"]["subscriberCount"])
mesubs = (json.loads(eu)["items"][0]["statistics"]["subscriberCount"])

if advsubs > mesubs:
    diferenca = int(mesubs) - int(advsubs)
else:
    diferenca = int(advsubs) - int(mesubs)

print('inscritos do adversario: ', advsubs)
print('seus inscritos: ', mesubs)
print('diferença', diferenca)