from flask import escape
import functions_framework


@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """

    # json gets data from POST requests; args gets from from URL
    request_json = request.get_json(silent=True)
    request_args = request.args

    print(f'request_json: {request_json}')
    print(f'request_args: {request_args}')

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'

    if request_json and 'age' in request_json:
        age = request_json['age']
    elif request_args and 'age' in request_args:
        age = request_args['age']
    else:
        age = 99



    return f'Hello {name} of age {age}!'