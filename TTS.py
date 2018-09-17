#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @author =__Uluç Furkan Vardar__



#Needed Libs are imported

import boto3
import requests
from google.cloud import texttospeech
import os
from imutils import paths

global aws_access_key
global aws_secret_key
global azure_api_key

aws_access_key= '******'
aws_secret_key = '******'
azure_api_key = "******"
# also you must generete google .json access file

def amazon_tts(text,path):
	global aws_access_key
	global aws_secret_key
	polly_client = boto3.Session(
                aws_access_key_id = aws_access_key,                     
    			aws_secret_access_key = ,
    			region_name='us-west-2').client('polly')
	response = polly_client.synthesize_speech(VoiceId='Filiz',
	                OutputFormat='mp3', 
	                Text = text)

	file = open(path+'-amazon.mp3', 'w')
	file.write(response['AudioStream'].read())
	file.close()


def azure_tts(text,path):
	global azure_api_key
	apiKey = azure_api_key
	header = {"Ocp-Apim-Subscription-Key": apiKey}
	r = requests.post("https://api.cognitive.microsoft.com/sts/v1.0/issueToken", headers = header)

	Authorization = 'Bearer '+ r.text

	header = { "X-Microsoft-OutputFormat" : "audio-16khz-32kbitrate-mono-mp3",
				"Authorization" : Authorization,
				"Content-Type" : "application/xml" }

	xml = """<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="http://www.w3.org/2001/mstts" xml:lang="tr-TR"><voice xml:lang="tr-TR" name="Microsoft Server Speech Text to Speech Voice (tr-TR, SedaRUS)">{}</voice></speak>"""

	rr= requests.post("https://speech.platform.bing.com/synthesize",  data=xml.format(text) ,headers = header )
	with open(path+'-azure.mp3', 'wb') as f:
	    f.write(rr.content)


