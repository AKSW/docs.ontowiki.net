---
layout: page
title: Concepts
---

# Understanding OntoWiki Installation Concepts

### Terminology
### Overview of Basic Concepts
### Introduction into the OntoWiki infrastructure
- explaining apache, php, sparql endpoint
- image of the stack

## Planing the OntoWiki Software System Base (wie kann man das eleganter formulieren?)

- tasks of the ontowiki servers (showing wiki, doing sparql queries, storage, import, export,...)
- what are the ontowiki hardware and software minimum requirements (cpu, ram, harddrive/ssd size and speed, network bandwith, operating system type name and versions)
### Operating System

Ubuntu (latest release), any other linux distro should be fine too. Windows is possible as well.

### Webserver
Most developers are using Apache but you may also but want to use a light program like NGINX. lighttpd should be possible too, but uses a different rewrite rule language and we don't have ported ours yet.

#### NGINX

##### Configuration File
The following configuration should usually be placed (at least on Ubuntu) in a file called `/etc/nginx/sites-available/ontowiki`. To enable the new configuration you have to create a symbolic link to this file at `/etc/nginx/sites-enabled/ontowiki`.

You can also find this file in its [github:gist](https://gist.github.com/3739707).

    ##
    # This is a configurationfile to run an instance of OntoWiki on a NGINX server
    # Read more about OntoWiki at http://ontowiki.net
    ##
    
    server {
        listen   8080; ## listen for ipv4; this line is default and implied
        #listen   [::]:80 default ipv6only=on; ## listen for ipv6
    
        # Make site accessible from http://localhost/
        server_name localhost;
    
        # path to ontowiki
        # !!! please adapt to fit your needs !!!
        root /home/ontowiki/ontowiki/;
    
        # where the logs should go
        # !!! you can also adapt this as you want !!!
        error_log /home/ontowiki/nginx/logs/ontowiki-error.log;
    
        index index.php;
    
        # rewrite for favicon
        rewrite ^/favicon\.(.*)$ /application/favicon.$1 break;
    
        # check if the request is an exception and should not be handled by the index.php
        if ($request_filename !~ ((extensions|libraries).*|\.(js|ico|gif|jpg|png|css|swf|json))$) {
            set $is_exception "f";
        }
    
        # rewrite all other URLs to index.php
        if ($is_exception = "f") {
            rewrite ^.*$ /index.php last;
        }
    
        # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
        # see also [1] for a UNIX socket configuration and some other details.
        # [1]: http://library.linode.com/web-servers/nginx/php-fastcgi/ubuntu-10.04-lucid
        location ~ \.php(.*)$ {
            include fastcgi_params;
            fastcgi_pass 127.0.0.1:9000;
            fastcgi_index index.php;
            fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
            fastcgi_param PATH_INFO $fastcgi_script_name;
    
            # tell OntoWiki that rewrite is enabled
            fastcgi_param ONTOWIKI_APACHE_MOD_REWRITE_ENABLED 1;
        }
    }

OntoWiki will be available through your browser at `http://localhost:8080`.

##### Trouble shooting
###### File uploads exceeding "client_max_body_size"
NGINX has a separate system for limiting interaction with the server. One of these, "client_max_body_size", limits the payload of a client request, thus limiting the allowed size of POST requests.  

To allow for larger file uploads in OntoWiki, one would need to adjust both the value of "[client_max_body_size](http://wiki.nginx.org/HttpCoreModule#client_max_body_size)" in Nginx setup and "[upload_max_filesize](http://www.php.net/manual/ini.core.php#ini.upload-max-filesize)" in the relevant php.ini file, /etc/php5/cli/php.ini in my case.  

##### Known Problems


(please add problems you may have with this configuration here and to the issue tracker)

##### Further Information
- <http://wiki.nginx.org/Zend_Framework>
- <http://www.linux-web-development.de/2010/11/03/zend-framework-mit-nginx> (German)

### PHP
You need PHP version 5.2 or higher.
You should set up your PHP environment with the following settings in php.ini:
  * `max_execution_time = 120`
  * `memory_limit = 128M`
  * `upload_max_filesize = 16M ; depending on the size of knowledge bases you plan to use`
  * `post_max_size = 16M`
  * `short_open_tag = Off`; if you have this turned on, some features will not work

To get rid of strict warnings, set the default timezone for your server, e.g.
  * `date.timezone=Europe/Berlin`

### Backend
Virtuoso Opensource Version 6.1.4 or higher, more details for installation [[here|VirtuosoBackend]]. MySQL backend is also posible but slower.

### Browser
Current Google Chrome, Safari and Firefox Browser tested, current MSIE not always tested but should work. Older browser are not fully compatible. More details [[here|Browser-Compatibility]]

### OntoWiki Version
We recommend the installation of a current snapshot release or directly from the repository.

- how does ontowiki scale with number of users and data? 
- reference to virtuoso documentation
4 gb ram
- example deployments (real life examples aksw.org, Caucasus Spiders maybe with number of accesses and data size)
<Setup>
