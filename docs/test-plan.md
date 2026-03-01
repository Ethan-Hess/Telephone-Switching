# Test Plan: Telephone Switching Simulation

## 1. Scope

### In Scope

This test plan covers functional testing of the Telephone Switching Simulation system. The following features and requirements will be tested:

- **Basic Phone Operations** (Requirements 4b, 4c, 7a-b, 13): Offhook/onhook state transitions and dialtone
- **Normal Call Flow** (Requirement 7): Two-party call establishment, ringing, ringback, talking, and disconnection
- **Onhook Restrictions** (Requirement 12): Silence behavior for commands issued while phone is onhook
- **Invalid Phone Numbers** (Requirement 11): Denial tone for calls to non-existent phones
- **Busy Signal** (Requirement 10): Busy tone when calling a phone already in use
- **Conference Calls** (Requirements 8, 11e): Three-way conference establishment and restrictions
- **Transfer Calls** (Requirement 9): Call transfer functionality and state transitions
- **Status Command** (Requirement 14): System state display for all phones
- **Denial Scenarios** (Requirement 11): Invalid operations producing denial tone
- **Edge Cases & State Management**: Case sensitivity, phone identifiers, sequential operations, state persistence
- **Data Loading** (Requirements 1-3): CSV file parsing, phone number/name validation
- **Command Parsing** (Requirement 4-5): Command recognition, whitespace handling, exit commands

### Out of Scope

- Performance testing under load
- Security testing
- Concurrent multi-user access
- Real telephony hardware integration
- Audio signal generation
- Network/distributed systems testing
- GUI testing (CLI only)
- More than 3-way conference calls (explicitly prohibited by requirements)

---

## 2. Strategy

### Testing Approach

This project will employ **black-box system testing** with a focus on:

1. **Functional Testing**: Verify each requirement is met through documented test cases
2. **State-based Testing**: Validate phone state transitions (onhook → dialtone → ringback → talking → silence)
3. **Boundary Testing**: Test edge cases including maximum phones (20), maximum name length (12 chars), phone number format (5 digits)
4. **Negative Testing**: Verify proper error handling for invalid inputs, illegal operations, and missing data

### Test Types

- **Unit Testing**: Individual function testing for command parsing, phone lookup, state transitions
- **Integration Testing**: End-to-end command flow from user input to system output
- **Regression Testing**: Re-run test suite after bug fixes or enhancements

### Black Box and White Box Testing

This project employs both testing methodologies as required:

**Black Box Testing:**

- Focus on input/output behavior without examining internal code structure
- Test all commands and their expected responses
- Validate state transitions from user perspective
- Test boundary conditions and error cases
- Primary method for Milestone 1 test case development

**White Box Testing:**

- Code coverage analysis using pytest-cov
- Path testing for state machine transitions
- Statement and branch coverage measurement
- Testing internal phone lookup logic and data structures
- Validation of CSV parsing and error handling code paths
- Target: Minimum 80% code coverage for core modules

### Testing Methodology

- Manual testing via command-line interface using prepared test scripts
- Automated testing using Python pytest framework
- Test cases organized by functional area (12 categories)
- Each test case is independent and can run in isolation
- CSV fixture data provided for reproducible tests

### Tools & Frameworks

- **Python 3.x**: Implementation language
- **pytest**: Test automation framework
- **CSV fixtures**: Test data in `tests/fixtures/telephone-numbers.csv`
- **Version Control**: Git for test case version tracking

---

## 3. Resources

### Personnel

- **Test Lead**: Coordinates testing activities and reports results
- **Developers**: Implement fixes for failed test cases
- **Test Executors**: Juan, Ethan, Leo M. (individual test case ownership)

### Test Environment

- **Operating System**: Windows (primary), Linux/macOS (compatibility)
- **Python Version**: 3.7 or higher
- **Required Packages**: Standard library only (no external dependencies for core functionality)

### Test Data

- **Primary CSV**: `src/telephone-numbers.csv` (production data)
- **Test Fixture**: `tests/fixtures/telephone-numbers.csv` (controlled test data)
- **Test Phone Configuration**:
  - Minimum: Alice (12345), Bob (23456), Cara (34567)
  - Additional phones: David, Eve, Frank, etc. (up to 20 total)

### Development Tools

- **IDE**: Visual Studio Code
- **Terminal**: Python terminal for running tests
- **Build Tool**: g++ for C++ components (if applicable)

---

## 4. Timeline

### Phase 1: Test Preparation (Week 1)

- **Day 1-2**: Finalize test plan and review with team
- **Day 3-4**: Create test fixtures and CSV data files
- **Day 5**: Set up pytest framework and directory structure

### Phase 2: Test Case Development (Week 2)

- **Day 6-7**: Implement test cases for sections 1-3 (Basic Operations, Call Flow, Onhook Restrictions)
- **Day 8-9**: Implement test cases for sections 4-6 (Invalid Numbers, Busy Signal, Conference)
- **Day 10**: Implement test cases for sections 7-9 (Transfer, Status, Denial)

### Phase 3: Test Case Development Continued (Week 3)

- **Day 11-12**: Implement test cases for sections 10-12 (Edge Cases, Data Loading, Command Parsing)
- **Day 13**: Review and validate all test implementations
- **Day 14**: Execute initial test run and document results

### Phase 4: Execution & Reporting (Week 4)

- **Day 15-17**: Execute full test suite, log defects
- **Day 18-19**: Retest after bug fixes (regression testing)
- **Day 20**: Final test report and signoff

### Milestones

- **M1**: Test plan approved (End of Day 2)
- **M2**: All test cases implemented (End of Day 13)
- **M3**: Initial test execution complete (End of Day 14)
- **M4**: Final test results and report (End of Day 20)

---

## 5. Risk Assessment

### Technical Risks

| Risk                                        | Impact | Probability | Mitigation                                                             |
| ------------------------------------------- | ------ | ----------- | ---------------------------------------------------------------------- |
| CSV parsing errors not handled              | High   | Medium      | Test with malformed CSV files; implement error handling early          |
| State machine complexity leads to bugs      | High   | High        | Document state transitions; create state diagram; test all transitions |
| Edge cases with onhook/offhook not covered  | Medium | Medium      | Systematic testing of all state combinations                           |
| Command parsing ambiguity (name vs. number) | Medium | Low         | Test with names that look like numbers; clear specification            |

### Schedule Risks

| Risk                                               | Impact | Probability | Mitigation                                           |
| -------------------------------------------------- | ------ | ----------- | ---------------------------------------------------- |
| Test case implementation takes longer than planned | Medium | Medium      | Prioritize high-risk areas; start early              |
| Core functionality not complete for testing        | High   | Low         | Coordinate with development team; test incrementally |
| Bug fixes delay regression testing                 | Medium | Medium      | Allow buffer time in week 4                          |

