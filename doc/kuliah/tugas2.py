graph = {
             'Barru': ['Panroko'],
             'Panroko': ['Bojo'],
             'Bojo': ['Lumpue'],
             'Lumpue': ['Mattirotasi'],
             'Mattirotasi': ['Lasinrang'],
             'Lasinrang': ['Bili-bili'],
             'Bili-bili': ['Suppa'],
             'Suppa': ['Pinrang'],        
        }

def rutepalingpendek(graph, lokasi_awal, lokasi_tujuan, rute=[]):
        rute = rute + [lokasi_awal]
        if lokasi_awal == lokasi_tujuan:
            return rute
            if not graph.has_key(lokasi_awal):
                    return None
        rutependek = None
        for node in graph[lokasi_awal]:
            if node not in rute:
                rutebaru = rutepalingpendek(graph, node, lokasi_tujuan, rute)
                if rutebaru:
                    if not rutependek or len(rutebaru) < len(rutependek):
                        rutependek = rutebaru
        return rutependek
print("Rute Jalan Raya Barru sampai Pinrang")
print("(Barru-Panroko-Bojo-Lumpue-Mattirotasi-Lasinrang-Bili-bili-Suppa)")
print("Nadia Ayu Lestari Arifin-1144002")
print("\n")
lokasi_awal = raw_input("Masukan Lokasi Awal : ")
lokasi_tujuan = raw_input("Masukan Lokasi Tujuan : ")
hasilnya = rutepalingpendek(graph, lokasi_awal, lokasi_tujuan, rute=[])
print "Rute Terpendek", hasilnya ,".",