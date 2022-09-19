[![app auto-test with Github Action](https://github.com/nogibjj/fan_project1/actions/workflows/apptest.yml/badge.svg)](https://github.com/nogibjj/fan_project1/actions/workflows/apptest.yml)


# Split-Money🤔

## Intro
Do you feel annoyed with calculation work after having fun with friends? For example, you went to skiing with friends. You paid the fee for skiing, but Tom rent the car and Jen took charge in food burget. After the joyful time, you and friends have to sit down, calculate the total fee and figure out if there is extra money you should pay. 

Although they are simple calculation tasks just using Plus or Minus, but when all of friends contribute to the team burget and the calculationn work accummulating, it is so tired to do such work. 

I built a microservice with FastAPI, Databricks to solve the split money problem and automatic calculate the account and everyone's fee for you. 

Hope this microservice will save my time lol. 

## Quick Start

### API call
- `/open`
  open new burget for calcuation, get the hashcode for payment.
  
- `/pay/{hashcode}/{your name}/{other's name}/{money}` 
  record the payment from you for others (If it works for all members please use "all") in the burget, which identified by hashcode
  If you pay the bill and you can clear the bill used this API. 
  
- `/cal/{hashcode}`
  Do calculation for you and show the result.


### CI/CD
```shell
Usage: cli_tool.py [OPTIONS] COMMAND [ARGS]...

  CLI to query SQL database

Options:
  --help  Show this message and exit.

Commands:
  cli-connect  Check if codebase is connected to databricks in Azure...
  cli-query    Query record based on code
```
 
### Demo video
[demo](https://ypve0vm4k0.feishu.cn/minutes/obcnihw2t945nlalry783595)


## Design
### System
 <img src="https://user-images.githubusercontent.com/26620662/190974371-8ce98923-e7de-4729-bb38-805b4b86ab3c.png" width = "600" height = "500" align=center />

### Repo framework
```shell
fan_project1
├── LICENSE
├── Makefile
├── README.md
├── __pycache__
│   └── test_pytmp.cpython-38-pytest-7.1.3.pyc
├── app.py
├── cli_tool.py
├── dbtool
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   └── dbst.cpython-38.pyc
│   └── dbst.py
├── pytmp.py
├── requirements.txt
└── test_pytmp.py

3 directories, 13 files
```

## Dataset
`default.diamonds`  
Default databricks dataset in Azure for testing connection. 



`money` The table to store records that users enter. The dataset from users and me. 

Schema:

 <img src="https://user-images.githubusercontent.com/26620662/190969290-4b5d1d3f-a89c-488e-ae87-35b50ee810cf.png" width = "300" height = "200" align=center />



## What's Next
- front-end design

  I only implement the json api call of the microservice. And by the end of Sept, I will add some UI-design with Vue make it more user-friendly. Welcome suggestions!
  
- deployment

  I will deploy in my own website. And later I will publish the link. Feel free to ask me the link if you are interested in this small tool!

- Authentication and Security

  I will not introduce the account in this tool, otherwise all of people can visit the burget with link(code), users can make it private by passwords. 
  

## Reference
[FastAPI](https://fastapi.tiangolo.com/)

## Author
yl734

Eva Lin

Have fun with code😎

