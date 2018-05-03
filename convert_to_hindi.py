import requests
import json

headers = {'Authorization' : 'your token'}
data= {'user':'your id', 'language':'HI'}

user_shoping_list = []

for each_command in range(0, NO_OF_ITEMS):
 
    filename = "microphone-results" + str(each_command) + ".wav"
    files= {'audio_file':open(filename,'rb')}
    url = 'https://dev.liv.ai/liv_transcription_api/recordings/'


    result = requests.post(url, headers = headers, data = data, files = files)
    #print(result.text)


    x= json.loads(result.text)
    answer=x['transcriptions'][0]['utf_text']
    answer.encode("utf-8")
    user_shoping_list.append(answer)

print(user_shoping_list)
