"""
Aplikasi Gempa Terkini
"""
from gempaterkini import ekstraksi_data, tampilkan_data

if __name__ == '__main__':
    print('aplikasi gempa')
    result = ekstraksi_data()
    tampilkan_data(result)