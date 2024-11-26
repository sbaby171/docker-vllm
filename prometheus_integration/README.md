# Overview



```
docker compose up --build
```


## Access Prometheus and Grafana Interfaces
Prometheus: Visit `http://localhost:9090` to access the Prometheus web UI.
Grafana: Visit `http://localhost:3000` to access the Grafana dashboard.
Default Credentials: Username: admin, Password: admin (you will be prompted to change this upon first login).


## Configure Grafana to Use Prometheus Data Source (Optional)
1. Add Data Source:
    * Navigate to Configuration > Data Sources.
    * Click Add data source.
    * Select Prometheus.
    * Set the URL to `http://prometheus:9090`.
    * Click Save & Test to verify the connection.

2. Import Dashboards:
    * You can import existing dashboards or create new ones to visualize vLLM metrics.
    * Click on Create > Import and enter a dashboard ID from Grafana's dashboard repository.

## Verify Metrics Collection
1. In Prometheus:
    * Go to Status > Targets.
    * Ensure that the vllm target is listed and the state is UP.
2. In Grafana:
    * Create a new dashboard.
    * Add a panel with a Prometheus query like `vllm_request_count_total` to visualize metrics.

## Understanding vLLM Metrics
vLLM exposes several metrics by default, such as:

- Request Metrics:
    * vllm_request_count_total: Total number of requests.
    * vllm_request_duration_seconds: Duration of requests.

- Token Metrics:
    * vllm_tokens_generated_total: Total number of tokens generated.
    * vllm_token_generation_duration_seconds: Time taken to generate tokens.

These metrics can be used in Prometheus queries and Grafana dashboards to monitor the performance and usage of your vLLM server.
