---
tags: [smoke, bug]
max_turns: 20
allowed_tools: [Read, Glob, Grep, Skill]
---

Can you check whether bug BUG-71 is actually confirmed and tell me where the investigation should go next? I can't run the mobile build locally.

Bug write-up b1: uploading a photo from Android build 7.1 sometimes returns HTTP 500 instead of creating an attachment.

- I tried it in a desktop browser on a different build and it didn't fail. We can't get the Android build here.
- We have an independently captured server trace: Android build 7.1, the upload endpoint, request ID R-71, and a matching 500 response at the reported time. It has no private payload and no stack trace.
- No code has been changed, and we have no evidence of the cause yet.
