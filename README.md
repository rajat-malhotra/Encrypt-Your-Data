# Encrypt-Your-Data

- Data masking utility written in Python which implements pseudonymization and annonmyzation of data using bouncy castle's FPE encryption algorithms.

# System requirements

- python version >= 3.8

# To-do's

- [x] Implement CSV reader and Writer
- [] Implement logic to encrypt data using bouncy castle FF1 algorithm
- [] Engineer the decrption logic
- [] Class to delete keys for anonmyzation
- [] Logic to write the encrypted data paired with it's encrytping key to a CSV (preferably s3 location)
- [] Write Unit tests (80% coverage)
- [] Implement functionality in AWS to stream data (kafka/kinesis) into an S3 bucket -> Pseudonymize it -> write to an S3 location for consumption
