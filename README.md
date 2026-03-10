<!-- ==================== BANNER ==================== -->
<p align="center">
  <img src="/img/awal.png" alt="Sneijderlino Banner" width="100%" style="border-radius:12px; box-shadow:0 0 25px #961808;">
</p
<h1 align="center">🚀 Ghost-QR Generator</h1>
<h3 align="center">Security Tool Developer</h3>

<!-- 🔥 Typing Intro -->
<p align="center">
  <a href="https://github.com/Sneijderlino">
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&pause=1000&color=00F7FF&center=true&vCenter=true&width=700&lines=Ghost-QR+%7C+QR+Code+Payload+Generator;Cyber+Security+Tool+%7C+Pentesting;Designed+for+Learning+and+Demo;Hack+the+Planet+%F0%9F%94%AA" />
  </a>
</p>

<!-- 🌊 Wave Animation -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=00f7ff&height=120&section=header&reversal=true&animation=fadeIn" width="100%"/>

## 👨‍💻 About Me

Saya adalah developer tool keamanan siber yang fokus pada offensive security, riset celah, dan otomatisasi yang aman. Ghost-QR Generator hanyalah salah satu proyek yang dibuat untuk edukasi, pentesting, dan demonstrasi teknik social engineering.

- 🔐 Offensive Security & Red Team
- 🛠️ Pengembangan Security Tool
- 🎯 Pembelajaran & Berbagi Ilmu

## 🌐 Connect with Me

<p align="center">
  <a href="https://www.linkedin.com/in/sneijderlino"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="https://github.com/Sneijderlino"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/></a>
  <a href="mailto:sneijderlino@example.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
</p>

## 🧰 Tech Arsenal

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,linux,git,cloudflare&theme=dark" />
</p>

<p align="center">
  <a href="https://github.com/Sneijderlino/Ghost-QR-Generator/stargazers">
   
  <a href="https://github.com/Sneijderlino/Ghost-QR-Generator/network/members">
    <img src="https://img.shields.io/github/forks/Sneijderlino/Ghost-QR-Generator?style=social" alt="Forks" />
  </a>
  <img src="https://img.shields.io/github/issues/Sneijderlino/Ghost-QR-Generator" alt="Issues" />
  <img src="https://img.shields.io/github/license/Sneijderlino/Ghost-QR-Generator" alt="License" />
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=Sneijderlino&show_icons=true&theme=radical" alt="GitHub Stats" />
  <img src="https://github-readme-activity-graph.cyclic.app/graph?username=Sneijderlino&theme=react-dark" alt="Activity Graph" />
</p>

---

## 📌 Daftar Isi

1. [Deskripsi Project](#deskripsi-project)
2. [Fitur Utama](#fitur-utama-tool)
3. [Preview Tool](#preview-tool)
4. [Struktur Folder](#struktur-folder-project)
5. [Cara Instalasi](#cara-instalasi)
   - [Windows](#windows)
   - [Kali Linux](#kali-linux)
   - [Termux](#termux)
6. [Cara Menjalankan Program](#cara-menjalankan-program)
7. [Dependencies](#dependencies)
8. [Contoh Penggunaan](#contoh-penggunaan)
9. [Warning / Disclaimer](#warning--disclaimer)
10. [Kontribusi](#kontribusi)
11. [Lisensi](#lisensi)
12. [Kontak Developer](#kontak-developer)

---

## 🔍 Deskripsi Project

Ghost-QR Generator adalah sebuah alat berbahaya (security tool) yang dirancang untuk menciptakan QR Code dengan berbagai mode: standar, poster, dan injeksi ke template kustom. Dibangun untuk keperluan pentesting atau demonstrasi keamanan, tool ini menyajikan antarmuka bergaya terminal hacker dengan efek-efek "cyber" dan animasi.

> Tema warna dominan: **hitam**, **merah**, dengan efek terminal/hacker.

## ⚙️ Fitur Utama Tool

- Generate QR Code standar sebagai file PNG.
- Buat poster profesional dalam format HTML dengan desain ala Google Security.
- Inject QR Code langsung ke file template apapun (`*.html`).
- Fungsi live update (Ghost-Eye) untuk sinkronisasi template tertentu.
- Animasi teks, banner ASCII, dan loading cyber.

## 🖥️ Preview Tool

<p align="center">
  <img src="/img/view.png" alt="Sneijderlino Banner" width="100%" style="border-radius:12px; box-shadow:0 0 25px #961808;">
</p

---

## 📁 Struktur Folder Project

```
Ghost-QR.py
requirements.txt
README.md
LICENSE
.gitignore
img/
  ├─ sampel.png
  ├─ view.png
  └─ awal.png
```

---

## 🚀 Cara Instalasi

### 🔹 Windows

1. Pastikan Python terinstall (≥3.8). Unduh dari [python.org](https://www.python.org/downloads/).
2. Clone repository:
   ```bash
   git clone https://github.com/Sneijderlino/Ghost-QR-Generator.git
   cd Ghost-QR-Generator
   ```
3. Install dependency:
   ```bash
   pip install -r requirements.txt
   ```
4. Jalankan program:
   ```bash
   python Ghost-QR.py
   ```

### 🔹 Kali Linux

```bash
git clone https://github.com/Sneijderlino/Ghost-QR-Generator.git
cd Ghost-QR-Generator
sudo apt update && sudo apt install python3 python3-pip -y
pip3 install -r requirements.txt
python3 Ghost-QR.py
```

### 🔹 Termux

```bash
pkg update && pkg upgrade -y
pkg install git python -y
git clone https://github.com/Sneijderlino/Ghost-QR-Generator.git
cd Ghost-QR-Generator
pip install -r requirements.txt
python Ghost-QR.py
```

---

## ▶️ Cara Menjalankan Program

```bash
python Ghost-QR.py
```

Ikuti instruksi interaktif pada terminal untuk memilih mode QR, memasukkan URL, atau melakukan injeksi.

---

## 📦 Dependencies

- `qrcode` – pembuatan QR code
- `colorama` – pewarnaan teks terminal
- Python standar (`os`, `sys`, `time`, `base64`)

> Semua dependency tercantum di `requirements.txt`.

---

## 💻 Contoh Penggunaan

1. Pilih opsi `01` untuk generate QR biasa, masukkan URL target.
2. Lihat file `GHOST_QR_*.png` dibuat di folder yang sama.
3. Pilih opsi `02` untuk membuat poster HTML.
4. Pilih opsi `03` untuk inject ke template HTML.

---

## ⚠️ Warning / Disclaimer

Tool ini dibuat untuk **tujuan edukasi dan penetration testing**. Penyalahgunaan untuk kegiatan ilegal merupakan tanggung jawab pengguna. Penulis tidak bertanggung jawab atas tindakan tidak sah.

---

## 🤝 Kontribusi

Pull request, issue, dan saran welcome! Pastikan perubahan sesuai dengan gaya dan tujuan project. Fork terlebih dahulu, buat branch fitur, lalu kirim PR.

---

## 📜 Lisensi

Ghost-QR Generator dilisensikan di bawah **MIT License**. Lihat file `LICENSE` untuk rincian.

---

## 📫 Kontak Developer

- GitHub: [@Sneijderlino](https://github.com/Sneijderlino)
- Email: developer@example.com

---

_Terima kasih telah mengunjungi Ghost-QR Generator._

<!-- 🌊 Footer Wave -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=00f7ff&height=120&section=footer&reversal=true&animation=fadeIn" width="100%"/>

<h3 align="center">⚡ Ethical Research · Secure Systems · Continuous Growth ⚡</h3>
# Ghost-QR-Generator
