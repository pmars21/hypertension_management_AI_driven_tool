# DEMO_L Dataset Summary: NHANES Demographic 

## General Information
- **Survey Name:** National Health and Nutrition Examination Survey (NHANES)
- **Data Cycle:** August 2021 - August 2023 
- **Component:** Demographic Variables and Sample Weights
- **Data File:** `DEMO_L.xpt`
- **First Published:** September 2024
- **Target Population:** All participants in the NHANES Aug 2021-Aug 2023 sample.
- **Missing Values:** Missing values are coded as *.*


## Survey Context & Analytic Notes (COVID-19 Impact)
- **Resumption of Operations:** Data collection resumed in Aug 2021 after being suspended in March 2020.
- **Sample Design Changes:** No person-level oversampling by race/Hispanic origin or income (unlike previous cycles), but oversampling by age group was added. This may result in lower statistical precision for certain demographic subgroups.
- **Data Gap Caution:** There is a 15-month data gap between the previous cycle and this one. Analysts should exercise strict caution when combining this data with previous cycles or conducting trend analyses.
- **Confidentiality Protections:** Due to disclosure risks, some variables (like marital status, pregnancy, age 80+, family sizes over 7) have been top-coded or restricted to certain age bands. Others are only accessible via the NCHS Research Data Center.

## Key Variables overview

### 1. Identifiers & Survey Administration
*   **`SEQN`**: Respondent sequence number (unique identifier).
*   **`SDDSRVYR`**: Data release cycle (`12` indicates the Aug 2021 - Aug 2023 cycle).
*   **`RIDSTATR`**: Interview/Examination status (1 = Interviewed only; 2 = Interviewed & MEC examined).
*   **`RIDEXMON`**: Six-month time period when the exam was performed.

### 2. Demographics
*   **`RIAGENDR`**: Gender (Male, Female).
*   **`RIDAGEYR`**: Age in years at screening (top-coded at 80 years).
*   **`RIDAGEMN` / `RIDEXAGM`**: Age in months (for toddlers/youth).
*   **`RIDRETH1` / `RIDRETH3`**: Race/Hispanic origin (Includes categories for Mexican American, Other Hispanic, Non-Hispanic White, Non-Hispanic Black, Non-Hispanic Asian, and Other/Multi-Racial).
*   **`DMDEDUC2`**: Education level for adults 20+.
*   **`DMDMARTZ`**: Marital status.
*   **`DMQMILIZ`**: Served on active duty in US Armed Forces.

### 3. Place of Birth & Residency
*   **`DMDBORN4`**: Country of birth (Born in US vs. Born in other countries).
*   **`DMDYRUSR`**: Length of time living in the US (categorical).

### 4. Household & Income
*   **`DMDHHSIZ`**: Total number of people in the household (top-coded at 7 or more).
*   **`INDFMPIR`**: Ratio of family income to poverty guidelines (top-coded at 5.00).
*   **`DMDHR***` Variables**: Information about the Household Reference Person (e.g., gender `DMDHRGND`, age `DMDHRAGZ`, education `DMDHREDZ`, marital status `DMDHRMAZ`).

### 5. Medical / Physical Status
*   **`RIDEXPRG`**: Pregnancy status at the time of exam (released only for women 20-44 years).

### 6. Sample Weights & Variance Estimation
*   **`WTINT2YR`**: Full sample 2-year interview weight.
*   **`WTMEC2YR`**: Full sample 2-year MEC exam weight.
*   **`SDMVSTRA` / `SDMVPSU`**: Masked variance pseudo-stratum and pseudo-PSU (vital for accurate variance estimation).
