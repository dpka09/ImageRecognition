import boto3
import json
client= boto3.client('rekognition', region_name='us-east-1')

file= open('sadkid.jpg', 'rb'). read()

response= client.detect_faces(
    Image={       
        'Bytes': file
    },
    Attributes= ['ALL']
    
)

for face in response["FaceDetails"]:
    
    print('The detected face is of' +' '+ str(face['Gender']['Value'])) 
    print('The detected face is between' +" "+ str(face['AgeRange']['Low']) + " " + 'and'+ " " + str(face['AgeRange']['High'])+ ' ' + 'years old')
    print('the detected emotion is' + ' '+ str(face['Emotions'][0]['Type']))

    Sunglass= str(face['Sunglasses']['Value'])

    if Sunglass=='True':
            print("the detected face is wearing sunglasses")
    else:
            print("The detected face is not wearing any glasses")

   # print("here are credentials:")
    #print(json.dumps(face, indent=4, sort_keys=True))
  
