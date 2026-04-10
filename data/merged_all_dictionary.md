# Dataset Summary: NHANES Merged Dataset (merged_all.csv)

## General Information
- **Survey Name:** National Health and Nutrition Examination Survey (NHANES)
- **Data Cycle:** August 2021 - August 2023 (primarily)
- **Component:** Merged multi-component dataset
- **Data File:** `merged_all.csv`
- **Target Population:** Varies by component (generally participants aged 1-80+ years, with specific age restrictions for components like blood pressure, balance, and elastography).

## Scope & Methodology
This dataset is a consolidated file combining multiple NHANES components into a single flat file. It relies on the respondent sequence number (`SEQN`) to link demographic, examination, laboratory, and questionnaire data for each participant. 

**Included Components based on variables:**
- Demographics (`DEMO_L`)
- Body Measures (`BMX_L`)
- Blood Pressure (`BPXO_L`)
- Balance (`BAX_L`)
- Liver Ultrasound Transient Elastography (`LUX_L`)
- Dietary Supplements (`DSQTOT_L`)
- Laboratory Data (Complete Blood Count, Lipids, Heavy Metals, Urine Albumin/Creatinine)

**Analytic Notes:**
- **Weights:** Because this dataset merges multiple components (Demographics, MEC Exams, Dietary, and Lab Subsamples), analysts must carefully choose the appropriate weight variable (e.g., `WTINT2YR`, `WTMEC2YR`, `WTDRD1`, `WTPH2YR`, `WTSAF2YR`) depending on the specific variables and sub-populations being analyzed.
- **Missing Data:** Many columns contain missing values (`NaN`) resulting from intentional exclusions (e.g., pregnant women for elastography) or age-based protocol restrictions.

## Key Variables Overview

### 1. Identifiers & Demographics (DEMO_L)
**Target Population:** All participants in the NHANES Aug 2021-Aug 2023 sample.
**First Published:** September 2024
**Missing Values:** Missing values are coded as *.*

**Survey Context & Analytic Notes (COVID-19 Impact):**
- **Resumption of Operations:** Data collection resumed in Aug 2021 after being suspended in March 2020.
- **Sample Design Changes:** No person-level oversampling by race/Hispanic origin or income (unlike previous cycles), but oversampling by age group was added. This may result in lower statistical precision for certain demographic subgroups.
- **Data Gap Caution:** There is a 15-month data gap between the previous cycle and this one. Analysts should exercise strict caution when combining this data with previous cycles or conducting trend analyses.
- **Confidentiality Protections:** Due to disclosure risks, some variables (like marital status, pregnancy, age 80+, family sizes over 7) have been top-coded or restricted to certain age bands. Others are only accessible via the NCHS Research Data Center.

**Key Variables:**
*   **Identifiers & Survey Administration:**
    *   **`SEQN`**: Respondent sequence number (unique identifier).
    *   **`SDDSRVYR`**: Data release cycle (`12` indicates the Aug 2021 - Aug 2023 cycle).
    *   **`RIDSTATR`**: Interview/Examination status (1 = Interviewed only; 2 = Interviewed & MEC examined).
    *   **`RIDEXMON`**: Six-month time period when the exam was performed.
*   **Demographics:**
    *   **`RIAGENDR`**: Gender (Male, Female).
    *   **`RIDAGEYR`**: Age in years at screening (top-coded at 80 years).
    *   **`RIDAGEMN` / `RIDEXAGM`**: Age in months (for toddlers/youth).
    *   **`RIDRETH1` / `RIDRETH3`**: Race/Hispanic origin (Includes categories for Mexican American, Other Hispanic, Non-Hispanic White, Non-Hispanic Black, Non-Hispanic Asian, and Other/Multi-Racial).
    *   **`DMDEDUC2`**: Education level for adults 20+.
    *   **`DMDMARTZ`**: Marital status.
    *   **`DMQMILIZ`**: Served on active duty in US Armed Forces.
