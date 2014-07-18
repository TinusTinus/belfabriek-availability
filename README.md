Belfabriek Availability
=======================

A script that checks for a team of [Belfabriek](http://www.belfabriek.nl) users, which of these users are currently available.

This Python script uses the [Belfabriek XMLRPC API](https://support.belfabriek.nl/forums/21983526-API-support).

Sample output:

```
Current time: 2014-07-18 22:02:55.840000

Name:         Alice
Extension id: 01234
Available:    1
Reason:       -
Extension:    31612345678

Name:         Bob
Extension id: 56789
Available:    0
Reason:       -
Extension:    31623456789

Name:         Carol
Extension id: 11111
Available:    1
Reason:       -
Extension:    31634567890
```

How to use
----------
* Make sure you have [Python](https://www.python.org/) (tested with version 2.7);
* download and extract the source zip, or just clone the repository;
* open belfabriek.py in your favourite text editor;
* replace the dummy account code by your actual Belfabriek account code;
* replace the dummy names and extension ids by your team members' actual names and extension ids;
* run the script.
