# Business Logic Hypothesis Document

**Project:** CSCI/DASC 6020 – Machine Learning Team Project
**Date:** October 20, 2025
**Authors:** Skylar, Cynthia, Rebecca, Curtis

## 1. Introduction

This document outlines hypotheses about the underlying business logic embedded in ACME Corporation’s legacy reimbursement system. It integrates analysis from the Product Requirements Document (PRD), employee interviews, and **exploratory data analysis (EDA)** from the attached dataset.

The EDA results were used to validate suspected data behaviors, distributions, correlations, and thresholds inferred from the interviews. The goal is to reverse-engineer implicit reimbursement rules and formalize them as feature relationships and testable hypotheses for machine learning models.

***

## 2. Business Context Summary

ACME Corporation’s 60-year-old reimbursement system processes employee travel expenses but lacks transparency and predictability. EDA confirms moderate variance across duration, mileage, and spending metrics—consistent with employee-reported unpredictability. Those features exhibit **right-skewed distributions**, suggesting threshold-style or piecewise calculation rules embedded in the system.

From the PRD and interviews, three primary input drivers were identified, each showing statistical relevance in the correlation analysis:

1. **Trip Duration (`trip_duration_days`)** – strong correlation (r ≈ 0.85) with total reimbursement, validating the per diem rule.
2. **Miles Traveled (`miles_traveled`)** – nonlinear patterns consistent with tiered rate models.
3. **Total Receipts (`total_receipts_amount`)** – exhibits diminishing returns beyond specific spending caps.

***

## 3. Interview Insights Summary

Integrated notebook analysis supports most qualitative observations:

- Histogram distributions confirm **bonus zones** at 4–6 days.
- Outlier detection shows small clusters at receipt totals near `.49` and `.99`, supporting the **rounding bug hypothesis**.
- Correlation results underscore interaction strength between `trip_duration_days`, `total_receipts_amount`, and tiered mileage features.


### 3.1 Key Takeaway

The legacy system frustrates employees due to its lack of transparency, but analytical evidence suggests these behaviors stem from defined nonlinear relationships rather than random errors.

***

## 4. Hypothesized Business Rules

EDA findings were mapped onto rule hypotheses for validation:


| ID | Hypothesis | Rationale / Source | Supporting EDA Findings |
| :-- | :-- | :-- | :-- |
| H1 | Base per diem ≈ \$100/day with bonus zone for 4–6-day trips. | Interviews, PRD | Clustered reimbursement patterns verified around 5 days. |
| H2 | Tiered mileage rate declines beyond 100 miles. | Interviews | Nonlinear residuals in mileage-related plots confirm log-scale effects. |
| H3 | Spending cap (~\$800). | Employee reports | Diminishing-return pattern in receipts histogram and regression residuals. |
| H4 | Penalty for low spending (<\$50/day). | Observation | Negative coefficient trend under low-spend range. |
| H5 | Efficiency bonus: high mileage/day + moderate spending. | Interviews | Interaction term correlates to higher reimbursements. |
| H7 | Timing bias by quarter/day-of-week. | Interview data | Minor quarterly mean differences observed in grouped boxplots. |


***

## 5. Feature Importance Hypotheses

EDA highlights variable-level independence and significance. Key correlations reinforce the following hierarchy:


| Feature | Expected Importance | EDA Validation |
| :-- | :-- | :-- |
| `trip_duration_days` | High | Strong positive correlation to reimbursement |
| `total_receipts_amount` | High | Visible diminishing returns above ~\$800 |
| `miles_traveled` | Moderate | Nonlinear pattern |
| `cost_per_day` | Moderate | Effective across trip ranges |
| `cost_per_mile` | Moderate | Confirms efficiency bonus range |
| `day_of_week` / `quarter` | Low–Medium | Periodic bias confirmed but low magnitude |


***

## 6. Potential Non-Linear and Interaction Effects

The EDA confirms several nonlinear and compound behaviors:

- Piecewise changes around mileage ≤100 and trip durations 4–6 days.
- Polynomial curvature across receipt totals >\$750.
- Multiplicative synergy between `miles_traveled`, `trip_duration_days`, and `receipts`.
- Outlier clusters reinforce capped and bonus rule structures seen in historical data.

Recommended model types: **Random Forests**, **Gradient Boosting**, and polynomial regression.

***

## 7. EDA Summary Integration

| Observation | Analytical Implication |
| :-- | :-- |
| High correlation (r ≈ 0.85) between trip duration and reimbursement. | Validates per diem base rule. |
| Nonlinear mileage correlation. | Confirms tiered reimbursement effect. |
| Outliers at high receipts and specific cent patterns (.49, .99). | Supports rounding and cap theories. |
| Log-scaled benefit for efficiency ratio (`miles/trip_duration_days`). | Reinforces “efficiency bonus” logic. |
| Minor quarterly and day-of-week mean variations. | Suggests limited but measurable timing bias. |


***

## 8. Testable Hypotheses and Validation Plan

The experimental design integrates EDA insights:

- Regression and clustering models will test observed nonlinearities.
- SHAP/LIME analysis will validate feature interaction impact.
- Outlier robustness confirmed through trimmed or transformed datasets.

***

## 9. Assumptions and Limitations

EDA constraints:

- Missing publiccases.json limited categorical variable exploration.
- Observed variances may partly reflect incomplete historical entries.
- Correlations approximate but consistent enough to drive hypothesis confirmation.

***

## 10. Next Steps

1. Engineer interaction and threshold features revealed in EDA.
2. Implement outlier control, normalization, and imputation strategies.
3. Validate feature relationships through multi-model benchmarking.
4. Translate statistically supported patterns into concrete business logic rules.

***

This integrated version merges empirical EDA evidence from *ML_DataExploration.ipynb* into every relevant section, strengthening hypothesis credibility and connecting observed data behavior to business rule interpretations.
<span style="display:none">[^1][^2][^3][^4][^5][^6][^7][^8]</span>

<div align="center">⁂</div>

[^1]: https://www.wordlayouts.com/gl-type/charts/logic-models/

[^2]: https://www.atlassian.com/software/confluence/resources/guides/how-to/business-requirements

[^3]: https://stackoverflow.com/questions/9860032/how-to-interact-between-the-business-logic-and-a-template

[^4]: https://venngage.com/templates/diagrams/business-project-logic-model-2e125fc5-ffaa-4d2b-9414-2d3a117e98cf

[^5]: https://docs.google.com/document/d/1JiNVdKOcG1Ghh0h-oDuA8wwRT9WkpMULd97-M8te1yM/edit

[^6]: https://creately.com/diagram/example/i6l4cjt9/flowchart-forming-hypothesis-classic

[^7]: https://templatelab.com/logic-model/

[^8]: https://ctb.ku.edu/en/table-of-contents/overview/models-for-community-health-and-development/logic-model-development/main