*   **Place of Birth & Residency:**
    *   **`DMDBORN4`**: Country of birth (Born in US vs. Born in other countries).
    *   **`DMDYRUSR`**: Length of time living in the US (categorical).
*   **Household & Income:**
    *   **`DMDHHSIZ`**: Total number of people in the household (top-coded at 7 or more).
    *   **`INDFMPIR`**: Ratio of family income to poverty guidelines (top-coded at 5.00).
    *   **`DMDHR***` Variables**: Information about the Household Reference Person (e.g., gender `DMDHRGND`, age `DMDHRAGZ`, education `DMDHREDZ`, marital status `DMDHRMAZ`).
*   **Medical / Physical Status:**
    *   **`RIDEXPRG`**: Pregnancy status at the time of exam (released only for women 20-44 years).
*   **Sample Weights & Variance Estimation:**
    *   **`WTINT2YR`**: Full sample 2-year interview weight.
    *   **`WTMEC2YR`**: Full sample 2-year MEC exam weight.
    *   **`SDMVSTRA` / `SDMVPSU`**: Masked variance pseudo-stratum and pseudo-PSU (vital for accurate variance estimation).

### 2. Dietary Supplements (DSQTOT_L)
**Target Population:** All survey participants
**First Published:** February 2025

**Scope & Content:**
This component captures 30-day use of:
1. **Dietary Supplements (DS):** Both prescription and non-prescription (e.g., vitamins, minerals, herbals).
2. **Antacids:** Specifically, non-prescription antacids containing **calcium and/or magnesium**.

Two main files are generated from this component:
*   **Total Dietary Supplements (`DSQTOT_L`):** Summarizes the **total average daily intake** of 34 nutrients per participant from *all* their reported supplements and antacids combined. (This is the file described here).
*   **Individual Dietary Supplements (`DSQIDS_L`):** Detailed breakdown of each specific product reported by the user.

**Protocol Highlights & COVID-19 Impact:**
- **Mode of Administration:** To adapt to the COVID-19 pandemic, data collection shifted from in-person to **telephone interviews** (Computer-Assisted Telephone Interview - CATI). This was conducted following the first 24-hour dietary recall.
- **Reporting:** Participants were asked to read the supplement container labels to the interviewer over the phone.
- **Dropped Questions:** Questions regarding *how long* a supplement had been taken and the *reason* for taking it were discontinued in this survey cycle.

**Data Processing & Matching:**
- **Matching to Database:** Reported supplements were matched by NCHS nutritionists to known labels in the NHANES Dietary Supplement Database (NHANES-DSD). 
- **Match Confidence (`DSDMTCH`):** Because participants read labels over the phone, precision varied. Products were matched as exact, probable, generic, reasonable, or default (based on common market strengths). Analysts should know that generic or default nutrient profiles are assigned when exact brand data is missing.
- **Exclusions:** Foods, beverages, homeopathic remedies, and most prescription drugs were removed from this dataset. 

