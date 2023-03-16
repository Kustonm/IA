# mira.py
# -------


# Mira implementation

import util
PRINT = True


class MiraClassifier:
    """
    Mira classifier.

    Note that the variable 'datum' in this code refers to a counter of features
    (not to a raw samples.Datum).
    """
    def __init__( self, legalLabels, max_iterations):
        self.legalLabels = legalLabels
        self.type = "mira"
        self.automaticTuning = False
        self.C = 0.001
        self.max_iterations = max_iterations
        self.initializeWeightsToZero()

    def initializeWeightsToZero(self):
        "Resets the weights of each label to zero vectors"
        self.weights = {}
        for label in self.legalLabels:
            self.weights[label] = util.Counter() # this is the data-structure you should use

    def train(self, trainingData, trainingLabels, validationData, validationLabels):
        "Outside shell to call your method. Do not modify this method."

        if (self.automaticTuning):
            Cgrid = [0.002, 0.004, 0.008]
        else:
            Cgrid = [self.C]

        return self.trainAndTune(trainingData, trainingLabels, validationData, validationLabels, Cgrid)

    
    
    
    def trainAndTune(self, trainingData, trainingLabels, validationData, validationLabels, Cgrid):
        
       
        # DO NOT ZERO OUT YOUR WEIGHTS BEFORE STARTING TRAINING, OR
        # THE AUTOGRADER WILL LIKELY DEDUCT POINTS.
        

        self.features = trainingData[0].keys()

        newWeights = self.weights.copy()
        self.features = trainingData[0].keys()
        newWeights = self.weights.copy()

        bestAccuracy = 0
        correct = 0.0

        for c in Cgrid:
            self.weights = newWeights.copy()
            for iteration in range(self.max_iterations):
                print("Starting iteration", iteration, "...")
                for datum,trueLabel in zip(trainingData,trainingLabels):
                    scores = util.Counter()
                    for label in self.legalLabels: scores[label] = self.weights[label] * datum
                    guess = scores.argMax()
                    if guess != trueLabel:
                        dif = self.weights[guess] - self.weights[trueLabel]
                        prod = 0 #producto
                        sumC = 0 #Suma de los cuadrados
                        for feature in self.features:
                            prod += datum[feature] * dif[feature]
                            sumC += datum[feature]**2
                        tau = min(c, (prod + 1.0) / (2.0 * sumC))
                        for feature in datum:
                            self.weights[trueLabel][feature] += tau * datum[feature]
                            self.weights[guess][feature] -= tau * datum[feature]
                    else: correct +=1.0
                    
            #Calcular la precision
            accuracy = correct / len(validationData)
            if accuracy > bestAccuracy:
                bestAccuracy = accuracy
                bestWeight = self.weights

        self.weights = bestWeight
    
    
             
    def classify(self, data ):
        """
        Classifies each datum as the label that most closely matches the prototype vector
        for that label.  See the project description for details.

        Recall that a datum is a util.counter...
        """
        
        guesses = []
        #for i in range(len(data)):
        for datum in data:
            scores = util.Counter()
            for label in self.legalLabels:
                scores[label] = self.weights[label] * datum
            guess = scores.argMax()
            guesses.append(guess)

        return guesses


