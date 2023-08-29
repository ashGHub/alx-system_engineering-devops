#setup nginx

package {
    'nginx':
    ensure => installed,
}

file {'/var/www/html/index.nginx-debian.html':
    content => 'Hello World!',
}

file_line {'configure redirection':
    path  =>  '/etc/nginx/sites-available/default',
    after =>  'server_name _;',
    line  =>  53,
    content => "location /redirect_me { return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4; }"
}

service {'nginx':
    ensure => running,
}