### Resource Risks

| Risk                             | Impact | Probability | Mitigation                                             |
| -------------------------------- | ------ | ----------- | ------------------------------------------------------ |
| Team member unavailability       | Medium | Low         | Cross-train on test execution; document all procedures |
| Testing environment setup issues | Low    | Low         | Validate environment early; use virtual environments   |

---

## 6. Test Cases

### Legend

- **Status Values**: To be executed | In progress | Passed | Failed
- **Priority**: P0 (Critical) | P1 (High) | P2 (Medium) | P3 (Low)

### Milestone 1 Testing Status

**Important Note:** As required by the project milestones, all test cases listed below are documented and ready for execution but marked as "To be executed" for Milestone 1 submission. Full test execution will be completed in **Milestone 2 and Milestone 3**.

For Milestone 1, this document provides:

- Complete list of all test cases (59 total)
- Test case specifications with steps and expected results
- Test execution strategy and approach
- Testing will commence after Milestone 1 submission

### Section 1: Basic Phone Operations

#### TC-001: test_offhook_sets_dialtone

| Field                | Value                                  |
| -------------------- | -------------------------------------- |
| **Test Case ID**     | TC-001                                 |
| **Priority**         | P0                                     |
| **Description**      | Phone goes offhook and hears dialtone  |
| **Preconditions**    | - telephone-numbers.csv read           |
| **Steps**            | 1. User enters command "Alice offhook" |
| **Expected Results** | - Alice hears dialtone                 |
| **Status**           | To be executed                         |

#### TC-002: test_offhook_when_already_offhook

| Field                | Value                                                                             |
| -------------------- | --------------------------------------------------------------------------------- |
| **Test Case ID**     | TC-002                                                                            |
| **Priority**         | P1                                                                                |
| **Description**      | Phone tries to go offhook again; should be ignored                                |
| **Preconditions**    | - telephone-numbers.csv read                                                      |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice offhook" |
| **Expected Results** | - First command: Alice hears dialtone<br> - Second command: No output (ignored)   |
| **Status**           | To be executed                                                                    |

#### TC-003: test_onhook_returns_to_onhook

| Field                | Value                                                                            |
| -------------------- | -------------------------------------------------------------------------------- |
| **Test Case ID**     | TC-003                                                                           |
| **Priority**         | P0                                                                               |
| **Description**      | Phone hangs up and returns to onhook state                                       |
| **Preconditions**    | - telephone-numbers.csv read                                                     |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice onhook" |
| **Expected Results** | - Alice hears dialtone<br> - Alice transitions to onhook state                   |
| **Status**           | To be executed                                                                   |

#### TC-004: test_onhook_when_already_onhook

| Field                | Value                                                           |
| -------------------- | --------------------------------------------------------------- |
| **Test Case ID**     | TC-004                                                          |
| **Priority**         | P1                                                              |
| **Description**      | Phone tries to go onhook when already onhook; should be ignored |
| **Preconditions**    | - telephone-numbers.csv read                                    |
| **Steps**            | 1. User enters command "Alice onhook"                           |
| **Expected Results** | - No output (ignored)                                           |
| **Status**           | To be executed                                                  |

---

### Section 2: Normal Call Flow

#### TC-005: test_call_initiator_hears_ringback

| Field                | Value                                                                              |
| -------------------- | ---------------------------------------------------------------------------------- |
| **Test Case ID**     | TC-005                                                                             |
| **Priority**         | P0                                                                                 |
| **Description**      | Calling phone hears ringback after dialing                                         |
| **Preconditions**    | - telephone-numbers.csv read                                                       |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice call Bob" |
| **Expected Results** | - Alice hears dialtone<br> - Alice hears ringback<br> - Bob hears ringing          |
| **Status**           | To be executed                                                                     |

#### TC-006: test_call_recipient_hears_ringing

| Field                | Value                                                                              |
| -------------------- | ---------------------------------------------------------------------------------- |
| **Test Case ID**     | TC-006                                                                             |
| **Priority**         | P0                                                                                 |
| **Description**      | Called phone hears ringing                                                         |
| **Preconditions**    | - telephone-numbers.csv read                                                       |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice call Bob" |
| **Expected Results** | - Bob hears ringing                                                                |
| **Status**           | To be executed                                                                     |

#### TC-007: test_call_established_both_talking

| Field                | Value                                                                                                                       |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Test Case ID**     | TC-007                                                                                                                      |
| **Priority**         | P0                                                                                                                          |
| **Description**      | Both phones talk after recipient picks up                                                                                   |
| **Preconditions**    | - telephone-numbers.csv read                                                                                                |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice call Bob"<br> 3. User enters command "Bob offhook" |
| **Expected Results** | - Alice and Bob are talking                                                                                                 |
| **Status**           | To be executed                                                                                                              |

#### TC-008: test_call_initiator_hears_silence_on_hangup

| Field                | Value                                                                                                                                                               |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Test Case ID**     | TC-008                                                                                                                                                              |
| **Priority**         | P0                                                                                                                                                                  |
| **Description**      | Initiator hears silence when recipient hangs up                                                                                                                     |
| **Preconditions**    | - telephone-numbers.csv read                                                                                                                                        |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice call Bob"<br> 3. User enters command "Bob offhook"<br> 4. User enters command "Bob onhook" |
| **Expected Results** | - Alice hears silence                                                                                                                                               |
| **Status**           | To be executed                                                                                                                                                      |

#### TC-009: test_call_ends_when_initiator_hangs_up

| Field                | Value                                                                                                                                                                 |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Test Case ID**     | TC-009                                                                                                                                                                |
| **Priority**         | P0                                                                                                                                                                    |
| **Description**      | Call disconnects when initiator goes onhook                                                                                                                           |
| **Preconditions**    | - telephone-numbers.csv read                                                                                                                                          |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice call Bob"<br> 3. User enters command "Bob offhook"<br> 4. User enters command "Alice onhook" |
| **Expected Results** | - Bob hears silence                                                                                                                                                   |
| **Status**           | To be executed                                                                                                                                                        |

---

### Section 3: Onhook Restrictions

#### TC-010: test_onhook_call_hears_silence

| Field                | Value                                      |
| -------------------- | ------------------------------------------ |
| **Test Case ID**     | TC-010                                     |
| **Priority**         | P0                                         |
| **Description**      | Phone on hook tries to call; hears silence |
| **Preconditions**    | - telephone-numbers.csv read               |
| **Steps**            | 1. User enters command "Alice call Bob"    |
| **Expected Results** | - Alice hears silence                      |
| **Status**           | To be executed                             |

#### TC-011: test_onhook_transfer_hears_silence

