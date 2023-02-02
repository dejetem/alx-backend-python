#!/usr/bin/env python3
"""a function that returns values with the appropriate types"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list of tuples with lenth"""
    return [(i, len(i)) for i in lst]
