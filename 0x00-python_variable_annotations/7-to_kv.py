#!/usr/bin/env python3
"""
a function that converts a Python variable to a KV
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Convert a Python variable to a KV pair."""
    return k, v ** 2
