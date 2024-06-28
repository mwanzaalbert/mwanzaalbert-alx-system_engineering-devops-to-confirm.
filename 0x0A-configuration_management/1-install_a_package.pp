# installing flask using puppet from pip3
package { 'python3-pip':
  ensure => installed,
  provider => 'pip3',
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
  require => Package['python3-pip'],
}
