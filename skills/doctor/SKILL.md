---
name: doctor
description: Check Docker CLI, daemon, Compose, act and .NET availability on an authorized local host without installing or starting software. USE FOR read-only Docker/host readiness checks before setup. DO NOT USE FOR installation, daemon startup, container mutation, pruning, or PMCR-O host execution; use host or an explicitly authorized runtime capability.
---
# Docker Doctor

## Purpose
Establish observed host readiness.

## When to Use
Use /docker:doctor before Docker or PMCR-O host setup.

## When Not to Use
Do not install, start, prune, mount arbitrary directories or expose credentials.

## Inputs
Explicit execution host; run the script on that machine.

## Deliverables
JSON readiness receipt distinguishing CLI, daemon and related tools.

## Workflow
1. Run scripts/doctor.py on the selected host.
2. Report missing or unreachable dependencies; do not assume the cloud sandbox is the user's computer.
3. Route a separate setup action after authorization.

## Validation
Check exit status and each reported prerequisite.

## Pitfalls
Docker socket access is privileged. Never grant broad socket access to agent workloads.

## Resources
- references/host.md
- assets/readiness.json
- scripts/doctor.py
