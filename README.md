# Chef - CampusHash Events Framework #

Chef is a full-fledged event framework to be used at [CampusHash](http://campushash.com) events - workshops and hackathons. It runs on a local server during the events, to which the participants can connect. It is basically aimed at solving the problem of annoyingly low-speed internet connections during events at most colleges. Chef will provide the participants everything that they may need during an event, and more.

## Features ##

### Registration ###

Attendee registration and UEID (Unique Event ID) generation. All registrations would be synced to CampusHash central database.

### SlideCast ###

Attendees can screen-share the presentation on the speaker's computer. The presentations would be HTML-based, so they can be embedded in an UI-view on the Chef control panel. Use [Django-SocketIO](https://github.com/stephenmcd/django-socketio) for the implementation (maybe). This would eliminate the need for a projector during the event (hopefully).

### Broadcast ###

Speaker-level push broadcasts to all connected participants. This can be used to quickly share code-snippets or other important information to the participants.

### Intra-event Chat ###

IRC-styled chat board. Participants can use it for conversations.

### Notes ###

Take quick notes.

### Offline Docs ###

Local copy of docs of all the technologies involved in the events. And more. This comes with a search engine.

### Browser IDE ###

Full-fledged IDE in your browser.

### Downloadable data ###

At the end of the event, the participants can download all the relevant data - broadcasts, chats, code, docs - nicely packed and served.

## Technology ##

### Server ###

- [Django](http://djangoproject.com/) for server-side logic
	- [Tastypie](http://tastypieapi.org) for REST API
	- [Django-SocketIO](https://github.com/stephenmcd/django-socketio) for real-time
- [SQLite3](www.sqlite.org) for persistence

### Client ###

- [Twitter Bootstrap](http://getbootstrap.com/) for UI
- [AngularJS](http://angularjs.org/) for front-end magic
- [socket.io](http://socket.io/) for real-time