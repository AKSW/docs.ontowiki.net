---
title: Install-on-IIS
tags: [ontowiki, install]
sidebar: ontowiki_sidebar
permalink: /Install-on-IIS.html
editme_path: ontowiki/Install-on-IIS.md
---
## OntoWiki on Microsoft IIS 7

OntoWiki was built for Apache thus it requires additional setup in order to work with Microsoft's webserver. 

> The following instructions assume you already have PHP installed with IIS. If not [install PHP here](http://php.iis.net/) or [read this](http://learn.iis.net/page.aspx/246/using-fastcgi-to-host-php-applications-on-iis/) to install manually.

### Install URL rewrite module

You can install it for free from: http://www.iis.net/download/urlrewrite

### web.config

You can skip this if your OntoWiki already comes with a web.config file or if you downloaded OntoWiki from the repository.

Apache uses the .htaccess file to configure web applications it is running. Simmilarly on IIS there is an XML file named web.config. Below is a minimal configuration file required for OntoWiki to work. It mimics OntoWiki's configuration, namely:

instructs IIS to deny access to *.ini files

creates rewrite rules for Zend Framework

when rewriting, creates a server variable called ONTOWIKI_APACHE_MOD_REWRITE_ENABLED, which enables OntoWiki to construct valid URLs

    <?xml version="1.0" encoding="UTF-8"?>
    <configuration>
    <system.webServer>
		<handlers>
			<add name="deny ini" verb="*" path="*.ini" type="System.Web.HttpForbiddenHandler" />
		</handlers>
        <rewrite>
            <rules>
                <rule name="Don't rewrite physical files" stopProcessing="true">
                    <match url="((extensions|libraries).*|\.(js|ico|gif|jpg|png|css|php|swf|json))$" />
                    <conditions logicalGrouping="MatchAny">
                        <add input="{REQUEST_FILENAME}" matchType="IsFile" pattern="" ignoreCase="false" />
                        <add input="{REQUEST_FILENAME}" matchType="IsDirectory" pattern="" ignoreCase="false" />
                    </conditions>
                    <action type="None" />
                </rule>
				<rule name="Redirect favicon" stopProcessing="true">
					<match url="^favicon\.(.*)$" />
					<action type="Redirect" url="application/favicon.{R:1}" />
				</rule>
                <rule name="Rewrite" stopProcessing="true">
                    <match url="^.*$" />
					<serverVariables>
						<set name="ONTOWIKI_APACHE_MOD_REWRITE_ENABLED" value="true" />
					</serverVariables>
                    <action type="Rewrite" url="index.php" />
                </rule>
            </rules>
        </rewrite>
    </system.webServer>
    </configuration>

Web.config file should be placed in the root folder of OntoWiki (ie. same folder where .htaccess is).

### Server variables

The last rule in the file above creates a server variable named ONTOWIKI_APACHE_MOD_REWRITE_ENABLED. By default IIS does not allow changing or creating of server variables. If you encounter a 500.50 error saying 

> "The server variable "ONTOWIKI_APACHE_MOD_REWRITE_ENABLED" is not allowed to be set. Add the server variable name to the allowed server variable list."

follow the instructions below.

1. Open InetMgr.exe
2. Go to your OntoWiki web application
3. Open the URL Rewrite feature (section IIS)
4. On the right pane locate 'View Server Variables...' and click it
5. Click 'Add'
6. Insert variable's name: ONTOWIKI_APACHE_MOD_REWRITE_ENABLED and click OK

Now OntoWiki should work on your IIS

## OntoWiki on Microsoft IIS 6 / IIS 5

Version prior to IIS7 aren't currently supported, though it should be possible to set up rewrite rules simmilar to the above using one of the free or commercially available ISAPI rewrite filters.

Also the handler would have to be moved to secton `system.web/httpHandlers` as `system.webServer` section has been introduced in IIS7
