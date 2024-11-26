from openai import OpenAI
# --------------------------------------------------------------------|-------:
"""
$ docker run --runtime nvidia --gpus all \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HUGGING_FACE_HUB_TOKEN=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" \
    -p 8000:8000 \
    --ipc=host vllm/vllm-openai:latest \
    --tensor-parallel-size 2 \
    --model meta-llama/Llama-3.2-8B-Instruct
"""
def summarize(txt):
    api_token = "EMPTY"
    client = OpenAI(
        #base_url=f"http://0.0.0.0:8000/v1",
        base_url=f"http://vllm:8000/v1",
        #base_url=f"http://localhost:8000/v1",
        api_key=api_token,
    )

    prompt = f"""
    I need help summarizing the following text. Note it was parsed from 
    a PDF file to markdown. 

    Please try to keep the summary below 1000 tokens. 

    Text: 
    {txt}
    """

    completion = client.chat.completions.create(
        model="meta-llama/Llama-3.1-8B-Instruct",
        max_tokens = 1024, 
        temperature = 0.8, 
        messages=[
          {"role": "user", 
           "content": prompt}
        ], 
    )
    return f"{completion.choices[0].message.content}"

def key_features(txt):
    api_token = "EMPTY"
    client = OpenAI(
        #base_url=f"http://localhost:8000/v1",
        base_url=f"http://vllm:8000/v1",
        api_key=api_token,
    )

    prompt = f"""
    I need help extracting the key topics or findings in the following text.
     Note it was parsed from a PDF file to markdown. 

    Please try to keep the summary below 1000 tokens. 

    Text: 
    {txt}
    """

    completion = client.chat.completions.create(
        model="meta-llama/Llama-3.1-8B-Instruct",
        max_tokens = 1024, 
        temperature = 0.8, 
        messages=[
          {"role": "user", 
           "content": prompt}
        ], 
    )
    return f"{completion.choices[0].message.content}"

def critique(txt):
    api_token = "EMPTY"
    client = OpenAI(
        base_url=f"http://vllm:8000/v1",
        #base_url=f"http://localhost:8000/v1",
        api_key=api_token,
    )

    prompt = f"""
    I need help critiquing the following text. Can you read it and evaluate it for 
    any flaws in logic or argument, or highlight any simplifications they made. 
    Note it was parsed from a PDF file to markdown. 

    Please try to keep the summary below 1000 tokens. 

    Text: 
    {txt}
    """

    completion = client.chat.completions.create(
        model="meta-llama/Llama-3.1-8B-Instruct",
        max_tokens = 1024, 
        temperature = 0.8, 
        messages=[
          {"role": "user", 
           "content": prompt}
        ], 
    )
    return f"{completion.choices[0].message.content}"
