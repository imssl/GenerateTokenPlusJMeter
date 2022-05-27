tokenCount=$1
randGuidCount=$2
users=$3
rpm=$4
duration=$5
host=$6

echo "Generating Tokens."
sudo python3 createToken.py $tokenCount $randGuidCount
echo "Running the JMeter Test Scenario:"
./apache-jmeter/bin/jmeter -n -t DynamicTokenTest.jmx -l testresults.jtl -Jusers=$users -Jrpm=$rpm -Jduration=$duration -JTestIP=$host -Jrequest=LicenseRequest.bin -Jtokens=tokens.csv
echo "Deleting previous test report if there is."
if [ -d "TestResults" ]; then
   sudo rm -R TestResults
fi
echo "Creating the test report. Moving jmeter.log and testresults.jtl into TestResults folder."
./apache-jmeter/bin/jmeter -g testresults.jtl -o TestResults
sudo mv jmeter.log TestResults/
sudo mv testresults.jtl TestResults/
echo "Finished."