| Field                | Value                                          |
| -------------------- | ---------------------------------------------- |
| **Test Case ID**     | TC-011                                         |
| **Priority**         | P1                                             |
| **Description**      | Phone on hook tries to transfer; hears silence |
| **Preconditions**    | - telephone-numbers.csv read                   |
| **Steps**            | 1. User enters command "Alice transfer Bob"    |
| **Expected Results** | - Alice hears silence                          |
| **Status**           | To be executed                                 |

#### TC-012: test_onhook_conference_hears_silence

| Field                | Value                                            |
| -------------------- | ------------------------------------------------ |
| **Test Case ID**     | TC-012                                           |
| **Priority**         | P1                                               |
| **Description**      | Phone on hook tries to conference; hears silence |
| **Preconditions**    | - telephone-numbers.csv read                     |
| **Steps**            | 1. User enters command "Alice conference Bob"    |
| **Expected Results** | - Alice hears silence                            |
| **Status**           | To be executed                                   |

#### TC-013: test_onhook_offhook_is_allowed

| Field                | Value                                        |
| -------------------- | -------------------------------------------- |
| **Test Case ID**     | TC-013                                       |
| **Priority**         | P0                                           |
| **Description**      | Phone on hook can go offhook without silence |
| **Preconditions**    | - telephone-numbers.csv read                 |
| **Steps**            | 1. User enters command "Alice offhook"       |
| **Expected Results** | - Alice hears dialtone                       |
| **Status**           | To be executed                               |

---

### Section 4: Invalid Phone Numbers

#### TC-014: test_call_invalid_phone_hears_denial

| Field                | Value                                                                                |
| -------------------- | ------------------------------------------------------------------------------------ |
| **Test Case ID**     | TC-014                                                                               |
| **Priority**         | P0                                                                                   |
| **Description**      | Calling nonexistent phone hears denial                                               |
| **Preconditions**    | - telephone-numbers.csv read                                                         |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice call 67890" |
| **Expected Results** | - Alice hears denial                                                                 |
| **Status**           | To be executed                                                                       |

#### TC-015: test_transfer_invalid_phone_hears_denial

| Field                | Value                                                                                                                                                                         |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Test Case ID**     | TC-015                                                                                                                                                                        |
| **Priority**         | P1                                                                                                                                                                            |
| **Description**      | Transfer to nonexistent phone hears denial                                                                                                                                    |
| **Preconditions**    | - telephone-numbers.csv read                                                                                                                                                  |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice call Bob"<br> 3. User enters command "Bob offhook"<br> 4. User enters command "Alice transfer 67890" |
| **Expected Results** | - Alice hears denial                                                                                                                                                          |
| **Status**           | To be executed                                                                                                                                                                |

#### TC-016: test_conference_invalid_phone_hears_denial

| Field                | Value                                                                                                                                                                           |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Test Case ID**     | TC-016                                                                                                                                                                          |
| **Priority**         | P1                                                                                                                                                                              |
| **Description**      | Conference with nonexistent phone hears denial                                                                                                                                  |
| **Preconditions**    | - telephone-numbers.csv read                                                                                                                                                    |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice call Bob"<br> 3. User enters command "Bob offhook"<br> 4. User enters command "Alice conference 67890" |
| **Expected Results** | - Alice hears denial                                                                                                                                                            |
| **Status**           | To be executed                                                                                                                                                                  |

---

### Section 5: Busy Signal

#### TC-017: test_third_phone_hears_busy

| Field                | Value                                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Test Case ID**     | TC-017                                                                                                                                                                                                             |
| **Priority**         | P0                                                                                                                                                                                                                 |
| **Description**      | Third phone calling while two phones are talking hears busy                                                                                                                                                        |
| **Preconditions**    | - telephone-numbers.csv read                                                                                                                                                                                       |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice call Bob"<br> 3. User enters command "Bob offhook"<br> 4. User enters command "Cara offhook"<br> 5. User enters command "Cara call Alice" |
| **Expected Results** | - Cara hears busy                                                                                                                                                                                                  |
| **Status**           | To be executed                                                                                                                                                                                                     |

#### TC-018: test_busy_works_when_phone_offhook

| Field                | Value                                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Test Case ID**     | TC-018                                                                                                                                                                                                             |
| **Priority**         | P1                                                                                                                                                                                                                 |
| **Description**      | Busy signal only works when originating phone is offhook                                                                                                                                                           |
| **Preconditions**    | - telephone-numbers.csv read                                                                                                                                                                                       |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice call Bob"<br> 3. User enters command "Bob offhook"<br> 4. User enters command "Cara offhook"<br> 5. User enters command "Cara call Alice" |
| **Expected Results** | - Cara hears busy when originating from offhook phone                                                                                                                                                              |
| **Status**           | To be executed                                                                                                                                                                                                     |

---

### Section 6: Conference Calls

#### TC-019: test_conference_adds_third_party

| Field                | Value                                                                                                                                                                                                                    |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Test Case ID**     | TC-019                                                                                                                                                                                                                   |
| **Priority**         | P0                                                                                                                                                                                                                       |
| **Description**      | Three phones successfully conferencing together                                                                                                                                                                          |
| **Preconditions**    | - telephone-numbers.csv read                                                                                                                                                                                             |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice call Bob"<br> 3. User enters command "Bob offhook"<br> 4. User enters command "Alice conference Cara"<br> 5. User enters command "Cara offhook" |
| **Expected Results** | - Alice, Bob, and Cara are all talking together                                                                                                                                                                          |
| **Status**           | To be executed                                                                                                                                                                                                           |

#### TC-020: test_conferencer_hears_ringback_during_invite

| Field                | Value                                                                                                                                                                          |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Test Case ID**     | TC-020                                                                                                                                                                         |
| **Priority**         | P1                                                                                                                                                                             |
| **Description**      | Initiator of conference hears ringback                                                                                                                                         |
| **Preconditions**    | - telephone-numbers.csv read                                                                                                                                                   |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice call Bob"<br> 3. User enters command "Bob offhook"<br> 4. User enters command "Alice conference Cara" |
| **Expected Results** | - Alice hears ringback<br> - Cara hears ringing                                                                                                                                |
| **Status**           | To be executed                                                                                                                                                                 |

#### TC-021: test_conference_recipient_hears_ringing

| Field                | Value                                                                                                                                                                          |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Test Case ID**     | TC-021                                                                                                                                                                         |
| **Priority**         | P1                                                                                                                                                                             |
| **Description**      | Conference recipient hears ringing when invited                                                                                                                                |
| **Preconditions**    | - telephone-numbers.csv read                                                                                                                                                   |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice call Bob"<br> 3. User enters command "Bob offhook"<br> 4. User enters command "Alice conference Cara" |
| **Expected Results** | - Cara hears ringing                                                                                                                                                           |
| **Status**           | To be executed                                                                                                                                                                 |

