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
    from_messages_ids = []
    async for message in client.iter_messages(from_channel, None, filter=InputMessagesFilterMusic):
        from_messages_ids.append(message.id)
    print('Got', len(from_messages_ids), 'tracks to shuffle\n')

    shuffle(from_messages_ids)

    # Creates a list with message IDs of your shuffled music channel
    to_messages_ids = []
    async for message in client.iter_messages(to_channel, None, filter=InputMessagesFilterMusic):
        to_messages_ids.append(message.id)

    # Clears your shuffled music channel from previous shuffled tracks
    await client.delete_messages(to_channel, to_messages_ids)
    print('Deleted', len(to_messages_ids), 'previous shuffled tracks\n\nShuffling tracks...\n')

    # Forwards music from your main music channel to your shuffled music channel
    # Method: message by message
    fwd_time = 0
    for message_id in from_messages_ids:
        await client.forward_messages(to_channel, message_id, from_channel, silent=True)
        fwd_time += 1
        # Pins the message with the first shuffled track to easily jump to it
        # then deletes the message about pinning
        if fwd_time == 1:
            to_messages_ids = []
            async for message in client.iter_messages(to_channel, None, filter=InputMessagesFilterMusic):
                to_messages_ids.append(message.id)
            await client.pin_message(to_channel, to_messages_ids[-1], notify=False)
            await client.delete_messages(to_channel, to_messages_ids[0] + 1)
            print('First track pinned\n')
    print('Forwarded', len(from_messages_ids), 'shuffled tracks\n\nEnjoy your listening!')

with client:
    client.loop.run_until_complete(main())
