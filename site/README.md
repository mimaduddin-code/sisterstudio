# Home Sister Studio (versi foto)

Halaman Home dengan kamera yang digerakkan scroll, memakai foto asli Kebaya Srikandi Kemuning (Koleksi 008). Tanpa video AI dan tanpa pustaka luar; cukup buka `index.html` di browser atau unggah folder ini ke hosting statis.

Alur kamera (6 titik henti): pembuka "The Art of Indonesian Elegance" → 1 Pilih kebaya (badan penuh, menyamping) → 2 Pesan jadwal fitting (dari atas ke payet kerah) → 3 Terima invoice (payet tepi depan, kilau bergerak) → 4 Pakai, lalu kembalikan (turun ke songket) → penutup dengan tombol WhatsApp.

- `assets/srikandi-full.jpg` dipotong dari poster katalog lalu diperbesar 2× dan dipertajam supaya zoom tetap tajam.
- Titik henti kamera ada di array `D` (desktop) dan `M` (HP) di skrip: `s` zoom, `rx`/`ry` kemiringan, `sh` kilau payet. Titik fokus (kerah, payet depan, kain bawah) dan label detail per kebaya ada di objek `KB`.
- Di langkah "Pilih kebaya" pengunjung bisa memilih 4 koleksi (008–011).
- Home hanya berisi landing interaktif ini; kontak (Admin 1–3, Instagram) ada di kartu penutup, dan menu atas melompat ke titik kamera.
- Pengunjung dengan setelan "kurangi gerakan" melihat versi statis empat kartu.
- Versi artifact: https://claude.ai/artifact/WLrdUgiWw5F3Ube2fMmxnb

Untuk versi video 3D (Higgsfield, skill scroll-world) foto bisa diganti klip video yang di-scrub dengan pola titik henti yang sama.
