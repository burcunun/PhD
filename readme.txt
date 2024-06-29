** Not: 4. ve 5. adım uzun süren bir adımdır ve webdeki bilgileri çekip düzenlemeye yönelik bir adımdır ve daha önce yapılmıştır. bu yüzden tekrar yapılmasına gerek yoktur. Diğer adımlar yapılarak uygulama çalıştırılabilir. 

1. Python son sürümü yüklenir.
2. Nodejs son sürümü yüklenir.
3. Docker son sürümü yüklenir ve çalıştırılır.
4. Python ile \backend\crawler klasöründeki crawler.py dosyası çalıştırılır
5. \backend\crawler klasöründe oluşan publishes.json dosyası \backend\server klasörüne taşınır.
6. \backend\server klasöründeki elastic.cmd çift tıklayarak çalıştırılır. 
7. pip install -r requirements.txt ile gerekli paketler yüklenir.
8. \backend\server klasöründeki index_data.py dosyası çalıştırılır (Burada yaklaşık yarım saat boyunca kayıtların indekslenmesi beklenir).
9. \backend\server klasöründeki server.py dosyası çalıştırılır.
10. \frontend klasöründe npm install komutu çalıştırılır.
11. \frontend klasöründe npm start komutu çalıştırılır.
12. localhost:3000 adresine gidilip uygulama kullanılabilir.

