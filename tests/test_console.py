#!/usr/bin/python3

# Import the modules
import unittest
from unittest.mock import patch
from console import HBNBCommand
from models.base_model import BaseModel

# Define the TestHBNBCommand class
class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.hbnb_command = HBNBCommand()

    def tearDown(self):
        self.hbnb_command = None

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_EOF(self, mock_stdout):
        self.assertTrue(self.hbnb_command.do_EOF(''))
        self.assertEqual(mock_stdout.getvalue(), '\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_quit(self, mock_stdout):
        self.assertTrue(self.hbnb_command.do_quit(''))

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline(self, mock_stdout):
        self.hbnb_command.emptyline()
        self.assertEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        with patch('builtins.input', return_value='User'):
            self.hbnb_command.do_create('')
        self.assertIn('User', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show(self, mock_stdout):
        with patch('builtins.input', return_value='User'):
            self.hbnb_command.do_show('User')
        self.assertIn("** instance id missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy(self, mock_stdout):
        with patch('builtins.input', return_value='User'):
            self.hbnb_command.do_destroy('User')
        self.assertIn("** instance id missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_all(self, mock_stdout):
        self.hbnb_command.do_all('')
        self.assertIn('** class name missing **', mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
