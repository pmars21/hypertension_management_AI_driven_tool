# Dataset Summary: Cholesterol – High-Density Lipoprotein (HDL_L)

## General Information
- **Survey Name:** National Health and Nutrition Examination Survey (NHANES)
- **Data Cycle:** August 2021 - August 2023
- **Component:** Cholesterol – High-Density Lipoprotein (HDL-C)
- **Data File:** `HDL_L.xpt`
- **First Published:** September 2024
- **Target Population:** Examined participants aged 6 years and older were eligible.

## Component Description
Blood lipid levels are fundamental measures used for cardiovascular risk assessment. Heart disease is the leading cause of death in the United States. The blood lipids measurements in NHANES include total cholesterol, high-density lipoprotein cholesterol (HDL-C), low-density lipoprotein cholesterol (LDL-C), and triglycerides.

*Note: This specific dataset (`HDL_L`) focuses exclusively on High-Density Lipoprotein (HDL-C). Details for total cholesterol are found in `TCHOL_L`, and LDL-C and triglycerides in `TRIGLY_L`.*

## Laboratory Methodology
High-Density Lipoprotein (HDL-C) is measured utilizing an automated HDLC4 assay using detergents, cholesterol esterase (CHER), cholesterol oxidase (CHOD), and peroxidase to form a colored pigment evaluated optically. This assay blocks non-HDL lipoproteins (LDL, VLDL, chylomicrons) using polyanions and a detergent so that only HDL-particles can react enzymatically with CHER and CHOD.

*Note: There were no changes to the lab method or lab site. However, the laboratory equipment changed from the Cobas 6000 Analyzer to the Cobas 8000. A bridging study confirmed no significance difference bridging the instruments, making data adjustment unnecessary.*

## Data Processing and Editing
One derived variable was created to convert conventional units into standardized SI units:
- **`LBDHDDSI`:** HDL-cholesterol in mg/dL (`LBDHDD` / `LBXHDD`) was converted to mmol/L (`LBDHDDSI`) by multiplying by 0.02586.

## Analytic Notes
- **Phlebotomy Weights:** Due to nonresponse differences across demographic groups (e.g., higher response rate in adults vs. children), an additional phlebotomy weight (`WTPH2YR`) is included to address possible nonresponse bias. Participants eligible but without a blood specimen receive a weight of "0". The phlebotomy weight should be used for analyses deriving from blood analytes.
- **Detection Limits:** For analytes with measurements below the lower limit of detection, an imputed fill value was placed in the analyte results field, calculated as LLOD/sqrt(2).
  - LLOD for HDL Cholesterol: 3 mg/dL

## Key Variables Overview
*   **Survey & Weights:**
    *   **`SEQN`**: Respondent Sequence Number.
    *   **`WTPH2YR`**: Phlebotomy 2 Year Weight.
*   **HDL-Cholesterol:**
    *   **`LBDHDD`**: Direct HDL-Cholesterol (mg/dL).
    *   **`LBDHDDSI`**: Direct HDL-Cholesterol (mmol/L).
