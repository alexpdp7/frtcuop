# Prerequisites

* A server with:
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
