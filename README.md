# Federated Real Time Communication Using Open Protocols

## Vision

Federated real-time communication using open protocols is possible and valuable.

## Mission

To deliver a simple mechanism to deliver a system that implements federated real-time communication using open protocols.

## Introduction

Whatsapp, Telegram, Facebook Messenger, iMessage, and others are heavily used nowadays for real-time communication (instant messaging, audio, video). All are under control of private companies.

Email is a federated, non-real-time, communication using open protocols. You can own your email address (by owning a domain name), and run your own service or use an email provider. You can transfer your data between different providers.

The same experience should be possible for real-time communications.

## Implementation

FRTCUOP will deliver Ansible playbooks that allow deploying a FRTCUOP system, and the necessary documentation for administrators, and users.

All FRTCUOP assets will be in the public domain.

FRTCUOP will be based in existing open source projects.

## Roadmap

## What's working

* XMPP server deployment, usable by the Conversations XMPP client, with the following features:
  * Instant messaging
  * Group messaging
  * Audio/video calls
  * Modern experience (push notifications, low battery usage, delivery/read receipts, etc.)

### Version 0

* Backup/restore, allowing the entire state of the FRTCUOP system to be stored in a file, and restoring an FRTCUOP system from such file
* Monitoring, creating Nagios plugins that can check the correct operation of the FRTCUOP system
* Automatic updates
* XMPP server deployment, usable by the Conversations XMPP client, with the following features:
  * Instant messaging
  * Group messaging
  * Audio/video calls
  * Federation
  * Modern experience (multiple device synchronization, inline multimedia, real-time location sharing, etc.)

### Version 1

* Web client for XMPP server, with the following features:
  * Instant messaging
  * Group messaging
  * Audio/video calls
  * Federation

### Version 2

* XMPP (Jingle)/SIP gateway, allowing the XMPP server to interoperate with an external SIP provider (for interoperation with hardware SIP phones and the PSTN)

### Version 3

* Room conference system ("TV mode", or using existing solutions)

### Version 4

* LDAP interoperation, allowing FRTCUOP to use an external LDAP server as an authentication and directory source

### Ideas

Those features are not part of the roadmap right now:

* Text/voice/video conference rooms
* Guest browser access (URLs to message/call an internal user, and join conference rooms)
* Call/conference recording
* Real-time transcription
* Internal PBX
* Whitelabelling/reselling/multitenancy/billing
* Bridging to additional services
* Clustering/high availability
* End-to-end encryption
* Accessibility

However, the project could benefit from those features and would initially consider contributions to the project in those areas.
