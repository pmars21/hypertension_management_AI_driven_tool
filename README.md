# NHANES Merged Dataset General Information

This document provides a general overview of all the component datasets merged into `merged_all.csv` (August 2021 - August 2023 cycle) and a consolidated list of all variables included, as defined in `merged_all_dictionary.md`.

## Datasets Overview

1. **Identifiers & Demographics (`DEMO_L`)**: Contains demographics, socioeconomic indicators, household information, and sequence IDs for all participants.
2. **Dietary Supplements (`DSQTOT_L`)**: Captures 30-day use of dietary supplements and antacids, summarizing the total daily intake of 34 nutrients per participant.
3. **Balance (`BAX_L`)**: Assesses balance for participants aged 20–69 via a Modified Romberg Test.
4. **Blood Pressure - Oscillometric (`BPXO_L`)**: Provides consecutive systolic and diastolic BP measurements using an Omron electronic device (8+ years).
5. **Body Measures (`BMX_L`)**: Major anthropometric measurements like weight, height, BMI, and various circumferences for all ages.
6. **Liver Ultrasound Transient Elastography (`LUX_L`)**: Measures liver stiffness (fibrosis) and controlled attenuation parameter (steatosis) for participants 12+ years.
7. **Albumin & Creatinine - Urine (`ALB_CR_L`)**: Biomarkers assessing kidney health and cardiovascular risks (3+ years).
8. **alpha-1-Acid Glycoprotein (`AGP_L`)**: Acute phase reactant measuring systemic inflammation.
9. **Complete Blood Count (`CBC_L`)**: Provides counts of white/red blood cells, platelets, and cell subtypes (1+ years).
10. **Cholesterol – High-Density Lipoprotein (`HDL_L`)**: Focuses on direct HDL-Cholesterol values (6+ years).
11. **High-Sensitivity C-Reactive Protein (`HSCRP_L`)**: Crucial biomarker for inflammation and cardiovascular disease risk (1+ years).
12. **Heavy Metals (`PBCD_L`)**: Evaluates whole-blood amounts of Lead, Cadmium, Mercury, Selenium, and Manganese (1+ years).
13. **Low-Density Lipoproteins & Triglycerides (`TRIGLY_L`)**: Fasting measurements for Triglycerides and three equations for calculated LDL-C (12+ years).

---

## Consolidated Variable Dictionary

### General Identifiers & Survey Weights
*   **`SEQN`**: Respondent sequence number (unique identifier linking all datasets).
*   **`SDDSRVYR`**: Data release cycle (`12` indicates the Aug 2021 - Aug 2023 cycle).
*   **`WTINT2YR`**: Full sample 2-year interview weight.
*    **`WTMEC2YR`**: Full sample 2-year MEC exam weight.
*   **`WTDRD1`**: Dietary day one sample weight.
*   **`WTPH2YR`**: Phlebotomy 2 Year Weight.
*   **`WTSAF2YR`**: Fasting Subsample 2 Year MEC Weight.
*   **`SDMVSTRA` / `SDMVPSU`**: Masked variance pseudo-stratum and pseudo-PSU (vital for accurate variance estimation).

### Demographics & Household (`DEMO_L`)
*   **`RIDSTATR`**: Interview/Examination status (1 = Interviewed only; 2 = Interviewed & MEC examined).
*   **`RIDEXMON`**: Six-month time period when the exam was performed.
*   **`RIAGENDR`**: Gender (Male, Female).
*   **`RIDAGEYR`**: Age in years at screening (top-coded at 80 years).
*   **`RIDRETH1` / `RIDRETH3`**: Race/Hispanic origin.
*   **`DMDBORN4`**: Country of birth.
*   **`DMDHHSIZ`**: Total number of people in the household.
*   **`INDFMPIR`**: Ratio of family income to poverty guidelines.
*   **`DMDHR***`**: Information about the Household Reference Person (Gender, Age, Education, Marital Status).

### Dietary Supplements (`DSQTOT_L`)
*   **`DSD010`**: Any Dietary Supplements Taken? (1 = Yes, 2 = No)
*   **`DSD010AN`**: Any Antacids Taken? (1 = Yes, 2 = No)
*   **`DSDCOUNT`**: Total number of dietary supplements taken.
*   **`DSDANCNT`**: Total number of antacids taken.
*   **`DSQT...` variables**: Aggregated daily macro/micronutrient intakes (Energy, Protein, Vitamins, Minerals).

### Balance (`BAX_L`)
*   **`BAXMSTAT`**: MRT exam status (1 = Complete, 2 = Partial).
*   **`BAX5STAT`**: Eligibility specifically for Condition 5.
*   **`BAQ110` - `BAQ173`**: Pre-test screening questions.
*   **`BAXPF__`** (e.g., `BAXPF11`): Pass/Did not pass for the specific condition and trial.
*   **`BAXTC__`** (e.g., `BAXTC11`): Time/duration maintained during the trial.
*   **`BAARFC__`** (e.g., `BAARFC11`): Reason the trial was stopped.

### Blood Pressure (`BPXO_L`)
*   **`BPAOARM`**: Arm selected for the measurement (L = Left, R = Right).
*   **`BPAOCSZ`**: Coded cuff size based on mid-arm circumference.
*   **`BPXOSY1`, `BPXOSY2`, `BPXOSY3`**: Systolic BP (1st, 2nd, 3rd readings).
*   **`BPXODI1`, `BPXODI2`, `BPXODI3`**: Diastolic BP (1st, 2nd, 3rd readings).
*   **`BPXOPLS1`, `BPXOPLS2`, `BPXOPLS3`**: Pulse (1st, 2nd, 3rd readings).