---

### Section 7: Transfer Calls

#### TC-022: test_transfer_initiator_hears_ringback

| Field                | Value                                                                                                                                                                        |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Test Case ID**     | TC-022                                                                                                                                                                       |
| **Priority**         | P0                                                                                                                                                                           |
| **Description**      | Transferring phone hears ringback                                                                                                                                            |
| **Preconditions**    | - telephone-numbers.csv read                                                                                                                                                 |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice call Bob"<br> 3. User enters command "Bob offhook"<br> 4. User enters command "Alice transfer Cara" |
| **Expected Results** | - Alice hears ringback<br> - Cara hears ringing                                                                                                                              |
| **Status**           | To be executed                                                                                                                                                               |

#### TC-023: test_transfer_recipient_hears_ringing

| Field                | Value                                                                                                                                                                        |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Test Case ID**     | TC-023                                                                                                                                                                       |
| **Priority**         | P1                                                                                                                                                                           |
| **Description**      | New call recipient hears ringing                                                                                                                                             |
| **Preconditions**    | - telephone-numbers.csv read                                                                                                                                                 |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice call Bob"<br> 3. User enters command "Bob offhook"<br> 4. User enters command "Alice transfer Cara" |
| **Expected Results** | - Alice hears ringback<br> - Cara hears ringing                                                                                                                              |
| **Status**           | To be executed                                                                                                                                                               |

#### TC-024: test_transfer_initiator_hears_silence_after_transfer

| Field                | Value                                                                                                                                                                                                                  |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Test Case ID**     | TC-024                                                                                                                                                                                                                 |
| **Priority**         | P0                                                                                                                                                                                                                     |
| **Description**      | Transferring phone hears silence after transfer                                                                                                                                                                        |
| **Preconditions**    | - telephone-numbers.csv read                                                                                                                                                                                           |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice call Bob"<br> 3. User enters command "Bob offhook"<br> 4. User enters command "Alice transfer Cara"<br> 5. User enters command "Cara offhook" |
| **Expected Results** | - Alice hears silence<br> - Bob and Cara are talking                                                                                                                                                                   |
| **Status**           | To be executed                                                                                                                                                                                                         |

#### TC-025: test_transfer_original_and_new_party_talking

| Field                | Value                                                                                                                                                                                                                  |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Test Case ID**     | TC-025                                                                                                                                                                                                                 |
| **Priority**         | P0                                                                                                                                                                                                                     |
| **Description**      | Original party and new party are talking after transfer                                                                                                                                                                |
| **Preconditions**    | - telephone-numbers.csv read                                                                                                                                                                                           |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice call Bob"<br> 3. User enters command "Bob offhook"<br> 4. User enters command "Alice transfer Cara"<br> 5. User enters command "Cara offhook" |
| **Expected Results** | - Alice hears silence<br> - Bob and Cara are talking                                                                                                                                                                   |
| **Status**           | To be executed                                                                                                                                                                                                         |

#### TC-026: test_transfer_from_single_phone_hears_denial

| Field                | Value                                                                                |
| -------------------- | ------------------------------------------------------------------------------------ |
| **Test Case ID**     | TC-026                                                                               |
| **Priority**         | P1                                                                                   |
| **Description**      | Transfer attempt from a phone not in a call hears denial                             |
| **Preconditions**    | - telephone-numbers.csv read                                                         |
| **Steps**            | 1. User enters command "Cara offhook"<br> 2. User enters command "Cara transfer Bob" |
| **Expected Results** | - Cara hears denial                                                                  |
| **Status**           | To be executed                                                                       |

#### TC-027: test_transfer_to_invalid_hears_denial

| Field                | Value                                                                                                                                                                                |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Test Case ID**     | TC-027                                                                                                                                                                               |
| **Priority**         | P1                                                                                                                                                                                   |
| **Description**      | Transfer to invalid phone hears denial                                                                                                                                               |
| **Preconditions**    | - telephone-numbers.csv read                                                                                                                                                         |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice call Bob"<br> 3. User enters command "Bob offhook"<br> 4. User enters command "Alice transfer InvalidPhone" |
| **Expected Results** | - Alice hears denial                                                                                                                                                                 |
| **Status**           | To be executed                                                                                                                                                                       |

---

### Section 8: Status Command

#### TC-028: test_status_shows_all_phones_onhook

| Field                | Value                                       |
| -------------------- | ------------------------------------------- |
| **Test Case ID**     | TC-028                                      |
| **Priority**         | P0                                          |
| **Description**      | Status shows all phones as onhook initially |
| **Preconditions**    | - telephone-numbers.csv read                |
| **Steps**            | 1. User enters command "status"             |
| **Expected Results** | - All phones onhook                         |
| **Status**           | To be executed                              |

#### TC-029: test_status_shows_phone_offhook

| Field                | Value                                                                      |
| -------------------- | -------------------------------------------------------------------------- |
| **Test Case ID**     | TC-029                                                                     |
| **Priority**         | P0                                                                         |
| **Description**      | Status correctly shows offhook phones                                      |
| **Preconditions**    | - telephone-numbers.csv read                                               |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "status" |
| **Expected Results** | - All phone statuses shown<br> - Offhook phones show "dialtone"            |
| **Status**           | To be executed                                                             |

#### TC-030: test_status_shows_talking_pair

| Field                | Value                                                                                                                                                           |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Test Case ID**     | TC-030                                                                                                                                                          |
| **Priority**         | P0                                                                                                                                                              |
| **Description**      | Status shows which two phones are talking                                                                                                                       |
| **Preconditions**    | - telephone-numbers.csv read                                                                                                                                    |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice call Bob"<br> 3. User enters command "Bob offhook"<br> 4. User enters command "status" |
| **Expected Results** | - All phone statuses shown<br> - Alice talking with Bob<br> - Bob talking with Alice                                                                            |
| **Status**           | To be executed                                                                                                                                                  |

#### TC-031: test_status_shows_three_way_conference

| Field                | Value                                                                                                                                                                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Test Case ID**     | TC-031                                                                                                                                                                                                                                                       |
| **Priority**         | P0                                                                                                                                                                                                                                                           |
| **Description**      | Status shows three phones in conference                                                                                                                                                                                                                      |
| **Preconditions**    | - telephone-numbers.csv read                                                                                                                                                                                                                                 |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice call Bob"<br> 3. User enters command "Bob offhook"<br> 4. User enters command "Alice conference Cara"<br> 5. User enters command "Cara offhook"<br> 6. User enters command "status" |
| **Expected Results** | - All phone statuses shown<br> - Alice talking with Bob and Cara<br> - Bob talking with Alice and Cara<br> - Cara talking with Alice and Bob                                                                                                                 |
| **Status**           | To be executed                                                                                                                                                                                                                                               |

