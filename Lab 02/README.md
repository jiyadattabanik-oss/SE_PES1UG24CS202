# Lab 02 — Agile Backlog Creation & Sprint Simulation in Jira

## Project
**Pharmacy Expiry & Re-order Dispatch Engine**

This backlog is derived from the project actors and use cases visible in the Lab 03 UML: Pharmacy Clerk, Inventory Supplier, Pharmacy Administrator; view medicine stock, dispense medicine, generate FEFO dispensing list, send purchase order (automatic re-order), and manage safety-stock threshold. The user stories below operationalize those functions for Lab 2.

## 1. Epics and User Stories

### EPIC 1 — Medicine Stock Visibility
**Description:** Allow pharmacy staff to view current medicine inventory so they can make informed dispensing and replenishment decisions.

| Story | User story | Priority | Story points |
|---|---|---:|---:|
| LAB2-01 — View Medicine Stock | As a Pharmacy Clerk, I want to view the available stock of each medicine, so that I can check availability before dispensing. | High | 3 |
| LAB2-02 — View Medicine Details | As a Pharmacy Clerk, I want to view medicine details including batch and expiry information, so that I can identify the correct stock to dispense. | High | 5 |

### EPIC 2 — Safe Medicine Dispensing (FEFO)
**Description:** Support safe dispensing by presenting stock in First-Expiry-First-Out (FEFO) order.

| Story | User story | Priority | Story points |
|---|---|---:|---:|
| LAB2-03 — Generate FEFO Dispensing List | As a Pharmacy Clerk, I want the system to generate a dispensing list ordered by earliest expiry date, so that medicines closest to expiry are dispensed first. | High | 8 |
| LAB2-04 — Dispense Medicine | As a Pharmacy Clerk, I want to record medicine dispensing against the selected batch, so that stock levels remain accurate after each transaction. | High | 5 |

### EPIC 3 — Automatic Re-order and Supplier Dispatch
**Description:** Create and send purchase orders when inventory reaches the configured replenishment threshold.

| Story | User story | Priority | Story points |
|---|---|---:|---:|
| LAB2-05 — Detect Re-order Requirement | As a Pharmacy Administrator, I want the system to identify medicines that reach the re-order threshold, so that low stock can be replenished on time. | High | 5 |
| LAB2-06 — Generate and Send Purchase Order | As a Pharmacy Administrator, I want the system to generate and send a purchase order to the Inventory Supplier, so that replenishment can begin without manual order preparation. | High | 8 |

### EPIC 4 — Safety-stock Configuration
**Description:** Let the Pharmacy Administrator maintain safety-stock thresholds used by the re-order process.

| Story | User story | Priority | Story points |
|---|---|---:|---:|
| LAB2-07 — Configure Safety-stock Threshold | As a Pharmacy Administrator, I want to set or update the safety-stock threshold for a medicine, so that re-ordering reflects the pharmacy's required minimum stock. | Medium | 3 |
| LAB2-08 — Review Threshold-based Stock Status | As a Pharmacy Administrator, I want to identify medicines at or below their safety-stock threshold, so that I can monitor items requiring attention. | Medium | 3 |

### Story-point rationale

The estimates use the Fibonacci-style values specified by the Lab 2 handout (1, 2, 3, 5, 8, 13, ...). They are proposed relative estimates, not measured implementation times.

- **3 points:** straightforward view/configuration work with limited logic.
- **5 points:** more involved batch/expiry or inventory-state handling.
- **8 points:** multi-step logic and integration/validation, such as FEFO selection or purchase-order dispatch.

A team should discuss and agree estimates using Planning Poker; update these values if your team's discussion produces a different consensus.

## 2. Suggested Backlog Ordering

Order the stories in this sequence to reflect value and dependencies:

1. LAB2-01 — View Medicine Stock (High, 3)
2. LAB2-02 — View Medicine Details (High, 5)
3. LAB2-03 — Generate FEFO Dispensing List (High, 8)
4. LAB2-04 — Dispense Medicine (High, 5)
5. LAB2-05 — Detect Re-order Requirement (High, 5)
6. LAB2-06 — Generate and Send Purchase Order (High, 8)
7. LAB2-07 — Configure Safety-stock Threshold (Medium, 3)
8. LAB2-08 — Review Threshold-based Stock Status (Medium, 3)

## 3. Two-sprint simulation plan

The handout asks students to finish two sprints. A reasonable division for an educational simulation is:

### Sprint 1 — Stock visibility and safe dispensing
**Goal:** Enable the clerk to inspect available medicine and follow FEFO dispensing.

| Story | Points | Suggested final status |
|---|---:|---|
| LAB2-01 — View Medicine Stock | 3 | Done |
| LAB2-02 — View Medicine Details | 5 | Done |
| LAB2-03 — Generate FEFO Dispensing List | 8 | Done |
| LAB2-04 — Dispense Medicine | 5 | Done |
| **Total** | **21** | |

