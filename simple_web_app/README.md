# Overview 

In this demo, I wanted to create a simple web-application that allows 
the user to paste a PDF URL and select if they want to have it summarized, 
key features listed, or critiqued. 

It runs with a vLLM docker container in the backend. My local setup 
is 2x 4090s. So if you have more or less hardware, then be sure to 
change the docker-compose file as necessary. 

## Web app
placeholder

## vLLM Docker container

To run the vLLM docker container directly, you can use something like below - 
be sure to change it based on your needs: 
```
docker run --runtime nvidia --gpus all \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HUGGING_FACE_HUB_TOKEN=hf_XXX" \ 
    -p 8000:8000 \
    --ipc=host vllm/vllm-openai:latest \ 
    --tensor-parallel-size 2 \    
     --model meta-llama/Llama-3.1-8B-Instruct
```
**NOTE** the docker-compose file has this functionality integrated. 


