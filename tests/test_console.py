#!/usr/bin/python3
"""
test_console module
"""
from unittest import TestCase
from console import HBNBCommand


class TestHBNBCommand(TestCase):
    """
    TestHBNBCommand class
    """

    def setUp(self):
        """
        Set up the test environment
        """
        self.console = HBNBCommand()

    def tearDown(self):
        """
        Tear down the test environment
        """
        try:
            del self.console
        except:
            pass

    def test_pep8(self):
        """
        Test that the code follows PEP8 style guide
        """
        pep8style.check_files(['console.py'])

    def test_console_prompt(self):
        """
        Test that the console prompt is "(hbnb) "
        """
        self.assertEqual(self.console.prompt, "(hbnb) ")

    def test_do_quit(self):
        """
        Test that the "quit" command exits the console
        """
        self.console.onecmd("quit")

    def test_do_EOF(self):
        """
        Test that pressing Ctrl+D exits the console
        """
        with self.assertRaises(EOFError):
            self.console.onecmd("")

    def test_do_create(self):
        """
        Test that the "create" command creates a new instance of a class
        """
        self.console.onecmd("create BaseModel")

    def test_do_show(self):
        """
        Test that the "show" command displays an instance of a class
        """
        self.console.onecmd("create BaseModel")
        self.console.onecmd("show BaseModel 1234-1234-1234")

    def test_do_destroy(self):
        """
        Test that the "destroy" command deletes an instance of a class
        """
        self.console.onecmd("create BaseModel")
        self.console.onecmd("destroy BaseModel 1234-1234-1234")

    def test_do_all(self):
        """
        Test that the "all" command displays all instances of a class
        """
        self.console.onecmd("create BaseModel")
        self.console.onecmd("all BaseModel")

    def test_do_update(self):
        """
        Test that the "update" command updates an instance of a class
        """
        self.console.onecmd("create BaseModel")
        self.console.onecmd("update BaseModel 1234-1234-1234 name Abby")
