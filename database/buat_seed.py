"""Build seed documents for the Sister Studio database (one JSON file per document)."""
import json, sys, pathlib, shutil
out = pathlib.Path(sys.argv[1])
if out.exists(): shutil.rmtree(out)
docs = {}
def put(col, did, data): docs[(col, did)] = data

# ---------- pengaturan (data asli + placeholder) ----------
put('pengaturan', 'studio', {
  'nama': 'Sister Studio', 'tagline': 'Sewa Kebaya & Dress', 'website': 'sisterstudio.com',
  'instagram': '@sisterstudio.plg',
  'admin': [
    {'nama': 'Admin 1', 'whatsapp': '081271116292'},
    {'nama': 'Admin 2', 'whatsapp': '081368685449'},
    {'nama': 'Admin 3', 'whatsapp': '082216219763'}],
  'alamat': '[Alamat studio]', 'jam_buka': '[Hari dan jam buka]', 'email': '[email]@sisterstudio.com', 'maps': '[Tautan Google Maps]',
  'dp_persen': 50, 'lama_sewa_hari': 3, 'jam_fitting': ['10.00', '11.30', '13.00', '14.30', '16.00', '19.00'],
  'jam_kirim_pengingat': '09.00', 'catatan': 'DP, lama sewa, dan jam fitting adalah nilai contoh dari desain; sesuaikan.',
  'contoh': False})

# ---------- agen ----------
for aid, nama, tugas in [
  ('admin', 'Admin Agen', ['Mengumpulkan dan mencatat aktivitas semua agen', 'Melaporkan ke owner', 'Reminder reservasi', 'Menerima perintah owner dan menjawab']),
  ('cs', 'Agen CS', ['Menjawab FAQ', 'Reminder reservasi', 'Membagikan S/K dan kontak sewa']),
  ('kreator', 'Agen Kreator', ['Tambah, edit, hapus katalog', 'Marketing media sosial']),
  ('kasir', 'Agen Kasir & Akuntan', ['Invoice dan pembayaran', 'Kas masuk dan keluar', 'Rekap keuangan dan analisa usaha']),
  ('stok', 'Agen Stok Inventaris', ['Menambah stok', 'Mencatat stok keluar dan kembali', 'Reminder pengembalian', 'Riwayat peminjaman', 'Kondisi dan perawatan'])]:
  put('agen', aid, {'nama': nama, 'tugas': tugas, 'status': 'Aktif', 'contoh': False})

# ---------- koleksi (data asli dari katalog) ----------
K = [
 ('008', 'Srikandi Kemuning', 250000, 'Perpaduan gaya Jawa yang anggun dengan sentuhan Melayu yang mewah, melambangkan kelembutan, ketegasan, dan keanggunan seorang wanita Nusantara.', {'S': (1,0,1,0), 'M': (2,2,0,0), 'L': (2,2,0,0), 'XL': (1,0,0,1)}),
 ('009', 'Fuchsia Glam', 300000, 'Kebaya modern bernuansa elegan dengan taburan payet yang berkilau, memancarkan pesona anggun dan glamor di setiap momen istimewa.', {'S': (1,0,0,1), 'M': (2,1,1,0), 'L': (2,1,1,0), 'XL': (1,0,1,0)}),
 ('010', 'Candrakirana Nusantara', 300000, 'Kebaya anggun bernuansa hijau lembut, terinspirasi dari kemilau cahaya rembulan (Candrakirana) yang memancarkan ketenangan, keanggunan, dan pesona wanita Nusantara.', {'S': (1,0,0,1), 'M': (2,1,1,0), 'L': (2,1,1,0), 'XL': (1,1,0,0)}),
 ('011', 'Mocha Elegance', 200000, 'Kebaya renda bernuansa mocha yang memancarkan kesan anggun, lembut, dan berkelas di setiap suasana istimewa.', {'S': (1,1,0,0), 'M': (2,1,0,1), 'L': (2,1,1,0), 'XL': (1,1,0,0)}),
]
slug = {'008': 'srikandi-kemuning', '009': 'fuchsia-glam', '010': 'candrakirana-nusantara', '011': 'mocha-elegance'}
for kode, nama, harga, desk, st in K:
  stok = {u: {'total': t, 'tersedia': a, 'disewa': d, 'perawatan': p} for u, (t, a, d, p) in st.items()}
  for u, s in stok.items(): assert s['total'] == s['tersedia'] + s['disewa'] + s['perawatan'], (kode, u)
  put('koleksi', kode, {'kode': f'Koleksi {kode}', 'nama': nama, 'kategori': 'Kebaya', 'harga': harga, 'satuan': 'stel',
    'deskripsi': desk, 'foto': f'design/assets/foto/koleksi-{kode}-{slug[kode]}.jpg', 'tampil': True,
    'stok': stok, 'stok_sumber': 'contoh', 'contoh': False})

