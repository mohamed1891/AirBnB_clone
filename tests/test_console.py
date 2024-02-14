#!/usr/bin/python3

# Import the modules
import unittest
from unittest.mock import patch
from console import HBNBCommand  # Import the HBNBCommand class from your console module
import io


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.HBNBCommand = HBNBCommand()
        self.console_output = io.StringIO()
        self.HBNBCommand.stdout = self.console_output
    
    def tearDown(self):
        self.HBNBCommand = None
        self.console_output = None
        
    def test_emptyline(self):
        self.HBNBCommand.emptyline()
        self.assertEqual(self.console_output.getvalue(), '')
        
    def test_do_quit(self):
        self.assertTrue(self.HBNBCommand.do_quit(''))
        
    def test_do_EOF(self):
        self.assertTrue(self.HBNBCommand.do_EOF(''))
        
    def test_create(self):
        with patch('sys.stdout', new=self.console_output) as stdout_mock:
            self.HBNBCommand.onecmd("create BaseModel")
            output = stdout_mock.getvalue()
            self.assertGreater(len(output), 0)
            self.assertIsInstance(output, str)
            self.assertIn("BaseModel", output)
            self.assertIn("created", output)
            self.assertIn("uuid", output)
        
    def test_show(self):
        with patch('sys.stdout', new=self.console_output) as stdout_mock:
            self.HBNBCommand.onecmd("create BaseModel")
            self.HBNBCommand.onecmd("show BaseModel <id>")
            output = stdout_mock.getvalue()
            self.assertGreater(len(output), 0)
            self.assertIsInstance(output, str)
            self.assertIn("BaseModel", output)
            self.assertIn("<id>", output)
            self.assertIn("created", output)
            self.assertIn("uuid", output)
        
    def test_destroy(self):
        with patch('sys.stdout', new=self.console_output) as stdout_mock:
            self.HBNBCommand.onecmd("create BaseModel")
            self.HBNBCommand.onecmd("destroy BaseModel <id>")
            output = stdout_mock.getvalue()
            self.assertGreater(len(output), 0)
            self.assertIsInstance(output, str)
            self.assertIn("BaseModel", output)
            self.assertIn("<id>", output)
            self.assertIn("destroyed", output)
        
    def test_all(self):
        with patch('sys.stdout', new=self.console_output) as stdout_mock:
            self.HBNBCommand.onecmd("create BaseModel")
            self.HBNBCommand.onecmd("all BaseModel")
            output = stdout_mock.getvalue()
            self.assertGreater(len(output), 0)
            self.assertIsInstance(output, str)
            self.assertIn("BaseModel", output)
            self.assertIn("<id>", output)
            self.assertIn("created", output)
            self.assertIn("uuid", output)
    
    def test_update(self):
        with patch('sys.stdout', new=self.console_output) as stdout_mock:
            self.HBNBCommand.onecmd("create BaseModel")
            self.HBNBCommand.onecmd("update BaseModel <id> name Abby")
            output = stdout_mock.getvalue()
            self.assertGreater(len(output), 0)
            self.assertIsInstance(output, str)
            self.assertIn("BaseModel", output)
            self.assertIn("<id>", output)
            self.assertIn("updated", output)
            self.assertIn("name", output)
            self.assertIn("Abby", output)
if __name__ == '__main__':
    unittest.main()
