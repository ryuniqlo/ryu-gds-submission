# ryu-gds-submission

## Introduction
This repository contains Python code for Task 1 - processing restaurant data retrieved from an external API.

## Instructions
### Running the Code Locally
To run the source code locally on your laptop, follow these steps:

1. Clone the repository locally
```
git clone https://github.com/ryuniqlo/ryu-gds-submission.git
```
2. Navigate to the project directory
```
cd ryu-gds-submission
```
3. Install the required dependencies
```
pip install -r requirements.txt
```
4. Run the main script
```
python main.py
```

## Assumptions
- Restaurant data is always retrieved from the API endpoint provided in the assessment details.
- Input data will always be in the same format.
- Empty/Null values are populated as 'NA'.
- For Q1: All relevant countries are in the mapping xlsx file, anything not in it will be regarded as irrelevant and value will just be populated as NA.
- For Q3: Anything below 2.5 is to be classified as Poor.
- Since we are not doing analysis in this context, I did not remove dummy rows or dirty data.

## Notes
- Unit tests are included to ensure the correctness of the implemented functionalities. In the event that changes are made to the code, I can run these unit tests to ensure that output is still accurate and as expected.
- Do run the code to get the output csv files for Q1 and Q2!
