# Scenario 16

## User request and selected stage

The user explicitly invokes `$handoff` for ticket PAY-7: "Save a handoff checkpoint
now so I can resume verification in a new conversation." The candidate has no writable
repository or destination in this read-only scenario. Return the two documents in the
response and state that they were not saved.

## Available task state

- Target: virtual `checkout` repository, branch `main`, clean at full commit
  `bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb`. PROJECT CONTEXT pc2 is available and
  maps the payment gateway integration and its test command. No dirty/untracked inputs.
- Original request: Implement PAY-7 payment confirmation. The user authorized code
  changes and later requested this checkpoint. The changed source was committed at the
  baseline above; no new changes are requested now.
- Complete conversation-only governing contract body:

  ```text
  # TASK CONTRACT
  - Task ID: PAY-7
  - Revision: r1
  - Status: READY
  ## Acceptance Criteria
  AC1 original: "A successful gateway response marks the payment confirmed."
  Interpretation: A matching success response updates payment state to confirmed.
  Verification: Run the real gateway success-path integration check.
  ```

- Implementation report i1 says `payments/confirm.py` handles matching success
  responses. CODE REVIEW REPORT cr1 APPROVED the exact clean commit above in a fresh
  reviewer session. No review findings or open blockers; `review_cycles=0`.
- Verification report v1 is BLOCKED because the real gateway test environment is
  unavailable. It did not run the required integration check; `failed_cycles=0`.
  The environment owner must restore gateway access before verification resumes.
- No execution record for the real gateway integration check exists. Do not infer PASS
  from the implementation or approval. No prior handoff folder exists.

## Requested response

Produce complete `HANDOFF.md` and `CHANGELOG.md` content for one
`PAY-7-payment-confirmation` folder, with CHECKPOINT status, original AC wording,
current DoD gap, governing contract body, next owner and resume condition. State the
persistence gap. Do not claim that files were written or verification passed.
