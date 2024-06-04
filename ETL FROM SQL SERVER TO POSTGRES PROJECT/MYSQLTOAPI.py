import mysql.connector
import requests

# Konfigurasi koneksi MySQL
db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'sample_employee'
}

try:
    # Menghubungkan ke database MySQL
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    print("SUKSES CONNECTION")

    # Query untuk mengambil data dari tabel MySQL
    query = "SELECT NIP, nama FROM sample_employee"
    cursor.execute(query)
    print("execute ke DB berhasil")

    # Mengambil semua baris data
    rows = cursor.fetchall()
    if not rows:
        print("No data found in the database.")
        cursor.close()
        conn.close()
        exit()

    # URL API tujuan
    api_url = "http://172.16.200.155:8069/api-employee-integration"

    # Loop melalui data dan kirim ke API
    for row in rows:
        NIP, name = row
        print(f"Sending data: NIP={NIP}, name={name}")

        # Data untuk dikirim ke API
        data = {
            'token': 'AFZALGANTENG',
            'nip': NIP,
            'name': name
        }

        # Mengirim data ke API
        response = requests.post(api_url, data=data)

        # Cek status response dari API
        if response.status_code == 200:
            print(f"Data berhasil dikirim: NIP={NIP}, name={name}")
        else:
            print(f"Data gagal dikirim: NIP={NIP}, name={name}, Status Code: {response.status_code}, Response: {response.text}")

    # Menutup koneksi ke database
    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")

except Exception as e:
    print(f"An error occurred: {str(e)}")

