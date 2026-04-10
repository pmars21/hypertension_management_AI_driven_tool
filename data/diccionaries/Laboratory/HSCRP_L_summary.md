# Dataset Summary: High-Sensitivity C-Reactive Protein (HSCRP_L)

## General Information
- **Survey Name:** National Health and Nutrition Examination Survey (NHANES)
- **Data Cycle:** August 2021 - August 2023
- **Component:** High-Sensitivity C-Reactive Protein
- **Data File:** `HSCRP_L.xpt`
- **First Published:** September 2024
- **Target Population:** Examined participants aged 1 year and older were eligible.

## Component Description
C-reactive protein (CRP) is an acute phase protein synthesized in the liver. It is involved in the activation of complement, enhancement of phagocytosis, and detoxification of substances released from damaged tissue. It is one of the most sensitive, though nonspecific, indicators of inflammation. CRP levels may rise within six hours of an inflammatory stimulus. Measurement of CRP concentrations by this highly sensitive method is performed primarily to ascertain the level of cardiovascular disease risk in individuals who have no existing inflammatory conditions. Increases in CRP concentration are non-specific and should be used in conjunction with traditional clinical laboratory evaluation of acute coronary syndromes.

## Laboratory Methodology
This is a two-reagent, immunoturbidimetric system. The specimen is first combined with a Tris buffer, then incubated. The second reagent (latex particles coated with mouse anti-human CRP antibodies) is then added. In the presence of circulating CRP the latex particles aggregate, forming immune complexes. These complexes cause an increase in light scattering that is proportional to the CRP concentration. The light absorbance resulting from this light scatter is read against a stored CRP standard curve. Turbidity is measured at a primary wavelength of 546 nm.

*Note: There were no changes to the lab method or lab site. However, the laboratory equipment changed from the Cobas 6000 Analyzer to the Cobas 8000.*

## Analytic Notes
- **Methodology Shift:** Because of the equipment change from the Cobas 6000 to the Cobas 8000, a bridging study showed values measured with the old Cobas 6000 instrument were 14.28% higher than values measured with the Cobas 8000 instrument. Regression equations are provided in the official documentation to compare data across cycles.
- **Phlebotomy Weights:** Due to nonresponse differences, an additional phlebotomy weight (`WTPH2YR`) is included to address possible nonresponse bias. Eligible participants who did not provide a blood specimen receive a weight of "0". This weight should be used for analyses deriving from blood analytes.
- **Detection Limits:** For analytes with measurements below the lower limit of detection (e.g., `LBDHRPLC=1`), an imputed fill value was placed in the analyte results field, calculated as LLOD/sqrt(2).
  - LLOD for High-Sensitivity C-Reactive Protein (`LBXHSCRP`): 0.15 mg/L

## Key Variables Overview
*   **`SEQN`**: Respondent Sequence Number.
*   **`WTPH2YR`**: Phlebotomy 2 Year Weight.
*   **`LBXHSCRP`**: High-Sensitivity C-Reactive Protein (hs-CRP) (mg/L).
*   **`LBDHRPLC`**: High-Sensitivity C-Reactive Protein (hs-CRP) Comment Code (0 = At or above detection limit; 1 = Below lower detection limit).