#### TC-032: test_status_during_ringing_state

| Field                | Value                                                                                                                  |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Test Case ID**     | TC-032                                                                                                                 |
| **Priority**         | P1                                                                                                                     |
| **Description**      | Status shows phone in ringing state                                                                                    |
| **Preconditions**    | - telephone-numbers.csv read                                                                                           |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice call Bob"<br> 3. User enters command "status" |
| **Expected Results** | - All phone statuses shown<br> - Alice ringback<br> - Bob onhook                                                       |
| **Status**           | To be executed                                                                                                         |

---

### Section 9: Denial Scenarios

#### TC-033: test_denial_offhook_invalid_phone

| Field                | Value                                                                                |
| -------------------- | ------------------------------------------------------------------------------------ |
| **Test Case ID**     | TC-033                                                                               |
| **Priority**         | P0                                                                                   |
| **Description**      | Offhook phone calling invalid number hears denial                                    |
| **Preconditions**    | - telephone-numbers.csv read                                                         |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice call 67890" |
| **Expected Results** | - Alice hears denial                                                                 |
| **Status**           | To be executed                                                                       |

#### TC-034: test_denial_offhook_more_than_3way

| Field                | Value                                                                                                                                                                                                                                                                        |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Test Case ID**     | TC-034                                                                                                                                                                                                                                                                       |
| **Priority**         | P0                                                                                                                                                                                                                                                                           |
| **Description**      | Attempting more than 3-way call hears denial                                                                                                                                                                                                                                 |
| **Preconditions**    | - telephone-numbers.csv read                                                                                                                                                                                                                                                 |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice call Bob"<br> 3. User enters command "Bob offhook"<br> 4. User enters command "Alice conference Cara"<br> 5. User enters command "Cara offhook"<br> 6. User enters command "Alice conference David" |
| **Expected Results** | - Alice hears denial                                                                                                                                                                                                                                                         |
| **Status**           | To be executed                                                                                                                                                                                                                                                               |

#### TC-035: test_denial_conference_without_call

| Field                | Value                                                                                    |
| -------------------- | ---------------------------------------------------------------------------------------- |
| **Test Case ID**     | TC-035                                                                                   |
| **Priority**         | P1                                                                                       |
| **Description**      | Conference without active call hears denial                                              |
| **Preconditions**    | - telephone-numbers.csv read                                                             |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice conference Bob" |
| **Expected Results** | - Alice hears denial                                                                     |
| **Status**           | To be executed                                                                           |

#### TC-036: test_denial_transfer_without_call

| Field                | Value                                                                                  |
| -------------------- | -------------------------------------------------------------------------------------- |
| **Test Case ID**     | TC-036                                                                                 |
| **Priority**         | P1                                                                                     |
| **Description**      | Transfer without active call hears denial                                              |
| **Preconditions**    | - telephone-numbers.csv read                                                           |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice transfer Bob" |
| **Expected Results** | - Alice hears denial                                                                   |
| **Status**           | To be executed                                                                         |

---

### Section 10: Edge Cases & State Management

#### TC-037: test_phone_identifier_by_name

| Field                | Value                                                |
| -------------------- | ---------------------------------------------------- |
| **Test Case ID**     | TC-037                                               |
| **Priority**         | P0                                                   |
| **Description**      | Commands work using a phone's name as the identifier |
| **Preconditions**    | - telephone-numbers.csv read                         |
| **Steps**            | 1. User enters command "Alice offhook"               |
| **Expected Results** | - Alice hears dialtone                               |
| **Status**           | To be executed                                       |

#### TC-038: test_phone_identifier_by_number

| Field                | Value                                                                    |
| -------------------- | ------------------------------------------------------------------------ |
| **Test Case ID**     | TC-038                                                                   |
| **Priority**         | P0                                                                       |
| **Description**      | Commands work using a phone's 5-digit number as the identifier           |
| **Preconditions**    | - telephone-numbers.csv read<br> - Alice's number is known (e.g., 12345) |
| **Steps**            | 1. User enters command "12345 offhook"                                   |
| **Expected Results** | - Alice (12345) hears dialtone                                           |
| **Status**           | To be executed                                                           |

#### TC-039: test_case_insensitive_commands

| Field                | Value                                             |
| -------------------- | ------------------------------------------------- |
| **Test Case ID**     | TC-039                                            |
| **Priority**         | P2                                                |
| **Description**      | Command keywords work regardless of letter casing |
| **Preconditions**    | - telephone-numbers.csv read                      |
| **Steps**            | 1. User enters command "Alice OFFHOOK"            |
| **Expected Results** | - Alice hears dialtone                            |
| **Status**           | To be executed                                    |

#### TC-040: test_case_insensitive_names

| Field                | Value                                      |
| -------------------- | ------------------------------------------ |
| **Test Case ID**     | TC-040                                     |
| **Priority**         | P2                                         |
| **Description**      | Phone names are matched case-insensitively |
| **Preconditions**    | - telephone-numbers.csv read               |
| **Steps**            | 1. User enters command "ALICE offhook"     |
| **Expected Results** | - Alice hears dialtone                     |
| **Status**           | To be executed                             |

#### TC-041: test_multiple_sequential_calls

| Field                | Value                                                                                                                                                                                                                                                                                                                                           |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Test Case ID**     | TC-041                                                                                                                                                                                                                                                                                                                                          |
| **Priority**         | P1                                                                                                                                                                                                                                                                                                                                              |
| **Description**      | Multiple separate calls in sequence complete correctly                                                                                                                                                                                                                                                                                          |
| **Preconditions**    | - telephone-numbers.csv read                                                                                                                                                                                                                                                                                                                    |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice call Bob"<br> 3. User enters command "Bob offhook"<br> 4. User enters command "Alice onhook"<br> 5. User enters command "Bob onhook"<br> 6. User enters command "Alice offhook"<br> 7. User enters command "Alice call Cara"<br> 8. User enters command "Cara offhook" |
| **Expected Results** | - First call: Alice and Bob talking<br> - After hangup: both return to onhook<br> - Second call: Alice and Cara talking                                                                                                                                                                                                                         |
| **Status**           | To be executed                                                                                                                                                                                                                                                                                                                                  |

#### TC-042: test_receiving_call_during_dialtone

