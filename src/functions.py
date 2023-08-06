from src.dependencies import *
def combine_dataframes(dfs):
    """The combine_dataframes function takes a list of dataframes as input and concatenates them into a single dataframe.

    Args:

    dfs: a list of pandas dataframes to be combined
    Returns:

    combined_df: a single pandas dataframe with all the rows from the input dataframes
    The function iterates through each dataframe in the input list,
    and uses the append() method to concatenate it to the previously combined dataframe.
    It also sets ignore_index=True to ensure that the row indexes are reset in the final dataframe.
    Finally, it returns the concatenated dataframe."""
    combined_df = pd.DataFrame()  # create an empty dataframe to start with
    for df in dfs:
        combined_df = combined_df.append(df, ignore_index=True)  # append the rows of the current dataframe to the previous one
    return combined_df