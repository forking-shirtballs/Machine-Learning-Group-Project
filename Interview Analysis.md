**Interview Analysis**

***Key Takeaway:** Current legacy system frustrates employees due to its lack of transparency and predictability*

**Overview:** The sections titled *Analysis of Specific System Behaviors* and *Employee Sentiments and Desired Improvements* summarize insights from interviews with five ACME Corporation employees about their experiences with the legacy reimbursement system. The *Employee Interview Data* section summaries of each interview, is also included if further information is needed.

**Analysis of Specific System Behaviors**

1. **Trip Length and Per Diem**  
   * Base Rate: $100 per diem  
   * Bonuses:  
     * 4 \- 6 day trips (“Sweet Spot”) treated pretty well  
     * 5 day trips almost always receive bonus  
   * Penalties: trips shorter that 4 days or longer than 6 days often receive less than expected

2. **Mileage Calculations**  
   * Tiered rates  
     * First 100 miles receives $0.58/mile  
     * Drops off after 100 miles, not linear, most likely logarithmic  
   * Interaction Effects: mileage is related to spending  
     * High mileage (180-220 miles/day) with modest spending (\<$100/day) do well  
     * Low mileage and high spending do worse

3. **Receipt and Spending Patterns**  
   * Diminishing returns: cap/penalty for high spending  
     * Once a certain dollar amount is reached (the cap), any amount over the cap is reimbursed at a lower rate  
   * Penalties for low spending: submitting receipts with low amounts (\<$50) reduces the base per diem  
     * Employees are better off not submitting low valued receipts  
   * Optimal Ranges Based on Trips by Length  
     * Short trips \- spend under $75/day  
     * Medium trips (4-6 days) \- spend up to $120/day  
     * Long trips \- spend under $90/day

4. **Timing and Randomness**  
   * Certain quarters and days may result in better reimbursements  
     * End of Q4 has performed better  
     * Tuesday receipt submissions performs the best of all days of the week  
   * Anti-Gaming Learning Component  
     * System may learn submissions of employees over time and diminish returns as a result to prevent employees of “playing” the system for bigger rewards  
   * Rounding and “Bugs”  
     * Bonus received if receipt ends in .49 or .99   
     * Rounds up twice, in favor of the employee  
   * External Correlation \- noise may be present  
     * Possibilities include: external data source, pseudo-randomization  
     * Cited reasons: market indices, lunar cycles

5. **Patterns in Data and Possible Interactions Between Factors**  
   * trip length x efficiency  
   * spending/day x total mileage  
   * 6 different calculation paths depending on trip characteristics (decision tree?)

**Employee Sentiments and Desired Improvements**

| *Need* | *Description* | *Priority* |
| ----- | ----- | :---: |
| Transparency | Clear explanation and understanding of how reimbursements are calculated | High |
| Consistency | Similar trips receive similar reimbursements | High |
| Predictability | Ability to estimate reimbursement before a trip | High |
| Fairness | Confidence that all employees are treated fairly by the system | High |
| Simplicity | Easy to understand inputs and outputs | Medium |
| Feedback/Clarity | Post-submission breakdown or explanation | Medium |

**Employee Interview Data**

***Regional Sales Director (Marcus)***

* System is unpredictable  
* Different reimbursements when same trip was taken twice, two weeks apart  
  * Cleveland → Detroit  
  * 180 miles driving  
  * 3 days  
  * hotel  
  * $847 first time, $623 two weeks later  
* Theory \- reimbursement amounts depend on time of the month  
* Discrepancy between reimbursement based on trips that include a lot of travel vs trips that involve little travel  
* Discrepancy between reimbursement based on mileage of shorter trips vs longer trips  
* Discrepancy between amount spent in expenses vs reimbursement amount  
  * Reimbursement usually less when spending is higher  
* Reimbursements possibly more at end of Q4  
* Other possible theories at workplace:  
  * Magic number theory \- certain number of receipt totals get good reimbursements (people think $847 is a “lucky” number)  
  * Efficiency bonus theory \- extra money for covering more ground in a short time  
  * Rounding bug theory \- if receipt ends in certain cents amount, system errors calculation against your favor

***Senior Staff Accountant (Lisa)***

* Seems to be a per diem base rate of $100, some adjustments unclear after that  
* 5 day trips usually get extra bonus (4 day and 6 day trips receive normal rates)  
  * One instance where a 5 day trip did not get bonus  
* Does not see clear patterns with quarterly variations  
* Mileage is tiered  
  * First 100 miles \- full rate ($0.58/mi)  
  * Rate drops after 100 miles  
    * Thinks drop is logarithmic, has a curve \- tried mapping it in Excel  
  * Has seen evidence that disputes Marcus’s claim that 800 mile trips get better per mile rate than 600 mile trips  
* Receipt reimbursement not proportional  
  * “Weird” curve  
    * Med/high amounts ($600-800) get good returns  
    * Diminishing returns on anything over $800  
    * Very low amounts ($50) also penalized  
* System does not categorize trips  
* Seems to be different calculation paths for trips \- quick trips, high mileage treated differently than long trips, low mileage  
* Bonuses for people who cover a lot of ground in short amount of time \- unsure about bonus calculation  
* Think rules, exceptions, and adjustments have been added to the system over time  
* Bonus if receipt ends in .49 or .99 \- rounds up twice?  
* Variations in reimbursement for same person, same type of trip has been observed, can’t figure out what pattern is

***Regional Marketing Manager (Dave)***

* Mileage reimbursement  
  * Austin \- good   
    * 4 days, normal expenses, 100 miles driving around city  
    * May  
  * Phoenix \- worse than Austin  
    * Similar to Austin  
    * September  
  * Chicago \- good  
    * 300 miles away  
  * Indianapolis \- mileage seemed higher per mile  
    * Closer than 300 miles away  
* Discrepancy between similar week long trips taken to 3 cities, other employee received higher reimbursement  
* Submitting receipts for small amounts result in smaller overall reimbursement  
* Thinks there could be possible bugs

***HR Business Partner (Jennifer)***

* Similar trips aren’t identical \- different dates, routes, spending patterns  
* Newer employees get lower reimbursements than seasoned employees  
* Advises employees not to submit receipts of small amounts, keeping receipts over a certain threshold  
* Thinks timing matters but not sure on when optimal time is  
* 4-6 day trips get good reimbursements, shorter/longer not as good

***Senior Procurement Specialist (Kevin)***

* Thinks system rewards high miles/day ratios, not linear  
  * Bonuses maximized around 180-220 miles  
  * Too high/too low mileage \- penalized  
* Theory on spending patterns to maximize reimbursements (based on trial and error):  
  * Short trips \- spend under $75/day  
  * Medium trips (4-6 days) \- spend up to $120/day  
  * Long trips \- spend under $90/day  
* Thinks timing affects reimbursement  
  * Days of the week  
    * Tuesday submissions outperform Monday submissions  
    * Thursday submissions have good returns  
    * Friday performs the worst  
    * Tuesdays outperforms Fridays by 8%  
  * Lunar correlation?  
    * New moon submissions average 4% higher than full moon submissions  
* Patterns in data  
  * 6 different calculation paths depending on trip characteristics  
  * K-means clustering performed on data \- can predict reimbursement with about 15% accuracy  
  * Interaction between factors \- trip length x efficiency, spending/day x total mileage  
  * Certain combinations trigger bonuses, others trigger penalties (hidden decision trees?)  
  * Identified combinations:  
    * Guaranteed bonus  
      * 5 day trip  
      * 180+ miles/day  
      * \< $100/day spending  
    * Guaranteed penalty  
      * 8+ day trip  
    * Good reimbursement  
      * High mileage, low spending  
    * Bad reimbursement  
      * Low mileage, high spending  
* Learning adaptation component?  
  * Trips receive different treatment  
* Noise in the system to prevent gaming the system?