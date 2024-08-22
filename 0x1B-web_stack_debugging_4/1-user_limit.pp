# A puppet script
exec { 'fixing the security file':
  command => "sed -i -E 's/(holberton (hard|soft) nofile )[0-9]+/1-1/' etc/security/limits.conf",
  path    => ['/bin/', '/usr/bin/']
}
