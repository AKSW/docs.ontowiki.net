The embedded Erfurt library contains a background worker implementation using Gearman. This means: OntoWiki and its extensions can handle expensive tasks in the background by calling a job for execution which were registered on the server beforehand.

Now here is how it works and how you can use it:

### Server
To make use of Gearman as worker background, you need to install the Gearman service on the server.

#### Installation
This process depends on the operating system.
##### RHEL/Fedora
	yum install gearmand-server
##### Debian/Ubuntu
	apt-get install gearman-job-server
##### Windows
Please use [CYGWIN][3]!
##### Compilation from archive
At first, download the Gearman [daemon archive][???] and install:

	tar xzf gearmand-X.Y.tar.gz
	cd gearmand-X.Y
	./configure
	make
	make install

After installation via package management the server already should be running <b>but only listening to localhost</b>.<br/>
More on [Gearman documentation][2] or by typing `gearmand --help`.

### Client and Worker API for PHP
First install needed libraries - for Debian/Ubuntu this would be:

	apt-get install php5-dev php5-cli libgearman6

Now download the archive from <a href="http://pecl.php.net/package/gearman">PECL</a>.

	tar xzf gearman-X.Y.tgz
	cd gearman-X.Y
	phpize
	./configure
	make
	make install

**HINT: If you are having trouble with the version if libgearman, try an older archive (<a href="http://serverfault.com/questions/487331/not-able-to-install-gearman-on-ubuntu-12-04">read more</a>).**

### Test
#### Console

Open a terminal and create a new worker, which will register a function "wc" which will count list items of given data.

	gearman -w -f wc -- wc -l

Open _another_ terminal and call the worker:

	gearman -f wc < /etc/passwd

... and you should see the number of entries on your passwords file.

#### PHP example
##### Server script
	<?php
	class MyWorker{
		public function reverse( GearmanJob $job ){
			return strrev( $job->workload() );
		}
	}
	$worker= new GearmanWorker();
	$worker->addServer();
	$worker->addFunction( "reverse", array( "MyWorker", "reverse" ) );
	while( $worker->work() );

##### Client script
	<?php
	$client     = new GearmanClient();
	$client->addServer();
	print($client->do("reverse", "Hello World!"));

### Usage in OntoWiki / Erfurt

#### Classes in Erfurt

##### Worker_Registry
This class will be started by the server side shell script to start the job server.

It triggers the event `onAnnounceWorker` and will allow OntoWiki / Erfurt components to state their worker jobs.
These will be stored within the registry as a later input for the worker backend.

##### Worker_Backend
This class is wrapper for the Gearman worker, which runs server side.
It knows the worker registry and add the registered jobs to the Gearman server.
Afterwards the server side worker script will set the backend and Gearman server to listen mode.

While this is the empty engine for handling job calls, you will now also need jobs classes to register.

##### Worker_Job_Interface
Every job class will implement the interface.
At the moment you will need to implement the `run` method by your needs.
So every job class only has one public method, which will be called automatically.

##### Worker_Job_Container
This class is used to store registerable worker jobs within the worker registry.
You do not need to use this class at all.

#### Configuration
Configure in either `OntoWiki/application/config/default.ini` or `OntoWiki/libraries/Erfurt/library/Erfurt/config/default.ini`:

	worker.enable  = true
	worker.backend = "Gearman"
	worker.servers = "127.0.0.1:4730"

Fakts:
- Gearman is the only worker backend at the moment.
- Several servers can be enlisted separated by comma.
- You must set the port. Default port is 4730.

#### Integration in OntoWiki
First register the event `onAnnounceWorker` in the `doap.n3` file of a plugin, module or extension.
This is an example for a plugin:

	owconfig:pluginEvent event:onAnnounceWorker ;

Within the plugin class implement:

	public function onAnnounceWorker($event)
	{
		$event->registry->registerJob(
			"myJobName",                                    //  job key name
			"extensions/myPlugin/jobs/MyJobName.php",       //  job class file
			"MyPlugin_Job_MyJobName"                        //  job class name
		);
	}

The Erfurt worker backend will register your job class once it is started.<br/>
Now you need to implement your job class. Here is a simple example:

	class MyPlugin_Job_MyJobName implements Erfurt_Worker_Job_Interface {
		public function run( GearmanJob $job ){
			$workload   = $job->workload();                 //  extract job workload
			return strrev( $workload );                     //  reverse string and return
		}
	}
	
#### Worker execution
##### On the server 
Go into OntoWiki's application folder and run the worker script:

	cd OntoWiki/application
	php shell.worker.php &

Please keep in mind that this script will not quit since it will listen for new job calls.
Therefore the script is told to run in background (by the ampersand).

To stop or restart the worker, please kill the process and start the script again.

**Hint: For job accessing filesystem resources, it is important to run the script as a user which has access to the desired resources.**

##### On the client

You can call jobs for synchronous execution like this:

	$client		= Erfurt_Worker_Frontend::getInstance( $bootstrap->config );
	$result		= $client->call( "myJobName", "MyWorkloadData" );

Executing job asynchronously (in the background) can be done like this:

	$jobHandle	= $client->callAsync( "myJobName", "MyWorkloadData" );

Afterwards you can check the job status like this: 

	$state	= $client->isStillRunning( $jobHandle );

[1]: http://gearman.org/
[2]: http://gearman.org/getting_started
[3]: http://www.phpvs.net/2010/11/30/installing-gearman-and-gearmand-on-windows-with-cygwin/