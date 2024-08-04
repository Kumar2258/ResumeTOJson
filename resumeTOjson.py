import requests
import json
openaikey="sk-Api_Key"

from pypdf import PdfReader
reader=PdfReader('Kumar_CV.pdf')
text=reader.pages[0]
finaltext=text.extract_text()

chatgpt_url="https://api.openai.com/v1/chat/completions"
chatgpt_headers= {
    "content-type":"application/json",
    "Authorization":"Bearer {}".format({openaikey})
    }

prompt_pre=f"""{finaltext}
----------------------------
Retrive the information from this above provided resume in Strictly output in JSON format.The JSON should have the following format: """

sample_format=[
    {
        "Name":"---",
        "contact_info":{
            "address":"---",
            "phone":"---",
            "email":"----"
            
        },
        
        "Skills":{
            "Programming_laguages":"---",
            "Framwork":"---",
            "tools":"---"
        },

        "Projects":[
            {
                "Project_name":"---",
                "Tech_Stack":"---",
                "details":"---",
                "date":"---"
            }
        ],
        "Certifications":[
            {
                "Certification_name":"----",
                "Source/platform":"---",
                "Date":"---"
            }
        ],        

        "education":[
            {
            "degree":"---",
            "collage":"---",
            "graduation_date":"---",
            "Grade":"---"
            }

        ],
        
    }

    
]
prompt=prompt_pre+ json.dumps(sample_format)

messages=[
        {"role":"system","content":"You are an Resume info retriver who parse the resume in json format."},
        {"role":"user","content":prompt}
]
chatgpt_payload={
    "model":"gpt-3.5-turbo-16k",
    "messages":messages,
    "temperature":1.2,
    "max_tokens":300,
    "top_p":1,
    "stop":["###"]
}

response=requests.request("POST",chatgpt_url,json= chatgpt_payload,headers=chatgpt_headers)
response=response.json()
print(response)
