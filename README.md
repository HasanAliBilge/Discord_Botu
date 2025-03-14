# Task Manager Bot

Discord sunucunuz için görev yönetim botu.

## Sistem Gereksinimleri
- Python 3.8 veya daha yüksek
- pip (Python paket yöneticisi)

## Kurulum
1. Python'u yükleyin (3.8 veya üstü): https://www.python.org/downloads/
2. Virtual environment oluşturun:
   ```bash
   python -m venv venv
   ```
3. Virtual environment'ı aktif edin:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/MacOS:
     ```bash
     source venv/bin/activate
     ```
4. Gerekli paketleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

## Kullanım
1. **Bot Token'ınızı Ayarlayın** Discord botunuzu oluşturduktan sonra, botunuzu Discord Developer Portal üzerinden oluşturun ve **bot token'ınızı alın**.
   ```
2. **Botu Başlatın:** Botu başlatmak için terminal üzerinden aşağıdaki komutu çalıştırın:
   ```bash
   python bot.py
   ```
3. **Bot Discord Sunucunuza Davet Edin:** Botunuzu Discord sunucunuza davet etmek için, aşağıdaki URL'yi kullanarak davet bağlantısı oluşturun:
   ```
   https://discord.com/oauth2/authorize?client_id=YOUR_BOT_CLIENT_ID&scope=bot&permissions=PERMISSION_LEVEL
   ```
   Burada `YOUR_BOT_CLIENT_ID` yerine botunuzun **client ID**'sini ve `PERMISSION_LEVEL` yerine botun alacağı izinleri belirleyin. Botun her zaman sunuculara ve mesajlara erişebilmesi için gerekli izinleri verdiğinizden emin olun.

## Bot Komutları
Aşağıda, botun sağlayacağı bazı komutlar ve açıklamaları verilmiştir:
1. `!task add [task_name]` Yeni bir görev ekler. Görev ismini vererek ekleyebilirsiniz.
2. `!task list` O anki tüm görevleri listeler.
3. `!task complete [task_id]` Verilen görev ID'sine sahip görevi tamamlar.
4. `!task delete [task_id]` Verilen görev ID'sine sahip görevi siler.
5. `!task help` Komutların listesini ve açıklamalarını gösterir.

## Örnek Kullanım
* **Görev Ekleme:**
  ```
  !task add Yapılacaklar listesi oluştur
  ```
* **Görevleri Görüntüleme:**
  ```
  !task list
  ```
* **Görevi Tamamlama:**
  ```
  !task complete 1
  ```
* **Görev Silme:**
  ```
  !task delete 1
  ```

## İzinler
Botun düzgün çalışabilmesi için aşağıdaki izinlere sahip olması gerekir:
* **Mesajları okuma ve yazma**
* **Mesajları yönetme** (görevleri düzenlemek ve silmek için)
* **Kullanıcı adı ve avatarını okuma** (botun kullanıcı bilgilerini alması gerekebilir)

## Sorun Giderme
1. **Bot Başlatılmıyor:**
   * Bot token'ınızın doğru olduğundan emin olun.
   * Python 3.8 veya daha yüksek bir sürüm kullanıldığından emin olun.
2. **Komutlar Çalışmıyor:**
   * Gerekli tüm paketlerin yüklü olduğundan emin olun (`pip install -r requirements.txt` komutunu tekrar çalıştırın).
   * Kodun doğru şekilde yapılandırıldığını kontrol edin.
3. **Bot Davet Edilemiyor:**
   * Botun doğru izinlere sahip olduğundan emin olun ve doğru OAuth2 URL'sini kullanarak botu davet edin.
