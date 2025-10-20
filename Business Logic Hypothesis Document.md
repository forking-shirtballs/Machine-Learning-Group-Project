# **Business Logic Hypothesis Document**

**Project:** CSCI/DASC 6020 – Machine Learning Team Project  
**Date:** October 20, 2025  
**Authors:** Skylar, Cynthia, Rebecca, Curtis

## **1\. Introduction**

This document outlines hypotheses about the underlying business logic embedded in ACME Corporation’s legacy reimbursement system. It integrates analysis from the Product Requirements Document (PRD), employee interviews, and preliminary exploratory data analysis (EDA).

The goal is to reverse-engineer the implicit rules that determine reimbursement amounts and translate them into features, relationships, and testable hypotheses for machine learning models.

## **2\. Business Context Summary**

ACME Corporation’s 60-year-old reimbursement system processes employee travel expenses but lacks transparency and predictability. Employees report inconsistent reimbursements for similar trips and suspect complex, hidden rules embedded over decades of code modifications.

From the PRD and interviews, three primary input drivers were identified:

1. **Trip Duration (`trip_duration_days`)** – determines per diem and length-based adjustments.  
2. **Miles Traveled (`miles_traveled`)** – associated with tiered mileage reimbursement rates.  
3. **Total Receipts (`total_receipts_amount`)** – captures reimbursable expenses, potentially capped or discounted.

Additionally, **timing effects** (e.g., day of submission, quarter of year) and **interaction effects** between variables (e.g., miles per day vs. spending per day) appear to influence outcomes.

## **3\. Interview Insights Summary**

### **3.1 Key Takeaway**

The legacy system frustrates employees due to its *lack of transparency, predictability, and fairness.*

### **3.2 Specific Observed Behaviors**

**Trip Length and Per Diem**

* Base per diem ≈ **$100/day**.  
* **Bonuses:** trips of 4–6 days (“sweet spot”) — especially 5-day trips — tend to receive extra reimbursement.  
* **Penalties:** shorter (\<4 days) or longer (\>6 days) trips often yield less-than-expected reimbursement.

**Mileage Calculations**

* **Tiered structure:**  
  * First 100 miles reimbursed at $0.58/mile.  
  * Rate declines non-linearly beyond 100 miles, possibly logarithmic.  
* **Interaction:** high mileage with modest spending (\<$100/day) is rewarded; low mileage with high spending is penalized.

**Receipt and Spending Patterns**

* **Diminishing returns:** once receipts exceed a spending cap, reimbursements taper off.  
* **Penalty for low spending:** receipts \<$50/day reduce the base per diem.  
* **Optimal ranges:**  
  * Short trips: \<$75/day  
  * Medium (4–6 days): up to $120/day  
  * Long: \<$90/day

**Timing and Randomness**

* **Quarterly effects:** Q4 tends to yield higher reimbursements.  
* **Day-of-week effects:** Tuesday submissions perform best, Friday the worst.  
* **Rounding bugs:** bonuses triggered if receipt totals end in `.49` or `.99`.  
* **Possible “anti-gaming” feature:** system may learn user behavior and reduce payouts for repetitive patterns.  
* **External or random noise:** correlations to pseudo-random or external variables (e.g., market index, lunar cycles) suspected.

**Interacting Factors and Hidden Logic**

* Strong evidence of **non-linear interactions** (e.g., `trip_length × efficiency`, `spending_per_day × total_mileage`).  
* System might use **6 distinct calculation paths**, resembling a decision tree.  
* Reimbursements may include **“efficiency bonuses”** for covering more distance in less time.

### **3.3 Employee Sentiments and Desired Improvements**

| Need | Description | Priority |
| ----- | ----- | ----- |
| Transparency | Clear explanation of reimbursement calculations | High |
| Consistency | Similar trips yield similar outcomes | High |
| Predictability | Ability to estimate reimbursement before travel | High |
| Fairness | Confidence that system treats employees equally | High |
| Simplicity | Streamlined, understandable inputs and outputs | Medium |
| Feedback/Clarity | Explanation of reimbursement breakdown | Medium |

## **4\. Hypothesized Business Rules**

Synthesizing the interviews, PRD, and initial EDA, we propose the following rules governing the legacy reimbursement logic:

