#Crie um codigo em python que teste se o site Pudim esta acessivel pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('Erro')
else:
    print('Ok')
    print(site.read())