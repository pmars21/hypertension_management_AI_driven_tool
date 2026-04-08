# Dataset Summary: NHANES Reproductive Health (RHQ_L)

## General Information
- **Survey Name:** National Health and Nutrition Examination Survey (NHANES)
- **Data Cycle:** August 2021 - August 2023
- **Component:** Reproductive Health
- **Data File:** `RHQ_L.xpt`
- **First Published:** September 2024
- **Target Population:** Female participants aged 12 years and older.

## Scope & Methodology
- **Topics Covered:** Menstrual history, pregnancy history, current breastfeeding, and surgical/reproductive conditions (e.g., hysterectomy, ovary removal, pelvic infections).
- **Administration:** Administered at the Mobile Examination Center (MEC) using the Audio Computer-Assisted Self-Interview (ACASI) system (in English and Spanish only). In previous cycles this was administered face-to-face.
- **Exclusions:** Due to the sensitive nature of these questions, the interview was **not** administered to proxy informants. 

## Analytic Notes & Limitations
- **Data Disclosure Protections:** This public use file **excludes** select variables related to pregnancy and hysterectomies for females aged 12-19 and older than 44 years to protect confidentiality. (The unrestricted data is available via the NCHS Research Data Center).
- **Dropped Questions:** Numerous questions from previous cycles (e.g., specific birth control details, etc.) were dropped for this 2021-2023 cycle and are absent from the dataset.
- **Pregnancy Status Discrepancy Note:** The current pregnancy status variable within this dataset (`RHD143`) comes directly from the questionnaire response and may sometimes differ from the overarching pregnancy status variable (`RIDEXPRG`) found in the Demographic (DEMO) data file.
- **Weights:** Analysts should rely on the standard NHANES Analytic Guidelines for the use of sample weights.

## Key Variables Overview

### 1. Identifiers
*   **`SEQN`**: Respondent sequence number.

### 2. Menstrual History
*   **`RHQ010`**: Age when the first menstrual period occurred.
*   **`RHQ031`**: Has the participant had regular periods in the past 12 months?
*   **`RHD043`**: Reason for not having regular periods (e.g., pregnancy, breastfeeding, hysterectomy, menopause).
*   **`RHQ060`**: Age at the last menstrual period.

### 3. Pregnancy & Breastfeeding
*   **`RHQ131`**: Has the participant ever been pregnant?
*   **`RHD143`**: Is the participant currently pregnant?
*   **`RHD167`**: Total number of deliveries (counting vaginal/Cesarean, live births, and stillbirths; multiples count as a single delivery).
*   **`RHQ200`**: Is the participant currently breastfeeding a child?

### 4. Surgeries & Infections
*   **`RHQ078`**: Has the participant ever been treated for a pelvic infection or Pelvic Inflammatory Disease (PID)?
*   **`RHD280`**: Has the participant had a hysterectomy (uterus removed)?
*   **`RHQ305`**: Has the participant had both ovaries removed?
*   **`RHQ332`**: Age when both ovaries were removed (or age at last ovary removal).
