import requests as r
import json
class w:
 m = '\033[1;31m' # merah
 b = '\033[1;36m' # biru
 k = '\033[1;33m' # kuning
 h = '\033[1;32m' # hijau
 u = '\033[1;35m' # ungu
 p = '\033[1;37m' # putih
 i = '\033[1;90m' # abu abu
 ut = '\033[1;34m' # ungu tua
 c = '\033[1;96m' # cyan
 tu = '\x1b[103m\x1b[31m' # tebal merah
 df = '\x1b[0m' # default
class main:
 def banner():
     print (f"""{w.m}{w.k}  _     _      _ _      _____ _           _           
 | |   (_)_ __(_) | __ |  ___(_)_ __   __| | ___ _ __ 
 | |   | | '__| | |/ / | |_  | | '_ \ / _` |/ _ \ '__|
 | |___| | |  | |   <  |  _| | | | | | (_| |  __/ |   
{w.k} |_____|_|_|  |_|_|\_\ |_|   |_|_| |_|\__,_|\___|_|   """)
 def subanner():
     print (f"""
{w.m}[•] Author : {w.c}abilseno11
{w.m}[•] Nama Sc : {w.c}Pencari lirik
{w.m}[•] Github : {w.c}https://github.com/AbilSeno""")
 def start():
     lagu = str(input(f"{w.p}[{w.i}-{w.p}] {w.k}Masukkan nama lagu yang mau di cari : {w.ut}"))
     get = r.get(f'https://some-random-api.ml/lyrics?title={lagu}').text
     if 'error' in get:
      print (f"{w.p}[{w.i}-{w.p}] {w.m}Error, lirik tidak ditemukan")
      main.start()
     else:
      jsn = json.loads(get)
      with open(lagu+'.txt','w') as tod:
       tod.write(jsn['lyrics'])
       tod.close()
      print (f"""
    {w.tu}{lagu}{w.df}
{w.k}[{w.m}~{w.k}] {w.m}Title {w.i}: {w.u}{jsn['title']}
{w.k}[{w.m}~{w.k}] {w.m}Author {w.i}: {w.u}{jsn['author']}
{w.k}[{w.m}~{w.k}] {w.m}Lirik {w.i}: {w.u}\n{jsn['lyrics']}
{w.tu}Tersimpan ke : {lagu}.txt{w.df}""")
if __name__ == "__main__":
 try:
  main.banner()
  main.subanner()
  print(f"           {w.tu}INPUT{w.df}           ")
  main.start()
 except r.exceptions.ConnectionError:print (f"{w.p}[{w.m}•{w.p}] {w.m}Koneksi error!!!")
