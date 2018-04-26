import numpy as np
import pickle
from pre_processing import feature_extraction

class Sarcasm:
    def __init__(self, sentence):
        self.sentence = sentence

    """Returns the vectorized dictionary data

    Returns:
        [pickle object] -- [object that represents the vectorized dictionary]
    """
    def getVecDictionary(self):
        vec_dict_data = open('trainings/vecdict_all.p', 'rb')
        vec_obj = pickle.load(vec_dict_data, encoding="latin1")
        vec_dict_data.close()

        return vec_obj
    
    """Returns the classifier data

    Returns:
        [pickle object] -- [object that represents the classifier data]
    """
    def getClassifier(self):
        classifier_data = open('trainings/classif_all.p','rb')
        classifier_obj = pickle.load(classifier_data, encoding='latin1')
        classifier_data.close()

        return classifier_obj

    """Returns the sarcasm score
    
    Returns:
        [int] -- [sarcasm score where the higher value, the greater the probability]
    """
    def getScore(self):
        # Getting the training files
        vec = self.getVecDictionary()
        classifier = self.getClassifier()

        sentence = self.sentence.encode('ascii', 'ignore')
        features = feature_extraction.getallfeatureset(sentence)
        
        features_vec = vec.transform(features)
        score = classifier.decision_function(features_vec)[0]
        percentage = int(round(2.0*(1.0/(1.0+np.exp(-score))-0.5)*100.0))
        
        return percentage
