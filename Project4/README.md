## Part 2 - Setup Load Balancing TODOs

Setup the following and add documentation or screenshots to your `README.md` file as specified.

1. Create an `/etc/hosts` OR `.ssh/config` file on each system that correlates hostnames to private IPs.
   * Description of how `.ssh/config` is configured:
      * each server has an entry in `.ssh/config` for both of the other servers. So the proxy will have:
```
Host webserver1
    HostName 10.0.1.11
    user ubuntu
    IdentityFile /home/ubuntu/private-key.pem

Host webserver2
        HostName 10.0.1.12
        user ubuntu
        IdentityFile /home/ubuntu/private-key.pem
```
   * Continuation of 1...
      * The other servers have an entry for the proxy using its private ip instead of its own entry.
      * In a real world application we may want to avoid using the same key for everything like we have in this example. Given that the webservers are meant to be backups for each other it seems like an unnecessary risk to have them accessible with the same exact admin key.
2. Document how to SSH in between the systems utilizing their private IPs.
   - ssh-ception (Inception). The ssh into the proxy is simple. We just use the public IP, username (ubuntu by default) and the private key. To ssh into any other system we can ssh from the proxy server into username@private-ip-address. ie. `ssh -i private-key.pem ubuntu@10.0.1.11` . Once the `.ssh/config` is in place we can ssh just with specified keyword like `ssh webserver1` or `ssh proxy`. As long as we are already on one of the servers and the private key and config file is set up correctly we're good to go!.
3. **_HAProxy configuration & documentation requirements_**
   - How to set up a HAProxy load balancer
     - What file(s) where modified & their location:
       -  /etc/haproxy/haproxy - has the config info for the proxy. I added details for the frontend and backend
     - What configuration(s) were set (if any)
```
frontend proxyfrontend
        bind 10.0.0.10:80
        default_backend myservers

backend myservers
        balance roundrobin
        server webserver1 10.0.1.11:80
        server webserver2 10.0.1.12:80
```
   - Continuation of 3...
     - How to restart the service after a configuration change
       - `sudo systemctl restart haproxy`
     - Resources used (websites)
       - https://www.haproxy.com/blog/the-four-essential-sections-of-an-haproxy-configuration/
       - https://www.haproxy.com/blog/haproxy-configuration-basics-load-balance-your-servers/
       - https://www.digitalocean.com/community/tutorials/how-to-use-haproxy-to-set-up-http-load-balancing-on-an-ubuntu-vps
4. **_Webserver 1 & 2 configuration & documentation requirements_**
   - How set up a webserver
     - What file(s) were modified & their location
       - Only /var/www/html/index.html was modified (replaced)
     - What configuration(s) were set (if any)
       - everything worked with the default apache2 configurations
     - Where site content files were located (and why)
       - Default location for content is in /var/www/html/ . index.html in that folder will show the homepage by default.
     - How to restart the service after a configuration change
       - sudo systemctl restart apache2
     - Resources used (websites)
       - I've messed around with some basic apache2 stuff before
5. From the browser, when connecting to the proxy server, take two screenshots.
   - one screenshot that shows content from "server 1"
![Server1 page](Server1-CEG3120-ITDesign.png)
   - one screenshot that shows content from "server 2"
![Server1 page](Server2-CEG3120-ITDesign.png)
6. (Optional) - link to your proxy so I can click it.
   - http://54.236.178.130/
