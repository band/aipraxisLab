# 2023-08-26: some notes on llama-index documentation on PromptTemplates

**TO-DO**: fix the Markdown in this note

```python
Python 3.11.5 (main, Aug 24 2023, 15:09:45) [Clang 14.0.3 (clang-1403.0.22.14.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.

>>> from llama_index.prompts import PromptTemplate
>>> template = 'context information provided below\n-----------\n{context_str}\n-------------\ngiven this context, answer this question: {query_str}\n'
>>> qa_template = PromptTemplate(template)
>>> messages = qa_template.format_messages(context_str=..., query_str=...)
>>> messages
[ChatMessage(role=<MessageRole.USER: 'user'>, content='context information provided below \n-----------\nEllipsis\n-------------\ngiven this context, answer this question: Ellipsis\n', additional_kwargs={})]
```
- that excerpt shows how to use PromptTemplate.
- now i need an example of how to use it.



