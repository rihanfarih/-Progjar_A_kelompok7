# Tugas 5. Web Scrapping v2
--------------------------
## soal
modul yang digunakan:

- urllib - parse
	https://docs.python.org/3/library/urllib.parse.html

- requests
	pip install requests
	https://www.geeksforgeeks.org/python-requests-tutorial/

- beautifulsoup4
	 pip install beautifulsoup4
	https://beautiful-soup-4.readthedocs.io/en/latest/

=-*.=-*.=-*.=-*.=-*.=-*.=-*.=-*.=-*.=-*.=-*.=-*.=-*.=-*.=-*.=-*.=-*.=-*.=-*.=-*.

1. 

https://go.dev/doc/

def getGoBlog(num)  -> nomor blog keberapa yang akan diambil

ambil hasil query, parse ambil link dari list "Getting Started".
ambil isi dari blog ke "num" dari bagian "Getting Started"...
outputnya di dump saja ke layar

contoh:

1, akan mengambil: Installing Go
2, akan mengambil: Tutorial: Getting started
3, akan mengambil: Tutorial: Create a module
4, akan mengambil: Tutorial: Getting started with multi-module workspaces
5, akan mengambil: Tutorial: Developing a RESTful API with Go and Gin
6, akan mengambil: Tutorial: Getting started with generics
7, akan mengambil: Tutorial: Getting started with fuzzing
8, akan mengambil: Writing Web Applications
9, akan mengambil: Building a simple web application.
10, akan mengambil: How to write Go code
11, akan mengambil: A Tour of Go

Gunakan 'request'. Gunakan bs4 (beautiful soup) untuk parsing outputnya

2.

https://pkg.go.dev/
https://pkg.go.dev/search?q=llrb
https://pkg.go.dev/search?q=sort

ambil hasil query dan cetak url dari nomor 1 sd n tertinggi. Cetak kegunaan
package dan url nya..

def getGoPackage(query, n)

contoh:
	getGoPackage("llrb", 10) -> 1 halaman cukup
	getGoPackage("sort", 30) -> harus ambil 3 halaman..

Gunakan 'request'. Gunakan bs4 (beautiful soup) untuk parsing outputnya


3.

extend dari (2):

readGoDoc("llrb+petar")
https://pkg.go.dev/search?q=llrb+petar

ambil hasil query, pilih yang teratas, ambil link, lalu ambil bagian "Index"

Gunakan 'request'. Gunakan bs4 (beautiful soup) untuk parsing outputnya


ooOO SELAMAT MENGERJAKAN OOoo
