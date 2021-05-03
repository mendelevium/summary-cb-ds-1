from flask import Flask, request
import json

APP_NAME = 'example_model'
app = Flask(APP_NAME)
HTTP_ERROR_CLIENT = 400
HTTP_ERROR_SERVER = 500
EXPECTED_KEYS = ['age', 'income']

def validate_json(j):
    """
    Validate that the input has the expected format
    """
    try:
        # Make input into a python dict
        if not isinstance(j, dict):
            d = json.loads(j)
        else:
            d = j
    except Exception as e:
        raise ValueError(e)
    for ek in EXPECTED_KEYS:
        if ek not in d:
            raise ValueError(
                f"Expected key {ek} not in JSON\n{j}"
            )
    return d


def model_computation(j):
    """
    This is our "model"
    """
    return 3 * j['age'] - 2* j['income']


@app.route('/', methods=['GET'])
def model_info():
    """
    Returns expected input format
    """
    return str(
        """
        Expected JSON input:
        {
            "age" : NUMBER
            "income" : NUMBER
        }
        """
    )

@app.route('/', methods=['POST'])
def model_computation_main():
    """
    Main Model server round trip method
    """
    try:
        # This gets the data field in the post request
        j = validate_json(request.data)
        # Return a JSON back out
        return json.dumps({"result": model_computation(j)})
    except ValueError as ex:  # failed schema/values validation
        return json.dumps({ "Incorrect JSON format:\n": str(ex)}), HTTP_ERROR_CLIENT
    except Exception as ex:
        return json.dumps({ "Server Error:\n": str(ex)}), HTTP_ERROR_SERVER

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)