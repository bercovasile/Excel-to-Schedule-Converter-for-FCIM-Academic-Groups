FROM alpine:3.18
LABEL maintainer="NGINX Docker Maintainers "
ENV NGINX_VERSION 1.25.3
ENV PKG_RELEASE 1
RUN set -x && addgroup -g 101 -S nginx && adduser -S -D -H -u 101 -h /var/cache/nginx -s /sbin/nologin -G nginx -g nginx nginx && apkArch="$(cat /etc/apk/arch)" && nginxPackages=" nginx=${NGINX_VERSION}-r${PKG_RELEASE} " && apk add --no-cache --virtual .checksum-deps openssl && case "$apkArch" in x86_64|aarch64) set -x && KEY_SHA512="e09fa32f0a0eab2b879ccbbc4d0e4fb9751486eedda75e35fac65802cc9faa266425edf83e261137a2f4d16281ce2c1a5f4502930fe75154723da014214f0655" && wget -O /tmp/nginx_signing.rsa.pub https://nginx.org/keys/nginx_signing.rsa.pub && if echo "$KEY_SHA512 */tmp/nginx_signing.rsa.pub" | sha512sum -c -; then echo "key verification succeeded!"; mv /tmp/nginx_signing.rsa.pub /etc/apk/keys/; else echo "key verification failed!"; exit 1; fi && apk add -X "https://nginx.org/packages/mainline/alpine/v$(egrep -o '^[0-9]+\.[0-9]+' /etc/alpine-release)/main" --no-cache $nginxPackages ;; *) set -x && tempDir="$(mktemp -d)" && chown nobody:nobody $tempDir && apk add --no-cache --virtual .build-deps gcc libc-dev make openssl-dev pcre2-dev zlib-dev linux-headers bash alpine-sdk findutils && su nobody -s /bin/sh -c " export HOME=${tempDir} && cd ${tempDir} && curl -f -O https://hg.nginx.org/pkg-oss/archive/${NGINX_VERSION}-${PKG_RELEASE}.tar.gz && PKGOSSCHECKSUM=\"00b217979265cc9d66c991c9c89427558936dbaa568d175ca45780589171d94f1866217be09a83438d95494cf38baaa6788320f6d8d23f2fb29c03117391ff88 *${NGINX_VERSION}-${PKG_RELEASE}.tar.gz\" && if [ \"\$(openssl sha512 -r ${NGINX_VERSION}-${PKG_RELEASE}.tar.gz)\" = \"\$PKGOSSCHECKSUM\" ]; then echo \"pkg-oss tarball checksum verification succeeded!\"; else echo \"pkg-oss tarball checksum verification failed!\"; exit 1; fi && tar xzvf ${NGINX_VERSION}-${PKG_RELEASE}.tar.gz && cd pkg-oss-${NGINX_VERSION}-${PKG_RELEASE} && cd alpine && make base && apk index -o ${tempDir}/packages/alpine/${apkArch}/APKINDEX.tar.gz ${tempDir}/packages/alpine/${apkArch}/*.apk && abuild-sign -k ${tempDir}/.abuild/abuild-key.rsa ${tempDir}/packages/alpine/${apkArch}/APKINDEX.tar.gz " && cp ${tempDir}/.abuild/abuild-key.rsa.pub /etc/apk/keys/ && apk del --no-network .build-deps && apk add -X ${tempDir}/packages/alpine/ --no-cache $nginxPackages ;; esac && apk del --no-network .checksum-deps && if [ -n "$tempDir" ]; then rm -rf "$tempDir"; fi && if [ -f "/etc/apk/keys/abuild-key.rsa.pub" ]; then rm -f /etc/apk/keys/abuild-key.rsa.pub; fi && if [ -f "/etc/apk/keys/nginx_signing.rsa.pub" ]; then rm -f /etc/apk/keys/nginx_signing.rsa.pub; fi && apk add --no-cache --virtual .gettext gettext && mv /usr/bin/envsubst /tmp/ && runDeps="$( scanelf --needed --nobanner /tmp/envsubst | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' | sort -u | xargs -r apk info --installed | sort -u )" && apk add --no-cache $runDeps && apk del --no-network .gettext && mv /tmp/envsubst /usr/local/bin/ && apk add --no-cache tzdata && ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log && mkdir /docker-entrypoint.d

COPY docker-entrypoint.sh /
COPY docker-entrypoint.d/10-listen-on-ipv6-by-default.sh /docker-entrypoint.d
COPY docker-entrypoint.d/15-local-resolvers.envsh /docker-entrypoint.d
COPY docker-entrypoint.d/20-envsubst-on-templates.sh /docker-entrypoint.d
COPY docker-entrypoint.d/30-tune-worker-processes.sh /docker-entrypoint.d
ENTRYPOINT ["/docker-entrypoint.sh"]
EXPOSE 80
STOPSIGNAL SIGQUIT
COPY ./default.conf etc/nginx/conf.d/ 
COPY ./nginx.conf etc/nginx

CMD ["nginx", "-g", "daemon off;"]
