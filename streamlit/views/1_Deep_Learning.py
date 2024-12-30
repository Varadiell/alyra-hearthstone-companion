import streamlit as st
import pandas as pd
import requests

# Initialize session state for cards in deck if not already present
if 'cards_in_deck' not in st.session_state:
    st.session_state.cards_in_deck = []

if 'card_to_add' not in st.session_state:
    st.session_state.card_to_add = None

if 'predicted_deck_archetype' not in st.session_state:
    st.session_state.predicted_deck_archetype = None

def predict_deck_archetype():
    st.session_state.predicted_deck_archetype = None
    archetype = requests.get("http://127.0.0.1:8000/deep/predict", json={"cards": st.session_state.cards_in_deck})
    st.session_state.predicted_deck_archetype = archetype.json()['archetype']

# Function to add the selected card to the deck and reset the selectbox
def add_card_to_deck():
    st.session_state.predicted_deck_archetype = None
    if st.session_state.card_to_add and st.session_state.card_to_add not in st.session_state.cards_in_deck:
        st.session_state.cards_in_deck.append(st.session_state.card_to_add)
    # Reset the selectbox by clearing the session state value
    st.session_state.card_to_add = None

# Function to reset the deck
def reset_deck():
    st.session_state.cards_in_deck = []
    st.session_state.predicted_deck_archetype = None

# Page Config
st.title("Deep Learning")

# Columns
col1, col2 = st.columns(2)

# Read cards data
card_names_df = pd.read_csv('data/card_names.csv').sort_values(by=['card_name'], ignore_index=True)

# Col1 - Card Selection
col1.subheader("Cards", divider="blue")

# Reset key by specifying key='card_to_add' and relying on session_state reset
card_to_add = col1.selectbox(
    "Select a card",
    card_names_df['card_name'],
    index=None,
    placeholder="Select a card to add to your deck...",
    key='card_to_add' # Link selectbox to session state key
)

col1.button(
    "Add card to deck",
    icon="➕",
    on_click=add_card_to_deck,
    disabled=st.session_state.card_to_add is None
)

# Col2 - Display Current Deck
col2.subheader("Deck", divider="blue")
col2.write(st.session_state.cards_in_deck)
if len(st.session_state.cards_in_deck) == 0:
    col2.write("No cards in the deck yet.")
else:
    col2.button(
        "Reset Deck",
        icon="🗑️",
        on_click=reset_deck
    )

st.subheader("Prediction", divider="blue")
if len(st.session_state.cards_in_deck) < 5:
    st.write("Not enough cards in deck to predict deck archetype (min. 5 cards).")
else:
    if st.session_state.predicted_deck_archetype:
        st.write(f"Predicted deck archetype: :red[{st.session_state.predicted_deck_archetype}]")
    st.button(
        "Predict deck archetype",
        icon="🔮",
        on_click=predict_deck_archetype
    )
