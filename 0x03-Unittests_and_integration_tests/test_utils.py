#!/usr/bin/env python3
"""
Unit tests for utils.access_nested_map function.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


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


class TestGetJson(unittest.TestCase):
    """
    Test suite for the get_json function in utils mode
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test that get_json that returns the expected payload

        Args:
            test_url (str): The URL to be requested.
            test_payload (dict): The expected JSON payload.

        Asserts:
            - requests.get is called once with test_url.
            - get_json returns test_payload.
        """

        # Configure the mock to return a response with a JSON payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call get_json with the test URL and verify the output
        result = get_json(test_url)
        self.assertEqual(result, test_payload)

        # Check that requests.get was called once with the correct URL
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Tests the `memoize` function."""

    def test_memoize(self) -> None:
        """Tests `memoize`'s output."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
        ) as memo_fxn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_fxn.assert_called_once()


if __name__ == "__main__":
    unittest.main()
