#! /usr/bin/env python
"""
code derived from <https://gpt-index.readthedocs.io/en/latest/examples/vector_stores/SimpleIndexDemo.html>, accessed 2023-07-28

two arguments:
--directory/-d: directory containing Markdown and other files
--model/-m: LLM model name
--reindex/-r: build a new vector index; if omitted use the latest saved index
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
    parser = argparse.ArgumentParser(description='Generate OpenAI index from text or Markdown files.')
    parser.add_argument('--directory', '-d', required=True, help='directory containing Markdown + other files')
    parser.add_argument('--model', '-m', required=False, help='llm model_name')
    parser.add_argument('--reindex', '-r', action='store_true', help='build a new vector index')
    return parser

def main():
    argparser = init_argparse();
    args = argparser.parse_args();
    print(f"args: {args}")
    
    dir_name = str(args.directory)
    print(dir_name)

    # set LLM
    model_name = 'gpt-3.5-turbo-16k'
    if args.model:
        model_name = str(args.model)

    from llama_index.llms import OpenAI
    llm = OpenAI(model=model_name, temperature=0.0)
    
    # set service context
    service_context = ServiceContext.from_defaults(llm=llm)
    # Loading from a directory
    documents = SimpleDirectoryReader(dir_name).load_data()
    print(f"loaded {len(documents)} documents")

    # set storage context and load index
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    index = load_index_from_storage(storage_context, index_id="vector_index")

    if args.reindex:
        print("constructing a new index")
        # Construct a new simple vector index
        index = VectorStoreIndex.from_documents(documents)
        # and save index to disk
        index.set_index_id("vector_index")
        index.storage_context.persist("./storage")

    # Query the index
    query_engine = index.as_query_engine(
        service_context=service_context,
        response_mode="tree_summarize")

    question = "List the primary topics in the documents"
    try:
        response = query_engine.query(question)
    except Exception as e:
        print(f"query_enging error: {e}")
        sys.exit(1)
    
    print('model name: ', model_name)
    print('query: ', question)
    print(response)

if __name__ == "__main__":
    exit(main())

