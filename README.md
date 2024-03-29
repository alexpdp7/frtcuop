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

See [DEPLOYING.md](DEPLOYING.md).

All FRTCUOP assets are in the public domain.

FRTCUOP is based in existing open source projects.

## Roadmap

## What's working

* XMPP server deployment, usable by the Conversations XMPP client, with the following features:
  * Instant messaging
  * Group messaging
  * Audio/video calls
  * Federation
  * Modern experience (push notifications, low battery usage, delivery/read receipts, inline multimedia, multiple device synchronization, etc.)
* Monitoring
* Compatible with Movim servers (tested with https://chatterboxtown.us/)
* Automatic updates
* Backup/restore, allowing the entire state of the FRTCUOP system to be stored in a directory, and restoring an FRTCUOP system from such directory

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
* Real-time location sharing (Conversations does not support this directly. You can use Google Maps to share your location- it provides a URL you can share through XMPP)

However, the project could benefit from those features and would initially consider contributions to the project in those areas.
