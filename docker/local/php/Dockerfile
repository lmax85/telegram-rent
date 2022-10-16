FROM php:8.0.2-fpm-alpine

RUN apk --no-cache upgrade && \
    apk add --no-cache \
    icu-dev \
    zlib-dev \
    libzip-dev \
    libpng-dev  \
    libjpeg-turbo \
    freetype freetype-dev \
    libjpeg-turbo-dev \
    libwebp-dev \
    libxpm-dev \
    oniguruma-dev \
    git \
    openssh \
    vim \
    unzip \
    bash \
    composer \
    postgresql-dev

# Extensions
## Add build utils

ENV BUILD_DEPS 'autoconf git gcc g++ make bash openssh libssl1.1 openssl-dev'
RUN apk add --no-cache --update --virtual .phpize-deps $PHPIZE_DEPS $BUILD_DEPS

## Common Exts
RUN pecl install -o -f redis apcu \
    && docker-php-ext-enable redis apcu \
    && docker-php-ext-configure intl \
    && docker-php-ext-install intl iconv bcmath mbstring pdo pdo_pgsql opcache zip gd exif sockets pcntl

## XDebug

# RUN mkdir -p /usr/src/php/ext/xdebug && curl -fsSL https://pecl.php.net/get/xdebug | tar xvz -C "/usr/src/php/ext/xdebug" --strip 1 && docker-php-ext-install xdebug
# RUN docker-php-ext-enable xdebug

## Remove build utils

RUN apk del .phpize-deps $BUILD_DEPS \
    && rm -rf /tmp/pear

# Content

COPY ./config.ini /usr/local/etc/php/conf.d/config.ini
COPY ./xdebug.ini /usr/local/etc/php/conf.d/xdebug.ini

WORKDIR /app

COPY entrypoint.sh /tmp/entrypoint.sh
RUN chmod +x /tmp/entrypoint.sh

CMD ["/tmp/entrypoint.sh", "php-fpm"]
