from ..main import hash_names


def test_hash_names():
    names = ['Alexey', 'Ivan', 'Petr']
    hashed_names = []

    for name in names:
        hashed_names.append(hash(name))

    assert hashed_names == hash_names(names)
