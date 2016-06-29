---
title: OntoWiki-behind-a-reverseProxy-(with-SSL)
tags: [ontowiki, install]
sidebar: ontowiki_sidebar
permalink: /ontowiki_OntoWiki-behind-a-reverseProxy-(with-SSL)/
---
# OntoWiki behind a reverseProxy
##Preface
This page explains the necessary steps to use OntoWiki behind a reverseProxy (with ssl) - e.g. if OntoWiki is deployed as a docker-container

* install OntoWiki as described [here](http://docs.ontowiki.net/ontowiki_Install-Ontowiki/)
* install your favorite webserver (apache2/nginx)
* add config of your reverseProxy

## Configuration

###nginx
```
 server {
    listen 80;
    server_name path.to.your.ontowiki.com;
    return 301 https://path.to.your.ontowiki.com;
}

server {

    listen 443;
    server_name path.to.your.ontowiki.com;
    ssl_certificate           /etc/nginx/ssl/your_server_cert.cer;
    ssl_certificate_key       /etc/nginx/ssl/your_server_key.key;
   
    ssl on;
    ssl_session_cache  builtin:1000  shared:SSL:10m;
    ssl_protocols  TLSv1 TLSv1.1 TLSv1.2;
    ssl_ciphers HIGH:!aNULL:!eNULL:!EXPORT:!CAMELLIA:!DES:!MD5:!PSK:!RC4;
    ssl_prefer_server_ciphers on;

    access_log            /var/log/nginx/path.to.your.ontowiki.com.access.log;

location / {

      proxy_set_header        Host $host;
      proxy_set_header        X-Real-IP $remote_addr;
      proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header        X-Forwarded-Proto $scheme;
      add_header              Front-End-Https   on;

      # Fix the "It appears that your reverse proxy set up is broken" error.
      proxy_pass          http://path-to-your-internal-ontowiki:8000;
      proxy_read_timeout  90;

      proxy_redirect      http://path-to-your-internal-ontowiki:8000 https://path.to.your.ontowiki.com;
    }
}
```
