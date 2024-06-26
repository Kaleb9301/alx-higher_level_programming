#!/usr/bin/python3
"""
Contains the matrix_mul function
"""


def matrix_mul(m_a, m_b):
    """Multiply two Matrices.

        Args:
            m_a(list of lists ints/floats): The first matrix.
            m_b(list of lists of ints/floats): The second matrix
        Raise:
            TypeError: If m_a or m_b aren't a list
            TypeError: If m_a or m_b aren't a list of a lists
            TypeError: If either m_a or m_b is not a list of ints/floats.
            ValueError: If either m_a or m_b is empty.
            TypeError: If either m_a or m_b has different-sized rows.
            TypeError: If the rows of m_a  and m_b don't have the same size
            ValueError: If m_a and m_b cannot be multiplied.
        Returns:
            A new matrix representing the mulitplication of m_a by m_b.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for i in range(len(m_a)):
        if not isinstance(m_a[i], list):
            raise TypeError("m_a must be a list of lists")

    for i in range(len(m_b)):
        if not isinstance(m_b[i], list):
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[], []] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]] or m_b == [[], []]:
        raise ValueError("m_b can't be empty")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted_b = []
    for r in range(len(m_b[0])):
        new_row = []
        for c in range(len(m_b)):
            new_row.append(m_b[c][r])
        inverted_b.append(new_row)

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in inverted_b:
            prod = 0
            for i in range(len(inverted_b[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix
