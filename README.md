link football-shop : https://geraldus-catur-footballshop.pbp.cs.ui.ac.id/

Checklist 1:
instalasi dependencies terlebih dahulu sebelum membuat projek Django menggunakan requirements.txt dan tidak lupa menggunakan virtual env
setelah itu bisa membuat projek Django baru di direktori dengan nama "football_shop"
lalu melanjutkan dengan setup Environment Variables dan Proyek untuk memungkinkan kode berjalan di env berbeda tanpa perlu mengubah kode
tidak lupa kita setup .env.prod untuk menggunakan database yang telah diberikan
kita load juga .env di settings.py dengan function load_dotenv()
setelah itu melakukan setup lain nya di settings.py seperti ALLOWED_HOSTS, PRODUCTION, DATABASES
setelah itu kita coba runserver Django, kalo udah bisa kita lanjut ke next step yaitu setup main.

Checklist 2:
membuat main dengan perintah startapp main lalu setelah itu didaftarkan ke INSTALLED_APPS yang ada di settings.py setelah itu membuat direktori template dengan isi file main.html

Checkpoint 3:
Setelah itu, kita melakukan routing URL untuk aplikasi main yang telah dibuat, dengan cara menggunakan urls.py

Checkpoint 4:
Kita akan membuat model pada aplikasi main dengan nama Product. Saya memodifikasi file models.py
Setelah itu saya masukan atribut wajib dan beberapa atribut tambahan sebagaimana nanti gambaran web saya akan berjalan

Checkpoint 5:
Membuat function untuk dikembalikan ke template main.html dimana isi nya adalah dict untuk nama aplikasi, nama saya, kelas

Checkpoint 6:
Setelah itu saya melakukan routing untuk URL Proyek pada urls.py pada tingkat proyek yang ada di direktori football-shop

Checkpoint 7:
Melakukan deployment ke PWS agar bisa diakses oleh orang lain.

------------------------------------------------------------------------------------------------
Link Bagan: https://drive.google.com/file/d/1TlxxJMFOrxRQ8SdPoH9FegaUkL7nu9j7/view?usp=sharing
------------------------------------------------------------------------------------------------
settings.py untuk apa?

Sepengetahuan saya file tersebut berfungsi seperti nama nya, yaitu untuk melakukan beberapa pengaturan seperti menggunakan database apa? ingin aplikasi apa? host yang diperbolehkan siapa aja? dan lain lain.
------------------------------------------------------------------------------------------------
Migrasi di Django berfungsi untuk sinkronisasi database dengan model. 
makemigrations → buat file instruksi perubahan database.
migrate → jalankan instruksi ke databse.
------------------------------------------------------------------------------------------------
Menurut saya, Django dipilih sebagai permulaan karena framework ini sudah lengkap dan punya banyak fitur bawaan sehingga memudahkan pemula. Django juga terstruktur dengan konsep MTV, jadi kita belajar membangun aplikasi dengan cara yang rapi. Selain itu, dokumentasinya jelas dan komunitasnya besar, jadi gampang mencari bantuan saat belajar.
------------------------------------------------------------------------------------------------
Untuk feedback nya sih sudah cukup bagus untuk pembuatan tutorial nya, jadi tidak perlu mencari tahu lagi fungsi masing masing step karena di dokumentasikan dengan baik dan lengkap.
