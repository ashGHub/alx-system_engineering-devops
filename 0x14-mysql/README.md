This is a readme file for MySql installation on web server

# How to install mysql server 5.7

0. Setup MySQL GPG public key as Signature Checking<br>
i. `sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 467B942D3A79BD29` <br>
I added this keyId because it was showing me it could find the keyId
ii. `sudo apt-key adv --keyserver pgp.mit.edu --recv-keys 3A79BD29` <br>
For MySql 8.0.28 and higher release package: keyID is <b>3A79BD29</b><br>
For earlier releases (in our case 5.7) is 5072E1F5

1. Create <b>mysql.list</b> file <br>
`sudo vi /etc/apt/sources.list.d/mysql.list`
2. Add the following content to the file <br>
`deb http://repo.mysql.com/apt/ubuntu/ bionic mysql-5.7`<br>
Pick the relevant options for your repository set up: <br>
I. Choose “debian” or “ubuntu” according to your platform. <br>
II. Choose platform version/code name (bionic, focal, and so on).
<br>
MySql download doesn't have support for version 5.7 on focal, so went with bionic<br>
To know which ubuntu version code name you have run the code `lsb_release -a` <br>

3. Run<br>
`sudo apt-get update`
4. Install MySql <br>
`sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*`

# Add holberton_user with permission
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';

# Create replica_user with permission
CREATE USER 'replica_user'@'%' IDENTIFIED BY 'per_replica_web1';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

# Add select permission
GRANT SELECT ON mydatabase.mytable TO 'myuser'@'%';
