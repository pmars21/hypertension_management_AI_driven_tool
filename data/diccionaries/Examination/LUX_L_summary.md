# Dataset Summary: NHANES Liver Ultrasound Transient Elastography (LUX_L)

## General Information
- **Survey Name:** National Health and Nutrition Examination Survey (NHANES)
- **Data Cycle:** August 2021 - August 2023
- **Component:** Liver Ultrasound Transient Elastography
- **Data File:** `LUX_L.xpt`
- **First Published:** September 2024
- **Target Population:** Participants aged 12 years and older.

## Goals & Objectives
This examination provides objective measures for two important liver disease manifestations:
1. **Liver Fibrosis (scarring):** Measured via liver stiffness.
2. **Hepatic Steatosis (fat in liver):** Measured via controlled attenuation parameter (CAP).

## Eligibility & Exclusions
Participants were **excluded** from this exam if they:
1. Expected or confirmed pregnancy (or unable to provide a urine sample).
2. Were unable to lie down flat on the exam table.
3. Had an implanted electronic medical device (e.g., insulin pump, pacemaker).
4. Were wearing a bandage or had lesions on the right side of their abdomen by the ribs where the probe is placed.

## Protocol Highlights
- **Device Used:** FibroScan® model 502 V2 Touch (with medium [M] or extra-large [XL] wands).
- **Procedures:** A vibrating tip sends a shear wave through the intercostal space into the liver. The velocity of this wave is converted to tissue stiffness (expressed in kilopascals). CAP is measured simultaneously to indicate fat content (expressed in dB/m).
- **Quality Control Target:** Technicians aimed to capture 10 valid measurements where the interquartile range to median ratio (IQR/M) was less than 30%.
- **Measurement Deletion:** To prevent bias, examiners could only delete measurements from the beginning of a sequence—not cherry-pick individual readings.

## Data Processing & Analytic Notes
- **Fasting Requirement:** A "Complete" exam ideally requires a fasting time of at least 3 hours. However, data is included regardless of the length of the fast.
- **Data Editing:** Extreme values were verified, but the final stiffness, CAP, IQRe, and IQRc values obtained from the machine were **not altered** and **no values were imputed**. High outliers may reflect true biological conditions or difficulties measuring due to body habitus (e.g., obesity or narrow intercostal spaces).
- **Weights:** Depending on the nature of the analysis, use the standard Examination sample weights, unless merging with the morning fasting sample (in which case, use the matching fasting weights).

## Key Variables Overview

### 1. Survey & Status Identifiers
*   **`SEQN`**: Respondent sequence number.
*   **`LUAXSTAT`**: Elastography exam status (1 = Complete, 2 = Partial, 3 = Ineligible, 4 = Not done).
*   **`LUARXNC`**: Reason for partial exam (e.g., fasting < 3hrs, <10 valid valid measures, IQR/M >30%).
*   **`LUARXND`** & **`LUARXIN`**: Reasons for an exam not done or participant ineligibility.
*   **`LUAPNME`**: Exam wand type used (M or XL).

### 2. Measure Counts
*   **`LUANMTGP`**: Count of total measures attempted.
*   **`LUANMVGP`**: Count of valid, complete measures retained.

### 3. Elastography Findings (Fibrosis vs Steatosis)
*   **`LUXSMED`**: Median stiffness (E) in kilopascals (kPa). High stiffness indicates fibrosis.
*   **`LUXSIQR`**: Interquartile range of stiffness (IQRe).
*   **`LUXSIQRM`**: Ratio of IQRe / Median stiffness (used for QC thresholding).
*   **`LUXCAPM`**: Median Controlled Attenuation Parameter (CAP) in decibels per meter (dB/m). Evaluates steatosis.
*   **`LUXCPIQR`**: CAP interquartile range (IQRc).
