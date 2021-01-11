# tshuffler
### While we don't have a [shuffle play](https://github.com/telegramdesktop/tdesktop/pull/7700) feature in [Telegram desktop client](https://github.com/telegramdesktop/tdesktop), this kludge solves this problem.

The script gets music from your private channel and randomly forwards it to another private channel.

# Usage guide

- Install telethon library: `pip3 install telethon`

- Download script: `git clone https://github.com/xtrahigh/tshuffler.git` or [Download ZIP](https://github.com/xtrahigh/tshuffler/archive/master.zip)

- Login to [my.telegram.org](https://my.telegram.org), go to [API development tools](https://my.telegram.org/apps) and create an app named `tshuffler`

- Create 2 private channels in the Telegram client. The first is for storing your music ([like that](https://t.me/cctracks_Rock)), the second is for mixing it.

- Type something in the first channel, then forward this message to [@getmyid_bot](https://t.me/getmyid_bot). Do the same with the second channel. This is how we can get the channel IDs. Look at the `Forwarded from chat` values.

- Go to the tshuffler folder, open the main.py script in any text editor and replace `api_id` and `api_hash` with your values from [API development tools](https://my.telegram.org/apps), `from_channel` and `to_channel` with your values from [@getmyid_bot](https://t.me/getmyid_bot)

- Open terminal and run main.py: `python3 main.py`

- Enter your account phone number, then enter login confirmation code. After a successful login, the `tshuffler.session` file will be created. This file is personal and must be kept secret!

In the future, you just need to execute the last command being in the script folder, or create a shortcut for it.
