import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
data =  {
  "Inputs": {
    "WebServiceInput0": [
      {
        "Bp": 80.0,
        "Sg": 1.02,
        "Al": 80.0,
        "Su": 80.0,
        "Rbc": 80.0,
        "Bu": 80.0,
        "Sc": 1.2,
        "Sod": 137.53,
        "Pot": 4.63,
        "Hemo": 15.4,
        "Wbcc": 80.0,
        "Rbcc": 5.2,
        "Htn": 80.0,
        "Class": 1
      },
      {
        "Bp": 80.0,
        "Sg": 1.02,
        "Al": 80.0,
        "Su": 80.0,
        "Rbc": 80.0,
        "Bu": 80.0,
        "Sc": 0.8,
        "Sod": 137.53,
        "Pot": 4.63,
        "Hemo": 11.3,
        "Wbcc": 80.0,
        "Rbcc": 4.71,
        "Htn": 80.0,
        "Class": 1
      },
      {
        "Bp": 80.0,
        "Sg": 1.01,
        "Al": 80.0,
        "Su": 80.0,
        "Rbc": 80.0,
        "Bu": 80.0,
        "Sc": 1.8,
        "Sod": 137.53,
        "Pot": 4.63,
        "Hemo": 9.6,
        "Wbcc": 80.0,
        "Rbcc": 4.71,
        "Htn": 80.0,
        "Class": 1
      },
      {
        "Bp": 80.0,
        "Sg": 1.005,
        "Al": 80.0,
        "Su": 80.0,
        "Rbc": 80.0,
        "Bu": 80.0,
        "Sc": 3.8,
        "Sod": 80.0,
        "Pot": 2.5,
        "Hemo": 11.2,
        "Wbcc": 80.0,
        "Rbcc": 3.9,
        "Htn": 80.0,
        "Class": 1
      },
      {
        "Bp": 80.0,
        "Sg": 1.01,
        "Al": 80.0,
        "Su": 80.0,
        "Rbc": 80.0,
        "Bu": 80.0,
        "Sc": 1.4,
        "Sod": 137.53,
        "Pot": 4.63,
        "Hemo": 11.6,
        "Wbcc": 80.0,
        "Rbcc": 4.6,
        "Htn": 80.0,
        "Class": 1
      }
    ]
  },
  "GlobalParameters": {}
}

body = str.encode(json.dumps(data))

url = 'http://57739a58-adf3-4d4f-b4b3-1f904d5d85d5.eastus.azurecontainer.io/score'
api_key = 'jBQ0sSaF4QEyZEGNY985aYga6tb5Zasy' # Replace this with the API key for the web service

# The azureml-model-deployment header will force the request to go to a specific deployment.
# Remove this header to have the request observe the endpoint traffic rules
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))