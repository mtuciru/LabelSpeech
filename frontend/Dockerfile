FROM alpine:3 as nginxbuild

# Install OpenSSl, PCRE and AIO libraries
RUN apk update && apk upgrade \
    && apk add git wget tar unzip gzip \
    && apk add linux-headers build-base openssl-dev pcre-dev zlib-dev \
    && wget -q https://nginx.org/download/nginx-1.23.3.tar.gz \
    && tar -xzf nginx-1.23.3.tar.gz
WORKDIR /nginx-1.23.3

RUN ./configure \
    --prefix=/nginx \
    --user=nginx \
    --group=nginx \
    --http-log-path=/dev/stdout \
    --error-log-path=/dev/stdout \
    --with-threads \
    --without-http_access_module \
    --without-http_auth_basic_module \
    --without-http_autoindex_module \
    --without-http_browser_module \
    --without-http_charset_module \
    --without-http_empty_gif_module \
    --without-http_fastcgi_module \
    --without-http_geo_module \
    --without-http_limit_conn_module \
    --without-http_limit_req_module \
    --without-http_memcached_module \
    --without-http_scgi_module \
    --without-http_ssi_module \
    --without-http_split_clients_module \
    --without-http_uwsgi_module \
    --without-http_userid_module \
    --without-http_upstream_hash_module \
    --without-http_upstream_ip_hash_module \
    --without-http_upstream_least_conn_module \
    --without-http_upstream_random_module \
    --without-http_upstream_keepalive_module \
    --without-http_upstream_zone_module \
    --with-http_ssl_module \
    --with-http_v2_module \
    && make -j$(nproc) \
    && make install \
    && rm -rf /nginx/conf/nginx.conf


FROM alpine:3
# Install libs we built nginx with
RUN apk update && apk upgrade \
    && apk add --no-cache gettext openssl pcre
RUN addgroup -S nginx && adduser --disabled-password --ingroup nginx nginx
WORKDIR /

COPY --from=nginxbuild /nginx /nginx
COPY nginx.conf /nginx/conf/nginx.conf
RUN mkdir /public
RUN chown -R nginx:nginx /public && chmod -R 777 /public

CMD [ "./nginx/sbin/nginx" ]