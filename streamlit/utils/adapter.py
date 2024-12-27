import pandas as pd

def adapt_array_to_dataframe(card_array, dataframe):
    # Create an empty DataFrame with one row and the same columns as the existing DataFrame
    transformed_df = pd.DataFrame(0, index=[0], columns=dataframe.columns)
    # Set 1 for each card present in the array
    transformed_df.loc[0, [card for card in card_array if card in dataframe.columns]] = 1
    return transformed_df