# ---------- pelanggan (contoh) ----------
names = ['Nur', 'Rina', 'Sari', 'Ayu', 'Dewi', 'Maya', 'Nadia', 'Putri', 'Lestari', 'Fitri', 'Indah', 'Wulan', 'Yuni', 'Tika', 'Laras', 'Citra', 'Dinda']
for n in names:
  put('pelanggan', n.lower(), {'nama': n, 'email': '[email]', 'whatsapp': '[08xx]', 'login': 'Google', 'pengingat': ['WhatsApp', 'Email'], 'contoh': True})

# ---------- reservasi + invoice (contoh) ----------
# no, pelanggan, koleksi, ukuran, fitting, ambil, acara, kembali, total, dibayar, status_inv, status_res, terbit
R = [
 ('0031', 'lestari', '009', 'M', None, '2026-11-10', '2026-11-11', '2026-11-13', 300000, 300000, 'Lunas', 'Terlambat kembali', '2026-11-02'),
 ('0032', 'putri', '010', 'L', None, '2026-11-09', '2026-11-10', '2026-11-12', 300000, 300000, 'Lunas', 'Terlambat kembali', '2026-11-01'),
 ('0034', 'tika', '008', 'S', None, '2026-11-13', '2026-11-14', '2026-11-15', 250000, 250000, 'Lunas', 'Disewa', '2026-11-04'),
 ('0035', 'laras', '010', 'S', None, '2026-11-10', '2026-11-11', '2026-11-13', 300000, 300000, 'Lunas', 'Selesai', '2026-11-03'),
 ('0036', 'wulan', '011', 'M', None, '2026-11-11', '2026-11-12', '2026-11-14', 275000, 200000, 'Belum lunas', 'Selesai', '2026-11-05'),
 ('0037', 'sari', '009', 'M', '2026-11-15T10:00', '2026-11-20', '2026-11-21', '2026-11-22', 300000, 150000, 'DP diterima', 'Dipesan', '2026-11-08'),
 ('0038', 'ayu', '008', 'M', None, '2026-11-15T11:30', '2026-11-16', '2026-11-17', 250000, 250000, 'Lunas', 'Dipesan', '2026-11-06'),
 ('0039', 'rina', '010', 'M', None, '2026-11-12', '2026-11-14', '2026-11-15', 300000, 300000, 'Lunas', 'Disewa · minta perpanjangan', '2026-11-03'),
 ('0040', 'indah', '010', 'L', '2026-11-17T13:00', '2026-11-20', '2026-11-21', '2026-11-22', 300000, 0, 'Lewat tempo', 'Menunggu DP', '2026-11-10'),
 ('0041', 'fitri', '009', 'L', '2026-11-17T14:30', '2026-11-20', '2026-11-21', '2026-11-22', 300000, 0, 'Lewat tempo', 'Menunggu DP', '2026-11-10'),
 ('0042', 'nur', '008', 'M', '2026-11-21T10:00', '2026-12-04', '2026-12-05', '2026-12-06', 250000, 0, 'Menunggu DP', 'Menunggu DP', '2026-11-14'),
 ('0043', 'maya', '011', 'M', '2026-11-16T14:30', '2026-11-18', '2026-11-19', '2026-11-20', 200000, 0, 'Menunggu DP', 'Menunggu DP', '2026-11-14'),
 ('0044', 'nadia', '009', 'M', '2026-11-21T11:30', '2026-11-27', '2026-11-28', '2026-11-29', 300000, 150000, 'DP diterima', 'Dipesan', '2026-11-14'),
 ('0045', 'yuni', '009', 'L', None, '2026-11-14', '2026-11-15', '2026-11-17', 300000, 300000, 'Lunas', 'Disewa', '2026-11-07'),
 ('0046', 'dewi', '010', 'M', '2026-11-15T13:00', '2026-11-25', '2026-11-26', '2026-11-27', 300000, 150000, 'DP diterima', 'Dipesan', '2026-11-11'),
]
for no, p, k, u, fit, ambil, acara, kembali, total, bayar, sinv, sres, terbit in R:
  inv = f'INV-2026-11-{no}'
  put('reservasi', f'RSV-2026-11-{no}', {'pelanggan': p, 'koleksi': k, 'ukuran': u, 'fitting': fit, 'ambil': ambil, 'acara': acara,
    'kembali': kembali, 'status': sres, 'invoice': inv, 'contoh': True})
  item = [{'keterangan': f'Sewa {dict((x[0], x[1]) for x in K)[k]} ({u})', 'jumlah': 1, 'harga': dict((x[0], x[2]) for x in K)[k]}]
  if total > item[0]['harga']:
    item.append({'keterangan': 'Biaya perbaikan payet', 'jumlah': 1, 'harga': total - item[0]['harga']})
  put('invoice', inv, {'reservasi': f'RSV-2026-11-{no}', 'pelanggan': p, 'item': item, 'total': total, 'dp': total // 2,
    'dibayar': bayar, 'sisa': total - bayar, 'status': sinv, 'terbit': terbit, 'contoh': True})

