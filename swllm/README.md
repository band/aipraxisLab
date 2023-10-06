# README

- This folder holds note on working with Simon Willison's PyPi module
  `llm`.  
  Link: <https://llm.datasette.io/en/stable/index.html>  

2023-09-05: some install notes on using embeds with `llm`

```shell
(venv) $ pip install --upgrade llm
(venv) $ llm install llm-sentence-transformers
(venv) $ llm sentence-transformers register all-MiniLM-L6-v2
(venv) $ llm embed-multi readmes \\n--model sentence-transformers/all-MiniLM-L6-v2 \\n--files ~/Documents/Github/ '**/README.md'
(venv) $ llm similar readmes -c sqlite |jq .id
```


