"""
Aplikasi monitoring terkini
"""
from gempaterkini import ekstraksi_data, tampilkan_data

import gempaterkini

if __name__ == '__main__':
    print('aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)
