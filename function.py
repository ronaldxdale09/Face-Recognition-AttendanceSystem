from os import name
from ml_models import ml_models as ml
import warnings


warnings.filterwarnings("ignore", category=DeprecationWarning)
 
 
class face_reco():

    def startRecog(self):
        ml.start_faceRG()


    def startTraining(self):
            ml.train_classifier()

    def generateDataset(self,name,birthdate,gender,course,userType):
        ml.generate_dataset(name,birthdate,gender,course,userType)

