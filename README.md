# Chef - CampusHash Events Framework #

Chef is a full-fledged event framework to be used at [CampusHash](http://campushash.com) events - workshops and hackathons. It runs on a local server during the events, to which the participants can connect. It is basically aimed at solving the problem of annoyingly low-speed internet connections during events at most colleges. Chef will provide the participants everything that they may need during an event, and more.

## Features ##

### Registration ###

Attendee registration and UEID (Unique Event ID) generation.

### Broadcast ###

Speaker-level push broadcasts to all connected participants. This can be used to quickly share code-snippets or other important information to the participants.

### Intra-event Chat ###

IRC-styled chat board. Participants can use it for conversations.

### Offline Docs ###

Local copy of docs of all the technologies involved in the events. And more. This comes with a search engine.

### Browser IDE ###

Full-fledged IDE in your browser.

### Downloadable data ###

At the end of the event, the participants can download all the relevant data - broadcasts, chats, code, docs - nicely packed and served.

## Technology ##

### Server ###

- [Flask Microframework](http://flask.pocoo.org/) for server-side logic
	- [Juggernaut](http://flask.pocoo.org/snippets/80/) for real-time pushes
- [PostgreSQL](www.postgresql.org) database, primarily

### Client ###

- [Twitter Bootstrap](http://getbootstrap.com/) for UI
- [AngularJS](http://angularjs.org/) for front-end magic
- [socket.io](http://socket.io/) for real-time pushes