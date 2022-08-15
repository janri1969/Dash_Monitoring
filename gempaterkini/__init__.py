"""
Aplikasi gempa terkini dari BMKG
"""
import requests
from bs4 import BeautifulSoup

def ekstraksi_data():

    try:
        content = requests.get('https://bmkg.go.id')
        except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.paser')

        result = soup.find('span', {'class' : 'waktu'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div', {'class' : 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        i = 0
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None

        for res in result:
            if i == 1:
                magnitudo = rest.text
            elif i == 2:
                kedalaman = rest.text
            elif i == 3:
                koordinat = rest.text.split[' - ']
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = rest.text
            elif i == 5:
                dirasakan = rest.text
            i = i + 1

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'ls' : ls, 'bt' : bt}
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan
        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print("Tidak menemukan data gempa terkini")
        return

    print("Gempa Terakhir berdasarkan BMKG")
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi {result['lokasi']}")
    print(f"Koordinat : LS = {result['koordinat']['ls']}, BT = {result['koordinat']['bt']}")
    print(f"{f"Dirasakan {result['dirasakan']}")


if __name == '__main__':
    print('Ini adalah Package Gempa Terkini')


