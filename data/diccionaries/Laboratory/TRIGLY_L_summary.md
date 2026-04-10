# Dataset Summary: Cholesterol - Low-Density Lipoproteins (LDL) & Triglycerides (TRIGLY_L)

## General Information
- **Survey Name:** National Health and Nutrition Examination Survey (NHANES)
- **Data Cycle:** August 2021 - August 2023
- **Component:** Cholesterol - Low-Density Lipoproteins (LDL-C) & Triglycerides
- **Data File:** `TRIGLY_L.xpt`
- **First Published:** September 2025
- **Target Population:** Participants aged 12 years and older who were examined in the morning sessions were eligible.

## Component Description
Blood lipid levels are fundamental measures used for cardiovascular risk assessment. In 2018, new Blood Cholesterol Guidelines were released, which aim to reduce the risk of atherosclerotic cardiovascular disease through cholesterol management. The blood lipids measurements in NHANES include total cholesterol, high-density lipoprotein cholesterol (HDL-C), low-density lipoproteins cholesterol (LDL-C), and triglycerides. 
*Note: This specific dataset (`TRIGLY_L`) provides data on LDL-C and triglycerides. Data on total cholesterol are provided in `TCHOL_L`, and HDL-C data are provided in `HDL_L`.*

## Laboratory Methodology
- **Triglycerides:** Measured using a method based on lipoprotein lipase for the rapid/complete hydrolysis of triglycerides to glycerol. The derived hydrogen peroxide reacts to form a red dyestuff with color intensity directly proportional to triglyceride concentration.
   *Change in Cycle:* The glycerol blanked assay used in previous cycles was phased out by the manufacturer. The equipment was updated from the Cobas 6000 Analyzer to the Cobas 8000. 
- **LDL-C:** Serum LDL-C levels were calculated from directly measured values of total cholesterol, triglycerides, and HDL-C (they were not directly measured, but derived).

## Data Processing and Editing
Seven derived variables were created: one for triglycerides and six for LDL-C.

**Triglycerides:**
- **`LBDTRSI`:** Triglycerides values in mg/dL (`LBXTLG`) were converted to mmol/L (`LBDTRSI`) (x 0.01129).

**Calculated LDL-C (Derived from Total Cholesterol, Triglycerides, HDL-C):**
Three equations are used/released, with both standard and SI units:
1. **Friedewald Equation:** The standard clinical equation for decades. It uses a fixed factor of 5 to estimate the triglyceride to VLDL-C ratio. Known to underestimate LDL-C at levels <70 mg/dL or high triglycerides. Not valid for triglycerides >400 mg/dL.
    - **`LBDLDL`** (mg/dL) & **`LBDLDLSI`** (mmol/L)
2. **Martin-Hopkins Equation:** Recommended in the 2018 guidelines for LDL-C <70 mg/dL. Retains the standard equation form but applies an adjustable factor based on non-HDL cholesterol and triglyceride concentrations. Not valid for triglycerides >400 mg/dL.
    - **`LBDLDLM`** (mg/dL) & **`LBDLDMSI`** (mmol/L)
3. **NIH Equation 2:** Released in 2020. Validated for triglyceride levels up to 800 mg/dL.
    - **`LBDLDLN`** (mg/dL) & **`LBDLDNSI`** (mmol/L)

## Analytic Notes
- **Subsample Weights:** Triglycerides were measured in a fasting subsample. Analysts must use the **Fasting Subsample 2 Year MEC Weight (`WTSAF2YR`)**. Participants who did not provide blood or failed the 8 to <24 hours fasting criteria received a sample weight of "0" for analyzing triglycerides.
- **Data Source Choice:** Use `LBXTLG` from this file rather than the older `LBXSTR` from the Standard Biochemistry Profile (`BIOPRO_L`).
- **Detection Limits:** LLOD for Serum Triglycerides (`LBXTLG`) is 9 mg/dL.
- **Methodology Shift:** Bridging studies resulting from instrument and method upgrades indicated a correlation (r=0.999). Two regression equations are available in the official codebook documentation to ensure comparability with non-glycerol and glycerol blanked methods across cycles.

## Key Variables Overview
*   **Survey & Weights:**
    *   **`SEQN`**: Respondent Sequence Number.
    *   **`WTSAF2YR`**: Fasting Subsample 2 Year MEC Weight.
*   **Triglycerides:**
    *   **`LBXTLG`**: Triglyceride (mg/dL).
    *   **`LBDTRSI`**: Triglyceride (mmol/L).
*   **LDL-Cholesterol Calculated (Friedewald):**
    *   **`LBDLDL`**: LDL-Cholesterol, Friedewald (mg/dL).
    *   **`LBDLDLSI`**: LDL-Cholesterol, Friedewald (mmol/L).
*   **LDL-Cholesterol Calculated (Martin-Hopkins):**
    *   **`LBDLDLM`**: LDL-Cholesterol, Martin-Hopkins (mg/dL).
    *   **`LBDLDMSI`**: LDL-Cholesterol, Martin-Hopkins (mmol/L).
*   **LDL-Cholesterol Calculated (NIH Equation 2):**
    *   **`LBDLDLN`**: LDL-Cholesterol, NIH equation 2 (mg/dL).
    *   **`LBDLDNSI`**: LDL-Cholesterol, NIH equation 2 (mmol/L).
