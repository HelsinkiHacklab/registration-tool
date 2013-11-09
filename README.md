Helsinki Hacklab Registration Tool
==================================

Since it seems too hard to actually go through available things and setup a registration tool for Helsinki Hacklab,
we'll create new one instead. Idea behind this is that we are going to do it (very small) step by step. By keeping
individual steps very small, progressing the effort is made as easy as possible. Hopefully thus enabling participation.

Development model
-----------------
I got idea for this when reading [Test-Driven Web Development with Python](http://chimera.labs.oreilly.com/books/1234000000754/).
I combined its way to develop tests with idea I've been using in [Agile-Tools](https://github.com/jautero/Agile-Tools)
where I list requirements in `README.mdown`. 

Model is that people write on this file short description of a feature they want on this file. Anyone can pick one of
those descriptions and start writing **functional test** for it. She (In this document "she" is used as gender-neutral
pronoun meaning "he or she" because sometimes it's good to look at things from different point-of-view.) can write as
large or small part of the test as she likes, but usually the amount should be as small as possible.

When there is enough **functional test** to test code, anyone can start developing code with **TDD** writing **unit
tests**. The idea of this model is that it is easy to do something when that *something* is as little as possible. This
also enables participation because all you need to know is in [this
repository](https://github.com/HelsinkiHacklab/registration-tool). This also also conflict resolution method. **Code
only exists when it has been pulled into HelsinkiHacklab repository.** Everyone is free to pick any tool or framework as
need arises. Pull requests are good place to have arguments about right amount of spaces or correct JavaScript framework.

Requirements
============

Registration
------------
As a user I want to provide my email address in order to register to the course.
