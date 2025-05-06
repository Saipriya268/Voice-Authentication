from model_testing import verifyUser
import sounddevice as sd
from scipy.io.wavfile import write
from createingData import extract_mfcc
from sklearn.native_bayes import BernoulliNB
import pandas as pd
from skleran.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from skleran.ensemble import RandomForestClassifier
from sklearn.neighbor import KneighborsClassifier
from sklearn.naive_bayes import GaussianNB
import time
import warnings
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voice[1].id)
engine.setProperty("rate",200)
def speaker_identifier();
    fs  = 44100
    duration = 3
    print("speak Akash when the recording starts")
    engine.say("Speak Akash when thw recording starts!")
    engine.runAndWait()
time.sleep(0.1)
print("recording started")
rec = sd.rec(int((duration * fs)), samplerate=fs, channels=1)
sd.wait()
print("recording stopped")
file = "data/history/last_try.wav"
write(filename=file, rate=fs, data=rec)
mfcc = extract_mfcc(file, n_mfcc=40)
input = pd.DataFrame(columns=range(0, 40))
lst = list(mfcc)
input.loc[len(input)] = lst
df = pd.read_csv("data\\csv\\final_data.csv")
Y = df["speaker"]
X = df.drop(coumns=["speaker","unnamed:0"])
classifier = MLPClassifier(solver='adam', alpha=0.001,random_state=1, max_iter=500,hidden_layer_sizer=100, activation="logistic")
warning.simplefilter("ignore")
classifier.fit(X, Y)
pred-mlp = classifier.predict(input)
return `1`