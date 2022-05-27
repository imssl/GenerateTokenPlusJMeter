import json
import jwt
import base64
import random
import sys

# Quantity of the tokens to be generated.
tokenCount = int(sys.argv[1])

# Quantity of the Key GUIDs to be selected from the JSON file.
randGuidCount = int(sys.argv[2])

# Communication Key GUID and Communication Key as base64.
communicationKeyId = "69e54088-e9e0-4530-8c1a-1eb6dcd0d14e"
communicationKeyAsBase64 = "SGEpLQJ+JpeRCTMn5izu/b6kiaTH5aSXTMkEuED9fA8="

# Defining array tokens to be appended.
tokens = []

# Main loop to create the tokens.
for x in range(0, tokenCount):

    # Defining/Erasing arrays.
    guidRows = []
    keyIds = []

    # One of the Key GUID is going to be static.
    StaticKeyId = {"id": "7459975d-b2f8-48ed-a325-56e4f34d19c7"}
    keyIds.append(StaticKeyId)

    # Open and read the JSON file containing Key GUIDs.
    with open("guids.json") as f:
        data = json.load(f)

    # Random row numbers are generated.
    for i in range(0, randGuidCount):
        guidRows.append(random.randint(0, len(data)-1))

    # GUIDs are selected using random row numbers.
    for k in guidRows:
        KeyId = {"id": data[k]["id"]}
        keyIds.append(KeyId)

    # Entitlement Message JSON.
    entitlementMessage = {
        "type": "entitlement_message",
        "version": 2,
        "content_keys_source": {
            "inline": keyIds
        }
    }

    # License Server Message JSON.
    licenseServiceMessage = {
      "version": 1,
      "com_key_id": communicationKeyId,
      "message": entitlementMessage
    }

    # Create the token.
    communicationKey = base64.b64decode(communicationKeyAsBase64)
    jwtAsString = jwt.encode(payload=licenseServiceMessage, key=communicationKey, algorithm='HS256').decode()
    tokens.append(jwtAsString)

# Print the tokens into a .csv file.
f = open('tokens.csv', 'w')
for token in tokens:
    f.write(token+'\n')
f.close()
