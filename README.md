# DocuSign Downloader

Selenium Python script that will download all the envelopes stored in DocuSign that you have access to.

**Disclaimer**

This script has only been tested with Python 3 on MacOS.

**Requirements:**
1. Working installation of Selenium and Python. If you don't already have this, Google is your friend ;)
2. A CSV with the IDs of all the envelopes that you want to download. To create this CSV, sign into DocuSign and go to the reports page and click the [Envelope Report](https://app.docusign.com/reports/6/S6). Select the date range and filters to get the list of envelopes you want to download. Now edit columnes and ensure that "Envelope ID" is the only column selected. Click "Download CSV" and save it in the same folder as the python script as `envelopes.csv`.

With the requirements in place, just run the `docusign.py` script, enter your credentials and watch the downloads folder fill up with your envelopes.

Please feel free to provide feedback on any bugs or suggestions for improvement that you may have.
