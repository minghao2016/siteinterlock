import os
import sys


def mean(lst):
    n = len(lst)
    if not n:
        return None
    return sum(lst) / float(n)


def variance(lst, mu=None):
    n = len(lst)
    if not n:
        return None
    if mu is None:
        mu = mean(lst)
    dev = sum([((i - mu)**2) for i in lst])
    return dev / float(n)


def std_dev(lst, mu=None):
    return variance(lst, mu=mu)**0.5


def standardize(lst):
    mu = mean(lst)
    sigma = std_dev(lst, mu=mu)
    z = [(i - mu) / sigma for i in lst]
    return z
