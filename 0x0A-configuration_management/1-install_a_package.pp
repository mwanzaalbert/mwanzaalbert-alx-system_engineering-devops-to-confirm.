# Puppet manifest to install Flask 2.1.0 using pip3
package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  unless  => '/usr/bin/pip3 show flask | grep Version | grep -q 2.1.0',
  require => Package['python3-pip'],
}

exec { 'create_symlink_for_flask':
  command => '/usr/bin/ln -sf /usr/local/bin/flask /usr/bin/flask',
  unless  => '/usr/bin/test -L /usr/bin/flask',
  require => Exec['install_flask'],
}
