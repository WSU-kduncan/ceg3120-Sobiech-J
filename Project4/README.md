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
      * The other servers have an entry for the proxy using its private ip instead of its own entry.
      * In a real world application we may want to avoid using the same key for everything like we have in this example. Given that the webservers are meant to be backups for each other it seems like an unnecessary risk to have them accessible with the same exact admin key.
2. Document how to SSH in between the systems utilizing their private IPs.
   - ssh-ception (Inception). The ssh into the proxy is simple. We just use the public IP, username (ubuntu by default) and the private key. To ssh into any other system we can ssh from the proxy server into username@private-ip-address. ie. `ssh -i private-key.pem ubuntu@10.0.1.11` . Once the `.ssh/config` is in place we can ssh just with specified keyword like `ssh webserver1` or `ssh proxy`. As long as we are already on one of the servers and the private key and config file is set up correctly we're good to go!.
3. **_HAProxy configuration & documentation requirements_**
   - How to set up a HAProxy load balancer
     - What file(s) where modified & their location
     - What configuration(s) were set (if any)
     - How to restart the service after a configuration change
     - Resources used (websites)
4. **_Webserver 1 & 2 configuration & documentation requirements_**
   - How set up a webserver
     - What file(s) were modified & their location
     - What configuration(s) were set (if any)
     - Where site content files were located (and why)
     - How to restart the service after a configuration change
     - Resources used (websites)
5. From the browser, when connecting to the proxy server, take two screenshots.
   - one screenshot that shows content from "server 1"
   - one screenshot that shows content from "server 2"
6. (Optional) - link to your proxy so I can click it.
