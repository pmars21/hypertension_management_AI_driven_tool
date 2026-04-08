# Dataset Summary: NHANES Prescription Medications (RXQ_RX_L)

## General Information
- **Survey Name:** National Health and Nutrition Examination Survey (NHANES)
- **Data Cycle:** August 2021 - August 2023
- **Component:** Prescription Medications
- **Data File:** `RXQ_RX_L.xpt`
- **First Published:** September 2024
- **Target Population:** All survey participants.

## Scope & Limitations
- **Objective:** Provides personal interview data on self-assessed prescription medication use in the past 30 days.
- **Included Medications:** Only products prescribed by a health professional (e.g., doctor or dentist), including prescription birth control pills/patches.
- **Excluded Medications:** Prescription vitamins and minerals.
- **Key Limitation for this Cycle:** Detailed prescription medication names, durations of use, and specific reasons for use **were not collected** during this survey cycle.
- **COVID-19 Medications:** Questions regarding COVID-19 medications were asked in the second year, but this data is restricted and only available through the NCHS Research Data Center.

## Protocol Highlights
- **Administration:** Questionnaire administered in-home or by phone using the Computer-Assisted Personal Interview (CAPI) system.
- **Respondent:** Participants 16 years and older answered directly. A proxy was used for participants under 16 or those unable to answer for themselves.
- **Cross-Validation / Hard Edits:** The CAPI system is programmed to catch inconsistencies. If a participant answers "No" to taking prescription medications, but earlier in the interview reported taking insulin, diabetes pills, high blood pressure medication, or high cholesterol medication, the system warns the interviewer to make a correction. 

## Analytic Notes & Weights
- When analyzing this data alone, use the **Interview sample weights**.
- If merging this data with the Mobile Examination Center (MEC) examination data or laboratory full sample data, use the **MEC examination weights**.
- If merging with laboratory subsample data, use the **subsample weights**.

## Key Variables Overview

### 1. Identifiers
*   **`SEQN`**: Respondent sequence number.

### 2. Medication Use (Past 30 Days)
*   **`RXQ033`**: Has the participant used or taken medication for which a prescription is needed in the past 30 days? (1 = Yes, 2 = No).
*   **`RXQ050`**: Number of prescription medications taken in the past 30 days, categorized into buckets (1 = 1, 2 = 2, 3 = 3, 4 = 4, 5 = 5 or more).