**Analytic Notes & Sample Weights:**
- **Sample Weights (`WTDRD1`):** Because this specific survey was conducted concurrently with the Day 1 dietary recall, analysts **must use the Dietary Day One sample weight (`WTDRD1`)**. Do not use standard MEC or interview weights.
- **Missing Nutrients:** If the participant reported taking a supplement but the specific amount/dosage was unknown (or the container wasn't available), the aggregate nutrient amounts (e.g., total Vitamin C) for that participant will be set to missing, even though they are counted as a supplement user.
- **Total Dietary Intake:** To calculate a person's *total* nutrient intake, analysts must combine the supplement nutrients from this file with food/beverage nutrient intakes from the 24-hour dietary recall files.

**Key Variables:**
*   **Survey & Weight Identifiers:**
    *   **`SEQN`**: Respondent sequence number.
    *   **`WTDRD1`**: Dietary day one sample weight.
*   **General Usage & Counts:**
    *   **`DSD010`**: Any Dietary Supplements Taken? (1 = Yes, 2 = No)
    *   **`DSD010AN`**: Any Antacids Taken? (1 = Yes, 2 = No)
    *   **`DSDCOUNT`**: Total number of dietary supplements taken.
    *   **`DSDANCNT`**: Total number of antacids taken.
*   **Aggregated Daily Nutrient Intakes:**
    *Variables starting with `DSQT` represent the total aggregate mean daily intake from all supplements/antacids consumed by the individual.*
    *   **Macronutrients:** Energy (`DSQTKCAL`), Protein (`DSQTPROT`), Carbs (`DSQTCARB`), Sugar (`DSQTSUGR`), Fiber (`DSQTFIBE`), Fats (`DSQTTFAT`, `DSQTSFAT`, etc.).
    *   **Vitamins:** Vitamin C (`DSQTVC`), Vitamin D (`DSQTVD`), Vitamin B12 (`DSQTVB12`), Folic Acid (`DSQTFA`), etc.
    *   **Minerals/Other:** Calcium (`DSQTCALC`), Iron (`DSQTIRON`), Magnesium (`DSQTMAGN`), Zinc (`DSQTZINC`), Caffeine (`DSQTCAFF`), Lutein/Zeaxanthin (`DSQTLZ`), etc.
    *   *(Refer to Appendix 2 of the documentation for the full list of 34 calculated nutrients).*

### 3. Balance (BAX_L)
**Target Population:** Participants aged 20 to 69 years.
**First Published:** October 2024

**Eligibility & Exclusions:**
Participants were **excluded** from the test if they met certain criteria:
- Pregnant or exceeding 315 pounds (weight limit for foam surface).
- Severe vision impairment, inability to stand independently, leg/foot amputations, or lower-body prosthetics.
- Recent injuries/surgeries to legs/ankles/feet, or current dizziness with a history of falls due to dizziness.
- Wearing heels 3 inches or higher.
- Inability to fit the safety belt properly.

**Condition 5 Specific Exclusions:** Participants were additionally excluded from Condition 5 if they had current neck pain, previous neck surgery, chronic neck problems, or limited neck mobility.

**Protocol Highlights (Modified Romberg Test - MRT):**
The MRT assesses balance with five conditions of increasing difficulty. A participant failed a condition if they could not maintain balance for the required time across two trials.
- **Support Surface & Visual Input:**
  - **Condition 1:** Bare floor, eyes open
  - **Condition 2:** Bare floor, eyes closed
  - **Condition 3:** Dense foam, eyes open
  - **Condition 4:** Dense foam, eyes closed
  - **Condition 5:** Dense foam, eyes closed, moving head side-to-side
- **Passing criteria:**
  - **Conditions 1 & 2:** 15 seconds.
  - **Conditions 3, 4, & 5:** 20 seconds (the actual duration tested is 30 seconds, but research sets 20 seconds as a "pass" threshold).
- **Failure conditions:** Moving feet, uncrossing arms from chest, opening eyes (in closed-eye conditions), touching the wall, or needing technician intervention.

**Analytic Notes (Differences from 1999-2004 Cycle):**
If comparing this data to the 1999-2004 cycle, be aware of key differences:
- **Passing Times:** In 1999-2004, participants needed 30 seconds to pass Conditions 3 and 4, whereas this cycle considers 20 seconds a pass. You may need to recode 20-29 second durations as "did not pass" for direct comparisons.
- **Condition 5:** Was not assessed in 1999-2004.
- **Variable Overhaul:** Variable names have changed (e.g., `BAXPFC11` is now `BAXPF11`, and `BAXFTC11` is now `BAXTC11`). Additionally, this cycle reports *duration time attempted* rather than *failure time*.
- **Weights:** Use the standard Exam sample weights for all analyses.

**Key Variables:**
*   **Survey & Status Identifiers:**
    *   **`SEQN`**: Respondent sequence number.
    *   **`BAXMSTAT`**: MRT exam status (1 = Complete, 2 = Partial, 3 = Not done, 4 = Ineligible).
    *   **`BAX5STAT`**: Eligibility specifically for Condition 5.
    *   **`BAXRXNC` / `BAXRXND`**: Reason statements for Partial exams (`BAXRXNC`) or Not Done exams (`BAXRXND`).
*   **Pre-Test Screening Questions:**
    *   **`BAQ110` - `BAQ173`**: Screening questions addressing ability to stand, use of leg braces, injuries, past dizziness/falls, neck pain, neck surgery history, and explicit consent to begin the test.
*   **Trial Results (Repeated for Conditions 1-5, Trials 1 & 2):** Variable naming convention: **[Prefix][Condition #][Trial #]**
    *   **`BAXPF__`** (e.g., `BAXPF11`): Pass/Did not pass for the specific condition and trial.
    *   **`BAXTC__`** (e.g., `BAXTC11`): Time/duration maintained during the trial.
    *   **`BAARFC__`** (e.g., `BAARFC11`): Reason the trial was stopped (1 = Feet moved, 2 = Arms moved off waist, 3 = Eyes opened, 4 = Tech intervention, 5 = Grab/touch wall).

### 4. Blood Pressure - Oscillometric (BPXO_L)
**Target Population:** Participants aged 8 years and older.
**First Published:** September 2024

**Eligibility & Exclusions:**
Participants were **excluded** from blood pressure measurement if they had specific conditions on **both arms** (or specific conditions on the affected arm):
- Rashes, gauze dressings, casts, edema, paralysis, tubes, open sores or wounds, withered arms, or A-V shunts.
- Women who have had an axillary nodal biopsy or resection, or a unilateral radical mastectomy, did not have BP measured in the affected arm.

**Protocol Highlights:**
- **Measurement Method:** Three consecutive blood pressure (systolic and diastolic) and pulse measurements were taken 60 seconds apart.
- **Device Used:** A digital upper-arm electronic blood pressure measurement device (Omron HEM–907XL).
- **Procedures:** 
  - Standardized measurements were typically taken on the **right arm** unless conditions prohibited it.
  - Participants rested quietly in a seated position for 5 minutes prior to the measurements.
  - Upper arm circumference was measured first to determine the appropriate cuff size.

**Data Processing Rules:**
- Systolic BP cannot be greater than 300 mmHg.
- Systolic BP must be strictly greater than Diastolic BP.
- If no Systolic BP is recorded, no Diastolic BP can be recorded (though a Systolic measurement can exist without a Diastolic one).

**Analytic Notes:**
- **Methodology Shift:** After the 2017-2018 cycle, NHANES strictly transitioned to the oscillometric measurement method (Omron HEM–907XL) and discontinued the auscultatory method (mercury sphygmomanometer).
- **Weights:** Analysts should use the standard Exam sample weights for data analysis.

**Key Variables:**
*   **Survey & Measurement Identifiers:**
    *   **`SEQN`**: Respondent sequence number.
    *   **`BPAOARM`**: Arm selected for the measurement (L = Left, R = Right).
    *   **`BPAOCSZ`**: Coded cuff size based on mid-arm circumference (2 = 17-21.9 cm, 3 = 22-31.9 cm, 4 = 32-41.9 cm, 5 = 42-50 cm).
*   **Blood Pressure Readings (Systolic & Diastolic):**
    Three consecutive readings are provided:
    *   **Systolic (1st, 2nd, 3rd):** `BPXOSY1`, `BPXOSY2`, `BPXOSY3`
    *   **Diastolic (1st, 2nd, 3rd):** `BPXODI1`, `BPXODI2`, `BPXODI3`
*   **Pulse Readings:**
    Three corresponding pulse readings:
    *   **Pulse (1st, 2nd, 3rd):** `BPXOPLS1`, `BPXOPLS2`, `BPXOPLS3`

### 5. Body Measures (BMX_L)
**First Published:** September 2024

**Target Age Groups by Measurement:**
There were no medical/safety exclusions for this protocol. Measurements were collected based on age:
- **Weight:** All ages
- **Head Circumference:** Birth - 6 months
- **Recumbent Length:** Birth - 47 months
- **Standing Height:** 2+ years
- **Upper Leg Length:** 8+ years
- **Upper Arm Length & Mid-upper Arm Circumference:** 2+ months
- **Waist Circumference:** 2+ years
- **Hip Circumference:** 12+ years

**Protocol & Procedure Highlights:**
- **Location:** Measurements were collected in the Mobile Examination Center (MEC) by trained health technicians.
- **Arm/Leg Side:** Measurements were taken on the **right** side of the body. If an amputation or medical condition prevented this, the left side was used. 
- **Amputations:** Body weight data is set to "missing" for individuals with limb amputations due to confidentiality/disclosure risks.
- **Pregnancy:** Pregnant women were measured, but if a woman was outside the 20-44 age range (the only range where pregnancy status is publicly disclosed), her body measures data is hidden to prevent disclosure.
- **Clothing:** Technicians documented if excessive clothing or medical appliances interfered with weight measurements via comment codes.

**Data Processing & Analytic Notes:**
- **Editing:** Extreme values (above the 99th or below the 1st percentile) were reviewed against subject characteristics (age, sex, height, etc.). Unrealistic values were deleted. There is **no imputed data**. 
- **BMI Calculation (`BMXBMI`):** Weight in kilograms divided by height in meters squared, rounded to one decimal place.
- **Children's BMI categories (`BMDBMIC`):** Calculated for ages 2-19 based on CDC growth charts matching age explicitly in months (1 = Underweight, 2 = Normal, 3 = Overweight, 4 = Obese). *Note: child/adolescent weight classification is not directly comparable to adult definitions.*
- **Weights:** Analysts should use the Examination sample weights for analyzing this data.

**Key Variables:**
*Most physical measurements have a corresponding comment code variable starting with "BMI" (e.g., `BMXWT` has `BMIWT`) used to indicate if the measurement could not be obtained, was affected by clothing, or was not perfectly straight.*
*   **Survey & Status Identifiers:**
    *   **`SEQN`**: Respondent sequence number.
    *   **`BMDSTATS`**: Component Status Code (1 = Complete, 2 = Partial [height/weight only], 3 = Other partial, 4 = No exam data).
*   **Major Body Measurements:**
    *   **`BMXWT`**: Weight (kg) & **`BMIWT`**: Comment
    *   **`BMXHT`**: Standing Height (cm) & **`BMIHT`**: Comment
    *   **`BMXRECUM`**: Recumbent Length (cm) & **`BMIRECUM`**: Comment
    *   **`BMXHEAD`**: Head Circumference (cm) & **`BMIHEAD`**: Comment
*   **Derived Indices:**
    *   **`BMXBMI`**: Body Mass Index (kg/m²)
    *   **`BMDBMIC`**: BMI Category for Children/Youth (aged 2-19)
*   **Limb & Trunk Measurements:**
    *   **`BMXLEG`**: Upper Leg Length (cm) & **`BMILEG`**: Comment
    *   **`BMXARML`**: Upper Arm Length (cm) & **`BMIARML`**: Comment
    *   **`BMXARMC`**: Arm Circumference (cm) & **`BMIARMC`**: Comment
    *   **`BMXWAIST`**: Waist Circumference (cm) & **`BMIWAIST`**: Comment
    *   **`BMXHIP`**: Hip Circumference (cm) & **`BMIHIP`**: Comment

### 6. Liver Ultrasound Transient Elastography (LUX_L)
**Target Population:** Participants aged 12 years and older.
**First Published:** September 2024

**Goals & Objectives:**
This examination provides objective measures for two important liver disease manifestations:
1. **Liver Fibrosis (scarring):** Measured via liver stiffness.
2. **Hepatic Steatosis (fat in liver):** Measured via controlled attenuation parameter (CAP).

**Eligibility & Exclusions:**
Participants were **excluded** from this exam if they:
1. Expected or confirmed pregnancy (or unable to provide a urine sample).
2. Were unable to lie down flat on the exam table.
3. Had an implanted electronic medical device (e.g., insulin pump, pacemaker).
4. Were wearing a bandage or had lesions on the right side of their abdomen by the ribs where the probe is placed.

**Protocol Highlights:**
- **Device Used:** FibroScan® model 502 V2 Touch (with medium [M] or extra-large [XL] wands).
- **Procedures:** A vibrating tip sends a shear wave through the intercostal space into the liver. The velocity of this wave is converted to tissue stiffness (expressed in kilopascals). CAP is measured simultaneously to indicate fat content (expressed in dB/m).
- **Quality Control Target:** Technicians aimed to capture 10 valid measurements where the interquartile range to median ratio (IQR/M) was less than 30%.
- **Measurement Deletion:** To prevent bias, examiners could only delete measurements from the beginning of a sequence—not cherry-pick individual readings.

**Data Processing & Analytic Notes:**
- **Fasting Requirement:** A "Complete" exam ideally requires a fasting time of at least 3 hours. However, data is included regardless of the length of the fast.
- **Data Editing:** Extreme values were verified, but the final stiffness, CAP, IQRe, and IQRc values obtained from the machine were **not altered** and **no values were imputed**. High outliers may reflect true biological conditions or difficulties measuring due to body habitus (e.g., obesity or narrow intercostal spaces).
- **Weights:** Depending on the nature of the analysis, use the standard Examination sample weights, unless merging with the morning fasting sample (in which case, use the matching fasting weights).

**Key Variables:**
*   **Survey & Status Identifiers:**
    *   **`SEQN`**: Respondent sequence number.
    *   **`LUAXSTAT`**: Elastography exam status (1 = Complete, 2 = Partial, 3 = Ineligible, 4 = Not done).
    *   **`LUARXNC`**: Reason for partial exam (e.g., fasting < 3hrs, <10 valid valid measures, IQR/M >30%).
    *   **`LUARXND`** & **`LUARXIN`**: Reasons for an exam not done or participant ineligibility.
    *   **`LUAPNME`**: Exam wand type used (M or XL).
*   **Measure Counts:**
    *   **`LUANMTGP`**: Count of total measures attempted.
    *   **`LUANMVGP`**: Count of valid, complete measures retained.
*   **Elastography Findings (Fibrosis vs Steatosis):**
    *   **`LUXSMED`**: Median stiffness (E) in kilopascals (kPa). High stiffness indicates fibrosis.
    *   **`LUXSIQR`**: Interquartile range of stiffness (IQRe).
    *   **`LUXSIQRM`**: Ratio of IQRe / Median stiffness (used for QC thresholding).
    *   **`LUXCAPM`**: Median Controlled Attenuation Parameter (CAP) in decibels per meter (dB/m). Evaluates steatosis.
    *   **`LUXCPIQR`**: CAP interquartile range (IQRc).

### 7. Albumin & Creatinine - Urine (ALB_CR_L)
**Target Population:** Examined participants aged 3 years and older.
**First Published:** September 2025

**Component Description:**
Albumin is the most abundant plasma protein. Kidney elimination of serum albumin may be observed in severe kidney disease and cardiovascular events. Creatinine is a breakdown product of creatine phosphate in muscle. Creatinine measurement is useful in the diagnosis and treatment of kidney diseases, and as a calculation basis for other urinary analytes.

**Analytic Notes:**
- **Methodology Shift (Albumin):** Regression equations are provided in the official documentation if cross-cycle comparisons are needed between the new LC-MS/MS method and the prior fluorescent immunoassay method.
- **Detection Limits:** For analytes with measurements below the lower limit of detection, an imputed fill value was placed in the analyte results field, calculated as LLOD/sqrt(2).

**Key Variables:**
*   **`URXUMA`**: Albumin, urine (ug/mL).
*   **`URXUMS`**: Albumin, urine (mg/L).
*   **`URDUMALC`**: Albumin, urine comment code.
*   **`URXUCR`**: Creatinine, urine (mg/dL).
*   **`URXCRS`**: Creatinine, urine (umol/L).
*   **`URDUCRLC`**: Creatinine, urine comment code.
*   **`URDACT`**: Albumin creatinine ratio (mg/g).

### 8. alpha-1-Acid Glycoprotein (AGP_L)
**Target Population:** Examined participants 1-5 years old and 12-49 years old females.
**First Published:** September 2024

**Component Description:**
Alpha-1-Acid Glycoprotein (AGP) is synthesized in the liver. It is a sensitive acute phase reactant whose concentration can increase when inflammation occurs. This was a new component in the NHANES August 2021–August 2023 cycle.

**Analytic Notes:**
- **Phlebotomy Weights:** Because analysis of nonresponse patterns for the phlebotomy component revealed differences, an additional phlebotomy weight (`WTPH2YR`) has been included to address possible nonresponse bias.

**Key Variables:**
*   **`WTPH2YR`**: Phlebotomy 2 Year Weight.

### 9. Complete Blood Count with 5-Part Differential in Whole Blood (CBC_L)
**Target Population:** Examined participants aged 1 year and over.
**First Published:** September 2024

**Component Description:**
The complete blood count (CBC) with 5-part differential counts red blood cells (RBCs), white blood cells (WBCs), and platelets, measures hemoglobin; estimates the red cells’ volume; and sorts the WBCs into subtypes. 

**Analytic Notes:**
- **Phlebotomy Weights:** Uses `WTPH2YR` for analyses deriving from blood analytes. Eligible participants who did not provide a specimen receive a weight of "0".

**Key Variables:**
*   **White Blood Cells & Differential:**
    *   **`LBXWBCSI`**: White blood cell count (1000 cells/uL).
    *   **`LBXLYPCT` / `LBDLYMNO`**: Lymphocyte percent (%) & number (1000 cells/uL).
    *   **`LBXMOPCT` / `LBDMONO`**: Monocyte percent (%) & number (1000 cells/uL).
    *   **`LBXNEPCT` / `LBDNENO`**: Segmented neutrophils percent (%) & number (1000 cell/uL).
    *   **`LBXEOPCT` / `LBDEONO`**: Eosinophils percent (%) & number (1000 cells/uL).
    *   **`LBXBAPCT` / `LBDBANO`**: Basophils percent (%) & number (1000 cells/uL).
*   **Red Blood Cells:**
    *   **`LBXRBCSI`**: Red blood cell count (million cells/uL).
    *   **`LBXHGB`**: Hemoglobin (g/dL).
    *   **`LBXHCT`**: Hematocrit (%).
    *   **`LBXMCVSI`**: Mean cell volume (fL).
    *   **`LBXMC`**: Mean Cell Hemoglobin Concentration (g/dL).
    *   **`LBXMCHSI`**: Mean cell hemoglobin (pg).
    *   **`LBXRDW`**: Red cell distribution width (%).
    *   **`LBXNRBC`**: Nucleated red blood cells (/100 WBC).
*   **Platelets:**
    *   **`LBXPLTSI`**: Platelet count (1000 cells/uL).
    *   **`LBXMPSI`**: Mean platelet volume (fL).

### 10. Cholesterol – High-Density Lipoprotein (HDL_L)
**Target Population:** Examined participants aged 6 years and older.
**First Published:** September 2024

**Component Description:**
Focuses exclusively on High-Density Lipoprotein (HDL-C), fundamental for cardiovascular risk assessment.

**Analytic Notes:**
- **Phlebotomy Weights:** Uses `WTPH2YR` to address possible nonresponse bias.
- **Methodology Shift:** Bridging testing was done for the Cobas 8000 upgrade, but adjustment was deemed unnecessary.

**Key Variables:**
*   **`LBDHDD`**: Direct HDL-Cholesterol (mg/dL).
*   **`LBDHDDSI`**: Direct HDL-Cholesterol (mmol/L).

### 11. High-Sensitivity C-Reactive Protein (HSCRP_L)
**Target Population:** Examined participants aged 1 year and older.
**First Published:** September 2024

**Component Description:**
C-reactive protein (CRP) is an acute phase protein synthesized in the liver, serving as a sensitive indicator of inflammation and cardiovascular disease risk.

**Analytic Notes:**
- **Phlebotomy Weights:** Uses `WTPH2YR` to address possible nonresponse bias.
- **Methodology Shift:** Bridging testing was done due to an upgrade to the Cobas 8000 instrument. Regression equations exist in official documentation.

**Key Variables:**
*   **`LBXHSCRP`**: High-Sensitivity C-Reactive Protein (hs-CRP) (mg/L).
*   **`LBDHRPLC`**: High-Sensitivity C-Reactive Protein (hs-CRP) Comment Code.

### 12. Lead, Cadmium, Total Mercury, Selenium, & Manganese – Blood (PBCD_L)
**Target Population:** Examined participants aged 1 year and older.
**First Published:** September 2024

**Component Description:**
Assesses exposure to heavy metals and trace elements using mass spectrometry (ICP-MS) from whole blood specimens.

**Analytic Notes:**
- **Phlebotomy Weights:** Uses `WTPH2YR` to address possible nonresponse bias.

**Key Variables:**
*   **Lead:**
    *   **`LBXBPB` / `LBDBPBSI`**: Blood lead in ug/dL and umol/L.
    *   **`LBDBPBLC`**: Blood lead comment code.
*   **Cadmium:**
    *   **`LBXBCD` / `LBDBCDSI`**: Blood cadmium in ug/L and nmol/L.
    *   **`LBDBCDLC`**: Blood cadmium comment code.
*   **Mercury:**
    *   **`LBXTHG` / `LBDTHGSI`**: Blood mercury, total in ug/L and nmol/L.
    *   **`LBDTHGLC`**: Blood mercury, total comment code.
*   **Selenium:**
    *   **`LBXBSE` / `LBDBSESI`**: Blood selenium in ug/L and umol/L.
    *   **`LBDBSELC`**: Blood selenium comment code.
*   **Manganese:**
    *   **`LBXBMN` / `LBDBMNSI`**: Blood manganese in ug/L and nmol/L.
    *   **`LBDBMNLC`**: Blood manganese comment code.

### 13. Cholesterol - Low-Density Lipoproteins (LDL) & Triglycerides (TRIGLY_L)
**Target Population:** Participants aged 12 years and older examined in morning sessions.
**First Published:** September 2025

**Component Description:**
Provides directly measured Triglycerides and derived LDL-C values.

**Analytic Notes:**
- **Subsample Weights:** Analysts must use the **Fasting Subsample 2 Year MEC Weight (`WTSAF2YR`)**. 
- **Methodology Shift:** The glycerol blanked assay was phased out. Regression equations ensure comparability across cycles.

**Key Variables:**
*   **Weights:**
    *   **`WTSAF2YR`**: Fasting Subsample 2 Year MEC Weight.
*   **Triglycerides:**
    *   **`LBXTLG`**: Triglyceride (mg/dL).
    *   **`LBDTRSI`**: Triglyceride (mmol/L).
*   **LDL-Cholesterol Calculated (Friedewald):**
    *   **`LBDLDL` / `LBDLDLSI`**: LDL-Cholesterol, Friedewald in mg/dL and mmol/L.
*   **LDL-Cholesterol Calculated (Martin-Hopkins):**
    *   **`LBDLDLM` / `LBDLDMSI`**: LDL-Cholesterol, Martin-Hopkins in mg/dL and mmol/L.
*   **LDL-Cholesterol Calculated (NIH Equation 2):**
    *   **`LBDLDLN` / `LBDLDNSI`**: LDL-Cholesterol, NIH equation 2 in mg/dL and mmol/L.
