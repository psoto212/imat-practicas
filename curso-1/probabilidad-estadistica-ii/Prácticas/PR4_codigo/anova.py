#!/usr/bin/env python

__author__ = "Francisco Rodríguez Cuenca, Universidad Pontificia Comillas"
__status__ = "Prototype"

"""
Anova functions for one and two factors with interaction options and integrated means model
"""

import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import itertools as it
import scipy
import re

def anova1(formula: str, df: pd.DataFrame):
    """
    Receives a dataframe and the formula
    Returns the means model and the anova table, as well as the dummy table with the dependent variable included
    """

    # Ordinary Least Squares -> ols
    model = ols(formula, df).fit()

    # Generación de la tabla
    aov_table = anova_lm(model)

    # Identificación de la variable dependiente
    y_name = model.summary2().tables[0][1][1]

    # Identificación del factor
    factor_name = re.findall(r'C\((.*?)\)',formula)[0]

    # Cálculo de mu y resta sobre la variable dependiente

    y = np.array(df[y_name])
    mu = y.mean()
    y = y-mu

    # Calculo de dmat y cmat
    
    dummies = pd.get_dummies(df[factor_name], columns = factor_name)
    dummies.insert(0, 'constant', 1)
    dmat = np.array(dummies)

    cmat = np.ones((1, len(dummies.columns)))
    cmat[0][0] = 0

    # Cálculo del modelo de medias

    # Find the null space of the constraints matrix

    Qc,Rc = scipy.linalg.qr(cmat.T)
    pc = np.linalg.matrix_rank(Rc)
    Qc0 = Qc[:,pc:]

    # Do qr decomposition on design matrix projected to null space
    Dproj = np.dot(dmat, Qc0)
    Qd,Rd,Ed = scipy.linalg.qr(Dproj, mode = "economic", pivoting=True)
    del Dproj
    dfx = np.linalg.matrix_rank(Rd)
    Qd = Qd[:,:dfx]
    Rd = Rd[:dfx,:dfx]

    # Fit y to design matrix in null space
    y2 = np.dot(Qd.T, y) # rotate y into that space
    zq, _ , rank , _ = np.linalg.lstsq(Rd, y2, rcond=None)       # fit rotated y to projected design matrix

    z = np.zeros([len(Ed),1]) # coefficient vector extend to full size ...
    z[Ed[:dfx]] = zq.reshape(rank,-1)      # ... and in correct order for null space

    b = np.dot(Qc0, z)             # coefficients back in full space
    b[0] = mu + b[0]

    meansmodel = pd.DataFrame(data = b, index=dummies.columns, columns = ["Mean"])

    return aov_table, meansmodel

def anova2(formula: str, df: pd.DataFrame):
    """
    Receives a dataframe and the formula
    Returns the means model and the anova table, as well as the dummy table with the dependent variable included
    """

    # Ordinary Least Squares -> ols
    model = ols(formula, df).fit()

    # Generación de la tabla
    aov_table = anova_lm(model)

    # Identificación de la variable dependiente
    y_name = model.summary2().tables[0][1][1]

    # Identificación del factor
    factor_names = re.findall(r'C\((.*?)\)',formula)

    #Identificación de si hay interacción
    interaction = False
    if("*" in formula):
        interaction = True

    # Cálculo de mu y resta sobre la variable dependiente

    y = np.array(df[y_name])
    mu = y.mean()
    y = y-mu

    # Calculo de dmat y cmat
    
    dummies = pd.get_dummies(df[factor_names], columns = factor_names)
    dummies.insert(0, 'constant', 1)

    if interaction:
        cols = np.logical_or.reduce([dummies.columns.str.startswith(f) for f in factor_names]) # columnas de dummies (factores)
        inter_df = pd.get_dummies(dummies.loc[:,cols].apply(lambda a: a.tolist(), axis=1).apply(lambda a: int("".join(str(x) for x in a), 2)))
        inter_df = inter_df.reindex(sorted(inter_df.columns, reverse=True), axis=1)
        dmat = pd.concat([dummies, inter_df], axis=1)
    else:
        dmat = np.array(dummies)

    cmat = np.array([dummies.columns.str.startswith(f) for f in factor_names]).astype("int")

    if interaction:
        nterms = [sum(a) for a in cmat]
        matrixs = [np.rot90(np.identity(n), k = 1) for n in nterms]
        combinations = np.array([np.concatenate(res) for res in it.product(*matrixs)])
        cmat1 = np.rot90(combinations, k = 1)
        cmat = scipy.linalg.block_diag(cmat, cmat1)

    # Cálculo del modelo de medias

    # Find the null space of the constraints matrix

    Qc,Rc = scipy.linalg.qr(cmat.T)
    pc = np.linalg.matrix_rank(Rc)
    Qc0 = Qc[:,pc:]

    # Do qr decomposition on design matrix projected to null space
    Dproj = np.dot(dmat, Qc0)
    Qd,Rd,Ed = scipy.linalg.qr(Dproj, mode = "economic", pivoting=True)
    del Dproj
    dfx = np.linalg.matrix_rank(Rd)
    Qd = Qd[:,:dfx]
    Rd = Rd[:dfx,:dfx]

    # Fit y to design matrix in null space
    y2 = np.dot(Qd.T, y) # rotate y into that space
    zq, _ , rank , _ = np.linalg.lstsq(Rd, y2, rcond=None)       # fit rotated y to projected design matrix

    z = np.zeros([len(Ed),1]) # coefficient vector extend to full size ...
    z[Ed[:dfx]] = zq.reshape(rank,-1)      # ... and in correct order for null space

    b = np.dot(Qc0, z)             # coefficients back in full space
    b[0] = mu + b[0]

    if interaction:
        columns = list(dummies.columns[1:])
        result = [[i for i in columns if i.startswith(f)] for f in factor_names]
        c = it.product(*result,repeat=1)
        comb = list(map(lambda a: f"{a[0]} : {a[1]}", c))
        cols = list(dummies.columns)+comb
        meansmodel = pd.DataFrame(data = b, index=cols, columns = ["Mean"])
    else:
        meansmodel = pd.DataFrame(data = b, index=dummies.columns, columns = ["Mean"])

    return aov_table, meansmodel




