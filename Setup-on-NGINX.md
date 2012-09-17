# Setup OntoWiki on a NGINX Server
Sometimes you don't want to run a heavy web server like Apache but want to use a light program like nginx. Thins page will eventually give you a step by step guide to setup OntoWiki on nginx.

## Configuration File
The following configuration should usually be placed (at least on Ubuntu) in a file called `/etc/nginx/sites-available/ontowiki`. To enable the new configuration you have to create a symbolic link to this file at `/etc/nginx/sites-enabled/ontowiki`.

You can also find this file in its [github:gist](https://gist.github.com/3739707).

    ##
    # This is a configurationfile to run an instance of OntoWiki on a nginx server
    # Read more about OntoWiki at http://ontowiki.net
    server {
        listen   8080; ## listen for ipv4; this line is default and implied
        #listen   [::]:80 default ipv6only=on; ## listen for ipv6
    
        # Make site accessible from http://localhost/
        server_name localhost;
    
        # path to ontowiki
        # !!! please adopt to fit your needs !!!
        root /home/ontowiki/ontowiki/;
    
        # where the logs should go
        # !!! you can also adopt this as you want !!!
        error_log /tmp/logs/error.log;
    
        index index.php;
    
        # prevent access to sensible files
        location ~ (\.ini)$ {
            deny all;
        }
    
        # deny access to .htaccess files, if Apache's document root
        # concurs with nginx's one
        location ~ /\.ht {
            deny all;
        }
    
        location / {
            # First attempt to serve request as file, then
            # as directory, then fall back to index.php
            try_files $uri $uri/ /index.php;
        }
    
        # rewrite all URLs to index.php
        if (!-e $request_filename) {
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

## Known Problems
_none_
(please add problems you may have with this configuration here and to the issue tracker)

## Further Information
* http://wiki.nginx.org/Zend_Framework
* http://www.linux-web-development.de/2010/11/03/zend-framework-mit-nginx (German)