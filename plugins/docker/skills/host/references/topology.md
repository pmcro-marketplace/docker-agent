# PMCR-O reference topology

Source: https://github.com/ShawnDelaineBellazanLoop/PMCR-O-Marketplace/blob/main/src/ProjectName.AppHost/AppHost.cs (main read-only reference).

The source has one MAF-native OrchestratorService with in-process Planner, Maker, Checker and Reflector workflow, an Ollama persistent GPU container (qwen3:8b, 16384 context, flash attention disabled), MCP filesystem/terminal/playwright references, OrchestratorApi and DevUI/AG-UI frontend.

The Compose asset is an isolated Ollama bootstrap; use it only if Aspire is not managing the same endpoint. The production host should preserve the .NET ProjectName convention, reuse its existing MAF code and portable skill directories, stage only selected skill inputs, and use structured validated intents instead of requiring small models to load the entire catalog.

Audit integration: preserve PMCR-O append-only trails in .pmcro/trails, capture agent/skill addresses, prompt references, input/output hashes, model, timestamps, errors, permissions and independent validation. AGT integration requires the exact AGT protocol/implementation and adapter contract; do not claim integration from local JSONL receipts. Keep sensitive runtime state private.
