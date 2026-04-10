# Dataset Summary: Complete Blood Count with 5-Part Differential in Whole Blood (CBC_L)

## General Information
- **Survey Name:** National Health and Nutrition Examination Survey (NHANES)
- **Data Cycle:** August 2021 - August 2023
- **Component:** Complete Blood Count
- **Data File:** `CBC_L.xpt`
- **First Published:** September 2024
- **Target Population:** Examined participants aged 1 year and over were eligible.

## Component Description
The complete blood count (CBC) with 5-part differential counts red blood cells (RBCs), white blood cells (WBCs), and platelets, measures hemoglobin; estimates the red cells’ volume; and sorts the WBCs into subtypes. A CBC is a routine blood test used to evaluate overall health and detect a wide range of disorders, including anemia, infection, and leukemia.

These data are used to estimate deficiencies and toxicities of specific nutrients in the population and subgroups, to provide population reference data, and to estimate the contribution of diet, supplements, and other factors to whole blood levels of nutrients.

## Laboratory Methodology
The methods used to derive CBC parameters are based on the Beckman Coulter methodology of counting and sizing, in combination with an automatic diluting and mixing device for sample processing, and a single beam photometer for hemoglobinometry. The WBC differential uses Volume Conductivity Scatter (VCS) technology, providing individual cell volume, high-frequency conductivity, and laser-light scatter measurements.

*Note: The Beckman Coulter DxH 800 instrument was used. There were no changes to the lab method, equipment, or site for this component in the August 2021–August 2023 cycle. In the MEC, the CBC results are measured in duplicate and averaged.*

## Data Processing and Editing
Five derived variables were created to determine absolute cell counts (rounded to 1 decimal) from percentage counts:
- **`LBDLYMNO`** = `LBXWBCSI` * `LBXLYPCT` / 100
- **`LBDMONO`** = `LBXWBCSI` * `LBXMOPCT` / 100
- **`LBDNENO`** = `LBXWBCSI` * `LBXNEPCT` / 100
- **`LBDEONO`** = `LBXWBCSI` * `LBXEOPCT` / 100
- **`LBDBANO`** = `LBXWBCSI` * `LBXBAPCT` / 100

## Analytic Notes
- **Phlebotomy Weights:** Due to nonresponse differences (e.g., 67% of children 1-17 vs. 95% of adults provided a blood specimen), an additional phlebotomy weight (`WTPH2YR`) has been included to address possible nonresponse bias. Eligible participants who did not provide a specimen receive a weight of "0". This weight should be used for analyses deriving from blood analytes.
- **Detection Limits:** Analytes with measurements below the lower limit of detection (e.g., `LBDHGBLC=1`) are imputed with the lower limit of detection divided by the square root of 2 (LLOD/sqrt[2]). 

## Key Variables Overview
*   **Survey & Weights:**
    *   **`SEQN`**: Respondent sequence number.
    *   **`WTPH2YR`**: Phlebotomy 2 Year Weight.
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
