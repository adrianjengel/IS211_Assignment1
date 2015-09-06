#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Week 1 Assignment 1 Part 2"""


class Book(object):
    """A custom class."""

    def __init__(self, title, author):
        self.author = author
        self.title = title

    def display(self):
        """A function that displays the title and author of the book."""

        print "{}, written by {}.".format(self.title, self.author)


class Mice(Book):
    """A subclass of the Book class."""

    def __init__(self):
        Book.__init__(self, "Of Mice and Men", "John Steinbeck")


class Mockingbird(Book):
    """A subclass of the Book class."""

    def __init__(self):
        Book.__init__(self, "To Kill a Mockingbird", "Harper Lee")

if __name__ == "__main__":

    mice = Mice()
    mockingbird = Mockingbird()

    mice.display()
    mockingbird.display()
