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


------------------------------------------------------------------------------
1. Pentingnya Data Delivery
Data delivery merujuk pada proses pengiriman data dari satu sistem (seperti server) ke sistem lain (seperti aplikasi client). Kita memerlukannya karena ini adalah inti dari setiap platform modern yang dinamis. Tanpa data delivery yang efisien, sebuah platform tidak dapat berfungsi. Misalnya, ketika kamu membuka Instagram, gambar dan feed yang kamu lihat dikirimkan dari server ke aplikasi di ponselmu. Ini memungkinkan data untuk selalu up-to-date dan diakses secara real-time oleh pengguna, tidak peduli lokasi dan perangkat yang mereka gunakan.

2. Perbandingan XML dan JSON
Menurut saya, JSON (JavaScript Object Notation) jauh lebih baik dan lebih populer daripada XML (Extensible Markup Language). Alasan utamanya adalah kesederhanaan dan kemudahan penggunaannya.

JSON memiliki sintaks yang ringkas dan mudah dibaca oleh manusia. Strukturnya mirip dengan objek JavaScript, sehingga sangat mudah untuk diurai (parse) dan digunakan dalam bahasa pemrograman modern, terutama JavaScript.

XML menggunakan tag, yang membuat ukurannya lebih besar dan sintaksnya lebih rumit. Meskipun sangat kuat dan self-describing, XML memerlukan parser yang lebih kompleks dan cenderung lebih verbose.

Popularitas JSON meningkat seiring dengan berkembangnya aplikasi web yang intensif dengan JavaScript dan mobile app. JSON menjadi standar de-facto untuk API karena efisiensi dan kemudahannya.

3. Fungsi is_valid() pada Form Django
Method is_valid() pada Django Forms berfungsi untuk memeriksa validitas data yang disubmit oleh pengguna. Ketika method ini dipanggil, Django akan melakukan beberapa validasi secara otomatis, seperti:

Memeriksa apakah field yang disubmit sesuai dengan tipe data yang ditentukan (e.g., integer, email, tanggal).

Memastikan field yang wajib diisi (required=True) tidak kosong.

Memeriksa batasan panjang karakter, format, atau aturan kustom lainnya yang didefinisikan dalam form.

Kita membutuhkan method ini untuk mencegah data yang tidak valid atau berbahaya masuk ke database. Tanpa is_valid(), aplikasi akan rentan terhadap kesalahan data dan bahkan serangan siber seperti SQL Injection. Jika validasi gagal, method ini akan mengembalikan False dan form akan menyimpan pesan error yang bisa ditampilkan kepada pengguna.

4. Peran csrf_token di Django
csrf_token (Cross-Site Request Forgery Token) adalah token unik yang harus disertakan dalam setiap formulir POST di Django. Tujuannya adalah untuk melindungi aplikasi dari serangan CSRF.

Jika kita tidak menambahkan csrf_token, seorang penyerang dapat memanfaatkan celah ini. Mereka bisa membuat halaman web berbahaya yang berisi form tersembunyi. Ketika korban (yang sedang login di website kita) membuka halaman tersebut, form tersembunyi itu akan secara otomatis terkirim ke website kita. Website kita akan menganggapnya sebagai permintaan yang sah dan menjalankan aksi berbahaya, seperti mengubah kata sandi atau mentransfer uang, tanpa sepengetahuan korban.

Dengan csrf_token, Django akan memeriksa apakah token yang dikirimkan bersama form cocok dengan yang ada di sesi pengguna. Jika tidak cocok, permintaan akan ditolak. Ini memastikan bahwa permintaan tersebut benar-benar berasal dari formulir di situs kita dan bukan dari situs lain yang berbahaya.

Checklist 1&2:
pada views.py menerapkan fungsi untuk mengembalikan permintaan di url untuk /json,/xml,/json/:id,/xml/:id

Checklist 3,4,5:
Tambahkan button di main.html untuk href ke 2 file html lain nya dimana ada :
1. create_product.html untuk menampilkan form menambahkan produk baru di toko
2. product_details.html untuk menampilkan data data produk yang dipilih sesuai dengan apa yang disimpan database

Feedback Asdos: Sudah sangat membantu untuk kendala pengerjaan dan juga penjelasan materi

POSTMAN TEST:
https://drive.google.com/drive/folders/19CKgop3e_Do4X1lZoIb5OQz6VMOe4kJ3?usp=sharing

