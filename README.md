# Amazon EventBridge -  Bus
<p>
<img src="https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white" />
<img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white" />
<img src="https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white" />
<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
</p>

<img  src="https://github.com/khanasif1/amazon-eventbridge/blob/main/img/eb.png?raw=true">
EventBridge is a serverless service that uses events to connect application components together, making it easier for you to build scalable event-driven applications. An event bus is a pipeline that receives events. Rules associated with the event bus evaluate events as they arrive. Each rule checks whether an event matches the rule's criteria. You associate a rule with a specific event bus, so the rule only applies to events received by that event bus.

## Steps to setup environement :octocat:

- :snake: Download and install python https://www.python.org/downloads/
- Create a python virtual environment
```
    pip install virtualenv
    python -m venv msg
    NAMENEV\Scripts\activate.bat # ON WINDOWS
    source NAMENEV/bin/activate # ON LINUX/MAC
```
- Update the values for items marked with  :+1: {}
- Run
```
    python3 send_msg.py
```
:tada: