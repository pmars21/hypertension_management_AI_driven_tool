# Dataset Summary: NHANES Dietary Supplement Use 30-Day - Total Form (DSQTOT_L)

## General Information
- **Survey Name:** National Health and Nutrition Examination Survey (NHANES)
- **Data Cycle:** August 2021 - August 2023
- **Component:** Dietary Supplement Use 30-Day - Total Dietary Supplements
- **Data File:** `DSQTOT_L.xpt`
- **First Published:** February 2025
- **Target Population:** All survey participants

## Scope & Content
This component captures 30-day use of:
1. **Dietary Supplements (DS):** Both prescription and non-prescription (e.g., vitamins, minerals, herbals).
2. **Antacids:** Specifically, non-prescription antacids containing **calcium and/or magnesium**.

Two main files are generated from this component:
*   **Total Dietary Supplements (`DSQTOT_L`):** Summarizes the **total average daily intake** of 34 nutrients per participant from *all* their reported supplements and antacids combined. (This is the file described here).
*   **Individual Dietary Supplements (`DSQIDS_L`):** Detailed breakdown of each specific product reported by the user.

## Protocol Highlights & COVID-19 Impact
- **Mode of Administration:** To adapt to the COVID-19 pandemic, data collection shifted from in-person to **telephone interviews** (Computer-Assisted Telephone Interview - CATI). This was conducted following the first 24-hour dietary recall.
- **Reporting:** Participants were asked to read the supplement container labels to the interviewer over the phone.
- **Dropped Questions:** Questions regarding *how long* a supplement had been taken and the *reason* for taking it were discontinued in this survey cycle.

## Data Processing & Matching
- **Matching to Database:** Reported supplements were matched by NCHS nutritionists to known labels in the NHANES Dietary Supplement Database (NHANES-DSD). 
- **Match Confidence (`DSDMTCH`):** Because participants read labels over the phone, precision varied. Products were matched as exact, probable, generic, reasonable, or default (based on common market strengths). Analysts should know that generic or default nutrient profiles are assigned when exact brand data is missing.
- **Exclusions:** Foods, beverages, homeopathic remedies, and most prescription drugs were removed from this dataset. 

## Analytic Notes & Sample Weights
- **Sample Weights (`WTDRD1`):** Because this specific survey was conducted concurrently with the Day 1 dietary recall, analysts **must use the Dietary Day One sample weight (`WTDRD1`)**. Do not use standard MEC or interview weights.
- **Missing Nutrients:** If the participant reported taking a supplement but the specific amount/dosage was unknown (or the container wasn't available), the aggregate nutrient amounts (e.g., total Vitamin C) for that participant will be set to missing, even though they are counted as a supplement user.
- **Total Dietary Intake:** To calculate a person's *total* nutrient intake, analysts must combine the supplement nutrients from this file with food/beverage nutrient intakes from the 24-hour dietary recall files.

## Key Variables Overview

### 1. Survey & Weight Identifiers
*   **`SEQN`**: Respondent sequence number.
*   **`WTDRD1`**: Dietary day one sample weight.

### 2. General Usage & Counts
*   **`DSD010`**: Any Dietary Supplements Taken? (1 = Yes, 2 = No)
*   **`DSD010AN`**: Any Antacids Taken? (1 = Yes, 2 = No)
*   **`DSDCOUNT`**: Total number of dietary supplements taken.
*   **`DSDANCNT`**: Total number of antacids taken.

### 3. Aggregated Daily Nutrient Intakes
*Variables starting with `DSQT` represent the total aggregate mean daily intake from all supplements/antacids consumed by the individual.*
*   **Macronutrients:** Energy (`DSQTKCAL`), Protein (`DSQTPROT`), Carbs (`DSQTCARB`), Sugar (`DSQTSUGR`), Fiber (`DSQTFIBE`), Fats (`DSQTTFAT`, `DSQTSFAT`, etc.).
*   **Vitamins:** Vitamin C (`DSQTVC`), Vitamin D (`DSQTVD`), Vitamin B12 (`DSQTVB12`), Folic Acid (`DSQTFA`), etc.
*   **Minerals/Other:** Calcium (`DSQTCALC`), Iron (`DSQTIRON`), Magnesium (`DSQTMAGN`), Zinc (`DSQTZINC`), Caffeine (`DSQTCAFF`), Lutein/Zeaxanthin (`DSQTLZ`), etc.
*   *(Refer to Appendix 2 of the documentation for the full list of 34 calculated nutrients).*
