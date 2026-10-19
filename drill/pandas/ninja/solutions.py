"""pandas ninja solutions: one function per challenge, in order of difficulty.

Each function gets the input table as df and must return the expected table.
Step 1. Run ninja.py <name> to see the input and expected tables.
Step 2. Replace ... with your pandas code and return a DataFrame.
Step 3. Run ninja.py <name> again until it prints PASS, then the next one.
Aim for one or two lines per challenge; leave ... to skip one.
"""

import numpy as np
import pandas as pd



def introduction(df: pd.DataFrame) -> pd.DataFrame:
    """easy: This first challenge show you how pandas ninja works. You must write a python code to transform a dataframe (top-right) into the expected dataframe (bottom-right). - The top-right dataframe is available as `df` variable. - The module pandas is already imported as `pd` variable. - Try to solve the problem with the minimum of expression with chaining. - The number of stars won, depends of the number of expression. - You cannot instantiate a pd.DataFrame or a pd.Series. - Ask for help on the discussion forum if you get stuck. In this challenge, you must show the first 3 lines. Uncomment the following line to resolve the challenge df = df.head(3)"""
    ...


def square_it(df: pd.DataFrame) -> pd.DataFrame:
    """easy: Create a new column y which is the square of x"""
    ...


def sort_it(df: pd.DataFrame) -> pd.DataFrame:
    """easy: Sort lines by power level"""
    ...


def replace(df: pd.DataFrame) -> pd.DataFrame:
    """easy: In `name` columns Repace "xx" by "of" df["name"] = ...."""
    ...


def replace_nan(df: pd.DataFrame) -> pd.DataFrame:
    """easy: Replace NaN values by 0 and sort line"""
    ...


def group_mean(df: pd.DataFrame) -> pd.DataFrame:
    """easy: Compute mean by variety"""
    ...


def clip(df: pd.DataFrame) -> pd.DataFrame:
    """easy: clip values between 0 and 20"""
    ...


def split_expand(df: pd.DataFrame) -> pd.DataFrame:
    """easy: Extract all columns"""
    ...


def explode(df: pd.DataFrame) -> pd.DataFrame:
    """medium: Duplicate line to have one fruit per line print(df)"""
    ...


def aggregate(df: pd.DataFrame) -> pd.DataFrame:
    """medium: Get first job for each user"""
    ...


def sort_date(df: pd.DataFrame) -> pd.DataFrame:
    """medium: Sort line by date from the oldest to the most recent"""
    ...


def pivot(df: pd.DataFrame) -> pd.DataFrame:
    """medium: Create a matrix with fruit count per user"""
    ...


def prevalence(df: pd.DataFrame) -> pd.DataFrame:
    """medium: filter users non 0 in at leat 3 columns"""
    ...


def split_and_combine(df: pd.DataFrame) -> pd.DataFrame:
    """hard: Split into 2 dataframe and combine them to fill -1 values"""
    ...


def groups_anonymisation(df: pd.DataFrame) -> pd.DataFrame:
    """hard: group families/ make anonym/ calculate n and mean wages"""
    ...


def reorder(df: pd.DataFrame) -> pd.DataFrame:
    """hard: reorder data to have 2 columns"""
    ...


def get_dummies(df: pd.DataFrame) -> pd.DataFrame:
    """hard: Convert categorical variable into dummy variables print(df)"""
    ...