# ---------- kas (contoh) ----------
for i, (w, ket, kat, masuk, keluar, inv) in enumerate([
  ('2026-11-13T10:05', 'Pelunasan · Tika · transfer bank', 'Pelunasan sewa', 125000, 0, 'INV-2026-11-0034'),
  ('2026-11-13T14:20', 'Pelunasan · Laras · tunai', 'Pelunasan sewa', 150000, 0, 'INV-2026-11-0035'),
  ('2026-11-13T17:20', 'Iklan Instagram koleksi wisuda (7 hari)', 'Iklan', 0, 150000, None),
  ('2026-11-14T09:15', 'DP · Sari · QRIS', 'DP sewa', 150000, 0, 'INV-2026-11-0037'),
  ('2026-11-14T10:50', 'DP · Nadia · transfer bank', 'DP sewa', 150000, 0, 'INV-2026-11-0044'),
  ('2026-11-14T11:45', 'Laundry 3 stel (Mocha Elegance, Candrakirana, Fuchsia Glam)', 'Laundry', 0, 120000, None),
  ('2026-11-14T12:40', 'Pelunasan · Ayu · QRIS', 'Pelunasan sewa', 125000, 0, 'INV-2026-11-0038')], start=1):
  put('kas', f'KAS-2026-11-{i:03d}', {'waktu': w, 'keterangan': ket, 'kategori': kat, 'masuk': masuk, 'keluar': keluar, 'invoice': inv, 'contoh': True})

# ---------- rekap (contoh) ----------
put('rekap', '2026-11', {'periode': '2026-11-01 s.d. 2026-11-14', 'kas_masuk': 6450000, 'kas_keluar': 1320000, 'saldo': 5130000,
  'piutang': 675000, 'keluar_per_kategori': {'Laundry': 540000, 'Iklan': 400000, 'Perbaikan': 230000, 'Operasional': 150000},
  'disewa_per_koleksi': {'010': 6, '009': 5, '008': 4, '011': 3},
  'analisa': ['Pendapatan tertinggi pada Agustus dan Oktober, bersamaan dengan musim wisuda.',
              'Laundry 8% dari pendapatan November.', 'Mocha Elegance paling jarang disewa.', '2 DP lewat tempo minggu ini.'],
  'contoh': True})
put('rekap', 'bulanan-2026', {'pendapatan': {'2026-06': 5200000, '2026-07': 7800000, '2026-08': 9100000, '2026-09': 6400000, '2026-10': 8700000, '2026-11': 6450000},
  'catatan': 'November sampai tanggal 14', 'contoh': True})

