# Prerequisites

* A server with:
  * Debian 10
  * Access via SSH
  * Can log in as a non-privileged user and sudo
  * Public IP
* AWS Route 53 zone and credentials (optional, see instructions below for running without Route 53)

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

Set up DNS:

```
$ ./ansible-playbook -K -e @vars.yml dns.yml
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

# Backups

To create a backup, run the `ejabberd_backup` command as the `ejabberd` user, providing a target directory as the first argument.
The command creates the directory if it does not exist.
The directory will contain a dump of the PostgreSQL database and a copy of the uploads directory.

To restore, restore the PostgreSQL dump and restore uploads to `/opt/ejabberd/upload/`.

# Running without using AWS Route 53 as the DNS provider

From the steps above:

* In `vars.yml`, do not set up `dns_aws_zone` nor `acme_email`.
* Do not set up AWS credentials.
* Do not execute the `certs.yml`, `dns.yml` playbooks.
* Create the following DNS records:

```
_xmpp-server._tcp.{{ xmpp_domain }} SRV 0 0 5269 {{ public_ip }}
_xmpp-client._tcp.{{ xmpp_domain }} SRV 0 0 5222 {{ public_ip }}
_stun._udp.{{ xmpp_domain }}        SRV 0 0 3478 {{ public_ip }}
_stun._tcp.{{ xmpp_domain }}        SRV 0 0 3478 {{ public_ip }}
_stuns._tcp.{{ xmpp_domain }}       SRV 0 0 5349 {{ public_ip }}
_turn._udp.{{ xmpp_domain }}        SRV 0 0 3478 {{ public_ip }}
_turn._tcp.{{ xmpp_domain }}        SRV 0 0 3478 {{ public_ip }}
_turns._tcp.{{ xmpp_domain }}       SRV 0 0 5349 {{ public_ip }}
```

Replacing `{{ xmpp_domain }}` with your XMPP domain and `{{ public_ip }}` with your host's public IP address.

Obtain a valid certificate for `{{ xmpp_domain }}` and `xmpp-upload.{{ xmpp_domain }}` and drop the full chain and private key at:

* `/opt/ejabberd/conf/fullchain.pem`
* `/opt/ejabberd/conf/privkey.pem`
