"""Tests for fast-json-transform."""

import pytest
from fast_json_transform import transform


class TestTransform:
    """Test suite for transform."""

    def test_basic(self):
        """Test basic usage."""
        result = transform("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            transform("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = transform(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
