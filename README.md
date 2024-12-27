# How To

### Initialize the project

Execute the following Jupyter Notebooks:
- analysis.ipynb
- extract_card_names.ipynb

The analysis will export the csv file with all priest decks (only the most popular priest class decks in order to reduce the scope).

The extraction of card names is used in the streamlit app in order to display all available card names in the selectbox input.

Then, train your model:
- train_logistic_regression.ipynb

The logistic regression model has been chosen for the Machine Learning part, but you can use any other model in the notebooks if you tweak the streamlit app, by changing the path of the model used.

You are now ready to launch the streamlit app!

### Run the Streamlit app
```
$ streamlit run streamlit/app.py
```
