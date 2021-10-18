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
        List of hashes of strings from names param.

    Examples
    --------
    names = ['Alexey', 'Ivan', 'Petr']
    hash_names(names)
    [-6913778901462750956, 4044914442677255742, -8154646851311137882]
    """
    return list(map(hash, names))
