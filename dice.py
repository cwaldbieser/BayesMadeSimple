"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

from thinkbayes import Suite


class Dice(Suite):
    """Represents hypotheses about which die was rolled."""

    def Likelihood(self, data, hypo):
        """Computes the likelihood of the data under the hypothesis.

        hypo: integer number of sides on the die
        data: integer die roll
        """
        # write this method
        return 1


def main():
    suite = Dice([4, 6, 8, 12, 20])

    suite.Update(6)
    print('After one 6')
    suite.Print()

    for roll in [8, 7, 7, 5, 4]:
        suite.Update(roll)

    print('After more rolls')
    suite.Print()


if __name__ == '__main__':
    main()
