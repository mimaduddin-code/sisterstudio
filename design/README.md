# Sister Studio — desain website sisterstudio.com

Bahan desain website sewa kebaya Sister Studio, untuk dilanjutkan di Figma.

- Canvas Claude (privat): https://claude.ai/artifact/2okXqKdTbSCeeZkedHzRTZ
- Design system: Sister Studio (`tokens.json` di folder ini adalah salinannya)

## Isi folder

| Path | Isi |
| --- | --- |
| `pages/*.dc.html` | 5 halaman publik yang sudah jadi. Format canvas Claude (butuh `support.js` dari canvas), jadi pakai sebagai acuan tata letak, isi, dan gaya, bukan sebagai situs yang langsung jalan. |
| `canvas.json` | Daftar 12 halaman beserta ukuran dan susunannya di canvas. |
| `tokens.json` | Warna, tipografi, spasi, radius, dan bayangan dari design system. |
| `assets/foto/` | Foto kebaya yang dipotong dari poster katalog, foto manekin, dan 2 foto interior studio. |
| `assets/katalog/` | Poster katalog asli Koleksi 008–011. |
| `assets/logo/` | Logo PNG transparan (maroon) dan versi di latar putih. |

## Gaya (ringkas dari design system)

- Latar krem `ivory-50 #fdf3e7`; panel `ivory-100 #fbe9d7`; kartu `surface-card #fffaf3`.
- Merek `maroon-700 #730020` (tombol primer, badge, kotak harga, bar kontak); judul `maroon-900 #4e0014`.
- Emas: `gold-300 #f2d08c` untuk teks/ikon di atas maroon, `gold-500 #c8924a` hanya untuk bingkai dan ornamen, `gold-700 #85561c` untuk eyebrow di atas krem.
- Teks `ink #1f0a0a`, sekunder `ink-muted #6a4a44`; garis `line #e6c9a5`; border kontrol `control-border #9a7a5a`.
- Status (selalu disertai kata): sukses `#155e63` / `#dcefee`, menunggu `#7a4a00` / `#fbe7c0`, bermasalah `#a11d12` / `#fbe0da`, info `#3a4a72` / `#e4e8f3`.
- Huruf: Crimson Pro untuk semua teks, Great Vibes hanya untuk nama koleksi (satu baris).
- Foto produk selalu dalam bingkai lengkung (arch) bergaris `gold-500`. Tombol dan input sudut 2px, kartu 12px.

## Data asli dari katalog

| Kode | Nama | Harga sewa | Deskripsi di poster |
| --- | --- | --- | --- |
| Koleksi 008 | Kebaya Srikandi Kemuning | Rp250.000 / stel | Perpaduan gaya Jawa yang anggun dengan sentuhan Melayu yang mewah, melambangkan kelembutan, ketegasan, dan keanggunan seorang wanita Nusantara. |
| Koleksi 009 | Fuchsia Glam | Rp300.000 / stel | Kebaya modern bernuansa elegan dengan taburan payet yang berkilau, memancarkan pesona anggun dan glamor di setiap momen istimewa. |
| Koleksi 010 | Kebaya Candrakirana Nusantara | Rp300.000 / stel | Kebaya anggun bernuansa hijau lembut, terinspirasi dari kemilau cahaya rembulan (Candrakirana) yang memancarkan ketenangan, keanggunan, dan pesona wanita Nusantara. |
| Koleksi 011 | Kebaya Mocha Elegance | Rp200.000 / stel | Kebaya renda bernuansa mocha yang memancarkan kesan anggun, lembut, dan berkelas di setiap suasana istimewa. |

Kontak: Admin 1 081271116292 · Admin 2 081368685449 · Admin 3 082216219763 · Instagram @sisterstudio.plg

## Halaman

### Sudah jadi (website publik)

1. **Home** (`Main.dc.html`): menu, hero dengan foto manekin di bingkai lengkung, cara sewa 4 langkah, 4 koleksi, cuplikan testimoni, bagian Kunjungi Studio (foto interior, alamat, jam buka, 3 admin), bar kontak.
2. **Testimoni**: saring menurut momen, kartu testimoni dengan foto kebaya yang dipakai, formulir tulis testimoni untuk akun Google yang sudah mengembalikan kebaya (tampil setelah disetujui admin).
3. **Katalog**: saring menurut status, ukuran, tanggal acara, dan urutan; kartu koleksi dengan foto, harga, status stok, tombol Pesan fitting.
4. **Fitting** (interaktif): Masuk dengan Google → pilih kebaya dan ukuran → pilih tanggal dan jam → konfirmasi (WhatsApp, pengingat, cara bayar DP, setuju S/K) → selesai (invoice terkirim, daftar pengingat). Ringkasan di samping menghitung DP 50%.
5. **Kontak**: 3 admin WhatsApp, Instagram, email, studio, foto ruang fitting, formulir pesan, chat Agen CS dengan balasan cepat, FAQ, dan draf syarat & ketentuan sewa.

### Belum dibuat

6. **Akun saya** (login Google): reservasi mendatang, invoice (status DP/Lunas), pengingat terkirim/terjadwal, riwayat sewa, tombol tulis testimoni.
7. **Invoice**: dokumen bermerek; nomor INV, pelanggan, item sewa, DP, sisa, cara bayar, status, ringkasan S/K, bar kontak.
8. **Admin login**: email dan kata sandi admin, panel kayu walnut dengan wordmark.
9. **Admin Agen** (dashboard owner): ringkasan angka; laporan aktivitas semua agen dengan waktu dan label agen; konsol perintah (owner mengetik perintah, agen menjawab dengan ringkasan dan aksi); reminder reservasi 3 hari ke depan; status 5 agen.
10. **Agen CS**: kotak masuk percakapan (dijawab bot / perlu admin), utas chat dengan balasan cepat, basis FAQ yang bisa diedit, antrean reminder reservasi (WhatsApp/email), template S/K dan kontak sewa.
11. **Agen Kreator**: tabel katalog (tambah/edit/hapus), formulir koleksi (nama, kode, ukuran, harga, deskripsi dibantu agen, foto), pembuat posting medsos (caption, pratinjau, jadwal, kanal).
12. **Agen Kasir & Akuntan**: kas masuk/keluar/saldo/piutang, tabel invoice dan pembayaran, buku kas, rekap bulanan, analisa usaha (koleksi terlaris, tren).
13. **Agen Stok Inventaris**: stok per koleksi dan ukuran, catatan keluar dan kembali, reminder pengembalian (hari ini, besok, terlambat), riwayat peminjaman per kebaya, kondisi dan perawatan (laundry, perbaikan), formulir tambah stok.

Sidebar admin: maroon-900 dengan teks krem; item aktif maroon-700 dengan teks gold-300.

## Yang masih perlu diisi pemilik

- Alamat studio, jam buka, email, tautan Google Maps.
- Nilai di syarat & ketentuan: lama sewa, besar DP, jaminan, denda per hari, batas pembatalan, kebijakan antar.
- Ulasan pelanggan asli untuk halaman Testimoni (sekarang placeholder).
- Status stok, tanggal, dan nomor invoice di desain adalah contoh, begitu juga aturan DP 50% dan jam fitting.
- Ukuran tiap koleksi.
