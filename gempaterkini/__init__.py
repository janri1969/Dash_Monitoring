"""
Aplikasi gempa terkini dari BMKG
"""

def ekstraksi_data():
    hasil=dict()
    hasil['tanggal'] = '24 Agustuss 2021'
    hasil['waktu'] = '12:05:52 WIB'
    hasil['magnitudo'] = 4.0
    hasil['lokasi'] = {'ls':1.48, 'bt':134.01}
    hasil['pusat'] = 'Pusat gempa berada di darat 118 KM barat laut ransiki'
    hasil['dirasakan'] = 'Dirasakan (skala MMI): II-III Manokwari, II-III Ransiki'

    return hasil

def tampilkan_data(result):
    print("Gempa Terakhir berdasarkan BMKG")
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi : LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"{result['pusat']}")
    print(f"{result['dirasakan']}")

