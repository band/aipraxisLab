#! /usr/bin/env python
"""
code derived from <https://gpt-index.readthedocs.io/en/latest/examples/vector_stores/SimpleIndexDemo.html>, accessed 2023-07-28
"""
# Import necessary packages
from llama_index import(
    VectorStoreIndex,
    SimpleDirectoryReader,
    load_index_from_storage,
    StorageContext,
    ServiceContext,
)

# set up argparse
import argparse
def init_argparse():
    parser = argparse.ArgumentParser(description='Generate OpenAI index from wiki text or Markdown files.')
    parser.add_argument('--wiki', '-w', required=True, help='directory containing wiki files (Markdown + other)')
    parser.add_argument('--model', '-m', required=False, help='llm model_name')
    return parser

def main():
    argparser = init_argparse();
    args = argparser.parse_args();
    print(f"args: {args}")
    
    wiki_dir = str(args.wiki)
    print(wiki_dir)

    # set LLM
    model_name = 'gpt-3.5-turbo'
    if args.model:
        model_name = str(args.model)

    from llama_index.llms import OpenAI
    llm = OpenAI(model=model_name)
    
    # set service context
    service_context = ServiceContext.from_defaults(llm=llm)
    # Loading from a directory
    documents = SimpleDirectoryReader(wiki_dir).load_data()

    # Construct a simple vector index
    index = VectorStoreIndex.from_documents(documents)

    # Save index to disk
    index.set_index_id("vector_index")
    index.storage_context.persist("./storage")

    # rebuild storage context
#    storage_context = StorageContext.from_defaults(persist_dir="storage")
    # load index
#    index = load_index_from_storage(storage_context, index_id="vector_index")

    # Querying the index
    query_engine = index.as_query_engine(
        service_context=service_context,
        response_mode="tree_summarize")
    
    response = query_engine.query("List the primary topics in the wiki pages")
    print('model name: ', model_name)
    print(response)

if __name__ == "__main__":
    exit(main())