### Sprint 2 — Re-order and safety-stock management
**Goal:** Support threshold-based replenishment and supplier purchase-order dispatch.

| Story | Points | Suggested final status |
|---|---:|---|
| LAB2-05 — Detect Re-order Requirement | 5 | Done |
| LAB2-06 — Generate and Send Purchase Order | 8 | Done |
| LAB2-07 — Configure Safety-stock Threshold | 3 | Done |
| LAB2-08 — Review Threshold-based Stock Status | 3 | Done |
| **Total** | **19** | |

**Important:** These tables are a suggested simulation. In Jira, actually create the sprint(s), start the sprint, move cards from To Do → In Progress → Done, and capture the real Active Sprint and Burndown Chart screens. Do not use this document as a substitute for the Jira evidence.

## 4. Jira execution checklist

1. Create/open a **Scrum** software project (company-managed, as described in the handout) for the Pharmacy Expiry & Re-order Dispatch Engine.
2. In **Backlog**, create the four Epics above.
3. Create the eight Stories under the appropriate Epic. Use the story title as Summary and paste the complete “As a / I want / So that” text into Description.
4. Set each Story's Priority and Story Points as shown above. In the Jira issue details, look for the Story point estimate field (it may be under More fields / Configure fields depending on your Jira layout).
5. Reorder the backlog according to the suggested ordering.
6. Create **Sprint 1**, add LAB2-01 through LAB2-04, set a one-week duration, and use the goal stated above.
7. Start Sprint 1. Move each story through **To Do → In Progress → Done** as the handout directs. For a classroom simulation, perform the transitions deliberately rather than marking everything Done immediately.
8. Complete Sprint 1. Create **Sprint 2**, add LAB2-05 through LAB2-08, set a one-week duration and run the same workflow.
9. Open **Reports → Burndown Chart** for the relevant completed sprint and capture a screenshot. The chart should be based on the estimates and status transitions recorded in Jira.

## 5. Deliverable evidence checklist

Save the following screenshots inside this folder after performing the Jira actions:

- `screenshots/01_backlog_epics_stories.png` — backlog showing all Epics and Stories.
- `screenshots/02_story_points_priorities.png` — story details/backlog showing priorities and Story Point estimates.
- `screenshots/03_sprint1_active_board.png` — Sprint 1 Active Sprint board.
- `screenshots/04_sprint2_active_board.png` — Sprint 2 Active Sprint board (recommended because the handout says finish two sprints).
- `screenshots/05_burndown_chart.png` — Burndown Chart for a completed sprint.

Screenshots are intentionally not fabricated; add your own captures from the Jira workspace.

## 6. Reflection

Use these answers as a concise starting point and adjust them to match what actually happened in your Jira sprint simulation.

**1. Did your estimations reflect the actual effort?**  
The estimates provided a useful comparison of relative effort. The simpler stock-view and threshold-configuration stories were estimated at 3 points, while FEFO generation and purchase-order dispatch received higher estimates because they involve more decision logic and validation. Since this was a short simulation rather than a completed implementation, the estimates indicate expected complexity and may differ from actual development effort.

**2. Was your backlog well-prioritized?**  
The backlog placed stock visibility and safe dispensing first because the clerk needs reliable stock and expiry information before dispensing. Re-order detection and purchase-order dispatch followed, while threshold configuration and review were also included to support replenishment. This ordering reflects the main user workflows and the dependencies between them.

**3. How did your simulated sprint align with your plan?**  
The plan divided the work into two focused sprints. Sprint 1 covered stock visibility and FEFO-based dispensing. Sprint 2 covered automatic re-ordering, supplier dispatch and safety-stock management. After running the Jira simulation, this answer should be updated to mention whether each story reached Done within its sprint and any items that remained incomplete.

**4. What insights did the burndown chart give about your team's capacity?**  
The burndown chart compares remaining estimated work with an ideal progress line. A steady decline suggests work is progressing consistently; a flat section suggests little work was completed during that period; and a sudden drop can indicate several stories were completed together or that work was updated late. The chart helps assess whether the sprint commitment was realistic, but a short classroom simulation is not enough to establish long-term team velocity.

## 7. Notes and assumptions

- Project-specific scope was taken from the Lab 3 UML actors and use cases. The Lab 2 handout says to reuse Lab 1 functional requirements.
- The Epic/story breakdown, priorities, point estimates, ordering and two-sprint allocation in this file are a proposed Agile refinement of those UML functions.
- The detailed Lab 1 requirements spreadsheet and use-case flow PDF are present in the repository, but the GitHub file reader did not decode those binary files during preparation. Review them against this backlog before submitting and add or rename stories if they contain additional functions.
- A Backlog/board/report screenshot must come from the actual Jira project. This repository file documents the plan and reflection, not proof that Jira actions have been performed.
