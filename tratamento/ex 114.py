import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except:
    print('Não foi possivel acessar o site')
else:
    print('Site foi acessado com sucesso')


