# Prompt: Create Threat Model

**Purpose**: Generate security threat model for a requirement
**Input**: Requirement document path, scope (per-requirement | aggregate | grouped)
**Output**: Threat model diagram in `docs/diagrams/`
**References**:
- `.github/instructions/threat-modeling.instructions.md`
- Relevant CodeGuard instruction files

## Prompt

```
Create a security threat model for the requirement at {requirement_path}.

Scope: {per-requirement | high-level-aggregate | grouped-by-feature}

Instructions:
1. Read the requirement document
2. Follow threat modeling process in .github/instructions/threat-modeling.instructions.md
3. Apply STRIDE framework:
   - Spoofing
   - Tampering
   - Repudiation
   - Information Disclosure
   - Denial of Service
   - Elevation of Privilege
4. Create Mermaid diagrams showing:
   - Data flow diagram
   - Trust boundaries
   - Threat actors and attack vectors
5. For each identified threat:
   - Classify by STRIDE category
   - Assess impact and likelihood
   - Propose mitigation
   - Reference relevant CodeGuard instruction file
6. Save to docs/diagrams/threat-model-{name}.md
7. Update docs/SPEC-CROSS-REFERENCE.md
8. Log execution details to docs/output-logs/{timestamp}-threat-modeling.md

Note: When updating existing threat models, create a new version file (threat-model-{name}-v2.md) rather than editing the original.
```

## Example Usage

### With Claude Code

```
Use the create-threat-model prompt for docs/requirements/req-auth.md with scope per-requirement
```

### With GitHub Copilot

```
@workspace Create a threat model for @docs/requirements/req-auth.md following @.github/instructions/threat-modeling.instructions.md with STRIDE framework and Mermaid diagrams.
```

## Expected Output

- Threat model: `docs/diagrams/threat-model-{name}.md`
- Updated: `docs/SPEC-CROSS-REFERENCE.md`
- Log: `docs/output-logs/{timestamp}-threat-modeling.md`

**TODO**: Add complete threat model example with STRIDE analysis
