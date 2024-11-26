This much of this code is pulled directly from: https://github.com/vllm-project/vllm/tree/main/examples/production_monitoring

## Overview: 
i


## Launch vLLM: 
```
vllm serve mistralai/Mistral-7B-v0.1 \
    --max-model-len 2048 \
    --disable-log-requests
```


## Build the Docker containers
```
docker compose up --build
```

## Download dataset: 
```
wget https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/resolve/main/ShareGPT_V3_unfiltered_cleaned_split.json
```

## Run vLLM Benchmarking Server script
python3 ../../benchmarks/benchmark_serving.py \
    --model mistralai/Mistral-7B-v0.1 \
    --tokenizer mistralai/Mistral-7B-v0.1 \
    --endpoint /v1/completions \
    --dataset-path ShareGPT_V3_unfiltered_cleaned_split.json \
    --request-rate 3.0
```

**NOTE** - I removed the line `--dataset-name sharegpt` because it was throwing an error for me. 


Navigating to http://localhost:8000/metrics will show the raw Prometheus metrics being exposed by vLLM.

Grafana Dashboard
Navigate to http://localhost:3000. Log in with the default username (admin) and password (admin).

Add Prometheus Data Source
Navigate to http://localhost:3000/connections/datasources/new and select Prometheus.

On Prometheus configuration page, we need to add the Prometheus Server URL in Connection. For this setup, Grafana and Prometheus are running in separate containers, but Docker creates DNS name for each containers. You can just use http://prometheus:9090.

Click `Save & Test`. You should get a green check saying "Successfully queried the Prometheus API.".

Import Dashboard
Navigate to http://localhost:3000/dashboard/import, upload grafana.json, and select the prometheus datasource. 

Lastly, if the panels are empty, you may need to update the model name in the input text box above panel. Thats what I had to do.  
