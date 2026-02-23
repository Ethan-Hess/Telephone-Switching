# Telephone Switching Simulation - Test Cases

This document outlines all test cases that could be implemented to verify the telephone switching system behaves according to the assignment requirements.

## 1. Basic Phone Operations

### Offhook/Onhook

- [ ] `test_offhook_sets_dialtone` - Phone goes offhook and hears dialtone
- [ ] `test_offhook_when_already_offhook` - Phone tries to go offhook again; should be ignored
- [ ] `test_onhook_returns_to_onhook` - Phone hangs up and returns to onhook state
- [ ] `test_onhook_when_already_onhook` - Phone tries to go onhook when already onhook; should be ignored

## 2. Normal Call Flow (Requirement 7)

- [ ] `test_call_initiator_hears_ringback` - Calling phone hears ringback after dialing
- [ ] `test_call_recipient_hears_ringing` - Called phone hears ringing when offhook
- [ ] `test_call_established_both_talking` - Both phones talk after recipient picks up
- [ ] `test_call_initiator_hears_silence_on_hangup` - Initiator hears silence when recipient hangs up
- [ ] `test_call_ends_when_initiator_hangs_up` - Call disconnects when initiator goes onhook

## 3. Onhook Restrictions (Requirement 12)

- [ ] `test_onhook_call_hears_silence` - Phone on hook tries to call; hears silence
- [ ] `test_onhook_transfer_hears_silence` - Phone on hook tries to transfer; hears silence
- [ ] `test_onhook_conference_hears_silence` - Phone on hook tries to conference; hears silence
- [ ] `test_onhook_offhook_is_allowed` - Phone on hook can go offhook without silence

## 4. Invalid Phone Numbers (Requirement 11)

- [ ] `test_call_invalid_phone_hears_denial` - Calling nonexistent phone hears denial
- [ ] `test_transfer_invalid_phone_hears_denial` - Transfer to nonexistent phone hears denial
- [ ] `test_conference_invalid_phone_hears_denial` - Conference with nonexistent phone hears denial

## 5. Busy Signal (Requirement 10)

- [ ] `test_third_phone_hears_busy` - Third phone calling while phone1 and phone2 are talking hears busy
- [ ] `test_busy_works_when_phone_offhook` - Busy signal only works when originating phone is offhook

## 6. Conference Calls (Requirement 8)

- [ ] `test_conference_adds_third_party` - Three phones successfully conferencing together
- [ ] `test_conferencer_hears_ringback_during_invite` - Initiator of conference hears ringback
- [ ] `test_conference_recipient_hears_ringing` - New conference member hears ringing
- [ ] `test_all_three_talking_after_conference` - All three phones talking after conference established
- [ ] `test_conference_with_initiator_hanging_up` - When initiator hangs up, other two continue talking
- [ ] `test_conference_cannot_exceed_3_way` - Attempting 4-way conference hears denial
- [ ] `test_conference_from_single_phone_hears_denial` - Conference without active call hears denial

## 7. Transfer Calls (Requirement 9)

- [ ] `test_transfer_initiator_hears_ringback` - Transferring phone hears ringback
- [ ] `test_transfer_recipient_hears_ringing` - New call recipient hears ringing
- [ ] `test_transfer_initiator_hears_silence_after_transfer` - Transferring phone hears silence after transfer
- [ ] `test_transfer_original_and_new_party_talking` - Original party and new party connected after transfer
- [ ] `test_transfer_from_single_phone_hears_denial` - Transfer without active call hears denial
- [ ] `test_transfer_to_invalid_hears_denial` - Transfer to invalid phone hears denial

## 8. Status Command

- [ ] `test_status_shows_all_phones_onhook` - Status shows all phones as onhook initially
- [ ] `test_status_shows_phone_offhook` - Status correctly shows offhook phones
- [ ] `test_status_shows_talking_pair` - Status shows which two phones are talking
- [ ] `test_status_shows_three_way_conference` - Status shows three phones in conference
- [ ] `test_status_during_ringing_state` - Status shows phone in ringing state

## 9. Denial Scenarios (Requirement 11)

- [ ] `test_denial_offhook_invalid_phone` - Offhook phone calling invalid number hears denial
- [ ] `test_denial_offhook_more_than_3way` - Attempting more than 3-way call hears denial
- [ ] `test_denial_conference_without_call` - Conference without active call hears denial
- [ ] `test_denial_transfer_without_call` - Transfer without active call hears denial

## 10. Edge Cases & State Management

- [ ] `test_phone_identifier_by_name` - Commands work with phone names
- [ ] `test_phone_identifier_by_number` - Commands work with 5-digit phone numbers
- [ ] `test_case_insensitive_commands` - Commands work in mixed case
- [ ] `test_case_insensitive_names` - Phone names work case-insensitively
- [ ] `test_multiple_sequential_calls` - Multiple separate calls in sequence work correctly
- [ ] `test_receiving_call_during_dialtone` - Phone in dialtone receives call (hears ringing)
- [ ] `test_phone_state_after_session_ends` - Phone state resets properly after call ends

## 11. Data Loading

- [ ] `test_load_phones_from_csv` - CSV file loads correctly with name/number pairs
- [ ] `test_load_up_to_20_phones` - System handles up to 20 phones
- [ ] `test_phone_number_format_5_digits` - Phone numbers are exactly 5 digits
- [ ] `test_phone_number_can_start_with_zero` - Phone numbers like 01234 work correctly
- [ ] `test_phone_name_alphanumeric_only` - Phone names contain only A-Za-z characters
- [ ] `test_phone_name_max_12_chars` - Phone names don't exceed 12 characters
- [ ] `test_missing_csv_file_handled` - Program handles missing CSV file gracefully

## 12. Command Parsing

- [ ] `test_parse_status_command` - Status command recognizes variants (status, status())
- [ ] `test_parse_offhook_command` - Offhook command parsed correctly
- [ ] `test_parse_onhook_command` - Onhook command parsed correctly
- [ ] `test_parse_call_command` - Call command parsed correctly
- [ ] `test_parse_transfer_command` - Transfer command parsed correctly
- [ ] `test_parse_conference_command` - Conference command parsed correctly
- [ ] `test_parse_quit_command` - Quit command recognized (quit, exit variants)
- [ ] `test_parse_invalid_command` - Invalid commands handled gracefully
- [ ] `test_parse_whitespace_handling` - Extra whitespace handled correctly