# ---------- pengingat (contoh) ----------
for i, (kirim, p, jenis, jadwal, kanal, status, ref) in enumerate([
  ('2026-11-14T09:00', 'sari', 'H-1 fitting', '2026-11-15T10:00', 'WhatsApp + email', 'Terkirim', 'RSV-2026-11-0037'),
  ('2026-11-14T09:00', 'ayu', 'H-1 pengambilan', '2026-11-15T11:30', 'WhatsApp', 'Terkirim', 'RSV-2026-11-0038'),
  ('2026-11-14T09:00', 'dewi', 'H-1 fitting', '2026-11-15T13:00', 'WhatsApp + email', 'Terkirim', 'RSV-2026-11-0046'),
  ('2026-11-14T09:00', 'lestari', 'Terlambat kembali', '2026-11-13', 'WhatsApp', 'Gagal · nomor tidak aktif', 'RSV-2026-11-0031'),
  ('2026-11-14T09:00', 'putri', 'Terlambat kembali', '2026-11-12', 'WhatsApp', 'Terkirim', 'RSV-2026-11-0032'),
  ('2026-11-14T13:20', 'nur', 'Reservasi dibuat', '2026-11-14T13:20', 'Email', 'Terkirim', 'RSV-2026-11-0042'),
  ('2026-11-14T15:00', 'maya', 'Batas bayar DP', '2026-11-14T23:59', 'WhatsApp', 'Terjadwal', 'RSV-2026-11-0043'),
  ('2026-11-15T09:00', 'rina', 'Hari pengembalian', '2026-11-16T09:00', 'WhatsApp', 'Terjadwal', 'RSV-2026-11-0039'),
  ('2026-11-15T09:00', 'maya', 'H-1 fitting', '2026-11-16T14:30', 'WhatsApp + email', 'Terjadwal', 'RSV-2026-11-0043'),
  ('2026-11-15T09:00', 'tika', 'Hari pengembalian', '2026-11-15', 'WhatsApp', 'Terjadwal', 'RSV-2026-11-0034'),
  ('2026-11-16T10:00', 'nur', 'Batas bayar DP', '2026-11-16T23:59', 'WhatsApp + email', 'Terjadwal', 'RSV-2026-11-0042'),
  ('2026-11-20T10:00', 'nur', 'H-1 fitting', '2026-11-21T10:00', 'WhatsApp + email', 'Terjadwal', 'RSV-2026-11-0042'),
  ('2026-12-03T10:00', 'nur', 'H-1 pengambilan', '2026-12-04', 'WhatsApp', 'Terjadwal', 'RSV-2026-11-0042'),
  ('2026-12-06T09:00', 'nur', 'Hari pengembalian', '2026-12-06', 'WhatsApp', 'Terjadwal', 'RSV-2026-11-0042')], start=1):
  put('pengingat', f'PNG-{i:03d}', {'kirim': kirim, 'pelanggan': p, 'jenis': jenis, 'jadwal': jadwal, 'kanal': kanal, 'status': status, 'reservasi': ref, 'contoh': True})

# ---------- gerak stok / riwayat peminjaman (contoh) ----------
for i, (w, gerak, k, u, p, cat) in enumerate([
  ('2026-10-30T10:00', 'Keluar', '008', 'XL', 'yuni', 'Kembali 1 Nov'),
  ('2026-11-01T16:00', 'Kembali', '008', 'XL', 'yuni', 'Kancing kedua longgar → perbaikan'),
  ('2026-11-06T10:00', 'Keluar', '008', 'M', 'laras', 'Kembali 8 Nov'),
  ('2026-11-08T15:00', 'Kembali', '008', 'M', 'laras', 'Kondisi baik → laundry'),
  ('2026-11-09T10:00', 'Keluar', '010', 'L', 'putri', 'Kembali Kam, 12 Nov · belum kembali'),
  ('2026-11-10T15:30', 'Keluar', '009', 'M', 'lestari', 'Kembali Jum, 13 Nov · belum kembali'),
  ('2026-11-10T11:00', 'Keluar', '010', 'S', 'laras', 'Kembali 13 Nov'),
  ('2026-11-11T10:00', 'Keluar', '011', 'M', 'wulan', 'Kembali 14 Nov'),
  ('2026-11-12T10:00', 'Keluar', '010', 'M', 'rina', 'Kembali Min, 15 Nov'),
  ('2026-11-13T14:20', 'Kembali', '010', 'S', 'laras', 'Kondisi baik → laundry'),
  ('2026-11-13T16:00', 'Keluar', '008', 'S', 'tika', 'Kembali Min, 15 Nov'),
  ('2026-11-14T10:10', 'Keluar', '009', 'L', 'yuni', 'Kembali Sel, 17 Nov'),
  ('2026-11-14T11:30', 'Kembali', '011', 'M', 'wulan', 'Payet lepas di lengan kiri → perbaikan')], start=1):
  put('gerak_stok', f'GRK-{i:03d}', {'waktu': w, 'gerak': gerak, 'koleksi': k, 'ukuran': u, 'pelanggan': p, 'catatan': cat, 'contoh': True})

