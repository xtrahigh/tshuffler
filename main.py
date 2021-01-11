from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterMusic
from random import shuffle

# You must get your own api_id and api_hash from https://my.telegram.org
api_id = 123
api_hash = '123abc'
from_id = -100190  # Tracks will be forwarded from this chat
to_id = -100200  # Tracks will be forwarded to this chat

client = TelegramClient('tshuffler', api_id, api_hash)
client.start()


async def main():
    messages_ids = []
    async for message in client.iter_messages(from_id, limit=None, filter=InputMessagesFilterMusic):
        messages_ids.append(message.id)
    print('Got', len(messages_ids), 'tracks to shuffle\n')

    shuffle(messages_ids)

    to_messages_ids = []
    async for to_message in client.iter_messages(to_id, limit=None, filter=InputMessagesFilterMusic):
        to_messages_ids.append(to_message.id)

    await client.delete_messages(to_id, to_messages_ids)
    print('Deleted', len(to_messages_ids), 'previous shuffled tracks\n')

    for messages_id in messages_ids:
        await client.forward_messages(to_id, messages_id, from_id, silent=True)
    print('Forwarded', len(messages_ids), 'shuffled tracks\n\nEnjoy your listening')

with client:
    client.loop.run_until_complete(main())
