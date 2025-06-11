# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan institusi pendidikan tinggi yang telah beroperasi sejak tahun 2000. Dengan pengalaman lebih dari dua dekade, institusi ini telah berhasil mencetak banyak lulusan yang memiliki reputasi baik di dunia kerja maupun akademik. Keberhasilan ini mencerminkan kualitas kurikulum, pengajar, dan sistem pembelajaran yang diterapkan oleh institusi.

Namun, di balik keberhasilan tersebut, terdapat tantangan signifikan yang dihadapi: tingginya angka mahasiswa yang tidak menyelesaikan pendidikannya atau dropout. Fenomena ini menimbulkan kekhawatiran dari sisi reputasi institusi, efisiensi operasional, serta potensi kerugian finansial. Tingginya angka dropout bisa disebabkan oleh berbagai faktor seperti ketidakcocokan program studi, tekanan akademik, kendala finansial, atau kurangnya dukungan akademik dan psikologis.

Dari perspektif bisnis, isu ini penting untuk segera ditangani karena dapat berdampak langsung pada:
1. Citra Institusi: Dropout yang tinggi dapat menurunkan kepercayaan publik dan calon mahasiswa terhadap kualitas pendidikan di Jaya Jaya Institut.
2. Pendapatan dan Keuangan: Mahasiswa yang berhenti kuliah di tengah jalan akan mempengaruhi arus kas dan perencanaan keuangan institusi.
3. Daya Saing: Di tengah persaingan antar institusi pendidikan, angka kelulusan yang rendah bisa menjadi faktor negatif dalam menarik mahasiswa baru.

Oleh karena itu, Jaya Jaya Institut perlu melakukan evaluasi menyeluruh terhadap faktor-faktor penyebab dropout serta merancang strategi untuk meningkatkan retensi mahasiswa demi keberlanjutan bisnis pendidikan yang mereka jalankan.

### Permasalahan Bisnis
1. Tingginya Angka Dropout Mahasiswa
Jumlah siswa yang tidak menyelesaikan pendidikannya (dropout) tergolong tinggi. Hal ini menjadi masalah serius bagi reputasi, kepercayaan publik, serta keberlangsungan operasional institusi.

2. Minimnya Deteksi Dini terhadap Potensi Dropout
Saat ini, Jaya Jaya Institut belum memiliki sistem atau metode yang efektif untuk mendeteksi siswa yang berisiko tinggi mengalami dropout secara dini. Akibatnya, tindakan pencegahan sulit dilakukan.

3. Kurangnya Intervensi Spesifik bagi Siswa Berisiko
Karena tidak adanya deteksi awal, institusi belum bisa memberikan bimbingan khusus atau intervensi yang tepat sasaran kepada siswa yang membutuhkan dukungan lebih.

4. Penurunan Citra dan Daya Saing Institusi
Tingginya angka dropout dapat menurunkan kepercayaan masyarakat terhadap kualitas pendidikan yang ditawarkan, yang pada akhirnya mempengaruhi minat calon mahasiswa baru.

5. Dampak Finansial bagi Institusi
Setiap siswa yang dropout berpotensi menyebabkan kerugian finansial, baik dari sisi biaya operasional yang sudah dikeluarkan maupun kehilangan potensi pendapatan dari sisa masa studi.

6. Kurangnya Pemanfaatan Data Historis Mahasiswa untuk Pengambilan Keputusan
Data akademik dan non-akademik siswa belum dimanfaatkan secara optimal untuk menganalisis pola dropout atau mendukung pengambilan keputusan berbasis data.

### Cakupan Proyek
1. Data yang digunakan merupakan data mahasiswa
2. Pengembangan Model Prediksi Dropout dengan algoritma
3. Implementasi Dashboard Deteksi Dini Dropout
4. Rekomendasi Tindakan Intervensi

### Persiapan

Sumber data: (https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment:
===Jupyter Notebook==

1. Install requirments.txt ( pip3 install -r requirements.txt)
2. Run all

==Streamlit==
1. Install requirments.txt (pip3 install -r requirements.txt)
2. jalankan streamlit run app.py  

## Business Dashboard
Dasbor "Academic Performance & Retention Insights" ini adalah alat analisis untuk melacak kinerja dan status kelulusan dari 4424 mahasiswa.

Tujuan utamanya adalah untuk mengidentifikasi penyebab mahasiswa gagal dalam studi. Wawasan utamanya adalah:
1. Tingkat Dropout (DO) sangat tinggi, yaitu 32.12%, yang menjadi masalah utama.
2. Mahasiswa yang paling berisiko DO adalah mereka yang memiliki nilai sangat rendah di semester awal (Cluster "At Risk").
3. Terdapat korelasi kuat antara masalah finansial dengan kecenderungan mahasiswa untuk DO.

Secara singkat, dasbor ini membantu manajemen untuk secara proaktif menemukan mahasiswa bermasalah—baik secara akademik maupun finansial—agar dapat memberikan dukungan yang tepat sasaran untuk mengurangi angka DO.

Link Dashboard: https://public.tableau.com/app/profile/limitmax/viz/StudentAcademicDashboard/Dashboard1

## Menjalankan Sistem Machine Learning
==Local==
1. Clone repor berikut: https://github.com/LimitMax/predict-student-graduate.git
2. Install requirments.txt (pip3 install -r requirements.txt)
3. jalankan streamlit run app.py 
4. Pilih menu prediction
5. Isi data yang diperlukan
6. Lakukan prediksi & lihat hasilnya

==Online==
1. Masuk link: https://predictstudent.streamlit.app/
2. Pilih menu prediction
3. Isi data yang diperlukan
4. Lakukan prediksi & lihat hasilnya

## Conclusion
Proyek ini bertujuan untuk membangun sebuah model dan dashboard untuk memantau performa mahasiswa guna mencegah tingginya angka mahasiswa yang dropout. Hasilnya, proyek berhasil menghasilkan model prediktif yang mampu mengidentifikasi status kelulusan mahasiswa berdasarkan data historis, serta menyediakan dashboard interaktif yang memberikan wawasan terkait kinerja akademik mahasiswa.

Dengan demikian, proyek berhasil mencapai tujuannya dalam membantu pihak institusi pendidikan untuk melakukan deteksi dini terhadap mahasiswa yang berisiko tidak lulus, sehingga dapat dilakukan intervensi lebih cepat dan tepat. Ke depannya, model ini dapat terus dikembangkan dengan data yang lebih luas dan diperbarui secara berkala agar hasil prediksi semakin akurat dan relevan.

### Rekomendasi Action Items
Berikut beberapa rekomendasi action guna menyelesaikan permasalahan yang dihadapi perusahaan/company edutech:
- Terapkan program bimbingan akademik, tutoring tambahan, dan sistem monitoring performa sejak awal semester.
- Perluas Program Beasiswa untuk Mahasiswa
- Evaluasi dan Tingkatkan Kualitas Pengajaran Semester Awal, dikarenakan Rata-rata nilai semester 2 menurun dibandingkan semester 1
- Mayoritas orang tua berasal dari latar belakang pekerjaan yang mungkin kurang familiar dengan peran pendukung pendidikan,Buat program edukasi orang tua dan libatkan mereka melalui forum komunikasi berkala.
