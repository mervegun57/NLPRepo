from pydantic import Json
from factory.database import Database
import spacy
from spacy import displacy
from spacy.lang.en.examples import sentences
import pandas as pd

class Deneme(object):
    def __init__(self):
        self.db = Database()

        self.collection_name = 'deneme'

        self.fields = {
            "title": "string",
            "body": "string",
            "created": "datetime",
            "updated": "datetime",
        }

        self.create_required_fields = ["title", "body"]

        self.create_optional_fields = []

        self.update_required_fields = ["title", "body"]

        self.update_optional_fields = []

    def create(self, deneme):
        res = self.db.insert(deneme, self.collection_name)
        return "Inserted Id " + res

    def find(self, deneme):
        return self.db.find(deneme, self.collection_name)

    def find_by_id(self, id):
        return self.db.find_by_id(id, self.collection_name)

    def update(self, id, deneme):
        return self.db.update(id, deneme,self.collection_name)

    def delete(self, id):
        return self.db.delete(id, self.collection_name)

    def ner(self):
        nlp = spacy.load("en_core_web_lg")
        tweetsData = pd.read_csv("models/Kitap1.csv",encoding='unicode_escape', error_bad_lines=False, sep=';')


        kvkTweet = []
        for item in tweetsData.values.tolist():
            doc = nlp(item[5])
            for token in doc:
                if token.pos_ == 'PROPN':
                    kvkTweet.append(item)
        return kvkTweet


        
        #doc = nlp("Ukraine war: First civilian deaths in Lviv shatter sense of safety")
        #print(displacy.serve(doc, style="ent"))
        # print('text   |   lemma    |   pos')
        # for token in doc:
        #     print(40*'_')
        #     print(token.text,'|', token.lemma_,'|', token.pos_)
        
        # TRAIN_DATA = [
        #         ("Walmart is a leading e-commerce company", {"entities": [(0, 7, "ORG")]}),
        #         ("I reached Chennai yesterday.", {"entities": [(19, 28, "GPE")]}),
        #         ("I recently ordered a book from Amazon", {"entities": [(24,32, "ORG")]}),
        #         ("I was driving a BMW", {"entities": [(16,19, "PRODUCT")]}),
        #         ("I ordered this from ShopClues", {"entities": [(20,29, "ORG")]}),
        #         ("Fridge can be ordered in Amazon ", {"entities": [(0,6, "PRODUCT")]}),
        #         ("I bought a new Washer", {"entities": [(16,22, "PRODUCT")]}),
        #         ("I bought a old table", {"entities": [(16,21, "PRODUCT")]}),
        #         ("I bought a fancy dress", {"entities": [(18,23, "PRODUCT")]}),
        #         ("I rented a camera", {"entities": [(12,18, "PRODUCT")]}),
        #         ("I rented a tent for our trip", {"entities": [(12,16, "PRODUCT")]}),
        #         ("I rented a screwdriver from our neighbour", {"entities": [(12,22, "PRODUCT")]}),
        #         ("I repaired my computer", {"entities": [(15,23, "PRODUCT")]}),
        #         ("I got my clock fixed", {"entities": [(16,21, "PRODUCT")]}),
        #         ("I got my truck fixed", {"entities": [(16,21, "PRODUCT")]}),
        #         ("Flipkart started it's journey from zero", {"entities": [(0,8, "ORG")]}),
        #         ("I recently ordered from Max", {"entities": [(24,27, "ORG")]}),
        #         ("Flipkart is recognized as leader in market",{"entities": [(0,8, "ORG")]}),
        #         ("I recently ordered from Swiggy", {"entities": [(24,29, "ORG")]})
        #         ]
        # ner=nlp.get_pipe("ner")
        # for _, annotations in TRAIN_DATA:
        #     for ent in annotations.get("entities"):
        #         ner.add_label(ent[2])