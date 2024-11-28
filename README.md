# docker-vllm
A collection of simple Docker files for vLLM and web based applications


## Quick Reference - vLLM serve
```
docker run --runtime nvidia --gpus all \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HUGGING_FACE_HUB_TOKEN=hf_XXX" \
    -p 8000:8000 \
    --ipc=host vllm/vllm-openai:latest \
    --tensor-parallel-size 2 \
     --model meta-llama/Llama-3.1-8B-Instruct
```
**NOTE** - the may HUGGING_FACE_HUB_TOKEN not be necessary. 
