#!/usr/bin/python3
"""
test_city module
"""
from unittest import TestCase
from models.engine.file_storage import FileStorage
import pycodestyle
from models.city import City
from datetime import datetime


class TestCity(TestCase):
    """
    TestCity class
    """

    def test_pep(self):
        """test pep"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py',
                                    'tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_doc(self):
        """test module documentation"""
        doc = __import__('models.city').__doc__
        self.assertGreater(len(doc), 1)

    def test_class_doc(self):
        """test class documentation"""
        doc = City.__doc__
        self.assertGreater(len(doc), 1)

    def test_city_attributes(self):
        """test city attributes"""
        city = City()
        self.assertIsInstance(city.name, str)
        self.assertIsInstance(city.id, str)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)

    def test_city_create(self):
        """test city create"""
        city = City()
        city.save()
        self.assertNotEqual(city.id, '')
        self.assertNotEqual(city.created_at, None)
        self.assertNotEqual(city.updated_at, None)

    def test_city_to_dict(self):
        """test city to dict"""
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertIn('id', city_dict)
        self.assertIn('created_at', city_dict)
        self.assertIn('updated_at', city_dict)
        self.assertIn('__class__', city_dict)

    def test_city_str(self):
        """test city string representation"""
        city = City()
        string = str(city)
        self.assertGreater(len(string), 1)
        self.assertIn(city.__class__.__name__, string)
        self.assertIn(city.id, string)

    def test_city_save(self):
        """test city save"""
        city = City()
        city.save()
        city_reload = City.from_dict(city.to_dict())
        self.assertEqual(city.id, city_reload.id)
        self.assertEqual(city.created_at, city_reload.created_at)
        self.assertNotEqual(city.updated_at, city_reload.updated_at)

    def test_city_delete(self):
        """test city delete"""
        city = City()
        city.save()
        city_id = city.id
        FileStorage().new(city)
        FileStorage().save()
        city.delete()
        with self.assertRaises(KeyError):
            City.from_dict(City.to_dict(city))
        with self.assertRaises(KeyError):
            FileStorage()._FileStorage__objects[city_id]

if __name__ == '__main__':
    unittest.main()
