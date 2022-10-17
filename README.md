# Telegram-rent

--- 
This is project for parsing telegram channels and groups for rent ads and generate a website with this ads, for better search.

https://telegram-rent.com

## Getting Started

### Prerequisites

You must have docker and docker-compose installed on your machine.

Then must actualise values for the environment in next fodlers: `node-frontend, php-backend, python-parser`: copy `.env.example` to `.env` and fill it with actual values...

Then you can run project with docker-compose:

```bash
docker-compose up -d
```

### Parsing

Run command and enter your telegram phone number and code:

```bash
docker exec -i telegram_rent_python /usr/local/bin/python /app/history.py --channel ${channel name here} --parse-limit-hours 10 --parse-size 50 --country ${country name for current group ads} --city ${city name for current group ads}
```

For `histroy.py` script required next arguments:
- `--channel` - channel name for parsing
- `--parse-limit-hours` - limit for parsing in hours
- `--parse-size` - count messages for telegram api request
- `--country` - country name for current group ads
- `--city` - city name for current group ads

### Frontend

After parsing you can see parsed ads on frontend: http://localhost:7100

## DB scheme

countries
| id | name
|---|---|

cities
| id | country_id| name
|---|---|---|

telegram_groups
| id | username | title | avatar_path | description
|---|---|---|---|---|

telegram_authors
| id | username | type | first_name | last_name | title | avatar_path | description
|---|---|---|---|---|---|---|---|

telegram_messages
| telegarm_group_id | telegram_author_id | city_id | grouped_id | text | price
|---|---|---|---|---|---|

telegram_photos
| id | telegram_group_id | grouped_id | path
|---|---|---|---|

## License

MIT License