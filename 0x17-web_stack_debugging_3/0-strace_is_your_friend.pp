# Web-stack debugging script in puppet
exec { 'wsd3':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/' /var/www/html/wp-settings.php",
  path    =>  ['/bin', '/usr/bin']
}


server {     
    listen 80;      
    listen [::]:80;      
    server_name http://BANQUE_AGRICOLE_IPRES_FRONT_END.com;      
    root /var/www/BANQUE_AGRICOLE_IPRES_FRONT_END/dist/LBA;   
    server_tokens off;   
    index index.html index.htm;     
 
    location / {         
        # First attempt to server request as file, then         
        # as directory, then fall back to displaying a 404.          
        try_files $uri $uri/ /index.html =404;      
    }
}
