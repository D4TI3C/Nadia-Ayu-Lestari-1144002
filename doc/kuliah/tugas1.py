import time
start_time = time.time()
print("Menghitung nilai rumus matematika menggunakan bahasa itali")
m = raw_input("Masukan Nilai 1: ")
i = raw_input("Masukan Nilai 2: ")
n = raw_input("Masukan Nilai 3: ")
h = raw_input("Masukan Nilai 4: ")
o = raw_input("Masukan Nilai 5: ")

if m == 'uno':
	m=1

if m == 'due':
	m=2

if m == 'tre':
	m=3

if m == 'quattro':
	m=4

if m == 'cinque':
	m=5

if m == 'sei':
	m=6

if m == 'sette':
	m=7

if m == 'otto':
	m=8

if m == 'nove':
	m=9

if m == 'zero':
	m=0


if i == 'uno':
	i=1

if i == 'due':
	i=2

if i == 'tre':
	i=3

if i == 'quattro':
	i=4

if i == 'cinque':
	i=5

if i == 'sei':
	i=6

if i == 'sette':
	i=7

if i == 'otto':
	i=8

if i == 'nove':
	i=9

if i == 'zero':
	i=0

if n == 'uno':
	n=1

if n == 'due':
	n=2

if n == 'tre':
	n=3

if n == 'quattro':
	n=4

if n == 'cinque':
	n=5

if n == 'sei':
	n=6

if n == 'sette':
	n=7

if n == 'otto':
	n=8

if n == 'nove':
	n=9

if n == 'zero':
	n=0


if h == 'uno':
	h=1

if h == 'due':
	h=2

if h == 'tre':
	h=3

if h == 'quattro':
	h=4

if h == 'cinque':
	h=5

if h == 'sei':
	h=6

if h == 'sette':
	h=7

if h == 'otto':
	h=8

if h == 'nove':
	h=9

if h == 'zero':
	h=0


if o == 'uno':
	o=1

if o == 'due':
	o=2

if o == 'tre':
	o=3

if o == 'quattro':
	o=4

if o == 'cinque':
	o=5

if o == 'sei':
	o=6

if o == 'sette':
	o=7

if o == 'otto':
	o=8

if o == 'nove':
	o=9

if o == 'zero':
	o=0

jumlah =(m*i)+(n/h-o) 
print ("hasil" , jumlah) 
print("time : %s detik " % (time.time() - start_time))