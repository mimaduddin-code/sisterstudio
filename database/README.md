# Database Sister Studio

Semua data website sisterstudio.com dan kelima agen disimpan di database Claude (penyimpanan dokumen milik artifact).

- Halaman database (privat, hanya anggota organisasi): https://claude.ai/artifact/SyaPauyJr5rety3ULgpppy
- Hak akses: semua orang yang bisa membuka halaman bisa **membaca**. Hanya **owner dan editor** yang bisa menambah, mengubah, atau menghapus.
- Isi awal: 115 dokumen di 17 koleksi (`seed/`). Dokumen dengan `"contoh": true` adalah data contoh dari desain. Hapus sekaligus lewat tombol **Hapus data contoh** di halaman database.

## Isi folder

| Path | Isi |
| --- | --- |
| `seed/<koleksi>/<id>.json` | Satu file per dokumen, persis seperti yang dimasukkan ke database. |
| `seed/_index.json` | Daftar semua koleksi dan ID dokumen. |
| `buat_seed.py` | Skrip yang membuat isi `seed/`. Jalankan `python3 buat_seed.py seed` untuk membuat ulang. |
| `halaman-database.html` | Kode halaman database: daftar koleksi, tabel, editor dokumen, hapus data contoh, unduh JSON. |

## Koleksi

Format umum: tanggal ISO (`2026-11-21` atau `2026-11-21T10:00`, waktu lokal studio), uang dalam rupiah bulat (`250000`), ID pelanggan memakai nama kecil (`nur`), ID koleksi memakai kode (`008`).

| Koleksi | ID dokumen | Field utama | Dipakai oleh |
| --- | --- | --- | --- |
| `pengaturan` | `studio` | nama, tagline, website, instagram, admin[] (nama, whatsapp), alamat, jam_buka, email, maps, dp_persen, lama_sewa_hari, jam_fitting[], jam_kirim_pengingat | Website, semua agen |
| `agen` | `admin`, `cs`, `kreator`, `kasir`, `stok` | nama, tugas[], status | Admin Agen |
| `koleksi` | `008`…`011` | kode, nama, kategori, harga, satuan, deskripsi, foto, tampil, stok{S,M,L,XL → total, tersedia, disewa, perawatan} | Katalog, Fitting, Agen Kreator, Agen Stok |
| `gerak_stok` | `GRK-001`… | waktu, gerak (Keluar/Kembali), koleksi, ukuran, pelanggan, catatan | Agen Stok (riwayat peminjaman) |
| `perawatan` | `RWT-001`… | koleksi, ukuran, jenis (Laundry/Perbaikan), catatan, status, siap | Agen Stok |
| `pelanggan` | nama kecil | nama, email, whatsapp, login (Google), pengingat[] | Akun saya, Agen CS |
| `reservasi` | `RSV-2026-11-0042` | pelanggan, koleksi, ukuran, fitting, ambil, acara, kembali, status, invoice | Fitting, Akun saya, Admin Agen |
| `pengingat` | `PNG-001`… | kirim, pelanggan, jenis, jadwal, kanal, status, reservasi | Agen CS, Agen Stok, Akun saya |
| `testimoni` | bebas | pelanggan, koleksi, momen, ulasan, rating, status (Menunggu/Tampil) | Testimoni (kosong sampai ada ulasan asli) |
| `invoice` | `INV-2026-11-0042` | reservasi, pelanggan, item[] (keterangan, jumlah, harga), total, dp, dibayar, sisa, status, terbit | Invoice, Agen Kasir |
| `kas` | `KAS-2026-11-001`… | waktu, keterangan, kategori, masuk, keluar, invoice | Agen Kasir |
| `rekap` | `2026-11`, `bulanan-2026` | kas_masuk, kas_keluar, saldo, piutang, keluar_per_kategori{}, disewa_per_koleksi{}, analisa[]; pendapatan{bulan → rupiah} | Agen Kasir, Admin Agen |
| `faq` | `FAQ-01`… | pertanyaan, jawaban, dipakai_minggu_ini, tampil_di_website | Kontak, Agen CS |
| `dokumen` | `syarat-ketentuan`, `kontak-sewa`, `lokasi-jam-buka` | judul, butir[] / isi, versi, diperbarui | Kontak, Invoice, Agen CS |
| `konten` | `KTN-001`…, `ide` | tayang, judul, kanal[], status, koleksi, caption | Agen Kreator |
| `aktivitas` | tanggal (`2026-11-14`) | tanggal, entri[] (waktu, agen, teks) | Admin Agen (satu dokumen per hari agar tidak melewati batas jumlah dokumen) |
| `keputusan` | `KPT-001`… | agen, teks, rujukan, status, dibuat | Admin Agen |

## Data asli vs contoh

- **Asli** (`contoh: false`): 4 koleksi beserta harga dan deskripsi dari poster katalog, kontak Admin 1–3, Instagram, FAQ, draf S/K, daftar agen. Nilai dalam kurung siku (`[Alamat studio]`, `[Rp…]`) masih harus diisi.
- **Contoh** (`contoh: true`): pelanggan, reservasi, invoice, kas, rekap, pengingat, gerak stok, perawatan, konten, log aktivitas, keputusan. Angka stok di `koleksi` juga contoh (`stok_sumber: "contoh"`).

## Batas

- Paling banyak 25.000 dokumen dan 256 KiB per dokumen. Log yang terus bertambah (aktivitas agen) digabung per hari.
- Database ini milik artifact. Kalau website nanti dibangun di server sendiri, ekspor lewat tombol **Unduh JSON** lalu impor ke database server (strukturnya sama dengan `seed/`).