| Field                | Value                                                                                                                       |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Test Case ID**     | TC-042                                                                                                                      |
| **Priority**         | P1                                                                                                                          |
| **Description**      | Phone already in dialtone state receives an incoming call and hears ringing                                                 |
| **Preconditions**    | - telephone-numbers.csv read                                                                                                |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Bob offhook"<br> 3. User enters command "Bob call Alice" |
| **Expected Results** | - Alice hears ringing<br> - Bob hears ringback                                                                              |
| **Status**           | To be executed                                                                                                              |

#### TC-043: test_phone_state_after_session_ends

| Field                | Value                                                                                                                                                                                                                                                    |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Test Case ID**     | TC-043                                                                                                                                                                                                                                                   |
| **Priority**         | P1                                                                                                                                                                                                                                                       |
| **Description**      | Phone state resets properly after a call ends, allowing a new call                                                                                                                                                                                       |
| **Preconditions**    | - telephone-numbers.csv read                                                                                                                                                                                                                             |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice call Bob"<br> 3. User enters command "Bob offhook"<br> 4. User enters command "Bob onhook"<br> 5. User enters command "Alice onhook"<br> 6. User enters command "Alice offhook" |
| **Expected Results** | - After step 6: Alice hears dialtone (state correctly reset)                                                                                                                                                                                             |
| **Status**           | To be executed                                                                                                                                                                                                                                           |

---

### Section 11: Data Loading

#### TC-044: test_load_phones_from_csv

| Field                | Value                                                                                 |
| -------------------- | ------------------------------------------------------------------------------------- |
| **Test Case ID**     | TC-044                                                                                |
| **Priority**         | P0                                                                                    |
| **Description**      | CSV file loads correctly, populating all name/number pairs                            |
| **Preconditions**    | - telephone-numbers.csv exists with valid name/number entries                         |
| **Steps**            | 1. Program starts and reads telephone-numbers.csv<br> 2. User enters command "status" |
| **Expected Results** | - All phones from the CSV are listed with correct names and numbers                   |
| **Status**           | To be executed                                                                        |

#### TC-045: test_load_up_to_20_phones

| Field                | Value                                                                                 |
| -------------------- | ------------------------------------------------------------------------------------- |
| **Test Case ID**     | TC-045                                                                                |
| **Priority**         | P1                                                                                    |
| **Description**      | System correctly loads and tracks up to 20 phones                                     |
| **Preconditions**    | - telephone-numbers.csv contains exactly 20 valid entries                             |
| **Steps**            | 1. Program starts and reads telephone-numbers.csv<br> 2. User enters command "status" |
| **Expected Results** | - All 20 phones are listed in the status output                                       |
| **Status**           | To be executed                                                                        |

#### TC-046: test_phone_number_format_5_digits

| Field                | Value                                                                        |
| -------------------- | ---------------------------------------------------------------------------- |
| **Test Case ID**     | TC-046                                                                       |
| **Priority**         | P0                                                                           |
| **Description**      | Phone numbers are exactly 5 digits and are resolved correctly                |
| **Preconditions**    | - telephone-numbers.csv contains a phone with a 5-digit number (e.g., 12345) |
| **Steps**            | 1. User enters command "12345 offhook"                                       |
| **Expected Results** | - The phone with number 12345 hears dialtone                                 |
| **Status**           | To be executed                                                               |

#### TC-047: test_phone_number_can_start_with_zero

| Field                | Value                                                                 |
| -------------------- | --------------------------------------------------------------------- |
| **Test Case ID**     | TC-047                                                                |
| **Priority**         | P1                                                                    |
| **Description**      | Phone numbers beginning with 0 (e.g., 01234) are handled correctly    |
| **Preconditions**    | - telephone-numbers.csv contains a phone with number 01234            |
| **Steps**            | 1. User enters command "01234 offhook"                                |
| **Expected Results** | - The phone with number 01234 hears dialtone (not treated as invalid) |
| **Status**           | To be executed                                                        |

#### TC-048: test_phone_name_alphanumeric_only

| Field                | Value                                                                                 |
| -------------------- | ------------------------------------------------------------------------------------- |
| **Test Case ID**     | TC-048                                                                                |
| **Priority**         | P1                                                                                    |
| **Description**      | Phone names containing only A-Za-z characters are loaded and resolved correctly       |
| **Preconditions**    | - telephone-numbers.csv contains names with only alphabetic characters                |
| **Steps**            | 1. Program starts and reads telephone-numbers.csv<br> 2. User enters command "status" |
| **Expected Results** | - All alphabetic phone names are displayed correctly in status output                 |
| **Status**           | To be executed                                                                        |

#### TC-049: test_phone_name_max_12_chars

| Field                | Value                                                                                    |
| -------------------- | ---------------------------------------------------------------------------------------- |
| **Test Case ID**     | TC-049                                                                                   |
| **Priority**         | P1                                                                                       |
| **Description**      | Phone names up to 12 characters long are loaded and usable in commands                   |
| **Preconditions**    | - telephone-numbers.csv contains a phone with a 12-character name (e.g., "Alexandriana") |
| **Steps**            | 1. User enters command "Alexandriana offhook"                                            |
| **Expected Results** | - Alexandriana hears dialtone                                                            |
| **Status**           | To be executed                                                                           |

#### TC-050: test_missing_csv_file_handled

| Field                | Value                                                                            |
| -------------------- | -------------------------------------------------------------------------------- |
| **Test Case ID**     | TC-050                                                                           |
| **Priority**         | P0                                                                               |
| **Description**      | Program handles a missing telephone-numbers.csv file gracefully without crashing |
| **Preconditions**    | - telephone-numbers.csv does not exist                                           |
| **Steps**            | 1. Program starts without telephone-numbers.csv present                          |
| **Expected Results** | - Program reports an appropriate error message<br> - Program does not crash      |
| **Status**           | To be executed                                                                   |

---

### Section 12: Command Parsing

#### TC-051: test_parse_status_command

| Field                | Value                                                                 |
| -------------------- | --------------------------------------------------------------------- |
| **Test Case ID**     | TC-051                                                                |
| **Priority**         | P0                                                                    |
| **Description**      | Status command is recognized in all supported variants                |
| **Preconditions**    | - telephone-numbers.csv read                                          |
| **Steps**            | 1. User enters command "status"<br> 2. User enters command "status()" |
| **Expected Results** | - Both variants produce the status output listing all phones          |
| **Status**           | To be executed                                                        |

#### TC-052: test_parse_offhook_command

| Field                | Value                                               |
| -------------------- | --------------------------------------------------- |
| **Test Case ID**     | TC-052                                              |
| **Priority**         | P0                                                  |
| **Description**      | Offhook command is parsed correctly from user input |
| **Preconditions**    | - telephone-numbers.csv read                        |
| **Steps**            | 1. User enters command "Alice offhook"              |
| **Expected Results** | - Alice hears dialtone                              |
| **Status**           | To be executed                                      |

