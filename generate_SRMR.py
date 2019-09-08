#pip install git+https://github.com/detly/gammatone.git
import librosa
from srmrpy import srmr
import sys

x, sr= librosa.core.load(sys.argv[1], sr=16000)
a,b=srmr(x,sr)
print(a)
