from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterMusic
from random import shuffle

# You must get your own api_id and api_hash from https://my.telegram.org
api_id = 3333333
api_hash = 'abc123'
from_channel = -100333333333  # Tracks will be forwarded from this channel
to_channel = -100444444444  # Tracks will be forwarded to this channel

client = TelegramClient('tshuffler', api_id, api_hash)
client.start()


async def main():
    # Creates a list with message IDs of your main music channel
    messages_ids = []
    async for message in client.iter_messages(from_channel, None, filter=InputMessagesFilterMusic):
        messages_ids.append(message.id)
    print('Got', len(messages_ids), 'tracks to shuffle\n')

    shuffle(messages_ids)

    # Creates a list with message IDs of your shuffled music channel
    to_messages_ids = []
    async for to_message in client.iter_messages(to_channel, None, filter=InputMessagesFilterMusic):
        to_messages_ids.append(to_message.id)

    # Clears your shuffled music channel from previous shuffled tracks
    await client.delete_messages(to_channel, to_messages_ids)
    print('Deleted', len(to_messages_ids), 'previous shuffled tracks\n\nShuffling tracks...\n')

    # Forwards music from your main music channel to your shuffled music channel
    # Method: message by message
    for messages_id in messages_ids:
        await client.forward_messages(to_channel, messages_id, from_channel, silent=True)
    print('Forwarded', len(messages_ids), 'shuffled tracks\n')

    # Creates a list with message IDs of your shuffled music channel
    to_messages_ids = []
    async for to_message in client.iter_messages(to_channel, None, filter=InputMessagesFilterMusic):
        to_messages_ids.append(to_message.id)

    # Pins the message with the first shuffled track to easily jump to it
    await client.pin_message(to_channel, to_messages_ids[-1], notify=False)
    print('First track pinned\n\nEnjoy your listening')

with client:
    client.loop.run_until_complete(main())
