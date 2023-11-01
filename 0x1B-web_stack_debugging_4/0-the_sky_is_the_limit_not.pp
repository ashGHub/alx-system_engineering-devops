# Fix file limits for nginx

exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin'
}

exec { 'nginx-restart':
  command => 'service nginx restart',
  path    => '/usr/sbin:/usr/bin:/sbin:/bin',
  require => Exec['fix--for-nginx'],  # Ensure the configuration update has happened before restarting
}
