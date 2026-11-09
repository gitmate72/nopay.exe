import sys,json
from faster_whisper import WhisperModel
m=WhisperModel("small.en",device="cpu",compute_type="int8")
import subprocess,numpy as np
a=np.frombuffer(subprocess.run(["ffmpeg","-v","error","-i",sys.argv[1],"-f","f32le","-ac","1","-ar","16000","-"],capture_output=True).stdout,np.float32)
segs,_=m.transcribe(a,word_timestamps=True)
W=[]
for s in segs:
  for w in s.words: W.append([w.word.strip(),round(w.start,2),round(w.end,2)])
json.dump(W,open(sys.argv[2],'w'));print(' '.join(f"{a}@{b}" for a,b,c in W))
