# -*- coding: utf-8 -*-
"""Copy of eclat.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CsaaCvHPo89fDdmsGbXdiXoo64sM0lNB

# Eclat

## Importing the libraries
"""

!pip install pyECLAT

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Data Preprocessing"""

from pyECLAT import Example1, Example2
ex1 = Example1().get()
ex2 = Example2().get()

ex1

ex2

"""## Training the Eclat model on the dataset"""

from pyECLAT import ECLAT
eclat_instance = ECLAT(data=ex1, verbose=True)

eclat_instance.df_bin   #generate a binary dataframe, that can be used for other analyzes.
eclat_instance.uniq_    #a list with all the names of the different items

get_ECLAT_indexes, get_ECLAT_supports = eclat_instance.fit(min_support=0.08,
                                                           min_combination=1,
                                                           max_combination=3,
                                                           separator=' & ',
                                                           verbose=True)

"""## Visualising the results"""

get_ECLAT_indexes

get_ECLAT_supports

