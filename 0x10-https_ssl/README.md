This is a readme file for https ssl

How to create ssl using [certbot](https://certbot.eff.org/instructions?ws=haproxy&os=ubuntufocal)

Steps:
-----
1. SSH to the haproxy server
2. Install snapd `sudo apt install snapd`
3. Install cerbot <br>
You may need to stop the haproxy server service <br>
`sudo snap install --classic certbot`
<br> for domain name, give it the haproxy server domain name
4. Automatic renewal <br>
`sudo certbot renew --dry-run`
5. Create new PEM file by joing public key and private key <br>
`sudo cat /etc/letsencrypt/live/lb-01.ashalx.tech/fullchain.pem /etc/letsencrypt/live/lb-01.ashalx.tech/privkey.pem | sudo tee /etc/letsencrypt/live/lb-01.ashalx.tech/alx.pem`
6. Configure Haproxy config file