from multiprocessing.dummy import Array
import warnings
from pydantic import Json
from factory.database import Database
import spacy
from spacy import displacy
from spacy.lang.en.examples import sentences
import pandas as pd
import random
from spacy.util import minibatch, compounding
from pathlib import Path
from spacy.training.example import Example
from spacy.tokens import DocBin
from tqdm import tqdm

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
        #nlp = spacy.load("en_core_web_lg")
        tweetsData = pd.read_csv("models/Kitap1.csv",encoding='unicode_escape', error_bad_lines=False, sep=';')
        TRAIN_DATA = pd.read_csv("models/trainData.csv",encoding='unicode_escape',  error_bad_lines=False, sep=';')
        df=TRAIN_DATA.to_numpy()
        #ner=nlp.get_pipe('ner')

        #doc = nlp("Ukraine war: First civilian deaths in Lviv shatter sense of safety")
        #print(displacy.serve(doc, style="ent"))
        # print('text   |   lemma    |   pos')
        # for token in doc:
        #     print(40*'_')
        #     print(token.text,'|', token.lemma_,'|', token.pos_)
     

        # Training examples in the required format
        # TRAIN_DATA =[ ('RT @SLKollmann: Four judges failure to understand what coercion is, even with a video recording and as brilliantly explained by devoted ad?', {'entities': [(80, 92, 'SECRET')]}),
        #     ('RT @SLKollmann: Four judges failure to understand what coercion is, even with a video recording and as brilliantly explained by devoted ad?', {'entities': [(80, 92, 'SECRET')]}),
        #     ('RT @SLKollmann: Four judges failure to understand what coercion is, even with a video recording and as brilliantly explained by devoted ad?', {'entities': [(80, 92, 'SECRET')]}),
        #     ('There is video record of Child being raped in the Carpark. Forensic experts found sperm on 3 y.o. jeans.? https://t.co/hJIKS2Gi3w', {'entities': [(9, 21, 'SECRET')]}),
        #     ('RT @dorymanze: @Gidi_Traffic I believe her. I believe her. I believe @Ms_DSF. I have many similar recordings too. #MeToo. Women and girls,?', {'entities': [(98, 107, 'SECRET')]}),
        #     ('RT @dorymanze: @Gidi_Traffic I believe her. I believe her. I believe @Ms_DSF. I have many similar recordings too. #MeToo. Women and girls,?', {'entities': [(98, 107, 'SECRET')]}),
        #     ('Great time in @WRDA_team this afternoon recording a piece on #metoo for @BBCRadio4 with presenter @curranradio and? https://t.co/RAd4ywg5xW', {'entities': [(40, 49, 'SECRET')]}),
        #     ('Meghan Trainor re-recording Me Too with lyrics about the #MeToo movement', {'entities': [(18, 27, 'SECRET')]}),
        #     ('This is also #metoo, same thing: John Humphrys jokes about @BBCnews @bbcworld gender pay gap in leaked recording https://t.co/t5DG75GAWS', {'entities': [(103, 112, 'SECRET')]}),
        #     ('Watch recording of #MeToo at the #Txlege: https://t.co/mUp5rxS6AC', {'entities': [(6, 15, 'SECRET')]}),
        #     ('RT @ValerieComplex: Ambra Battliliana put her life and career on the line by recording Weinsteins antica and has been left out of every #M?', {'entities': [(77, 86, 'SECRET')]}),
        #     ('RT @ValerieComplex: Ambra Battliliana put her life and career on the line by recording Weinsteins antica and has been left out of every #M?', {'entities': [(77, 86, 'SECRET')]}),
        #     ('RT @ValerieComplex: Ambra Battliliana put her life and career on the line by recording Weinsteins antica and has been left out of every #M?', {'entities': [(77, 86, 'SECRET')]}),
        #     ('RT @ValerieComplex: Ambra Battliliana put her life and career on the line by recording Weinsteins antica and has been left out of every #M?', {'entities': [(77, 86, 'SECRET')]}),
        #     ('RT @MichaelBossetta: Miss our livestream recording of the 2018 Year in Review #podcast? Catch it here or in better quality on #Facebook:?', {'entities': [(41, 50, 'SECRET')]}),
        #     ('RT @EdwardsEvan: Heres a recording of my sermon yesterday! I talked about the women who have been writing #MeToo and #ChurchToo in regards?', {'entities': [(25, 34, 'SECRET')]}),
        #     ('RT @Unions21: We started recording our own podcasts in 2017 - missed them?  Have a listen back here https://t.co/ee2eioCFd0 #brexit #metoo?', {'entities': [(25, 34, 'SECRET')]}),

        #         ]
        # TRAIN_DATA =[ ("Pizza is a common fast food.", {"entities": [(0, 5, "FOOD")]}),
        #       ("Pasta is an italian recipe", {"entities": [(0, 5, "FOOD")]}),
        #       ("China's noodles are very famous", {"entities": [(8,14, "FOOD")]}),
        #       ("Shrimps are famous in China too", {"entities": [(0,7, "FOOD")]}),
        #       ("Lasagna is another classic of Italy", {"entities": [(0,7, "FOOD")]}),
        #       ("Sushi is extemely famous and expensive Japanese dish", {"entities": [(0,5, "FOOD")]}),
        #       ("Unagi is a famous seafood of Japan", {"entities": [(0,5, "FOOD")]}),
        #       ("Tempura , Soba are other famous dishes of Japan", {"entities": [(0,7, "FOOD")]}),
        #       ("Udon is a healthy type of noodles", {"entities": [(0,4, "ORG")]}),
        #       ("Chocolate soufflé is extremely famous french cuisine", {"entities": [(0,17, "FOOD")]}),
        #       ("Flamiche is french pastry", {"entities": [(0,8, "FOOD")]}),
        #       ("Burgers are the most commonly consumed fastfood", {"entities": [(0,7, "FOOD")]}),
        #       ("Burgers are the most commonly consumed fastfood", {"entities": [(0,7, "FOOD")]}),
        #       ("Frenchfries are considered too oily", {"entities": [(0,11, "FOOD")]})
        #    ]
                
        nlp = spacy.load('en_core_web_sm')  # load existing spaCy model
        ner = nlp.get_pipe('ner')
        ner.add_label('SECRET')
        ner.add_label('SEXUAL_LIFE')
        ner.add_label('MAIL')
        ner.add_label('POLITICS')
        ner.add_label('WEALTH')

        print(ner.move_names) # Here I see, that the new label was added
        optimizer = nlp.create_optimizer()
        # get names of other pipes to disable them during training
        other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
        with nlp.disable_pipes(*other_pipes):  # only train NER
            for itn in range(1):
                #random.shuffle(TRAIN_DATA)
                losses = {}
                for id, text, category, start_position_1,start_position_2,start_position_3,stop_position_1,stop_position_2,stop_position_3 in TRAIN_DATA.values:
                    print('girdi')
                    print(text)
                    doc = nlp(text)
                    split = category.split(',')
                    if(len(split) == 1):
                        example = Example.from_dict(doc, {'entities': [(int(start_position_1), int(stop_position_1),category)]})
                    elif(len(split) == 2 and start_position_2 >=0 and stop_position_2 >=0):
                        example = Example.from_dict(doc, {'entities': [(int(start_position_1), int(stop_position_1),split[0]),(int(start_position_2), int(stop_position_2),split[1])]})
                    elif(len(split) == 3 and start_position_2 >=0 and stop_position_2 >=0 and start_position_3 >=0 and stop_position_3 >=0):
                        example = Example.from_dict(doc, {'entities': [(int(start_position_1), int(stop_position_1),split[0]),(int(start_position_2), int(stop_position_2),split[1]),(int(start_position_3), int(stop_position_3),split[2])]})
                    else:
                        continue
                    nlp.update([example], drop=0.35, sgd=optimizer, losses=losses)
                print(losses)
        # test the trained model # add some dummy sentences with many NERs

        test_text = '@KeithUrban #metoo female pulls at my heart strings. Thank you so much for recording it.'
        doc = nlp(test_text)
        print("Entities in '%s'" % test_text)
        print('*'*30) 
        print(doc.ents)
        print('*'*30) 
        #NORP = Nationalities or religious or political groups
        for ent in doc.ents:
            print(ent.label_, " -- ", ent.text)
        

        kvkTweet = []
        for item in tweetsData.values.tolist():
            doc = nlp(item[5])
            for ent in doc.ents:
                print(ent.label_, " -- ", ent.text)
                kvkTweet.append({"text": item[5], "label": ent.label_, "word":ent.text})
        return kvkTweet
