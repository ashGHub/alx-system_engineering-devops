# Define the directory where the HTML file should be placed
$document_root = '/var/www/html'
# Fix wordpress wrong file extension

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
