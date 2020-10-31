#-*- coding:utf-8 -*-
import urllib3
import json
import base64
import os
openApiURL = "http://aiopen.etri.re.kr:8000/WiseASR/Pronunciation"
accessKey = "ada89ba0-ef6c-4136-8be7-7ea765c4f7ce"
audioFilePath = os.getcwd() + "\\app\\audio"
languageCode = "english: 영어 발음평가 코드"
script = "PRONUNCIATION_SCRIPT"

file = open(audioFilePath, "r")
audioContents = base64.b64encode(file.read())
file.close()

requestJson = {
	"access_key": accessKey,
	"argument": {
		"language_code": languageCode,
		"script": script,
		"audio": audioContents
	}
}

http = urllib3.PoolManager()
response = http.request(
	"POST",
	openApiURL,
	headers={"Content-Type": "application/json; charset=UTF-8"},
	body=json.dumps(requestJson)
)

print("[responseCode] " + str(response.status))
print("[responBody]")
print(response.data)