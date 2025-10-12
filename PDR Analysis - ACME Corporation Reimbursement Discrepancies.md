# **PDR Analysis \- ACME Corporation Reimbursement Discrepancies**

## **Summary**  
ACME Corporation is trying to understand why its newly developed reimbursement system produces different results from a legacy system that’s been in use for over 60 years. The original system is a black box—its source code is inaccessible, its logic undocumented, and its outputs often seem inconsistent or illogical. To bridge the gap, our goal is to reverse engineer the legacy system by training a machine learning model that mimics its behavior, including quirks and suspected bugs. Using 1,000 labeled historical cases and employee insights, the model will be tested for accuracy against both public and private datasets to ensure it closely replicates the legacy system’s outputs.

## **Problem**

* ACME Corp has been using same system for 60 years  
  * Frequent anomalies observed: inconsistent handling of receipts; unpredictable reimbursements; odd behavior related to trip length, and trip distances  
  * No one understands how it works  
  * Source code is inaccessible  
  * Documentation of system’s logic is unavailable  
* New system has been developed  
  * Discrepancies between new system results and old system results

## **Current Process**

* Old system input:  
  * Number of days traveled  
  * Total miles traveled  
  * Total cost of trip, submitted in receipts  
* Old system output:  
  * Single numeric reimbursement amount  
  * Issues:  
    * No breakdown or explanation of reimbursement  
    * Some reimbursements appear illogical (possible bugs in system or past modifications?)

## **Goal**

* Reverse engineer ACME Corp’s legacy reimbursement system to help the company understand how the old system functions and why there are discrepancies between the new and old systems.

## **Product Description**

* Build a reimbursement ML model that does the following  
  * Accepts same input parameters  
  * Produces same output of legacy system  
  * Matches behavior, including edge cases and possible bugs, of legacy system  
* Data needed:  
  * [1000 historical input/output example](https://github.com/8090-inc/top-coder-challenge/blob/main/public_cases.json) \- public\_cases.json  
  * [Employee interviews](https://github.com/8090-inc/top-coder-challenge/blob/main/INTERVIEWS.md)

## **Requirements and Success Criteria**

* Our ML system must:   
  * Match the legacy system’s output  
  * Handle all 1000 cases with minimal/zero deviation  
  * Known/suspected bugs must remain (be reflected in our output)  
* Testing cases  
  * Test our model against the 1000 public\_cases.json  
    * Answers provided in file to allow us to iterate on our solution  
  * Test our model against the 5000 private\_cases.json  
    * No answers provided  
* Success \= how close our system outputs compare to legacy system outputs
