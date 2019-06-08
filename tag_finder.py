"""Utility functions for searching the tag table."""
import pandas as pd


def find_children(start_tag, tag_table):
    """
    Find all leaf nodes below start_tag in the tag_table.

    Search from the start tag and down through the tag tree, until ending up at
    children that have no children of their own. Return the combined Series of
    these children.

    Parameters
    ----------
    start_tag:  str
                The tag at the top of the tree
    tag_table:  DataFrame
                The full DataFrame of tags and their parent tags

    Returns
    -------
    int

    """
    pure_child = pd.Series([])
    parents = pd.Series([start_tag])
    while parents.shape[0] > 0:
        pure_child = pd.concat([pure_child,
                                parents[~parents
                                        .isin(tag_table['Parent'])]])
        parents = tag_table.loc[tag_table['Parent']
                                .isin(parents[parents
                                              .isin(tag_table['Parent'])]),
                                'Child']
    return pure_child
