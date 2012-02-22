# Setup OntoWiki on a NGINX Server
Sometimes you don't want to run a heavy web server like Apache but want to use a light program like nginx. Thins page will eventually give you a step by step guide to setup OntoWiki on nginx.

## Configuration File
The following configuration usually (on my Linux Mint 12) should be placed in a file caled `/etc/nginx/sites-available/ontowiki`. To enable the new configuration you have to create a symbolic link to this file at `/etc/nginx/sites-enabled/ontowiki`.

    ##
    # This is a configurationfile to run an instance of OntoWiki on a nginx server
    # Read more about OntoWiki at http://ontowiki.net
    ##
    # You should look at the following URL's in order to grasp a solid understanding
    # of Nginx configuration files in order to fully unleash the power of Nginx.
    # http://wiki.nginx.org/Pitfalls
    # http://wiki.nginx.org/QuickStart
    # http://wiki.nginx.org/Configuration
    #
    # Generally, you will want to move this file somewhere, and start with a clean
    # file but keep this around for reference. Or just disable in sites-enabled.
    #
    # Please see /usr/share/doc/nginx-doc/examples/ for more detailed examples.
    ##
    
    server {
        listen   8080; ## listen for ipv4; this line is default and implied
        #listen   [::]:80 default ipv6only=on; ## listen for ipv6
        
        root /home/natanael/public_html/ontowiki; ## path to ontowiki
        index index.php;
        
        # Make site accessible from http://localhost/
        server_name localhost;
    
        # Zugriff auf sensible Dateien verwehren
        location ~ (\.inc\.php|\.tpl|\.sql|\.tpl\.php|\.db)$ {
            deny all;
        }
    
        # deny access to .htaccess files, if Apache's document root
        # concurs with nginx's one
        #
        location ~ /\.ht {
            deny all;
        }
        
        location / {
            # First attempt to serve request as file, then
            # as directory, then fall back to index.html
            try_files $uri $uri/ /index.php;
        }
    
    
        # Die eigentliche RewriteRule für das Zend Framework
        if (!-e $request_filename) {
            rewrite ^.*$ /index.php last;
        }    
    
        # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
        #
        location ~ \.php(.*)$ {
            fastcgi_pass 127.0.0.1:9000;
            fastcgi_index index.php;
            include fastcgi_params;
        }
    }

OntoWiki will be available through your browser at `http://localhost:8080`.

## Known Problems
_none_

## Further Information
http://wiki.nginx.org/Zend_Framework
http://www.linux-web-development.de/2010/11/03/zend-framework-mit-nginx (German)