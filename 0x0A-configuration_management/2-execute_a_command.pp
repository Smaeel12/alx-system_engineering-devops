# Using Puppet, create a manifest that kills a process named killmenow.
# Using exec Puppet resource
# Using pkill

exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin/'
}
