import joblib
import pandas as pd
from utils import adapter
from fastapi import FastAPI, HTTPException
from tensorflow import keras
from pydantic import BaseModel, Field

app = FastAPI()

class DeckList(BaseModel):
    cards: list[str] = Field(
        min_items=5,
        max_items=30,
        example=[
            "Duskbreaker",
            "Nightscale Matriarch",
            "Twilight Drake",
            "Cobalt Scalebane",
            "Bone Drake",
            "Wyrmguard"
        ]
    )

class DeckArchetype(BaseModel):
    archetype: str = Field(
        example="Dragon Priest"
    )

@app.get("/machine/predict")
async def predict_machine_learning(deck_list: DeckList) -> DeckArchetype:
    try:
        model = joblib.load('models/logistic_regression_model.pkl')
        df = pd.read_csv('data/priest_popular_archetype_decks.csv')
        df.drop(['deck_archetype'], axis=1, inplace=True)
        df.drop(df.index, inplace=True) # Drop all rows
        df = adapter.adapt_array_to_dataframe(
            card_array=deck_list.cards,
            dataframe=df
        )
        return DeckArchetype(archetype=model.predict(df)[0])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/deep/predict")
async def predict_deep_learning(deck_list: DeckList) -> DeckArchetype:
    try:
        model = keras.models.load_model('models/fnn_dense_layers_model.keras')
        encoder = joblib.load('models/fnn_dense_layers_encoder.pkl')
        df = pd.read_csv('data/priest_popular_archetype_decks.csv')
        df.drop(['deck_archetype'], axis=1, inplace=True)
        df.drop(df.index, inplace=True)  # Drop all rows to keep only the structure
        df = adapter.adapt_array_to_dataframe(
            card_array=deck_list.cards,
            dataframe=df
        )
        prediction = model.predict(df)
        predicted_class_index = prediction.argmax(axis=1)[0]
        archetype = encoder.inverse_transform([predicted_class_index])[0]
        return DeckArchetype(archetype=archetype)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
