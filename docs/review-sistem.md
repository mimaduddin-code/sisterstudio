# Review sistem Sister Studio

Per Sabtu, 14 November 2026. Mencakup desain website, database, koneksi email dan WhatsApp, dan bot kelima agen.

## Status per komponen

| Komponen | Status | Catatan |
| --- | --- | --- |
| Desain 13 halaman (canvas) | Selesai | Prototipe yang bisa diklik. Tidak terhubung ke database. |
| Form reservasi di halaman Fitting | **Diperbaiki** | Nama, email, dan WhatsApp sebelumnya terkunci atau tidak divalidasi. |
| Kontrol form di 6 halaman lain | **Diperbaiki** | 17 kotak centang, pilihan, dan isian sebelumnya tidak bisa diubah. |
| Database (artifact Claude) | Berjalan | 17 koleksi, 115 dokumen awal, hak tulis hanya owner/editor. |
| Form "Reservasi baru" di database | **Baru** | Admin/CS mencatat reservasi; otomatis membuat pelanggan, reservasi, invoice, 5 pengingat, dan log. |
| Bot 5 agen | Terjadwal | Berjalan otomatis, tetapi **belum bisa mengirim pesan** (lihat Batasan 3). |
| Gmail | Menunggu Anda | Tautan otorisasi lewat Composio sudah dibuat. |
| WhatsApp | Menunggu Anda | Hanya WhatsApp Business API (Meta). Perlu template pesan yang disetujui. |
| Website publik sisterstudio.com | Belum ada | Baru desain. Perlu hosting dan backend sendiri. |
| Login Google pelanggan | Belum ada | Baru desain. Perlu OAuth Google di website asli. |
| Pembayaran | Manual | Transfer/QRIS dicatat admin. Belum ada payment gateway. |

## Temuan dan perbaikan hari ini

1. **Reservasi tidak bisa diisi.** Di halaman Fitting, kolom Nama terkunci pada teks contoh, kolom Email diset hanya-baca, dan nomor WhatsApp tidak disimpan saat pindah langkah. Persetujuan S/K juga tidak wajib. Sekarang ketiganya bisa diketik dan dicek sebelum lanjut: nama minimal 2 huruf, format email, nomor WA diawali 08/+62 (disimpan sebagai 62xxx), minimal satu saluran pengingat, dan S/K wajib dicentang. Halaman selesai menampilkan email dan nomor yang benar-benar diisi. Logika ini diuji: isian kosong ditolak dengan 4 pesan, isian benar lanjut ke langkah selesai.
2. **Kontrol form terkunci di halaman lain.** Admin login (kata sandi, ingat perangkat), Agen Kreator (form edit koleksi, ukuran, tanggal posting), Agen Kasir (jenis transaksi), Agen Stok (kondisi, jumlah, tanggal), Akun saya (saluran pengingat), dan Katalog (tanggal acara). Semua sekarang bisa diubah.
3. **Halaman database melebar di HP.** Label tersembunyi di tabel keluar dari kotak geser. Sudah diperbaiki dan diukur pas di lebar 390 px.
4. **Belum ada cara memasukkan reservasi asli ke database.** Ditambahkan form "Reservasi baru" di halaman database. Diuji di browser dengan database tiruan: validasi bekerja, dan satu simpanan menghasilkan pelanggan, reservasi, invoice (DP sesuai persen di pengaturan), 5 pengingat, dan satu entri log.
5. **Agen belum berjalan sendiri.** Dibuat 5 tugas terjadwal (lihat `agents/README.md`), dengan aturan pengaman yang sama: lewati data contoh dan kontak placeholder, cegah kiriman ganda, maksimal 30 pesan per jalan, tidak pernah menghapus data, catat setiap jalan di log aktivitas.

## Batasan yang perlu diketahui

1. **Canvas adalah desain, bukan website.** Halaman di canvas tidak membaca atau menulis database. Reservasi yang dicoba di canvas tidak tersimpan dan tidak memicu pesan. Reservasi asli saat ini masuk lewat form "Reservasi baru" di halaman database.
2. **Database Claude hanya untuk anggota organisasi.** Pelanggan umum tidak bisa membukanya. Agar pelanggan bisa reservasi sendiri dengan login Google, website publik harus dibangun dan di-hosting terpisah, misalnya Next.js di Vercel dengan Firebase atau Supabase, Google OAuth, dan domain sisterstudio.com. Struktur koleksi di `database/README.md` bisa dipakai apa adanya.
3. **Bot belum punya akses Composio.** Tugas terjadwal yang dibuat dari sesi Claude Code tidak membawa penghubung. Bot tetap bisa membaca/menulis database, tetapi pesan email dan WA ditandai "Menunggu koneksi". Perbaikan: di claude.ai, buka daftar tugas terjadwal (routines), lalu tambahkan penghubung Composio ke **Agen CS**, **Agen Stok**, dan **Admin Agen**. Kalau pilihan itu tidak ada, buat ulang ketiganya dari halaman routines dengan instruksi yang sama (tersimpan di `agents/README.md`).
4. **WhatsApp Business API punya aturan sendiri.** Perlu akun Meta Business, nomor yang terdaftar di WhatsApp Business Platform, dan template pesan yang disetujui Meta. Pesan bebas hanya boleh dalam 24 jam setelah pelanggan mengirim chat. Template yang perlu diajukan (bahasa Indonesia): konfirmasi reservasi & invoice, batas bayar DP, H-1 fitting, H-1 pengambilan, hari pengembalian, terlambat kembali, laporan owner.
5. **Chat masuk tidak dijawab otomatis.** Bot terjadwal hanya bangun pada jam tertentu. Menjawab FAQ secara langsung butuh webhook WhatsApp yang memanggil agen setiap ada pesan masuk. Ini bagian dari website/backend asli.
6. **Data contoh masih ada di database.** Bot melewatinya, tetapi sebaiknya dihapus sebelum operasional (tombol "Hapus data contoh").
7. **Isian yang masih placeholder:** alamat dan jam buka studio, email studio, nomor rekening, nilai di S/K (lama sewa, DP, jaminan, denda, pembatalan), `owner_email` dan `owner_whatsapp` di `pengaturan/studio`, tautan Google Maps.
8. **Akses canvas.** Canvas desain sempat tercatat bisa dibuka siapa saja yang punya link. Periksa menu Share bila harus privat. Database tetap privat.
9. **Login admin di desain** memakai kata sandi. Untuk versi asli, sebaiknya admin masuk dengan Google + verifikasi dua langkah, dan peran owner/admin dibedakan.
10. **Biaya jalan bot.** Sekitar 43 sesi per minggu (CS 21, Stok 7, Kasir 7, Admin 7, Kreator 1). Bisa dijeda kapan saja dari daftar tugas terjadwal.

## Langkah berikut, urut prioritas

1. Selesaikan otorisasi Gmail di Composio (pakai akun Gmail studio).
2. Tambahkan penghubung Composio ke rutinitas Agen CS, Agen Stok, dan Admin Agen.
3. Isi `pengaturan/studio` dan dokumen S/K di halaman database.
4. Uji ujung ke ujung: buat satu reservasi lewat "Reservasi baru" memakai email dan nomor WA Anda sendiri, jalankan Agen CS sekali, lalu cek email masuk.
5. Siapkan WhatsApp Business API dan ajukan template. Sampai siap, pengingat WA dikirim manual oleh admin; email berjalan otomatis.
6. Hapus data contoh.
7. Bangun website publik (reservasi pelanggan, login Google, webhook WhatsApp) dari repo ini.
