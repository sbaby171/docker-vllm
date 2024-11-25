from openai import OpenAI
import argparse 
# --------------------------------------------------------------------|-------:
def __handle_cli_args():  
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-tokens", type=int, default = 120)
    parser.add_argument("--port", type=int, default = 5000)
    parser.add_argument("--model", type=str,default="NousResearch/Meta-Llama-3-8B-Instruct")
    parser.add_argument("--prompt", type=str,default="Yesterday I saw the craziest thing, a dog was ")
    parser.add_argument("--stream", action="store_true")
    parser.add_argument("--temp",type=float, default = 1.0, )
    parser.add_argument("--top_p",type=float, default = 1.0,) 
    args = parser.parse_args()
    return args
# --------------------------------------------------------------------|-------:
args = __handle_cli_args()
# --------------------------------------------------------------------|-------:
api_token = "EMPTY"
client = OpenAI(
    base_url=f"http://localhost:{args.port}/v1",
    api_key=api_token,
)
# --------------------------------------------------------------------|-------:
response = client.chat.completions.create(
    model=args.model,
    max_tokens = args.max_tokens, 
    temperature = args.temp, 
    top_p = args.top_p, 
    stream = args.stream,
    messages=[
      {"role": "user", 
       "content": args.prompt}
    ], 
)
# --------------------------------------------------------------------|-------:
if args.stream:  
    print(f"DEBUG: streaming - {type(response)}")
    for chunk in response:
        #print(chunk)
        print(chunk.choices[0].delta.content, end="")
        #print("****************")
    print("\n--------------------------------------------------------------:")
    print(response.__dict__)
else: 
    print(f"DEBUG: non-streaming - {type(response)}")
    print(response)
    print(args.prompt)
    print(response.choices[0].message)

