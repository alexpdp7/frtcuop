# Prerequisites

* A server with:
  * Debian 10
  * Access via SSH
  * Can log in as a non-privileged user and sudo
  * Public IP
* AWS Route 53 zone and credentials

# Procedure

Create your venv:

```
$ ./setup-venv.py
```

Setup your host connection:

```
$ cp hosts.example hosts
$ $EDITOR hosts
```

Setup your vars:

```
$ cp vars.yml.example vars.yml
$ $EDITOR vars.yml
```

Test host connection:

```
$ ./ansible -K -m ping '*'
```

Setup AWS credentials:

```
$ export AWS_ACCESS_KEY_ID=...
$ export AWS_SECRET_ACCESS_KEY=...
```

Deploy:

```
$ ./ansible-playbook -K -e @vars.yml deploy.yml
```

Create and deploy certs (or renew):

```
$ ./ansible-playbook -K -e @vars.yml certs.yml
```

Create users:

```
$ ssh your_server
$ sudo /opt/ejabberd-21.04/bin/ejabberdctl register user1 <domain> user1
```

# Monitoring

Using https://github.com/alexpdp7/ragent and standard Nagios checks:

```
$ /usr/lib64/nagios/plugins/check_ping -H <ip> -w 200,25% -c 400,45%
$ /usr/lib64/nagios/plugins/check_ssh <ip>
$ /usr/lib64/nagios/plugins/check_http -H <ip> -p 5443 --ssl -e 404
$ /usr/lib64/nagios/plugins/check_http -H <ip> -p 5443 --ssl -e 404 -C 7,14

# might fail on some providers until the server is rebooted, due to issues with cloud-init
$ /usr/bin/check_ragent http://<ip>:21488/

# TODO: check TLS
$ /usr/lib64/nagios/plugins/check_jabber <ip>
```