### Body Measures (`BMX_L`)
*   **`BMDSTATS`**: Component Status Code.
*   **`BMXWT`**: Weight (kg).
*   **`BMXHT`**: Standing Height (cm).
*   **`BMXBMI`**: Body Mass Index (kg/m²).
*   **`BMXLEG`**: Upper Leg Length (cm).
*   **`BMXARML`**: Upper Arm Length (cm).
*   **`BMXARMC`**: Upper Arm Circumference (cm).
*   **`BMXWAIST`**: Waist Circumference (cm).
*   **`BMXHIP`**: Hip Circumference (cm).

### Liver Ultrasound Transient Elastography (`LUX_L`)
*   **`LUAXSTAT`**: Elastography exam status.
*   **`LUAPNME`**: Exam wand type used (M or XL).
*   **`LUANMTGP`**: Count of total measures attempted.
*   **`LUANMVGP`**: Count of valid, complete measures retained.
*   **`LUXSMED`**: Median stiffness (E) in kilopascals (kPa).
*   **`LUXSIQR`**: Interquartile range of stiffness (IQRe).
*   **`LUXSIQRM`**: Ratio of IQRe / Median stiffness.
*   **`LUXCAPM`**: Median Controlled Attenuation Parameter (CAP) in dB/m.
*   **`LUXCPIQR`**: CAP interquartile range (IQRc).

### Albumin & Creatinine - Urine (`ALB_CR_L`)
*   **`URXUMA` / `URXUMS`**: Albumin, urine in ug/mL and mg/L.
*   **`URDUMALC`**: Albumin, urine comment code.
*   **`URXUCR` / `URXCRS`**: Creatinine, urine in mg/dL and umol/L.
*   **`URDUCRLC`**: Creatinine, urine comment code.
*   **`URDACT`**: Albumin creatinine ratio (mg/g).

### Complete Blood Count (`CBC_L`)
*   **`LBXWBCSI`**: White blood cell count (1000 cells/uL).
*   **`LBXLYPCT` / `LBDLYMNO`**: Lymphocyte percent (%) & number.
*   **`LBXMOPCT` / `LBDMONO`**: Monocyte percent (%) & number.
*   **`LBXNEPCT` / `LBDNENO`**: Segmented neutrophils percent (%) & number.
*   **`LBXEOPCT` / `LBDEONO`**: Eosinophils percent (%) & number.
*   **`LBXBAPCT` / `LBDBANO`**: Basophils percent (%) & number.
*   **`LBXRBCSI`**: Red blood cell count (million cells/uL).
*   **`LBXHGB`**: Hemoglobin (g/dL).
*   **`LBXHCT`**: Hematocrit (%).
*   **`LBXMCVSI`**: Mean cell volume (fL).
*   **`LBXMC`**: Mean Cell Hemoglobin Concentration (g/dL).
*   **`LBXMCHSI`**: Mean cell hemoglobin (pg).
*   **`LBXRDW`**: Red cell distribution width (%).
*   **`LBXNRBC`**: Nucleated red blood cells (/100 WBC).
*   **`LBXPLTSI`**: Platelet count (1000 cells/uL).
*   **`LBXMPSI`**: Mean platelet volume (fL).

### Lipids - HDL & Triglycerides / LDL (`HDL_L` & `TRIGLY_L`)
*   **`LBDHDD` / `LBDHDDSI`**: Direct HDL-Cholesterol in mg/dL and mmol/L.
*   **`LBXTLG` / `LBDTRSI`**: Triglyceride in mg/dL and mmol/L.
*   **`LBDLDL` / `LBDLDLSI`**: LDL-Cholesterol, Friedewald calculated.
*   **`LBDLDLM` / `LBDLDMSI`**: LDL-Cholesterol, Martin-Hopkins calculated.
*   **`LBDLDLN` / `LBDLDNSI`**: LDL-Cholesterol, NIH equation 2 calculated.

### Inflammation (`HSCRP_L` & `AGP_L`)
*   **`LBXHSCRP`**: High-Sensitivity C-Reactive Protein (hs-CRP) (mg/L).
*   **`LBDHRPLC`**: High-Sensitivity C-Reactive Protein (hs-CRP) Comment Code.
*   *(Note: The primary variable included from the AGP dataset per specifications is the Phlebotomy Weight `WTPH2YR`)*.

### Heavy Metals (`PBCD_L`)
*   **`LBXBPB` / `LBDBPBSI`**: Blood lead in ug/dL and umol/L.
*   **`LBDBPBLC`**: Blood lead comment code.
*   **`LBXBCD` / `LBDBCDSI`**: Blood cadmium in ug/L and nmol/L.
*   **`LBDBCDLC`**: Blood cadmium comment code.
*   **`LBXTHG` / `LBDTHGSI`**: Blood mercury, total in ug/L and nmol/L.
*   **`LBDTHGLC`**: Blood mercury, total comment code.
*   **`LBXBSE` / `LBDBSESI`**: Blood selenium in ug/L and umol/L.
*   **`LBDBSELC`**: Blood selenium comment code.
*   **`LBXBMN` / `LBDBMNSI`**: Blood manganese in ug/L and nmol/L.
*   **`LBDBMNLC`**: Blood manganese comment code.
