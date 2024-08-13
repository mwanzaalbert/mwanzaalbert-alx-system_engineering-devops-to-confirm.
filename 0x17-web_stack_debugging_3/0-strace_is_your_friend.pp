# This Puppet manifest fixes permission issues for the WordPress PHP files

file { '/var/www/html/wp-settings.php':
  ensure => file,
  mode   => '0755',
  owner  => 'www-data',
  group  => 'www-data',
}

# Ensure the necessary PHP module is installed
package { 'php5-mysql':
  ensure => installed,
}

# Restart the Apache service to apply changes
service { 'apache2':
  ensure  => running,
  enable  => true,
  require => Package['php5-mysql'],
}