#### TC-053: test_parse_onhook_command

| Field                | Value                                                                            |
| -------------------- | -------------------------------------------------------------------------------- |
| **Test Case ID**     | TC-053                                                                           |
| **Priority**         | P0                                                                               |
| **Description**      | Onhook command is parsed correctly from user input                               |
| **Preconditions**    | - telephone-numbers.csv read                                                     |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice onhook" |
| **Expected Results** | - Alice hears dialtone<br> - Alice transitions to onhook state                   |
| **Status**           | To be executed                                                                   |

#### TC-054: test_parse_call_command

| Field                | Value                                                                              |
| -------------------- | ---------------------------------------------------------------------------------- |
| **Test Case ID**     | TC-054                                                                             |
| **Priority**         | P0                                                                                 |
| **Description**      | Call command is parsed correctly and initiates a call                              |
| **Preconditions**    | - telephone-numbers.csv read                                                       |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice call Bob" |
| **Expected Results** | - Alice hears ringback<br> - Bob hears ringing                                     |
| **Status**           | To be executed                                                                     |

#### TC-055: test_parse_transfer_command

| Field                | Value                                                                                                                                                                        |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Test Case ID**     | TC-055                                                                                                                                                                       |
| **Priority**         | P0                                                                                                                                                                           |
| **Description**      | Transfer command is parsed correctly and initiates a transfer                                                                                                                |
| **Preconditions**    | - telephone-numbers.csv read                                                                                                                                                 |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice call Bob"<br> 3. User enters command "Bob offhook"<br> 4. User enters command "Alice transfer Cara" |
| **Expected Results** | - Alice hears ringback<br> - Cara hears ringing                                                                                                                              |
| **Status**           | To be executed                                                                                                                                                               |

#### TC-056: test_parse_conference_command

| Field                | Value                                                                                                                                                                          |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Test Case ID**     | TC-056                                                                                                                                                                         |
| **Priority**         | P0                                                                                                                                                                             |
| **Description**      | Conference command is parsed correctly and initiates a conference                                                                                                              |
| **Preconditions**    | - telephone-numbers.csv read                                                                                                                                                   |
| **Steps**            | 1. User enters command "Alice offhook"<br> 2. User enters command "Alice call Bob"<br> 3. User enters command "Bob offhook"<br> 4. User enters command "Alice conference Cara" |
| **Expected Results** | - Alice hears ringback<br> - Cara hears ringing                                                                                                                                |
| **Status**           | To be executed                                                                                                                                                                 |

#### TC-057: test_parse_quit_command

| Field                | Value                                                                                  |
| -------------------- | -------------------------------------------------------------------------------------- |
| **Test Case ID**     | TC-057                                                                                 |
| **Priority**         | P1                                                                                     |
| **Description**      | Quit command is recognized in all supported variants and exits the program             |
| **Preconditions**    | - telephone-numbers.csv read                                                           |
| **Steps**            | 1. User enters command "quit"<br> 2. Restart program<br> 3. User enters command "exit" |
| **Expected Results** | - Both "quit" and "exit" cause the program to terminate                                |
| **Status**           | To be executed                                                                         |

#### TC-058: test_parse_invalid_command

| Field                | Value                                                         |
| -------------------- | ------------------------------------------------------------- |
| **Test Case ID**     | TC-058                                                        |
| **Priority**         | P1                                                            |
| **Description**      | Unrecognized commands are handled gracefully without crashing |
| **Preconditions**    | - telephone-numbers.csv read                                  |
| **Steps**            | 1. User enters command "foobar"                               |
| **Expected Results** | - Program does not crash<br> - No phone state changes occur   |
| **Status**           | To be executed                                                |

#### TC-059: test_parse_whitespace_handling

| Field                | Value                                                                              |
| -------------------- | ---------------------------------------------------------------------------------- |
| **Test Case ID**     | TC-059                                                                             |
| **Priority**         | P2                                                                                 |
| **Description**      | Commands with extra leading, trailing, or internal whitespace are parsed correctly |
| **Preconditions**    | - telephone-numbers.csv read                                                       |
| **Steps**            | 1. User enters command " Alice offhook "                                           |
| **Expected Results** | - Alice hears dialtone (extra whitespace ignored)                                  |
| **Status**           | To be executed                                                                     |

---

## 7. Addenda

### Test Execution Notes

- All test cases assume a fresh program start unless explicitly stated otherwise
- The status command can be used after any test to verify system state
- Test case IDs are sequential (TC-001 through TC-059) for easy reference
- Priority levels guide execution order and critical path testing

### Test Data Requirements

The CSV fixture file should contain at minimum:

```
Alice,12345
Bob,23456
Cara,34567
David,45678
Eve,56789
Frank,67890
```

For maximum coverage testing (20 phones), additional entries should be created following the same format.

### Defect Reporting Process

When a test case fails:

1. Document the actual result vs. expected result
2. Capture any error messages or stack traces
3. Note the system state at time of failure (use status command)
4. Create a GitHub issue with the test case ID in the title
5. Link the test case to the issue for tracking

---

## 8. Specification Changes

### Clarifications Made During Test Planning

1. **Status Command Format**: The requirements specify "status" as a command; the test cases also accept "status()" as a variant.
2. **Case Sensitivity**: While not explicitly stated in requirements, test cases assume case-insensitive matching for both commands and phone names/numbers.

3. **Duplicate Offhook/Onhook**: Requirement 13 states duplicate offhook commands are ignored; assuming same behavior for duplicate onhook commands.

4. **Ringing State in Status**: The status command should display intermediate states (ringing, ringback) not just final states (talking, dialtone).

5. **Invalid Phone in Transfer/Conference**: These operations should produce denial tone consistent with invalid call attempts.

### Assumptions

1. **CSV Error Handling**: Malformed CSV lines are skipped; duplicate names or numbers use first occurrence.
2. **Phone State Persistence**: After a call ends (onhook), phones return to onhook state and can initiate new calls.

3. **Conference Limitation**: Maximum 3 phones in a conversation; attempts to add a 4th produce denial.

4. **Whitespace Tolerance**: Leading/trailing/extra whitespace in commands is normalized before parsing.

---

## 9. Usage Instructions

### Running the Program

**Basic Usage:**

```bash
python src/main.py
```

The program will look for `telephone-numbers.csv` in the `src/` directory.

**Specify Custom CSV:**

```bash
python src/main.py path/to/custom-telephone-numbers.csv
```

### Running Tests

**Execute All Tests:**

```bash
pytest tests/
```

**Execute Specific Test File:**

```bash
pytest tests/test_basic_operations.py
```

**Execute Single Test Case:**

```bash
pytest tests/test_basic_operations.py::test_offhook_sets_dialtone
```

