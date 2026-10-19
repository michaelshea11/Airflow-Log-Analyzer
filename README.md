***README***
This project was intended to be a log that iterates through the various logs created by an Airflow scheduler.

However, because I was not able to start the Airflow scheduler in the project this log analyzer is referencing,
I simply had to make do with the example script that was provided for me.

I attempted to make a mock Airflow log file with Google Gemini, but to no avail. 
I ended up just pointing the log analyzer to an Airflow DAG Processor log in my Airflow log folder.

I learned a lot about Pathlib, specifically the .rglob method in this project. 

I hope to build on this in the future by hopefully getting an Airflow scheduler 
to run in Docker instead of in a virtual environment on my local machine so that 
I can actually analyze a log.

Thank you for reading this README.
