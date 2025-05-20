# 🪨📄✂️ Gelişmiş Taş Kağıt Makas - Python Oyunu

Bu Python projesi, klasik **Taş-Kağıt-Makas** oyununa bazı eğlenceli özellikler eklenerek geliştirilmiştir. Kullanıcı, bilgisayara karşı rastgele seçimlerle yarışırken aynı zamanda puanları görüntüleyebilir, hile komutu kullanabilir ve oyunu sıfırlayabilir.

## 🚀 Özellikler

- Terminal tabanlı oynanış
- Dinamik puan sistemi
- Gizli komutlar:
  - `setpoints`: Hileyle puan ekleme
  - `puan_durumu`: Anlık puan tablosunu gösterir
  - `help`: Komut listesini gösterir
- Oyun sonunda tekrar oynama veya çıkış seçeneği

## 🧠 Oyun Kuralları

- **Taş**, makası yener.
- **Makas**, kağıdı yener.
- **Kağıt**, taşı yener.
- Beraberlik durumunda iki taraf da 1 puan alır.
- Kazanırsanız 3 puan, kaybederseniz rakip 3 puan alır.

## 📦 Gereksinimler

Bu oyunun çalışabilmesi için bilgisayarınızda **Python** kurulu olmalıdır.

Kullanılan `random` modülü, Python ile birlikte gelen **standart bir kütüphanedir**, bu nedenle ayrıca `pip install` komutuyla yüklemenize gerek yoktur.


## ▶️ Oyunu Başlat

```bash
python taş-kağıt-makas.py
