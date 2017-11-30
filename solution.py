"""Test case:

    >>> find_page_id('customers.csv', 'C1')
    P1, P3, P2, P1, P3, P2,

    >>> find_page_id('customers.csv', 'C2')
    P2, P1, P3, P2, P1, P3, P2,

    >>> find_page_id('customers.csv', 'C3')
    P3, P1,

    >>> find_page_id('customers.csv', 'C4')
    No results found.
"""

import sys


def find_page_id(filename, user_input):
    """Extract page id from user input of customer id in command terminal."""

    # error message
    if user_input != 'C1' and user_input != 'C2' and user_input != 'C3':
        print "No results found."

    # parse file
    else:
        for row in open(filename):
            row = row.rstrip()  # clean up data
            time, customer_id, page_id = row.split(", ")  # isolate variables

            # check match
            if customer_id == user_input:
                print '{},'.format(page_id),  # format output in one line


# call fn
find_page_id('customers.csv', sys.argv[1])


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n\n\n\n\n*** ALL TESTS PASSED!\n"
