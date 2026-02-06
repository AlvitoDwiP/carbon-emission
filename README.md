# Carbon Emission — ASEAN (2000–2024)

Repository ini berisi pipeline analisis emisi CO₂ negara ASEAN periode 2000–2024, dari pengambilan data hingga eksplorasi tren, ranking perubahan, dan decomposition sumber emisi.

## Struktur Proyek

- notebooks/01_data_loading.ipynb  
  Mengambil data Our World in Data (OWID), memfilter negara ASEAN dan periode 2000–2024, lalu menyimpan dataset processed ke data/process.

- notebooks/02_data_quality_check.ipynb  
  Pemeriksaan kualitas data: konsistensi skema, missing values, duplikasi country-year, dan cakupan tahun per negara. Notebook ini juga mendefinisikan kolom inti untuk analisis.

- notebooks/03_EDA.ipynb  
  EDA dan analisis ringkas: grouping 4-tahunan, visualisasi tren total dan per kapita, ringkasan statistik, korelasi (pooled dan within-country), ranking perubahan antar periode, dan decomposition perubahan berdasarkan sumber emisi.

- data/process/owid_co2_asean_2000_2024.csv  
  Dataset hasil filter ASEAN 2000–2024 yang dipakai sebagai input untuk Notebook 02 dan 03.

## Alur Kerja

1. Jalankan notebooks/01_data_loading.ipynb untuk menghasilkan data/process/owid_co2_asean_2000_2024.csv
2. Jalankan notebooks/02_data_quality_check.ipynb untuk memeriksa kualitas dan coverage data
3. Jalankan notebooks/03_EDA.ipynb untuk eksplorasi tren, ranking, dan decomposition

## Catatan Analisis

- Tren divisualisasikan menggunakan grouping 4-tahunan untuk mengurangi fluktuasi tahunan.
- Agregasi 4-tahunan menggunakan rata-rata, sehingga angka yang ditampilkan adalah average annual pada periode tersebut, bukan total emisi 4 tahun.
- Untuk perbandingan start vs end period, hanya grup 4-tahunan yang lengkap yang dipakai. Periode parsial seperti 2024 tunggal tidak digunakan untuk ranking dan decomposition.
- Decomposition sumber emisi hanya mencakup komponen yang tersedia di dataset. Total emisi dapat memiliki gap terhadap jumlah komponen, sehingga decomposition tidak merepresentasikan akuntansi penuh total emisi.

## Requirement

- Python 3.9+ (disarankan)
- pandas
- numpy
- matplotlib
- seaborn
- scipy
