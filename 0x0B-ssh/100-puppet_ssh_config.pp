# Ensure the ssh directory exists
file { '~/.ssh':
  ensure => directory,
  mode   => '0700',
  owner  => $USER,
  group  => $USER,
}

# Set the IdentityFile in SSH config
file_line { 'Declare identity file':
  path  => '~/.ssh/config',
  line  => 'IdentityFile ~/.ssh/school',
  match => '^IdentityFile',
}

# Refuse to authenticate using a password
file_line { 'Turn off passwd auth':
  path  => '~/.ssh/config',
  line  => 'PasswordAuthentication no',
  match => '^PasswordAuthentication',
}

# Ensure the config file has the correct permissions
file { '~/.ssh/config':
  ensure => file,
  mode   => '0600',
  owner  => $USER,
  group  => $USER,
}

