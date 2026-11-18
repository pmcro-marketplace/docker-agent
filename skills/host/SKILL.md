---
name: host
description: Prepare a local Ollama container and MAF-native ProjectName host integration plan. USE FOR bounded local-model/bootstrap planning after doctor passes. DO NOT USE FOR deployment, live agent execution, destructive Docker mutation, or claiming full MAF/AGT integration without target-host proof.
---
# Docker Host

## Purpose
Provide a bounded local-model bootstrap compatible with the reference Aspire topology.

## When to Use
Use /docker:host after doctor and before deploying a local agent host.

## When Not to Use
Do not start containers, pull images or models, overwrite a compose project, or claim full MAF/AGT integration.

## Inputs
Explicit host/workspace; approved Ollama image version and model.

## Deliverables
Validated Compose bootstrap asset and host integration plan.

## Workflow
1. Read references/topology.md.
2. Run python3 scripts/validate.py to validate the Compose asset.
3. Review image, resource needs and target machine. Provide OLLAMA_IMAGE as an explicitly chosen tag or digest.
4. After separate approval, use docker compose -f assets/compose.yaml config, then up -d. Pull the chosen model only after review.
5. Reuse the reference .NET Aspire/Microsoft Agent Framework host for actual PMCR-O phase orchestration.

## Validation
Require schema/structure checks, loopback exposure, persistent model volume, and no host socket mount. Live Docker and model inference require target-host verification.

## Pitfalls
This asset supplies Ollama only, not the full MAF host. Do not run Aspire-managed Ollama and this Compose service on the same port simultaneously.

## Resources
- references/topology.md
- assets/compose.yaml
- scripts/validate.py
