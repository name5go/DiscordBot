 # -*- coding: Shift-JIS -*-

import requests, json

class Voicevox:
 def __init__(self,host="127.0.0.1",port=50021):
  self.host = host
  self.port = port


 def get_voice(self,text=None,speaker=5):
  params = (("text", text),("speaker", speaker))
  res1 = requests.post(
                      f"http://{self.host}:{self.port}/audio_query",
                      params=params,
                      )
  res2 = requests.post(
                       f"http://{self.host}:{self.port}/synthesis",
                       params = {'speaker': speaker},data=json.dumps(res1.json())
                      )
  with open("talk.wav", mode="wb") as f:
   f.write(res2.content)
  return "talk.wav"