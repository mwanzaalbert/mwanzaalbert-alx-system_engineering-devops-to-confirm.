# Ensure the necessary package is installed
package { 'nginx':
  ensure => installed,
}

# Ensure the Nginx service is running and enabled at boot
service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
}

# Create the index.html file with "Hello World!" content
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}

# Ensure the directory for templates exists
file { '/etc/puppet/modules/nginx/templates':
  ensure => directory,
  owner  => 'root',
  group  => 'root',
  mode   => '0755',
}

# Template file for the default site configuration
file { '/etc/puppet/modules/nginx/templates/default.erb':
  ensure  => file,
  content => @("EOF"),
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }

    # Redirect /redirect_me to https://www.youtube.com/watch?v=QH2-TGUlwu4
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
}
  | EOF
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

# Configure Nginx to use the template
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

