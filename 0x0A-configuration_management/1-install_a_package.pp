# 1-install_a_package.pp

package { 'python3-pip':
<<<<<<< HEAD
  ensure   => installed,
  provider => 'pip3',
=======
  ensure => installed,
>>>>>>> 4cd5cf94aca6a1e93c76036eaac00a25deda1f8a
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  unless  => '/usr/bin/pip3 show flask | grep Version | grep -q 2.1.0',
  require => Package['python3-pip'],
}

<<<<<<< HEAD
=======
exec { 'create_symlink_for_flask':
  command => '/usr/bin/ln -sf /usr/local/bin/flask /usr/bin/flask',
  unless  => '/usr/bin/test -L /usr/bin/flask',
  require => Exec['install_flask'],
}
>>>>>>> 4cd5cf94aca6a1e93c76036eaac00a25deda1f8a
