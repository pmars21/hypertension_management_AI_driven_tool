# Dataset Summary: NHANES Mental Health - Depression Screener (DPQ_L)

## General Information
- **Survey Name:** National Health and Nutrition Examination Survey (NHANES)
- **Data Cycle:** August 2021 - August 2023
- **Component:** Mental Health - Depression Screener
- **Data File:** `DPQ_L.xpt`
- **First Published:** September 2024
- **Target Population (Public File):** Participants aged 18 years and older. *(Note: Data for youths aged 12-17 were collected but are restricted to the NCHS Research Data Center).*

## Scope & Methodology
- **Assessment Tool:** The Patient Health Questionnaire (PHQ-9), a 9-item depression screener incorporating DSM-IV depression diagnostic criteria.
- **Objective:** To determine the frequency of depression symptoms over the **past 2 weeks**.
- **Administration:** Conducted at the Mobile Examination Center (MEC) using the Audio Computer-Assisted Personal Interview (ACASI) system. This represents a shift from previous cycles, where questions were administered face-to-face.
- **Exclusions:** Due to the sensitive nature of these questions, the interview was **not** administered to participants who required a proxy informant or an interpreter. Participants had to be proficient in English or Spanish.

## Scoring & Analytic Notes
- **Symptom Scoring:** Each of the 9 symptom questions (`DPQ010` to `DPQ090`) is scored from 0 to 3 based on frequency:
  - `0` = Not at all
  - `1` = Several days
  - `2` = More than half the days
  - `3` = Nearly every day
- **Total Score:** A total score (ranging from 0 to 27) can be calculated for participants with complete responses to all 9 symptom questions. This score can be evaluated against clinical cut-points to assess major depression and severity.
- **Functional Impairment:** Question 10 (`DPQ100`) assesses the degree of difficulty these symptoms cause in daily life. It is only answered if the participant endorsed at least one symptom.
- **Weights:** Analysts should use the appropriate sample weights and survey design variables as outlined by the NHANES guidelines.

## Key Variables Overview

### 1. Identifiers
*   **`SEQN`**: Respondent sequence number.

### 2. PHQ-9 Symptom Questions (Past 2 Weeks)
*   **`DPQ010`**: Little interest or pleasure in doing things.
*   **`DPQ020`**: Feeling down, depressed, or hopeless.
*   **`DPQ030`**: Trouble falling/staying asleep, or sleeping too much.
*   **`DPQ040`**: Feeling tired or having little energy.
*   **`DPQ050`**: Poor appetite or overeating.
*   **`DPQ060`**: Feeling bad about yourself (or feeling like a failure).
*   **`DPQ070`**: Trouble concentrating on things.
*   **`DPQ080`**: Moving or speaking noticeably slowly, or conversely, being excessively fidgety/restless.
*   **`DPQ090`**: Thoughts that you would be better off dead, or thoughts of hurting yourself.

### 3. Functional Impairment
*   **`DPQ100`**: Difficulty these problems have caused with work, taking care of things at home, or getting along with people. *(0 = Not at all difficult, 1 = Somewhat difficult, 2 = Very difficult, 3 = Extremely difficult).*
