#!/usr/bin/env python3

import os
from datetime import date, datetime, timedelta, tzinfo

import database.database as database
import init_cli
import message_parser
from database.models.city import City
from dotenv import load_dotenv
# You can be more explicit about the type for said ID by wrapping
# it inside a Peer instance. This is recommended but not necessary.
from telethon import TelegramClient

load_dotenv()

STORAGE_PATH=os.getenv('STORAGE_ABSOLUTE_PATH')
# Remember to use your own values from my.telegram.org!
api_id = os.getenv('TELEGRAM_API_ID')
api_hash = os.getenv('TELEGRAM_API_HASH')

if (api_id == None or api_hash == None):
    print('TELEGRAM_API_ID or TELEGRAM_API_HASH is not set')
    exit()

client = TelegramClient('anon', int(api_id), api_hash)

async def prepare_params(args):
    global channel
    global channelId
    global channelName
    global cityId
    global cityName
    global limit
    global size
    global pricePattern

    try:
        channelId = int(args.channel)
    except ValueError:
        channelId = args.channel

    country = database.get_country_by_name(args.country)
    if country == None:
        country = database.insert_country(args.country)

    city = database.get_city_by_name(args.city)
    if city == None:
        city = database.insert_city(args.city, country.id)
    cityId = city.id
    cityName = city.name

    channel = database.get_group_by_name(channelId)
    if channel == None:
        print('Channel %s not found in database' % channelId)
        channel = await client.get_entity(channelId)
        channelAvatarPath = await client.download_profile_photo(entity = channel.id, file = str(STORAGE_PATH) + str(channel.id) + '.jpg')
        database.update_channel(channel, channelAvatarPath)

    channelName = channel.username
    size = 2500 if args.parse_size > 2500 else args.parse_size
    limit = args.parse_limit_hours
    pricePattern = args.price_pattern

async def main():
    args = init_cli.parse_command()
    await prepare_params(args)

    authors = database.get_authors()
    parsed = 0
    stop = False
    endDate = datetime.utcnow() - timedelta(hours=limit)
    messageParser = message_parser.MessageParser(client, channel, cityId, pricePattern, authors)
    toDatabase = {
        'photos': [],
        'authors': [],
        'messages': [],
        'authorIds': [],
    }

    while stop == False:
        async for message in client.iter_messages(channelId, limit=size, add_offset=parsed):
            # print(parsed, limit, localSize, stop)
            data = await messageParser.parse_message(message)

            if data.get('photo', None) != None:
                toDatabase['photos'].append(data['photo'])
            if data.get('message', None) != None:
                toDatabase['messages'].append(data['message'])
            if data.get('author', None) != None and not data['author']['id'] in toDatabase['authorIds']:
                toDatabase['authors'].append(data['author'])
                toDatabase['authorIds'].append(data['author']['id'])

            parsed += 1

            if message.date.replace(tzinfo=None) < endDate:
                print(message.date.replace(tzinfo=None), 
                    endDate)
                stop = True

            if parsed % size == 0 or stop == True:
                # insert to db
                database.upsertParsedData(toDatabase)
                print('[%s]: city %s group %s inserted %d messages to db' % (datetime.now(), cityName, channelName, toDatabase['messages'].__len__()))

            if stop == True:
                break

    database.session_close()

with client:
    client.loop.run_until_complete(main())
