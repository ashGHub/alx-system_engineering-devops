# Fix holberton user file limit

exec { 'update-holberton-limits':
  command => 'sed -i "/holberton hard/s/5/50000/; /holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin:/bin'
}
