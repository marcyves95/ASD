# -*- coding: utf-8 -*-

"""
:mod:`test` module : test module for experiences assignment

:author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

:date: 2018, january
"""

import sys
import experience
import marker

def compare (m1,m2):
    return m1.cmp(m2)

# STRATEGY 1
def negative_markers1(markers,positive):
    """
    Computes the list of negative markers from the list of markers and
    the list of positive markers.

    :param markers: The list of markers
    :type markers: List of String
    :param positive: The list of positive markers
    :type positive: List of String
    :return: The list of negative markers
    :rtype: List of String
    """
    negative = []
    for i in positive:
        for j in markers:
            if compare(i,j) == 0:
                break
            else:
                if j in positive:
                    break
                elif j not in negative:
                
                    negative.append(j)
    return negative

# STRATEGY 2
def negative_markers2(markers,positive):
    negative = []
    return negative

# STRATEGY 3
def negative_markers3(markers,positive):
    negative = []
    return negative
        
if __name__ == "__main__":
    p = int(sys.argv[1])
    m = int(sys.argv[2])

    assert (m > 0), "The number of markers must be greater than 0"
    assert (p <= m), "The number of positive markers must be less or equal to the number of markers"
    
    exp = experience.Experience(p,m)
    markers = exp.get_markers()
    positive = exp.get_positive_markers()

    print("Markers: %s" % (markers))
    print("Positive markers: %s" % (positive))
    
    # test stategy 1
    cpt = 0
    print("Negative markers: %s" % (negative_markers1(markers,positive)))
    print("Nb. comparisons: %d" % (cpt))

##    # test stategy 2
##    cpt = 0
##    print("Negative markers: %s" % (negative_markers2(markers,positive)))
##    print("Nb. comparisons: %d" % (cpt))
##
##    # test stategy 3
##    cpt = 0
##    print("Negative markers: %s" % (negative_markers3(markers,positive)))
##    print("Nb. comparisons: %d" % (cpt))
