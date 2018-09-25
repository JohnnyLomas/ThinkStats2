"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function
from collections import defaultdict

import numpy as np
import sys

import nsfg
import thinkstats2

def ReadFemResp2002(dct_file='2002FemResp.dct',
                    dat_file='2002FemResp.dat.gz'):
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    nsfg.CleanFemResp(df)
    return df

def ReadFemPreg2002(dct_file='2002FemPreg.dct',
                    dat_file='2002FemPreg.dat.gz'):            
	dct = thinkstats2.ReadStataDct(dct_file)
	df = dct.ReadFixedWidth(dat_file, compression='gzip')
	return df

def main(script):
	"""Tests the functions in this module.

	script: string script name
	"""
	resp2002 = ReadFemResp2002()
	print(resp2002.pregnum.value_counts(sort=True))
	CrazyPerson = resp2002[resp2002.pregnum==19]
	preg = ReadFemPreg2002()
	case19 = preg[preg.caseid==CrazyPerson.caseid[6528]]
	case19.nbrnaliv.sum()
	
	
	
	
	CasePreg = preg[preg.caseid == 6528]
	print(CasePreg.nbrnaliv[1])
	
	print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