# ---------- perawatan (contoh) ----------
for i, (k, u, jenis, cat, status, siap) in enumerate([
  ('011', 'M', 'Perbaikan', 'Payet lepas di lengan kiri · penjahit langganan · perkiraan Rp75.000', 'Menunggu persetujuan biaya', '2026-11-17'),
  ('010', 'S', 'Laundry', 'Cuci kering dan setrika uap', 'Proses', '2026-11-16'),
  ('009', 'S', 'Laundry', 'Cuci kering dan setrika uap', 'Proses', '2026-11-15'),
  ('008', 'XL', 'Laundry', 'Kancing kedua dijahit ulang, lalu laundry', 'Proses', '2026-11-18')], start=1):
  put('perawatan', f'RWT-{i:03d}', {'koleksi': k, 'ukuran': u, 'jenis': jenis, 'catatan': cat, 'status': status, 'siap': siap, 'contoh': True})

# ---------- FAQ (isi website; beberapa nilai placeholder) ----------
for i, (q, a, pakai) in enumerate([
  ('Apakah fitting dikenakan biaya?', 'Fitting di studio tidak dipungut biaya. Pesan jadwal lebih dulu agar ruang ganti siap untuk Anda.', 9),
  ('Berapa lama masa sewa?', 'Masa sewa standar [3] hari dari tanggal pengambilan. Perpanjangan bisa diajukan lewat CS sebelum tanggal kembali.', 18),
  ('Bagaimana jika ukurannya kurang pas?', 'Saat fitting tim kami membantu mencoba beberapa ukuran. Penyesuaian kecil tanpa mengubah jahitan bisa dibantu studio.', 12),
  ('Metode pembayaran apa saja?', 'Transfer bank, QRIS, atau tunai di studio. Bukti bayar dicatat otomatis di invoice Anda.', 14),
  ('Bagaimana saya tahu jadwal pengembalian?', 'Pengingat dikirim lewat WhatsApp dan email: H-1 fitting, H-1 pengambilan, dan pada hari pengembalian.', 18),
  ('Apakah kebaya bisa diantar?', '[Isi kebijakan antar-jemput dan biayanya.]', 6)], start=1):
  put('faq', f'FAQ-{i:02d}', {'pertanyaan': q, 'jawaban': a, 'dipakai_minggu_ini': pakai, 'tampil_di_website': True, 'contoh': False})

# ---------- dokumen ----------
put('dokumen', 'syarat-ketentuan', {'judul': 'Syarat & ketentuan sewa', 'versi': 3, 'diperbarui': '2026-11-02', 'status': 'Draf, isi nilai dalam kurung siku', 'butir': [
  'Lama sewa [3] hari, dihitung dari tanggal pengambilan.',
  'DP [50%] mengunci tanggal sewa. Pelunasan saat pengambilan kebaya.',
  'Jaminan: [kartu identitas asli / deposit Rp…], dikembalikan setelah kebaya kembali dalam kondisi baik.',
  'Keterlambatan pengembalian dikenakan denda [Rp…] per hari.',
  'Noda permanen, sobek, atau payet lepas dikenakan biaya perbaikan sesuai penilaian studio. Kebaya hilang diganti [nilai penggantian].',
  'Pembatalan kurang dari [H-7]: DP tidak dikembalikan, tetapi dapat dialihkan ke tanggal lain [1 kali].',
  'Kebaya tidak boleh dipotong, dijahit, atau diubah tanpa izin.',
  'Tidak perlu dicuci sendiri; laundry dan perawatan ditangani studio.'], 'contoh': False})
put('dokumen', 'kontak-sewa', {'judul': 'Kontak sewa', 'isi': 'Admin 1 0812 7111 6292 · Admin 2 0813 6868 5449 · Admin 3 0822 1621 9763 · Instagram @sisterstudio.plg · sisterstudio.com', 'contoh': False})
put('dokumen', 'lokasi-jam-buka', {'judul': 'Lokasi dan jam buka studio', 'isi': '[Alamat studio] · [Hari dan jam buka] · [Tautan Google Maps]', 'contoh': False})

