'''
    NAMA : DLIYA SYAHLA HARIYANTO
    NIM  : 2509116095
    SISTEM RESERVASI NAIL ART
'''
users={
    "manager":{"password":"123","status":"manager"},
    "karyawan":{"password":"456","status":"karyawan"}
}
reservasi=[]
from getpass import getpass
def login():
    while True:
        print("=== login sistem reservasi ===")
        username = input("Username : ")
        password = getpass("Password: ")
        if username in users and password == users[username]["password"]:
            print("Login berhasil sebagai", users[username]["status"])
            return users[username]["status"]
        else:
            print("Username atau password salah")


def tambah_data():
    data={}
    data["nama"] = input("Nama: ")
    data["layanan"] = input("Layanan: ")
    try:
        data["harga"]= float(input("Harga: "))
    except:
        print("Harga harus angkaaaa!!!")
        return
    data["tanggal"] = input("Tanggal: ")
    data["jam"] = input("Jam: ")
    reservasi.append(data)
    print("data berhasil di tambahkan")

def lihat_data():
    if reservasi:
        print("=== data reservasi ===")
        for data in reservasi:
            print("Nama:",data["nama"])
            print("Layanan:",data["layanan"])
            print("Harga:",data["harga"])
            print("Tanggal:",data["tanggal"])
            print("Jam:",data["jam"])
            print("=============================")
    else:
            print("anda blm reservasi")

def edit_data():
    if reservasi:
        data = reservasi[0]
        data["nama"] = input("nama baru: ")
        data["layanan"] = input("Layanan: ")
        try:
            data["harga"]= float(input("harga: "))
        except:
         print("Harga harus angkaaaa!!!")
        data["tanggal"] = input("tanggal: ")
        data["jam"] = input("jam: ")
        print("data berhasil di edit")
    else:
       print("belum ada data")

def hapus_data():
    if reservasi:
        lihat_data()
        hapus = input("hapus reservasi y/n: ")
        if hapus == "y":
            reservasi.pop(0)
            print("data berhasil di hapus")
        else:
            print("belum ada data")

status = login()

while True:
    print("=== Menu Sistem Reservasi Nail Art ===")
    print("1. tambah data ")
    print("2. lihat data ")
    if status == "manager":
        print("3. edit data")
        print("4. hapus data")
    print("5. keluar")

    pilih =input("menu : ")
    if pilih == "1":
            tambah_data()   
    elif pilih =="2":
            lihat_data()
    elif pilih == "3" and status == "manager":
            edit_data()
    elif pilih == "4" and status == "manager":
            hapus_data()
    elif pilih == "5":
            print("keluar program")
            break
    else:
            print("kamu tidak punya akses")