### While we don't have a [shuffle play](https://github.com/telegramdesktop/tdesktop/pull/7700) feature in [Telegram desktop client](https://github.com/telegramdesktop/tdesktop), this kludge solves this problem.
### Пока в [десктопном клиенте Telegram](https://github.com/telegramdesktop/tdesktop) нет функции [перемешивания треков](https://github.com/telegramdesktop/tdesktop/pull/7700), этот костыль решает эту проблему.

The script gets music from your private channel and randomly forwards it to another private channel.

Этот скрипт берёт музыку из вашего частного канала и в случайном порядке пересылает её в ваш другой частный канал.
![preview](https://github.com/xtrahigh/tshuffler/blob/master/preview.gif)

[English usage guide](https://github.com/xtrahigh/tshuffler#Usage-guide)

[Инструкция на русском](https://github.com/xtrahigh/tshuffler#Инструкция)
## Usage guide
At a high level, the usage instructions are:
1. Install telethon library
2. Download the script
3. Create 2 private channels
4. Replace ID and hash values in the script with your own
5. Run the script and log into your account

See below for more details.
## Detailed usage guide
- Install telethon library: `pip3 install telethon`

- Download script: `git clone https://github.com/xtrahigh/tshuffler.git` or [Download ZIP](https://github.com/xtrahigh/tshuffler/archive/master.zip)

- Login to [my.telegram.org](https://my.telegram.org), go to [API development tools](https://my.telegram.org/apps) and create an app named `tshuffler`

- Create 2 private channels in the Telegram client. The first is for storing your music ([like that](https://t.me/cctracks_Rock)), the second is for mixing it.

- Type something in the first channel, then forward this message to [@getmyid_bot](https://t.me/getmyid_bot). Do the same with the second channel. This is how you can get the channel IDs. Look at the `Forwarded from chat` values.

- Go to the tshuffler folder, open the main.py script in any text editor and replace `api_id` and `api_hash` with your values from [API development tools](https://my.telegram.org/apps), `from_channel` and `to_channel` with your values from [@getmyid_bot](https://t.me/getmyid_bot)

- Open terminal and run main.py: `python3 main.py`

- Enter your account phone number, then enter login confirmation code. After a successful login, the `tshuffler.session` file will be created. This file is personal and must be kept secret!

In the future, you just need to execute the `python3 main.py` command being in the script folder, or create a shortcut for it.

## Инструкция
Описать действия кратко можно так:
1. Установите библиотеку telethon
2. Скачайте скрипт
3. Создайте 2 частных канала
4. Замените значения ID и hash в скрипте на ваши
5. Запустите скрипт и войдите в свой аккаунт

Подробности смотрите ниже.
## Подробная инструкция
- Установите библиотеку telethon: `pip3 install telethon`

- Скачайте скрипт: `git clone https://github.com/xtrahigh/tshuffler.git` или [Скачать ZIP](https://github.com/xtrahigh/tshuffler/archive/master.zip)

- Авторизуйтесь на [my.telegram.org](https://my.telegram.org), перейдите в раздел [API development tools](https://my.telegram.org/apps) и создайте приложение с именем `tshuffler`

- В клиенте Telegram создайте 2 частных канала. Первый для хранения вашей музыки ([пример](https://t.me/cctracks_Rock)), второй для перемешивания треков.

- Напишите что-нибудь в первом канале и перешлите сообщение в [@getmyid_bot](https://t.me/getmyid_bot). То же самое сделайте и со вторым каналом. Так вы можете получить ID каналов. Смотрите значение `Forwarded from chat`.

- Перейдите в папку со скриптом, откройте скрипт main.py любым текстовым редактором и замените `api_id` и `api_hash` своими значениями из [API development tools](https://my.telegram.org/apps), `from_channel` и `to_channel` своими значениями из [@getmyid_bot](https://t.me/getmyid_bot)

- Откройте терминал и запустите скрипт main.py: `python3 main.py`

- Введите номер телефона, привязанный к аккаунту, затем введите код подтверждения. После успешного входа будет создан файл `tshuffler.session`. Этот файл является личным и должен храниться в секрете!

В будущем вам просто нужно выполнить `python3 main.py`, находясь в папке со скриптом, или создать ярлык для него.
