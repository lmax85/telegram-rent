#!/usr/bin/env python3

import os
import re

from dotenv import load_dotenv
from telethon.tl.types import Channel, PeerChannel, PeerChat, PeerUser, User

load_dotenv()
STORAGE_PATH=os.getenv('STORAGE_ABSOLUTE_PATH')

class MessageParser:
    def __init__(self, client, channel, cityId,  pricePattern, authors):
        self.client = client
        self.channel = channel
        self.cityId = cityId
        self.pricePattern = pricePattern
        self.authorsFromDb = authors

    def get_price_from_text(self, text):
        prices = re.search(self.pricePattern, text, re.IGNORECASE)

        if prices:
            priceText = re.sub('[,.]', '', prices.group(0)) # remove , and .
            price_number = re.search('[0-9]+', priceText, re.IGNORECASE)
            return int(price_number.group(0))

        return None

    async def parse_message(self, message):
        if message.grouped_id == None:
            return {}

        if message.message:
            price = self.get_price_from_text(message.message)
            if price == None:
                price = 0

            fromId = message.from_id.user_id if message.from_id != None and isinstance(message.from_id, PeerUser) else message.peer_id.channel_id

            # try to obtain user from database
            author = [author for author in self.authorsFromDb if author.id == fromId]

            if author == []:
                author = await self.client.get_entity(fromId)
                authorPhotoPath = await self.client.download_profile_photo(entity = author.id, file = str(STORAGE_PATH) + 'authors/' + str(author.id) + '.jpg')
                author.avatar_path = authorPhotoPath
                self.authorsFromDb.append(author)
            else:
                author = author[0]

            return {
                "message": {
                    'id': message.id,
                    "telegram_group_id": self.channel.id,
                    "telegram_author_id": author.id,
                    "grouped_id": message.grouped_id,
                    "city_id": self.cityId,
                    'text': message.message,
                    'price': price,
                    "created_at": message.date,
                    "updated_at": message.date,
                },
                "author": {
                    'id': author.id,
                    'type': author.__class__.__name__,
                    'username': author.username,
                    "first_name": author.first_name if isinstance(author, User) else None,
                    "last_name": author.last_name if isinstance(author, User) else None,
                    "title": None if isinstance(author, User) else author.title,
                    "avatar_path": author.avatar_path,
                    # "created_at": author.date,
                    # "updated_at": author.date,
                }
            }

        # You can download media from messages, too!
        # The method will return the path where the file was saved.
        if message.photo:
            file_path = str(STORAGE_PATH) + str(message.grouped_id) + '/' + str(message.id) + '.jpg'

            if os.path.isfile(file_path) == False:
                await message.download_media(file = file_path)

            return {
                "photo": {
                    "id": message.id,
                    "telegram_group_id": self.channel.id,
                    "grouped_id": message.grouped_id,
                    "path": file_path,
                    "created_at": message.photo.date,
                    "updated_at": message.photo.date,
                }
            }

        return {}
