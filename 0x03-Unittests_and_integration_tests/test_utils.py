#!/usr/bin/env python3
"""
Unit tests for utils.access_nested_map function.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test suite for the access_nested_map function in utils module.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: dict, path: tuple,
                               expected: object) -> None:
        """
        Test that access_nested_map returns the correct value for valid keys.

        Args:
            nested_map (dict): Dictionary representing a nested map.
            path (tuple): Tuple of keys to navigate through the nested map.
            expected (object): Expected value from accessing the nested map.

        Asserts:
            The value returned by access_nested_map matches the expected value
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map: dict,
                                         path: tuple) -> None:
        """
        Test that access_nested_map raises a KeyError for invalid keys.

        Args:
            nested_map (dict): Dictionary representing a nested map.
            path (tuple): Tuple of keys to navigate through the nested map.

        Asserts:
            A KeyError raised when the path does not exist in the nested map
            The error message includes the missing key.
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(str(e.exception), f"'{path[-1]}'")


if __name__ == "__main__":
    unittest.main()