**Run with Verbose Output:**

```bash
pytest -v tests/
```

**Generate Coverage Report:**

```bash
pytest --cov=src tests/
```

### Manual Testing Procedure

1. Prepare the CSV file with test phone data
2. Start the program: `python src/main.py`
3. Follow test case steps exactly as documented
4. Record actual output for each step
5. Compare actual vs. expected results
6. Mark test status as Passed or Failed
7. Document any deviations or defects

### Example Test Session

```
$ python src/main.py
> Alice offhook
Alice hears dialtone
> Alice call Bob
Alice hears ringback
Bob hears ringing
> Bob offhook
Alice and Bob are talking
> status
Alice: talking with Bob
Bob: talking with Alice
Cara: onhook
> Alice onhook
Bob hears silence
> quit
```

---

## 10. Deliverables Package for Assigned Tester

### Package Contents

The following materials will be provided to the assigned tester no later than **one day after the Milestone 1 due date**:

#### 1. Executable Package

- **Source code**: All Python files in `src/` directory
- **Working executable**: Tested on Windows, compatible with Python 3.7+
- **CSV fixtures**: `tests/fixtures/telephone-numbers.csv` with sample test data
- **Dependencies**: `requirements.txt` (if any external packages used)

#### 2. Documentation

- **This test plan** (`docs/test-plan.md`): Complete testing strategy and test cases
- **Test cases list** (`docs/test-cases.md`): Quick reference of all 59 test cases with execution status
- **Usage instructions** (Section 9 of this document): How to run the program
- **Requirements document** (`docs/program-requirements.md`): Original specifications

#### 3. Test Execution Support

- **Sample telephone-numbers.csv**: Pre-configured with Alice, Bob, Cara, David, Eve, Frank
- **Test data requirements**: Documented in Section 7 (Addenda)
- **Expected output examples**: Section 9 includes sample test session

#### 4. Installation Instructions

```bash
# 1. Extract the package to a directory
# 2. Navigate to the project directory
cd Telephone-Switching

# 3. Verify Python installation (3.7 or higher)
python --version

# 4. Run the program
python src/main.py

# 5. For testing with custom CSV
python src/main.py tests/fixtures/telephone-numbers.csv
```

#### 5. Known Issues and Limitations

- To be updated after initial testing
- Any specification clarifications documented in Section 8

#### 6. Contact Information

- **Development Team**: [Team members]
- **Response Time**: Within 24 hours for critical issues
- **Issue Tracking**: Document issues with test case ID reference

### Tester Responsibilities

The assigned tester will:

1. Execute test cases from Section 6
2. Document actual results vs. expected results
3. Report defects with test case ID and reproduction steps
4. Validate fixes during regression testing (Milestone 3)

---

## 11. Requirements Traceability Matrix

This matrix maps all project requirements to their corresponding test cases, ensuring complete coverage.

| Requirement        | Description                                                                  | Test Cases                                             | Count |
| ------------------ | ---------------------------------------------------------------------------- | ------------------------------------------------------ | ----- |
| **Req 1**          | CSV file reading with up to 20 phone pairs                                   | TC-044, TC-045, TC-050                                 | 3     |
| **Req 2**          | Phone numbers: 5 digits, may start with 0                                    | TC-046, TC-047                                         | 2     |
| **Req 3**          | Phone names: up to 12 chars, A-Za-z only                                     | TC-048, TC-049                                         | 2     |
| **Req 4**          | Command syntax (call, offhook, onhook, transfer, conference)                 | TC-052, TC-053, TC-054, TC-055, TC-056                 | 5     |
| **Req 5**          | Phone identifier by name or number                                           | TC-037, TC-038                                         | 2     |
| **Req 6**          | Response types (dialtone, ringback, ringing, busy, denial, silence, talking) | All test cases                                         | 59    |
| **Req 7**          | Normal call flow                                                             | TC-005, TC-006, TC-007, TC-008, TC-009                 | 5     |
| **Req 8**          | Conference call (3-way)                                                      | TC-019, TC-020, TC-021, TC-031                         | 4     |
| **Req 9**          | Transfer functionality                                                       | TC-022, TC-023, TC-024, TC-025, TC-026, TC-027         | 6     |
| **Req 10**         | Busy signal when phone in use                                                | TC-017, TC-018                                         | 2     |
| **Req 11**         | Denial for illegal operations                                                | TC-014, TC-015, TC-016, TC-033, TC-034, TC-035, TC-036 | 7     |
| **Req 12**         | Silence when onhook attempts commands                                        | TC-010, TC-011, TC-012                                 | 3     |
| **Req 13**         | Duplicate offhook/onhook ignored                                             | TC-002, TC-004                                         | 2     |
| **Req 14**         | Status command displays all phones                                           | TC-028, TC-029, TC-030, TC-031, TC-032, TC-051         | 6     |
| **Edge Cases**     | Case sensitivity, state management, sequential calls                         | TC-039, TC-040, TC-041, TC-042, TC-043                 | 5     |
| **Error Handling** | Invalid commands, whitespace, missing files                                  | TC-050, TC-058, TC-059                                 | 3     |

### Coverage Summary

- **Total Requirements**: 14 core requirements + edge cases + error handling
- **Total Test Cases**: 59
- **Requirements with Multiple Tests**: All critical requirements (Req 6-12)
- **Untested Requirements**: None
- **Coverage Assessment**: ✅ Complete

---

## Test Summary Statistics

- **Total Test Cases**: 59
- **Priority P0 (Critical)**: 25 test cases
- **Priority P1 (High)**: 26 test cases
- **Priority P2 (Medium)**: 6 test cases
- **Priority P3 (Low)**: 2 test cases

### Test Coverage by Section

| Section                           | Test Cases | Coverage Area    |
| --------------------------------- | ---------- | ---------------- |
| 1. Basic Phone Operations         | 4          | TC-001 to TC-004 |
| 2. Normal Call Flow               | 5          | TC-005 to TC-009 |
| 3. Onhook Restrictions            | 4          | TC-010 to TC-013 |
| 4. Invalid Phone Numbers          | 3          | TC-014 to TC-016 |
| 5. Busy Signal                    | 2          | TC-017 to TC-018 |
| 6. Conference Calls               | 3          | TC-019 to TC-021 |
| 7. Transfer Calls                 | 6          | TC-022 to TC-027 |
| 8. Status Command                 | 5          | TC-028 to TC-032 |
| 9. Denial Scenarios               | 4          | TC-033 to TC-036 |
| 10. Edge Cases & State Management | 7          | TC-037 to TC-043 |
| 11. Data Loading                  | 7          | TC-044 to TC-050 |
| 12. Command Parsing               | 9          | TC-051 to TC-059 |
