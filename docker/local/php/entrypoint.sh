#!/bin/sh

cd /app
echo "starting composer install"
composer install --ignore-platform-reqs
echo "starting migrate"
/usr/local/bin/php artisan migrate

echo "starting fpm"
exec "$@"
