# This Puppet script installs and configures an Nginx server with a root page and a 301 redirect.

# Ensure the Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Ensure the Nginx service is running and enabled
service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  require    => Package['nginx'],
}

# Create the root index.html with "Hello World!" content
file { '/var/www/html/index.html':
  ensure  => file,
  content => '<html><body>Hello World!</body></html>',
  require => Package['nginx'],
}

# Configure Nginx server block
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Template for the Nginx default site configuration
file { '/etc/puppetlabs/code/environments/production/modules/nginx/templates/default.erb':
  ensure  => file,
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html;

    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location = /redirect_me {
        return 301 http://\$host/;
    }
}
",
  require => Package['nginx'],
}

# Ensure the default site is enabled
exec { 'enable-nginx-default-site':
  command     => '/usr/sbin/nginx -s reload',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
}
