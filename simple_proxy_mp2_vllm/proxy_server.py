from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Logic to decide which backend to forward the request to
def choose_backend():
    # Example logic: Alternate between ports based on a counter
    # Replace this with your own custom logic
    if hasattr(choose_backend, "counter"):
        choose_backend.counter += 1
    else:
        choose_backend.counter = 0

    #return "http://localhost:8000/v1" if choose_backend.counter % 2 == 0 else "http://localhost:8080/v1"

    #return "http://vllm_gpu_0:8000" if choose_backend.counter % 2 == 0 else "http://vllm_gpu_1:8000"
    return "http://vllm_gpu_0:8000/v1" if choose_backend.counter % 2 == 0 else "http://vllm_gpu_1:8000/v1"

@app.route("/v1/chat/completions", methods=["POST"])
def handle_request():
    # Choose which backend to forward the request to
    backend_url = choose_backend()
    
    # Forward the incoming request to the chosen backend
    try:
        headers = {key: value for key, value in request.headers if key != "Host"}
        response = requests.post(
            backend_url + "/chat/completions",
            headers=headers,
            json=request.get_json(),
            stream=request.headers.get("accept", "") == "text/event-stream"
        )
        
        # Stream the response for compatibility with OpenAI API
        def generate():
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    yield chunk
        
        return app.response_class(generate(), headers=dict(response.headers), status=response.status_code)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def health_check():
    return "Proxy server is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

