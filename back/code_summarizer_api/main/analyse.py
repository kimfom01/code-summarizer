from flask import Blueprint, request, jsonify

analyse = Blueprint("analyse", __name__)


@analyse.route("/analyse", methods=["POST"])
def analyse_code():
    try:
        # Extract the code snippet from the request
        data = request.json
        code_snippet = data.get("code")

        if not code_snippet:
            return jsonify({"error": "No code snippet provided"}), 400

        # Placeholder for the code analysis and documentation (for now, just return a success message)
        analysis_result = f"Analysis of the code: {code_snippet}"

        return jsonify({"result": analysis_result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
