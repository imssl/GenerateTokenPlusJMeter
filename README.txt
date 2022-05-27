# https://jmeter.apache.org/download_jmeter.cgi
# Download Jmeter as zip, extract and rename the folder as "apache-jmeter".
# Copy the JSON file including KeyID GUIDs into current directory named as "guids.json".
# Copy the DynamicTokenTest.py Python script into current directory.
# Copy the DynamicTokenTest.jmx JMeter script into current directory.
# Copy the License Request into current directory and rename it as "LicenseRequest.bin".
# In case of permission errors: sudo chmod 777 createToken.py DynamicTokenTest.sh
# Make sure to move the test results into another directory for future performance comparisions, because script deletes TestResults folder belonging to previous tests.  

Usage:
./DynamicTokenTest.sh <tokenCount> <randGuidCount> <users> <rpm> <duration> <host>

tokenCount : Quantity of the tokens to be generated.
randGuidCount : Quantity of the random KeyIDs to be selected from the JSON file.
users : Quantity of the threads.
rpm : Request per Minute.
duration : Duration of whole test.
host : License Server API http|https hostname or IP Address. Endpoint "/AcquireLicense" is hardcoded in "DynamicTokenTest.jmx" JMeter configuration file.

Example:
./DynamicTokenTest.sh 100 5 3 300 60 https://10.0.6.96/
