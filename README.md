# Temassız Ses Kontrol Sistemi (Computer Vision)

Bu proje, bilgisayar kamerasından alınan görüntüleri işleyerek, el ve parmak hareketleriyle cihazın ses seviyesini temassız bir şekilde kontrol etmeyi sağlayan bir görüntü işleme uygulamasıdır. Geleneksel klavye/fare donanımlarına ihtiyaç duymadan, fiziksel mesafeyi dijital komutlara dönüştüren bir arayüz sunar.

## Projenin Amacı ve Çalışma Mantığı
Kamera üzerinden el iskelet haritası çıkarılır ve başparmak ile işaret parmağı arasındaki hipotenüs hesaplanır. Bu mesafe, matematiksel oran-orantı (`numpy.interp`) işlemleriyle 0-100 arasına çekilerek işletim sisteminin ses yüzdesine eşitlenir.

Ekranda anlık geri bildirim sağlamak amacıyla, ses seviyesi dinamik bir bar ve yüzdelik metin ile kullanıcıya gösterilmektedir.

##  Kullanılan Teknolojiler
* **Python 3**
* **OpenCV:** Görüntü okuma, işleme ve ekrana dinamik arayüz (dikdörtgen, metin, çizgi) çizdirme.
* **MediaPipe:** Gerçek zamanlı el ve eklem noktası (landmark) tespiti.
* **NumPy:** Piksel mesafesinin ses yüzdesine interpolasyonu (oranlanması).
* **OS / Math:** İşletim sistemine (macOS) donanım komutu gönderme ve koordinat hesabı.

##  Kurulum ve Çalıştırma

**1. Gerekli Kütüphaneleri Yükleyin:**
```bash
pip install -r requirements.txt