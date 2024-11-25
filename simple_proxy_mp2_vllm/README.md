




# Overview
This example uses a docker-compose file to tied together a proxy server and two 
separate vLLM docker containers. A simple client side script it provided. 

The key objective here was to separate two instances of an LLM model and direct
traffic to each of them from a proxy server. 

## The Proxy Server
The proxy server is merely meant to open a fixed port for client side apps 
and redirect the LLM prompt to either 8000 or 8080 port. These ports are all 
parameterized in the docker-compose and docker file. 

The proxy server simply alternates between each port. In a proper application 
some load balancing logic can be used or some other custom logic. 


## vLLM Docker containers
For the vLLM docker containers we intergrated the following docker container calls
into the docker-compose file.


```
docker run --runtime nvidia --gpus device=0 \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HUGGING_FACE_HUB_TOKEN=hf_<key>" \
    -p 8000:8000 \
    --ipc=host vllm/vllm-openai:latest \
    --model meta-llama/Llama-3.2-1B-Instruct
```


```
docker run --runtime nvidia --gpus device=1 \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HUGGING_FACE_HUB_TOKEN=hf_<key>" \
    -p 8080:8000 \
    --ipc=host vllm/vllm-openai:latest \
    --model meta-llama/Llama-3.2-1B-Instruct
```

## Client code
The client simply passes the prompt via OpenAI API text generation. Use port 5000
to talk to the proxy server. 



# Building the container 

To build the container: 
```
docker-compose up --build -d 
```

To ensure its working: 
```
docker-compose ps
```

To spin down the containers: 
```
docker-compose down
```


