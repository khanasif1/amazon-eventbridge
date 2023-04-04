# Amazon EventBridge -  Bus
<img src="" />
<img  src="https://github.com/khanasif1/amazon-eventbridge/blob/main/img/eb.png?raw=true">
EventBridge is a serverless service that uses events to connect application components together, making it easier for you to build scalable event-driven applications. An event bus is a pipeline that receives events. Rules associated with the event bus evaluate events as they arrive. Each rule checks whether an event matches the rule's criteria. You associate a rule with a specific event bus, so the rule only applies to events received by that event bus.

## Steps to setup environement

- Download and install python https://www.python.org/downloads/
- Create a python virtual environment
```
    pip install virtualenv
    python -m venv msg
    NAMENEV\Scripts\activate.bat # ON WINDOWS
    source NAMENEV/bin/activate # ON LINUX/MAC
```
- Update the values for items marked with  :+1: {}