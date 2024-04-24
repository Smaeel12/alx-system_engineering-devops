# Using Puppet, install flask from pip3.
# Install flask
# Version 2.1.0

package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
}

package { 'werkzeug':
    ensure   => '2.1.1',
    provider => 'pip3',
}
