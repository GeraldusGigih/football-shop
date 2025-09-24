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
---------------------------------------------------------------
# Jawaban Pertanyaan Django Authentication

## 1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.

**Django AuthenticationForm** adalah form bawaan Django yang digunakan untuk melakukan autentikasi pengguna (login). Form ini menerima username dan password, lalu memvalidasi kredensial tersebut terhadap database pengguna.

### Kelebihan:
- **Mudah digunakan**: Tinggal import dan pakai, tidak perlu membuat validasi manual
- **Keamanan terintegrasi**: Sudah dilengkapi proteksi seperti rate limiting dan password hashing
- **Validasi otomatis**: Melakukan pengecekan username/password secara otomatis
- **Fleksibel**: Bisa di-customize sesuai kebutuhan
- **Terintegrasi dengan User model**: Langsung kompatibel dengan Django User model

### Kekurangan:
- **Tampilan default sederhana**: Perlu styling CSS tambahan untuk tampilan yang menarik
- **Terbatas pada username/password**: Tidak mendukung login dengan email secara default
- **Kurang fleksibel untuk multi-authentication**: Sulit jika ingin login dengan berbagai metode (social login, dll)

## 2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?

### Perbedaan:
- **Autentikasi**: Proses memverifikasi identitas pengguna ("Siapa kamu?")
- **Otorisasi**: Proses menentukan hak akses pengguna ("Apa yang boleh kamu lakukan?")

### Implementasi Django:

#### Autentikasi:
- `django.contrib.auth.authenticate()` - memverifikasi kredensial
- `django.contrib.auth.login()` - membuat session pengguna
- `@login_required` decorator - memastikan user sudah login
- `AuthenticationForm` - form untuk login
- Session dan cookies untuk menjaga state login

#### Otorisasi:
- **Permissions**: `user.has_perm('app.permission_name')`
- **Groups**: Mengelompokkan user dengan hak akses sama
- **Decorators**: `@permission_required`, `@user_passes_test`
- **Template tags**: `{% if user.is_staff %}` untuk conditional rendering

## 3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

### Session

#### Kelebihan:
- **Keamanan tinggi**: Data disimpan di server, tidak bisa dimanipulasi client
- **Kapasitas besar**: Bisa menyimpan data kompleks tanpa batas ukuran
- **Data sensitif aman**: Password, role, dll tidak terekspos ke client

#### Kekurangan:
- **Beban server**: Membutuhkan memori/storage server untuk menyimpan data
- **Scalability issue**: Sulit di-scale pada multiple server
- **Dependency**: Bergantung pada session storage (database, Redis, dll)

### Cookies

#### Kelebihan:
- **Ringan untuk server**: Data disimpan di client, tidak membebani server
- **Persistent**: Bisa bertahan meski browser ditutup (jika diset)
- **Mudah diakses**: Bisa diakses via JavaScript di frontend

#### Kekurangan:
- **Keamanan rendah**: Bisa dimanipulasi dan dibaca oleh client
- **Ukuran terbatas**: Maksimal 4KB per cookie
- **Privacy issue**: Bisa digunakan untuk tracking pengguna

## 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

### Risiko Cookies:
- **XSS (Cross-Site Scripting)**: Cookies bisa dicuri via JavaScript malicious
- **CSRF (Cross-Site Request Forgery)**: Cookies otomatis dikirim pada setiap request
- **Man-in-the-Middle**: Cookies bisa disadap jika tidak dienkripsi
- **Session hijacking**: Session ID bisa dicuri dan digunakan orang lain

### Cara Django Menangani:

1. **HttpOnly Cookies**: `SESSION_COOKIE_HTTPONLY = True` - mencegah akses JavaScript
2. **Secure Cookies**: `SESSION_COOKIE_SECURE = True` - hanya dikirim via HTTPS
3. **SameSite**: `SESSION_COOKIE_SAMESITE = 'Strict'` - mencegah CSRF
4. **CSRF Protection**: `csrf_exempt` dan `{% csrf_token %}` di forms
5. **Secret Key**: Cookies di-sign dengan SECRET_KEY untuk mencegah manipulasi
6. **Session Expiry**: `SESSION_COOKIE_AGE` untuk membatasi waktu aktif session

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step

### Step 1: Setup Authentication System
```python
# 1. Membuat fungsi register di views.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main:show_main')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
```

### Step 2: Implementasi Login
```python
# 2. Membuat fungsi login_user
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
```

### Step 3: Implementasi Logout
```python
# 3. Membuat fungsi logout
from django.contrib.auth import logout

def logout_user(request):
    logout(request)
    return redirect('main:login')
```

### Step 4: Menghubungkan Model dengan User
```python
# 4. Menambahkan ForeignKey ke User di models.py
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # ... field lainnya
```

### Step 5: Membatasi Akses dengan Decorator
```python
# 5. Menggunakan @login_required
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def show_main(request):
    products = Product.objects.filter(user=request.user)
    # ... logic lainnya
```

### Step 6: Setup URLs
```python
# 6. Menambahkan URL patterns
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
```

### Step 7: Membuat Templates
- **register.html**: Form registrasi dengan UserCreationForm
- **login.html**: Form login dengan AuthenticationForm
- Navigation links untuk login/logout di template utama

### Step 8: Migrasi Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 9: Testing dan Security
- Test semua fungsi authentication
- Pastikan cookies aman dengan setting yang tepat di settings.py
- Implementasi CSRF protection di semua forms
