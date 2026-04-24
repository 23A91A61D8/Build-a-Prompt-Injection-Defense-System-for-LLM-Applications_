from flask import Flask, request, jsonify
from middleware.security_middleware import SecurityMiddleware

app = Flask(__name__)
middleware = SecurityMiddleware()


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")

    # Process input
    processed_input = middleware.process_input(user_input)

    if "Blocked" in processed_input:
        return jsonify({"response": processed_input})

    # Simulated LLM response (replace with real LLM if needed)
    llm_response = f"LLM Response: {processed_input}"

    # Process output
    safe_output = middleware.process_output(llm_response)

    return jsonify({"response": safe_output})


if __name__ == "__main__":
    app.run(debug=True)