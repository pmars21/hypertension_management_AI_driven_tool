# Dataset Summary: NHANES Balance (BAX_L)

## General Information
- **Survey Name:** National Health and Nutrition Examination Survey (NHANES)
- **Data Cycle:** August 2021 - August 2023
- **Component:** Balance
- **Data File:** `BAX_L.xpt`
- **First Published:** October 2024
- **Target Population:** Participants aged 20 to 69 years.

## Eligibility & Exclusions
Participants were **excluded** from the test if they met certain criteria:
- Pregnant or exceeding 315 pounds (weight limit for foam surface).
- Severe vision impairment, inability to stand independently, leg/foot amputations, or lower-body prosthetics.
- Recent injuries/surgeries to legs/ankles/feet, or current dizziness with a history of falls due to dizziness.
- Wearing heels 3 inches or higher.
- Inability to fit the safety belt properly.

**Condition 5 Specific Exclusions:** Participants were additionally excluded from Condition 5 if they had current neck pain, previous neck surgery, chronic neck problems, or limited neck mobility.

## Protocol Highlights (Modified Romberg Test - MRT)
The MRT assesses balance with five conditions of increasing difficulty. A participant failed a condition if they could not maintain balance for the required time across two trials.
- **Support Surface & Visual Input:**
  - **Condition 1:** Bare floor, eyes open
  - **Condition 2:** Bare floor, eyes closed
  - **Condition 3:** Dense foam, eyes open
  - **Condition 4:** Dense foam, eyes closed
  - **Condition 5:** Dense foam, eyes closed, moving head side-to-side
- **Passing criteria:**
  - **Conditions 1 & 2:** 15 seconds.
  - **Conditions 3, 4, & 5:** 20 seconds (the actual duration tested is 30 seconds, but research sets 20 seconds as a "pass" threshold).
- **Failure conditions:** Moving feet, uncrossing arms from chest, opening eyes (in closed-eye conditions), touching the wall, or needing technician intervention.

## Analytic Notes (Differences from 1999-2004 Cycle)
If comparing this data to the 1999-2004 cycle, be aware of key differences:
- **Passing Times:** In 1999-2004, participants needed 30 seconds to pass Conditions 3 and 4, whereas this cycle considers 20 seconds a pass. You may need to recode 20-29 second durations as "did not pass" for direct comparisons.
- **Condition 5:** Was not assessed in 1999-2004.
- **Variable Overhaul:** Variable names have changed (e.g., `BAXPFC11` is now `BAXPF11`, and `BAXFTC11` is now `BAXTC11`). Additionally, this cycle reports *duration time attempted* rather than *failure time*.
- **Weights:** Use the standard Exam sample weights for all analyses.

## Key Variables Overview

### 1. Survey & Status Identifiers
*   **`SEQN`**: Respondent sequence number.
*   **`BAXMSTAT`**: MRT exam status (1 = Complete, 2 = Partial, 3 = Not done, 4 = Ineligible).
*   **`BAX5STAT`**: Eligibility specifically for Condition 5.
*   **`BAXRXNC` / `BAXRXND`**: Reason statements for Partial exams (`BAXRXNC`) or Not Done exams (`BAXRXND`).

### 2. Pre-Test Screening Questions
*   **`BAQ110` - `BAQ173`**: Screening questions addressing ability to stand, use of leg braces, injuries, past dizziness/falls, neck pain, neck surgery history, and explicit consent to begin the test.

### 3. Trial Results (Repeated for Conditions 1-5, Trials 1 & 2)
Variable naming convention: **[Prefix][Condition #][Trial #]**
*   **`BAXPF__`** (e.g., `BAXPF11`): Pass/Did not pass for the specific condition and trial.
*   **`BAXTC__`** (e.g., `BAXTC11`): Time/duration maintained during the trial.
*   **`BAARFC__`** (e.g., `BAARFC11`): Reason the trial was stopped (1 = Feet moved, 2 = Arms moved off waist, 3 = Eyes opened, 4 = Tech intervention, 5 = Grab/touch wall).
