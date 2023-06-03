#Using Puppet, create a manifest that kills a process named killmenow

exec { 'killemenow':
	command => 'pkill killmenow',
	path => '/usr/local/bin/:/usr/bin:/bin/',
}
