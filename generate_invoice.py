import speech_recognition as sr
import requests
import json

NO_OF_ITEMS = 1

mic_name = "Built-in Microphone"
sample_rate = 48000
chunk_size = 2048
r = sr.Recognizer()

mic_list = sr.Microphone.list_microphone_names()

for i, microphone_name in enumerate(mic_list):
    if microphone_name == mic_name:
        device_id = i


for each_command in range(0, NO_OF_ITEMS):
    with sr.Microphone(device_index = device_id, sample_rate = sample_rate, 
                            chunk_size = chunk_size) as source:
        
        r.adjust_for_ambient_noise(source)
        print("Speak out the next item in the list")
        audio = r.listen(source)

    filename = "microphone-results" + str(each_command) + ".wav"

    with open(filename, "wb") as f:
        f.write(audio.get_wav_data())


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
