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


