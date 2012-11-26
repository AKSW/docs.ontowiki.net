# Setup OntoWiki on a NGINX Server
Sometimes you don't want to run a heavy web server like Apache but want to use a light program like nginx. Thins page will eventually give you a step by step guide to setup OntoWiki on nginx.

## Configuration File
The following configuration should usually be placed (at least on Ubuntu) in a file called `/etc/nginx/sites-available/ontowiki`. To enable the new configuration you have to create a symbolic link to this file at `/etc/nginx/sites-enabled/ontowiki`.

You can also find this file in its [github:gist](https://gist.github.com/3739707).

    ##
    # This is a configurationfile to run an instance of OntoWiki on a nginx server
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

## Trouble shooting
### File uploads exceeding "client_max_body_size"
Nginx has a separate system for limiting interaction with the server. One of these, "client_max_body_size", limits the payload of a client request, thus limiting the allowed size of POST requests.  

To allow for larger file uploads in OntoWiki, one would need to adjust both the value of "[client_max_body_size](http://wiki.nginx.org/HttpCoreModule#client_max_body_size)" in Nginx setup and "[upload_max_filesize](http://www.php.net/manual/ini.core.php#ini.upload-max-filesize)" in the relevant php.ini file, /etc/php5/cli/php.ini in my case.  

## Known Problems

What is the best value for PHP_FCGI_CHILDREN for use with OntoWiki?
c.f http://www.fastcgi.com/drupal/node/5?q=node/10, bottom of page.

(please add problems you may have with this configuration here and to the issue tracker)

## Further Information
* http://wiki.nginx.org/Zend_Framework
* http://www.linux-web-development.de/2010/11/03/zend-framework-mit-nginx (German)