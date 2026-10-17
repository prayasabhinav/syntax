# SYNTAX: a static site. The build runs before this image is made; nothing runs but nginx, with no access log.
FROM nginx:1.27-alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY site/ /usr/share/nginx/html/
