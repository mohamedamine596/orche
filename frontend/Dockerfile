FROM nginx:1.27-alpine
# Replace nginx's default site with our configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf
# Add our web page
COPY html/ /usr/share/nginx/html/
