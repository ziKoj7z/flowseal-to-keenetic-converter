***Автоматический скрипт, позволяющий конвертировать стратегии [Flowseal'a](https://github.com/Flowseal/zapret-discord-youtube) под [Keenetic](https://github.com/nfqws/nfqws-keenetic)***

---
# Использование

1. Подготовить необходимые файлы из [репозитория](https://github.com/Flowseal/zapret-discord-youtube) в роутер:
	Бинарные файлы `.bin` отправить по пути `/opt/etc/nfqws/fake/`;
	Листы отправить по пути `/opt/etc/nfqws/`, заранее изменив расширение файлов с `.txt` на `.list`.
	
2. Запустить файл `converter flowseal-keenetic.py`;

3. Перенести `.bat` файл со стратегией в консоль;

4. Готовый текстовый файл будет сохранён в папке с исходным файлом с постфиксом `_edited`. 
