# Setup and install

2023-09-03: reinstallation of `llm` and associated, required modules:

```shell
$ rm -fr venv
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install --upgrade pip
(venv) $ pip install --upgrade llm
(venv) $ llm install llm-gpt4all
(venv) $ llm install llm-palm
(venv) $ pip install llama-cpp-python
(venv) $ llm install llm-llama-cpp
(venv) $ llm models  # list openai and local models
```
 
