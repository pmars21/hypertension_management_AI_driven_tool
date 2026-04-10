# Dataset Summary: Lead, Cadmium, Total Mercury, Selenium, & Manganese – Blood (PBCD_L)

## General Information
- **Survey Name:** National Health and Nutrition Examination Survey (NHANES)
- **Data Cycle:** August 2021 - August 2023
- **Component:** Lead, Cadmium, Total Mercury, Selenium, & Manganese – Blood
- **Data File:** `PBCD_L.xpt`
- **First Published:** September 2024
- **Target Population:** Examined participants aged 1 year and older were eligible.

## Component Description
- **Lead:** A known environmental toxin known to affect the nervous, hematopoietic, endocrine, renal, and reproductive systems. Children are particularly susceptible.
- **Cadmium:** Reflects both recent and cumulative exposures (inhalation and ingestion). Occupational exposure and cigarette smoking are predominant sources. It is considered a human carcinogen and mainly targets the kidneys.
- **Manganese:** An essential trace nutrient, but toxic in excess. Used largely in iron/steel production, batteries, and as an oxidizer.
- **Total Mercury:** Assesses exposure particularly from fish consumption and latex paints. Vulnerable subpopulations include children 1-5 years old and women of childbearing age.
- **Selenium:** Trace amounts are necessary for cellular function (antioxidant enzymes, thyroid hormones), but toxic in large amounts.

## Laboratory Methodology
The method directly measures lead (Pb), cadmium (Cd), total mercury (Hg), manganese (Mn), and selenium (Se) content of whole blood specimens using mass spectrometry (ICP-MS) after a simple dilution sample preparation step.
- **Sample Preparation:** Whole blood is rigorously mixed and diluted (1 part sample + 1 part water + 48 parts diluent) utilizing reagents like TMAH, Triton X-100, and APDC to solubilize blood components and internal standards (rhodium, iridium, tellurium) to correct for instrument noise and drift. Clotted samples are not analyzed.
- **Measurement:** Analysis utilizes liquid samples introduced into an inductively coupled plasma (ICP) ionization source. The dynamic reaction cell (DRC) is utilized for certain metals (Methane gas for Selenium; Oxygen gas for Manganese and Mercury) to remove interferences and focus the ion beam.

*Note: There was a change to the lab methods for the August 2021–August 2023 cycle, though lab equipment and site remained the same.*

## Data Processing and Editing
Five additional derived variables were created to convert units:
- **`LBDBCDSI`:** Cadmium value in µg/L (`LBXBCD`) converted to nmol/L (x 8.897).
- **`LBDBPBSI`:** Lead value in µg/dL (`LBXBPB`) converted to µmol/L (x 0.0483).
- **`LBDBMNSI`:** Manganese value in µg/L (`LBXBMN`) converted to nmol/L (x 18.202).
- **`LBDBSESI`:** Selenium value in µg/L (`LBXBSE`) converted to µmol/L (x 0.0127).
- **`LBDTHGSI`:** Mercury value in µg/L (`LBXTHG`) converted to nmol/L (x 4.99).

## Analytic Notes
- **Phlebotomy Weights:** Due to nonresponse differences across age groups (e.g., 67% of children vs. 95% of adults provided blood), an additional phlebotomy weight (`WTPH2YR`) is included. Participants without a blood sample receive a weight of "0". This weight should be used for analyses deriving from blood analytes.
- **Detection Limits:** For analytes with measurements below the lower limit of detection (e.g., `LBDBCDLC=1`), an imputed fill value was placed in the analyte results field, calculated as LLOD/sqrt(2).
  - LLOD for Cadmium (`LBXBCD`): 0.065 µg/L
  - LLOD for Lead (`LBXBPB`): 0.049 µg/dL
  - LLOD for Manganese (`LBXBMN`): 0.52 µg/L
  - LLOD for Total Mercury (`LBXTHG`): 0.17 µg/L
  - LLOD for Selenium (`LBXBSE`): 9.90 µg/L

## Key Variables Overview
*   **Survey & Weights:**
    *   **`SEQN`**: Respondent sequence number.
    *   **`WTPH2YR`**: Phlebotomy 2 Year Weight.
*   **Lead:**
    *   **`LBXBPB` / `LBDBPBSI`**: Blood lead in ug/dL and umol/L.
    *   **`LBDBPBLC`**: Blood lead comment code (0 = At/above LOD; 1 = Below LOD).
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
