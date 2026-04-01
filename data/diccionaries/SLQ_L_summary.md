# Dataset Summary: NHANES Sleep Disorders (SLQ_L)

## General Information
- **Survey Name:** National Health and Nutrition Examination Survey (NHANES)
- **Data Cycle:** August 2021 - August 2023
- **Component:** Sleep Disorders
- **Data File:** `SLQ_L.xpt`
- **First Published:** September 2024
- **Target Population:** Participants aged 16 years and older.

## Scope & Limitations
- **Objective:** Captures respondents' usual sleep times and wake times for both weekdays and weekends, based on the Munich ChronoType Questionnaire.
- **Key Omission:** In this 2021-2023 cycle, explicit questions regarding **sleep disorders** that were present in previous cycles were **not asked**. 
- **Total Sleep Note:** The times queried apply to the "main sleeping period" and **do not** necessarily represent total sleep over a 24-hour period (i.e., regular daytime napping and light sleep periods are not included).

## Protocol Highlights
- **Administration:** Questionnaire administered in the participant's home or by telephone using the Computer-Assisted Personal Interview (CAPI) system.
- **Quality Control:** Built-in system consistency checks were used. Additionally, approximately 3% of audio-recorded interviews were reviewed to validate correct data entry, especially for unusual reported sleep/wake times.

## Data Processing & Analytic Notes
- **Derived Variables:** The variables for total sleep hours (`SLD012` and `SLD013`) were calculated from the raw sleep and wake times and rounded to the nearest half hour. If a participant did not report both a sleep time and a wake time, the total sleep hours could not be calculated.
- **Disclosure Risk Protections (Top/Bottom Coding):** To protect participant confidentiality, extreme sleep durations were recoded. Sleep lengths of less than 3 hours were assigned a code of `2`, and sleep lengths of 14 hours or more were assigned a code of `14`. For participants in these extreme categories, the raw reporting times (e.g., `SLQ300`, `SLQ310`) were wiped and set to "missing".
- **Weights:** Analysts should use the standard NHANES Analytic Guidelines for applying sample weights.

## Key Variables Overview

### 1. Identifiers
*   **`SEQN`**: Respondent sequence number.

### 2. Weekdays / Workdays
*   **`SLQ300`**: Usual time falling asleep on weekdays (Character variable 'HH:MM').
*   **`SLQ310`**: Usual time waking up on weekdays (Character variable 'HH:MM').
*   **`SLD012`**: Number of hours usually slept on weekdays (Derived from `SLQ300` and `SLQ310`. Numeric range 3 to 13.5; 2 = less than 3 hours; 14 = 14 hours or more).

### 3. Weekends / Non-Workdays
*   **`SLQ320`**: Usual time falling asleep on weekends (Character variable 'HH:MM').
*   **`SLQ330`**: Usual time waking up on weekends (Character variable 'HH:MM').
*   **`SLD013`**: Number of hours usually slept on weekends (Derived from `SLQ320` and `SLQ330`. Numeric range 3 to 13.5; 2 = less than 3 hours; 14 = 14 hours or more).
