import pandas as pd

def adapt_array_to_dataframe(card_array, dataframe):
    # Create an empty DataFrame with the same columns as the existing DataFrame
    transformed_df = pd.DataFrame(0, index=range(len(card_array)), columns=dataframe.columns)
    # Iterate through each set of cards (each deck)
    for idx, cards in enumerate(card_array):
        # Set 1 for each card present in the array
        transformed_df.loc[idx, [card for card in cards if card in dataframe.columns]] = 1
    return transformed_df
