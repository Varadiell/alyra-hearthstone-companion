# How To

### A Quick Word

This project was created for the AI Developer Training at Alyra, to pass the certification.

### What Is This?

This is an "Hearthstone Companion" AI Tool that will help you classify deck archetypes, depending on what cards are included in the given decklist.

### Initialize the Project

Execute the following Jupyter Notebooks:
- analysis.ipynb
- extract_card_names.ipynb

The analysis exports a CSV file containing all Priest decks (only the most popular Priest class decks, to reduce the scope).

The extraction of card names is used in the Streamlit app to display all available card names in the selectbox input.

Next, train your model:
- train_logistic_regression.ipynb

A logistic regression model has been chosen for the Machine Learning component, but you can use any other model in the notebooks by tweaking the Streamlit app and changing the path to the model used.

You are now ready to launch the Streamlit app!

### Run the Streamlit App
```
$ streamlit run streamlit/app.py
```

### Deck Archetype Predictions

Select any card and ask the model to predict the deck archetype.

At least 5 cards are required to make a prediction.

Don't know anything about Hearthstone but want to try the app? Some example decklists are available in the `DECK_EXAMPLE.md` file.

### Screenshots

![image](https://github.com/user-attachments/assets/f37b81bf-93b2-436f-83a3-015988d75190)
