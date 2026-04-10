# Dataset Summary: Albumin & Creatinine - Urine (ALB_CR_L)

## General Information
- **Survey Name:** National Health and Nutrition Examination Survey (NHANES)
- **Data Cycle:** August 2021 - August 2023
- **Component:** Albumin & Creatinine - Urine
- **Data File:** `ALB_CR_L.xpt`
- **First Published:** September 2025
- **Target Population:** Examined participants aged 3 years and older.

## Component Description
- **Albumin:** Albumin is the most abundant plasma protein in healthy individuals. Human serum albumin is synthesized by the liver and serves many important roles in human physiology such as maintaining oncotic pressure, and transport of various hormones, vitamins, and drugs throughout the body. Kidney elimination of serum albumin may be observed in severe kidney disease. Following the urinary albumin excretion has been shown to be a diagnostic and prognostic marker for kidney and cardiovascular events.
- **Creatinine:** Creatinine is a breakdown product of creatine phosphate in muscle and is usually produced at a fairly constant rate by the body, depending on muscle mass. Creatinine is excreted by glomerular filtration during normal kidney function. Creatinine measurement is useful in the diagnosis and treatment of kidney diseases, in monitoring kidney dialysis, and as a calculation basis for other urinary analytes (e.g. total protein, microalbumin).

## Laboratory Methodology
- **Urinary Albumin:** The liquid chromatography tandem mass spectrometry (LC-MS/MS) assay quantifies albumin concentrations in human urine following enzymatic digestion. This measurement procedure utilizes proteolysis with trypsin, targeting a peptide specific to human serum albumin. *Note: The lab method used in August 2021-August 2023 is different from the fluorescent immunoassay method used in previous cycles.*
- **Urinary Creatinine:** In this enzymatic method creatinine is converted to creatine under the activity of creatininase. The final colored product is measured at 546 nm. *Note: The lab equipment used was updated to Cobas 8000 (from Cobas 6000), but no correction to the data is needed.*

## Data Processing and Editing
- **`URXUMS`:** The urine albumin value in µg/mL (`URXUMA`) was converted to mg/L (`URXUMS`) by multiplying by 1.00 (rounded to 2 decimals).
- **`URXCRS`:** The urine creatinine value in mg/dL (`URXUCR`) was converted to µmol/L (`URXCRS`) by multiplying by 88.4 (rounded to 1 decimal).
- **`URDACT`:** The urine albumin/creatinine ratio in mg/g (`URDACT`) was calculated by dividing `URXUMA` by `URXUCR` and multiplying by 100 (rounded to 2 decimal places).

## Analytic Notes
- **Methodology Shift (Albumin):** A bridging study was done comparing the new LC-MS/MS method with the prior fluorescent immunoassay method. Regression equations are provided in the official documentation if cross-cycle comparisons are needed.
- **Detection Limits:** For analytes with analytic results below the lower limit of detection (e.g., `URXUMALC=1`), an imputed fill value was placed in the analyte results field, calculated as LLOD/sqrt(2).
  - LLOD for Albumin (`URXUMA`): 0.02 mg/L
  - LLOD for Creatinine (`URXUCR`): 1.1 mg/dL

## Key Variables Overview
*   **`SEQN`**: Respondent sequence number.
*   **`URXUMA`**: Albumin, urine (ug/mL).
*   **`URXUMS`**: Albumin, urine (mg/L).
*   **`URDUMALC`**: Albumin, urine comment code (0 = At or above detection limit; 1 = Below lower detection limit).
*   **`URXUCR`**: Creatinine, urine (mg/dL).
*   **`URXCRS`**: Creatinine, urine (umol/L).
*   **`URDUCRLC`**: Creatinine, urine comment code (0 = At or above detection limit; 1 = Below lower detection limit).
*   **`URDACT`**: Albumin creatinine ratio (mg/g).
