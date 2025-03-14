Task Manager Bot
Discord sunucunuz için görev yönetim botu.
Sistem Gereksinimleri

Python 3.8 veya daha yüksek
pip (Python paket yöneticisi)

Kurulum

Python'u yükleyin (3.8 veya üstü): https://www.python.org/downloads/
Virtual environment oluşturun:
bashCopypython -m venv venv

Virtual environment'ı aktif edin:

Windows:
bashCopyvenv\Scripts\activate

Linux/MacOS:
bashCopysource venv/bin/activate



Gerekli paketleri yükleyin:
bashCopypip install -r requirements.txt


Kullanım

Bot Token'ınızı Ayarlayın Discord botunuzu oluşturduktan sonra, botunuzu Discord Developer Portal üzerinden oluşturun ve bot token'ınızı alın.
Bot Token'ınızı Yapılandırma: config.json dosyasını oluşturun ve aşağıdaki gibi bot token'ınızı buraya ekleyin:
jsonCopy{ "token": "YOUR_DISCORD_BOT_TOKEN" }

Botu Başlatın: Botu başlatmak için terminal üzerinden aşağıdaki komutu çalıştırın:
bashCopypython bot.py

Bot Discord Sunucunuza Davet Edin: Botunuzu Discord sunucunuza davet etmek için, aşağıdaki URL'yi kullanarak davet bağlantısı oluşturun:
Copyhttps://discord.com/oauth2/authorize?client_id=YOUR_BOT_CLIENT_ID&scope=bot&permissions=PERMISSION_LEVEL
Burada YOUR_BOT_CLIENT_ID yerine botunuzun client ID'sini ve PERMISSION_LEVEL yerine botun alacağı izinleri belirleyin. Botun her zaman sunuculara ve mesajlara erişebilmesi için gerekli izinleri verdiğinizden emin olun.

Bot Komutları
Aşağıda, botun sağlayacağı bazı komutlar ve açıklamaları verilmiştir:

!task add [task_name] Yeni bir görev ekler. Görev ismini vererek ekleyebilirsiniz.
!task list O anki tüm görevleri listeler.
!task complete [task_id] Verilen görev ID'sine sahip görevi tamamlar.
!task delete [task_id] Verilen görev ID'sine sahip görevi siler.
!task help Komutların listesini ve açıklamalarını gösterir.

Örnek Kullanım

Görev Ekleme:
Copy!task add Yapılacaklar listesi oluştur

Görevleri Görüntüleme:
Copy!task list

Görevi Tamamlama:
Copy!task complete 1

Görev Silme:
Copy!task delete 1


İzinler
Botun düzgün çalışabilmesi için aşağıdaki izinlere sahip olması gerekir:

Mesajları okuma ve yazma
Mesajları yönetme (görevleri düzenlemek ve silmek için)
Kullanıcı adı ve avatarını okuma (botun kullanıcı bilgilerini alması gerekebilir)

Sorun Giderme

Bot Başlatılmıyor:

Bot token'ınızın doğru olduğundan emin olun.
Python 3.8 veya daha yüksek bir sürüm kullanıldığından emin olun.


Komutlar Çalışmıyor:

Gerekli tüm paketlerin yüklü olduğundan emin olun (pip install -r requirements.txt komutunu tekrar çalıştırın).
Kodun doğru şekilde yapılandırıldığını kontrol edin.


Bot Davet Edilemiyor:

Botun doğru izinlere sahip olduğundan emin olun ve doğru OAuth2 URL'sini kullanarak botu davet edin.



Katkıda Bulunma
Eğer bu projeyi geliştirmek veya katkıda bulunmak isterseniz, lütfen aşağıdaki adımları takip edin:

Repo'yu kendi hesabınıza fork edin.
Yeni bir branch oluşturun (git checkout -b feature-name).
Yaptığınız değişiklikleri commit edin (git commit -am 'Add new feature').
Değişiklikleri push edin (git push origin feature-name).
Bir pull request oluşturun.
