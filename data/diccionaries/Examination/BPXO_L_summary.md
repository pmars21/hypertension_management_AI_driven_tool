# Dataset Summary: NHANES Blood Pressure - Oscillometric Measurements (BPXO_L)

## General Information
- **Survey Name:** National Health and Nutrition Examination Survey (NHANES)
- **Data Cycle:** August 2021 - August 2023
- **Component:** Blood Pressure - Oscillometric Measurements 
- **Data File:** `BPXO_L.xpt`
- **First Published:** September 2024
- **Target Population:** Participants aged 8 years and older.

## Eligibility & Exclusions
Participants were **excluded** from blood pressure measurement if they had specific conditions on **both arms** (or specific conditions on the affected arm):
- Rashes, gauze dressings, casts, edema, paralysis, tubes, open sores or wounds, withered arms, or A-V shunts.
- Women who have had an axillary nodal biopsy or resection, or a unilateral radical mastectomy, did not have BP measured in the affected arm.

## Protocol Highlights
- **Measurement Method:** Three consecutive blood pressure (systolic and diastolic) and pulse measurements were taken 60 seconds apart.
- **Device Used:** A digital upper-arm electronic blood pressure measurement device (Omron HEM–907XL).
- **Procedures:** 
  - Standardized measurements were typically taken on the **right arm** unless conditions prohibited it.
  - Participants rested quietly in a seated position for 5 minutes prior to the measurements.
  - Upper arm circumference was measured first to determine the appropriate cuff size.

## Data Processing Rules
- Systolic BP cannot be greater than 300 mmHg.
- Systolic BP must be strictly greater than Diastolic BP.
- If no Systolic BP is recorded, no Diastolic BP can be recorded (though a Systolic measurement can exist without a Diastolic one).

## Analytic Notes
- **Methodology Shift:** After the 2017-2018 cycle, NHANES strictly transitioned to the oscillometric measurement method (Omron HEM–907XL) and discontinued the auscultatory method (mercury sphygmomanometer).
- **Weights:** Analysts should use the standard Exam sample weights for data analysis.

## Key Variables Overview

### 1. Survey & Measurement Identifiers
*   **`SEQN`**: Respondent sequence number.
*   **`BPAOARM`**: Arm selected for the measurement (L = Left, R = Right).
*   **`BPAOCSZ`**: Coded cuff size based on mid-arm circumference (2 = 17-21.9 cm, 3 = 22-31.9 cm, 4 = 32-41.9 cm, 5 = 42-50 cm).

### 2. Blood Pressure Readings (Systolic & Diastolic)
Three consecutive readings are provided:
*   **Systolic (1st, 2nd, 3rd):** `BPXOSY1`, `BPXOSY2`, `BPXOSY3`
*   **Diastolic (1st, 2nd, 3rd):** `BPXODI1`, `BPXODI2`, `BPXODI3`

### 3. Pulse Readings
Three corresponding pulse readings:
*   **Pulse (1st, 2nd, 3rd):** `BPXOPLS1`, `BPXOPLS2`, `BPXOPLS3`
