SBitter
=======

SBitter is SBHX's Twitter clone.  We're writing many such clones using
various languages and frameworks for comparison, then tying them
together into a federated network that anyone can join.


Terminology
-----------

* A "SBitter" is a user of this unique and impressive service

* Each message is "SBit"

* The act of sending a message is known as "SBitting"

* If you sent a SBit, you "SBot" (past tense)


Competition
-----------

If this becomes a language/framework/technology competition, here are
some ideas for how each app should be scored:

* Speed (requests/second)

* SLOC (source lines of code)

* Scalability (performance under load v. not)

* Memory use (per request, both under load v. not)


Logical match-ups include _Rails v. Django_ for succinctness, and _Go
v. JavaScript/Node_ v. Clojure/Erlang/Scala/etc rated on speed and
scalability.


Federatedness
-------------

Why throw away perfectly good Twitter clones when we could instead
build a federated network out of them?

* We'll design and implement an API so that _anyone_, including fellow
  super-geeks and hackerspaces, can build their own compatible SBitter
  node and join in!

* Register, sign in, and SBit from SBHX's golang.sbitter.net (for
  example), but follow SBitters SBitting from their own independent
  server