| ID | Hypothesis | Rationale / Source | Potential Feature Representation |
| ----- | ----- | ----- | ----- |
| H1 | Base per diem ≈ $100/day with a bonus “sweet spot” for 4–6-day trips, especially 5 days. | Interviews (Lisa, Jennifer); common per diem policy. | `trip_duration_days`, binary flag for 4–6-day range. |
| H2 | Mileage reimbursed at tiered rates: $0.58/mile for first 100 miles, lower thereafter (logarithmic decline). | Interviews (Lisa, Kevin); standard mileage tiers. | `miles_traveled`, log-transformed beyond 100 miles. |
| H3 | Receipts capped: diminishing reimbursement beyond a spending threshold (\~$800). | Interviews (Lisa, Kevin). | Piecewise feature: `min(receipts, cap)` \+ `(receipts > cap)` indicator. |
| H4 | Penalty for low spending (\<$50/day). | Multiple interviews (Lisa, Kevin). | Binary flag: `spend_per_day < 50`. |
| H5 | Interaction bonus: high mileage/day \+ moderate spending (\<$100/day) yields higher payout. | Kevin’s and Marcus’s “efficiency bonus theory.” | Interaction term: `miles_traveled/trip_duration_days × spend_per_day`. |
| H6 | 6 rule pathways based on trip type and efficiency — decision tree structure. | Kevin’s clustering findings. | Classification of trip archetypes. |
| H7 | Timing bias: Q4 and Tuesday submissions increase payout; Fridays lower it. | Interviews (Marcus, Kevin). | Temporal features: `quarter`, `day_of_week`. |
| H8 | Randomization/noise components or rounding bugs (.49/.99 bonus). | Multiple reports. | Derived categorical feature from cents digits of receipts. |
| H9 | Anti-gaming adjustment: employees repeating similar trips get lower reimbursements over time. | Employee feedback; adaptive “learning” theory. | Rolling average of past reimbursements per employee (if available). |

## **5\. Feature Importance Hypotheses**

| Feature | Expected Importance | Explanation |
| ----- | ----- | ----- |
| `trip_duration_days` | High | Base driver for per diem and trip bonuses. |
| `total_receipts_amount` | High | Reflects reimbursable expenses; interacts with duration and caps. |
| `miles_traveled` | Moderate | Tiered mileage rate influences totals, but non-linear. |
| `cost_per_day = total_receipts_amount / trip_duration_days` | Moderate | Captures daily spending efficiency. |
| `cost_per_mile = total_receipts_amount / miles_traveled` | Moderate | Reflects spending efficiency per mile. |
| `day_of_week` | Low–Medium | Tuesday bonuses and Friday penalties. |
| `quarter` | Low–Medium | Q4 trend from interviews. |
| `receipt_cents_pattern` | Low | Possible rounding bug signal. |

## **6\. Potential Non-Linear and Interaction Effects**

The following patterns indicate **non-linear relationships**:

* **Piecewise rules** for per diem, mileage, and spending tiers.  
  **Threshold effects** at 4–6-day trips and 100-mile segments.  
  **Diminishing returns** beyond spending cap (\~$800).  
* **Multiplicative interactions** between `trip_duration_days`, `miles_traveled`, and `total_receipts_amount`.  
* **Categorical splits** consistent with decision tree structures (6 archetypes).

Models such as **Random Forests**, **Gradient Boosting**, and **Polynomial Regression** will help capture these relationships.

## **7\. Initial EDA Findings (to date)**

| Observation | Implication |
| ----- | ----- |
| Strong correlation between trip duration and reimbursement (r ≈ 0.85). | Supports per diem base rule. |
| Nonlinear patterns between mileage and reimbursement. | Suggests tiered rate. |
| High-variance residuals at high receipt totals. | Indicates diminishing returns. |
| Several reimbursement clusters around 4–6-day trips. | Confirms “sweet spot” hypothesis. |

## **8\. Testable Hypotheses and Validation Plan**

| Hypothesis | Testing Method | Evaluation Criteria |
| ----- | ----- | ----- |
| H1: Per diem \+ bonus zone | Linear and polynomial regression on `trip_duration_days` | Coefficient pattern, residual reduction |
| H2: Tiered mileage rate | Decision tree split visualization | Split thresholds near 100 miles |
| H3: Spending cap | Piecewise regression, tree models | RMSE reduction for capped feature |
| H4: Low-spending penalty | Binary regression flag | Significant negative coefficient |
| H5: Efficiency interaction | Feature interaction term | SHAP feature interaction strength |
| H6: Decision path segmentation | Clustering \+ rule extraction | Group separability, rule interpretability |
| H7: Timing bias | Add temporal features | Mean difference analysis |
| H8: Rounding anomaly | Test cents digit correlation | t-test or feature importance ranking |
| H9: Anti-gaming effect | Temporal sequence analysis (if data permits) | Regression over repeated trips |

## **9\. Assumptions and Limitations**

* Interviews reflect employee perceptions, not formal documentation.  
* Policy changes over decades could cause inconsistencies.  
* Some features (e.g., submission day, employee ID) may not exist in current dataset.  
* The “randomness” or external noise factor may not be recoverable from available data.

## **10\. Next Steps**

1. Engineer hypothesized features (e.g., `spend_per_day`, `efficiency_ratio`, tiered mileage bins).  
2. Train baseline linear and tree-based models to detect threshold and interaction patterns.  
3. Use SHAP/LIME interpretability tools to validate which hypotheses align with model behavior.  
4. Iterate feature adjustments and rule tests based on model results.  
5. Document confirmed vs. rejected hypotheses in the final technical report.

## **11\. References**

* ACME Corporation PRD  
* Employee Interview Transcripts (Marcus, Lisa, Dave, Jennifer, Kevin)  
* Top Coder Challenge: *Black Box Legacy Reimbursement System* ([GitHub](https://github.com/8090-inc/top-coder-challenge))  
* Corporate Travel & Expense Management Industry Guidelines

