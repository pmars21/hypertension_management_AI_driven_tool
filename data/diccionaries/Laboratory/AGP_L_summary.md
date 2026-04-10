# Dataset Summary: alpha-1-Acid Glycoprotein (AGP_L)

## General Information
- **Survey Name:** National Health and Nutrition Examination Survey (NHANES)
- **Data Cycle:** August 2021 - August 2023
- **Component:** alpha-1-Acid Glycoprotein
- **Data File:** `AGP_L.xpt`
- **First Published:** September 2024
- **Target Population:** Examined participants 1-5 years old and 12-49 years old females were eligible.

## Component Description
Alpha-1-Acid Glycoprotein (AGP) is synthesized in the liver and structurally belongs to the lipocalin superfamily of secretory proteins. AGP is a sensitive acute phase reactant whose concentration can increase by a factor of 3 within 24-48 hours when inflammation occurs. It can also be used to differentiate between acute phase reactions (elevated serum level) and estrogen effects (normal or decreased serum level). The determination is used in the assessment of the activity of acute and recurring inflammations as well as of tumors with cell necrosis.

## Laboratory Methodology
The Tina-quant Roche AGP assay is based on the principle of immunological agglutination. Anti-alpha-1-acid glycoprotein antibodies react with antigen in the sample to form an antigen/antibody complex. Following agglutination, this is measured turbidimetrically. 

*Note: This was a new component in the NHANES August 2021–August 2023 cycle.*

## Analytic Notes
- **Phlebotomy Weights:** Because analysis of nonresponse patterns for the phlebotomy component revealed differences by age group and race/ethnicity, an additional phlebotomy weight (`WTPH2YR`) has been included in this data release to address possible nonresponse bias. Participants who are eligible but did not provide a blood specimen receive a weight of "0". The phlebotomy weight should be used for analyses that use variables derived from blood analytes.
- **Detection Limits:** For analytes with analytic results below the lower limit of detection (e.g., `LBDAGPLC=1`), an imputed fill value was placed in the analyte results field, calculated as LLOD/sqrt(2).
  - LLOD for alpha-1-acid glycoprotein (`LBXAGP`): 0.1 g/L

## Key Variables Overview
*   **`SEQN`**: Respondent sequence number.
*   **`WTPH2YR`**: Phlebotomy 2 Year Weight.
*   **`LBXAGP`**: alpha-1-acid glycoprotein (g/L).