# ---------- konten medsos (contoh) ----------
for i, (w, judul, kanal, status, koleksi) in enumerate([
  ('2026-11-15T19:00', 'Koleksi 009 · Fuchsia Glam', ['Instagram feed', 'Instagram story', 'Status WhatsApp'], 'Terjadwal', '009'),
  ('2026-11-17T12:00', 'Tips: merawat kebaya setelah dipakai', ['Instagram story'], 'Draf', None),
  ('2026-11-19T19:00', 'Cerita pelanggan: hari wisuda', ['Instagram feed'], 'Menunggu foto', None),
  ('2026-11-21T10:00', 'Di balik layar: fitting di studio', ['TikTok'], 'Draf', None)], start=1):
  d = {'tayang': w, 'judul': judul, 'kanal': kanal, 'status': status, 'koleksi': koleksi, 'contoh': True}
  if i == 1:
    d['caption'] = ('Koleksi 009 · Fuchsia Glam\nKebaya modern dengan taburan payet yang berkilau, untuk Anda yang ingin tampil anggun sekaligus glamor di hari istimewa.\n\n'
                    'Sewa Rp300.000 / stel. Pesan jadwal fitting lewat tautan di bio atau WhatsApp Admin 1 0812 7111 6292.\n\n#sewakebaya #kebayamodern #kebayawisuda #sisterstudio')
  put('konten', f'KTN-{i:03d}', d)
put('konten', 'ide', {'judul': 'Ide konten dari agen', 'ide': [
  'Seri “Kebaya untuk wisuda Desember”: 3 posting mulai akhir November.',
  'Mocha Elegance belum diposting 30 hari. Tampilkan untuk momen lamaran.',
  'Minta izin pelanggan yang sudah mengembalikan kebaya untuk berbagi foto hari istimewanya.'], 'contoh': True})

# ---------- aktivitas agen (satu dokumen per hari) ----------
put('aktivitas', '2026-11-14', {'tanggal': '2026-11-14', 'entri': [
  {'waktu': '08.00', 'agen': 'admin', 'teks': 'Mengirim laporan pagi ke WhatsApp owner.'},
  {'waktu': '08.30', 'agen': 'kasir', 'teks': 'Rekap Jum, 13 Nov: kas masuk Rp1.150.000, kas keluar Rp180.000.'},
  {'waktu': '09.00', 'agen': 'stok', 'teks': 'Mengirim pengingat pengembalian kedua ke 2 pelanggan yang terlambat.'},
  {'waktu': '09.40', 'agen': 'kreator', 'teks': 'Menyusun caption dan menjadwalkan posting Koleksi 009 Fuchsia Glam untuk Min, 15 Nov 19.00.'},
  {'waktu': '10.05', 'agen': 'cs', 'teks': 'Mengirim pengingat H-1 fitting ke 3 pelanggan lewat WhatsApp dan email.'},
  {'waktu': '11.30', 'agen': 'stok', 'teks': 'Mocha Elegance (M) kembali dari Wulan. Kondisi: payet lepas di lengan kiri. Masuk antrean perbaikan.'},
  {'waktu': '12.15', 'agen': 'cs', 'teks': 'Meneruskan permintaan perpanjangan sewa dari Rina (Candrakirana Nusantara, M) ke admin.'},
  {'waktu': '12.40', 'agen': 'kasir', 'teks': 'Mencatat pelunasan INV-2026-11-0038 sebesar Rp125.000 lewat QRIS. Status invoice: Lunas.'}],
  'contoh': True})

# ---------- keputusan owner (contoh) ----------
for i, (agen, teks, ref) in enumerate([
  ('cs', 'Rina minta perpanjangan sewa Candrakirana Nusantara (M) 1 hari, sampai Sen, 16 Nov.', 'RSV-2026-11-0039'),
  ('stok', 'Mocha Elegance (M) perlu perbaikan payet di lengan kiri. Perkiraan biaya penjahit Rp75.000.', 'RWT-001'),
  ('kasir', 'INV-2026-11-0040 dan INV-2026-11-0041 lewat batas bayar DP.', 'INV-2026-11-0040')], start=1):
  put('keputusan', f'KPT-{i:03d}', {'agen': agen, 'teks': teks, 'rujukan': ref, 'status': 'Menunggu', 'dibuat': '2026-11-14', 'contoh': True})

# ---------- write ----------
counts = {}
for (col, did), data in docs.items():
  p = out / col / f'{did}.json'
  p.parent.mkdir(parents=True, exist_ok=True)
  p.write_text(json.dumps(data, ensure_ascii=False, indent=2))
  counts[col] = counts.get(col, 0) + 1
(out / '_index.json').write_text(json.dumps([{'collection': c, 'doc_id': d} for (c, d) in docs], ensure_ascii=False))
print(counts, 'total', len(docs))
tot = {'tersedia': 0, 'disewa': 0, 'perawatan': 0}
for (c, d), v in docs.items():
  if c == 'koleksi':
    per = {k: sum(x[k] for x in v['stok'].values()) for k in tot}
    print(d, per)
    for k in tot: tot[k] += per[k]
print('stok total', tot)
