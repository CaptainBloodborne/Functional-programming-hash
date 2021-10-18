from typing import List


def hash_names(names: List[str]) -> List[int]:
    """
    Take a list of strings and return the list of their hashes

    Parameters
    ----------
    names: List[str]
        List of strings to hash.

    Returns
    ---------
    List[int]
        List of hashes for strings from names param.
    """
    return list(map(hash, names))
