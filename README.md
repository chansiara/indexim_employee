FEATURES :
Backend - Django (Python)
Frontend - jQuery
DB - PostgreSQL
Saya juga membuat cms sendiri untuk memudahkan penggunaan django & jquery agar code reusable dan mudah dipalikasikan

CARA RUN MINI EMPLOYEE MANAGER :

1. Install Python (version > 3.7)
2. Install Postgresql (version > 10)
3. clone project, taruh pada direktori yang diinginkan (misal c:\django\indexim_employee)
4. Buat venv (Virtual Environment python) di direktori sesuai tempat clone project
5. masuk pada virtual env dengan activate script command (c:\django\indexim_employee\Env\Scripts\Activate)
6. masuk pada folder project yang telah di clone (misal  c:\django\indexim_employee\indexim_employee)
7. jalankan requirements.txt yang ada pada project dengan perintah pip install -r requirements.txt
8. setelah selesai menginstall package, setting nama db postgre di settings.py, setelah sesuai jalankan perintah python manage.py makemigrations
9. setelah selesai, jalankan perintah python manage.py migrate
10. setelah selesai , jalankan perintah python manage.py loaddata initial_position.json

INFORMASI TAMBAHAN :

JIKA BERHASIL MAKA APLIKASI AKAN TERLIHAT SEPERTI GAMBAR-GAMBAR DI FOLDER DOCUMENTATION
