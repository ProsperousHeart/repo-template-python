# Setup Conversation: Documentation-Driven Development Template

**Date**: 2025-11-09
**Participants**: User (Template Creator), Claude Code (AI Assistant)
**Context**: Setting up a comprehensive documentation-driven development workflow for a Python template repository

## Summary

This conversation established a complete documentation-driven development framework for a Python template repository. The framework includes a multi-stage workflow from requirements through specifications to code generation, with integrated security (CodeGuard), threat modeling, architecture diagrams, and automated documentation updates. The system supports both Claude Code and GitHub Copilot.

## Initial Requirements

The user wanted to create a documentation system where:
1. `docs/` folder is the central hub for all documentation
2. `docs/requirements/` contains requirement markdown files
3. `docs/specifications/` contains technical specifications generated from requirements
4. Instructions and prompts are organized for both human and AI use
5. Multi-stage workflow with human approval gates:
   - Requirements → Specifications → Code Generation → Quality Review → Approval
6. Code is automatically reviewed and follows Test-Driven Development (TDD)
7. Comprehensive tracking via cross-reference tables

## Evolution of Requirements

### Phase 1: Basic Structure
User initially requested:
- `docs/` as central hub
- Separation between instructions and prompts
- Output files tracking workflow execution
- Example workflow in README

### Phase 2: Security Integration
User added requirements for:
- Integration with existing CodeGuard security files in `.github/instructions/`
- Automated security checks during code generation
- Threat modeling guidelines
- Architecture diagram guidelines
- Automated documentation updates

### Phase 3: Template Repository Context
User clarified this is a **template repository** for other developers, which changed the structure:
- `.github/instructions/` → Universal, reusable guidelines (part of template)
- `docs/` → Project-specific content (users fill this in)
- CodeGuard files stay in `.github/instructions/` (universal)
- Template needs clear distinction between what's template vs. what's project-specific

### Phase 4: Detailed Refinements

**CodeGuard Integration**:
- Automatically reference ALL relevant CodeGuard files
- Weight relevance based on spec content
- Log which rules were applied

**Threat Modeling & Architecture**:
- Both done at requirements stage
- Options for per-requirement, aggregate, or grouped by feature
- Markdown format with Mermaid diagrams
- Optional separate `.mmd` files
- **Versioning**: Create duplicate files for updates (don't edit originals in-place)

**Automated Documentation Updates**:
- Triggers: Changes to requirements, specifications, or code
- Updates: Master index, cross-reference table, READMEs, docstrings
- Three automation options: GitHub Actions, pre-commit hooks, manual scripts

**Error Tracking**:
- Error resolution KB auto-updated when code self-fixes
- Starter KB includes common issues (requests timeout, permission errors, etc.)

**UV Environment Management**:
- Check for existing environment
- Create if not found
- Use `uv add` (NOT `uv pip install`)
- Shared instruction file referenced by multiple workflows

**TDD Integration**:
- RED-GREEN-REFACTOR cycle
- Tests written BEFORE and alongside code
- Test directory mirrors `src/` structure
- Test naming: `test_{module_name}.py`

**Output Logging**:
- Format specification in `docs/rules/output-format.md`
- Logs saved to `docs/output-logs/` or `.github/prompts/output-logs/`
- Include: phases completed, CodeGuard rules applied, guidelines followed, issues & resolutions

### Phase 5: File Management Strategy

**Archive Strategy**:
- Move existing files to `.archive/` folders (not rename)
- Keep CodeGuard files as-is
- Keep `docs/templates/` as-is

**Diagrams Folder**:
- Flat structure: `docs/diagrams/`
- Filename prefixes: `architecture-`, `threat-model-`, `sequence-`, `erd-`, etc.
- Easier to maintain than nested subfolders

**Cross-Reference Table**:
- Own file: `docs/SPEC-CROSS-REFERENCE.md`
- Table format with links
- Tracks: Requirements → Specifications → Source → Tests → Diagrams
- Bidirectional linking (files link back to table)

**Master Index**:
- `docs/INDEX.md`
- Linked from other READMEs
- Always up-to-date

**Conversation History**:
- This conversation saved to `docs/history/2025-11-09-setup-conversation.md`
- Captures decision-making process

## Final Structure

```
repo-template-python/
├── .github/
│   ├── workflows/              # CI/CD workflows (template)
│   ├── instructions/           # Universal guidelines (template)
│   │   ├── README.md
│   │   ├── codeguard-*.instructions.md  # Security rules (existing)
│   │   ├── master-workflow.md           # Complete workflow
│   │   ├── uv-environment-setup.instructions.md
│   │   ├── tdd-workflow.instructions.md
│   │   ├── threat-modeling.instructions.md
│   │   ├── architecture-diagrams.instructions.md
│   │   ├── claude-usage.instructions.md
│   │   ├── copilot-usage.instructions.md
│   │   ├── automation-setup.instructions.md
│   │   ├── security-review.instructions.md
│   │   ├── post-test-review.instructions.md
│   │   ├── testcase.instructions.md
│   │   └── .archive/           # Archived original files
│   └── prompts/                # Reusable AI prompts (template)
│       ├── README.md
│       ├── generate-spec-from-requirement.prompt.md
│       ├── generate-code-from-spec.prompt.md
│       ├── create-threat-model.prompt.md
│       ├── create-architecture-diagram.prompt.md
│       └── output-logs/
│           └── README.md (gitignored logs)
├── docs/
│   ├── INDEX.md                # Master index
│   ├── SPEC-CROSS-REFERENCE.md # Implementation tracking
│   ├── README.md               # Documentation hub overview
│   ├── requirements/           # User's requirements (project-specific)
│   ├── specifications/         # User's specs (project-specific)
│   ├── diagrams/               # Architecture, threat models, etc.
│   │   └── README.md
│   ├── templates/              # Doc templates (already existed)
│   │   ├── requirements-template.md
│   │   └── spec-template.md
│   ├── rules/                  # Project standards (customizable)
│   │   ├── README.md
│   │   ├── docstring-standards.md
│   │   ├── output-format.md
│   │   └── error-resolution-kb.md
│   ├── history/                # Decision logs
│   │   ├── README.md
│   │   └── 2025-11-09-setup-conversation.md (this file)
│   ├── output-logs/            # Doc workflow logs
│   │   └── README.md
│   └── .archive/               # Archived original docs files
├── src/                        # User's source code
└── test/                       # User's tests (mirrors src/)
```

## Key Decisions Made

### 1. Template vs. Project-Specific Split
**Decision**: Keep universal guidelines in `.github/instructions/`, project-specific docs in `docs/`
**Reasoning**: Template repository needs to provide reusable workflows while allowing project customization

### 2. Diagram Versioning Strategy
**Decision**: Create duplicate files for updates, don't edit originals in-place
**Reasoning**: Preserves history, better IDE compatibility, easier rollback

### 3. Diagram Folder Structure
**Decision**: Flat structure with filename prefixes vs. nested subfolders
**Reasoning**: Simpler to maintain, less prone to user error, easier navigation

### 4. CodeGuard Integration
**Decision**: Reference (not copy) CodeGuard files from `.github/instructions/`, automatically apply during code generation
**Reasoning**: CodeGuard files are universal template content, should stay in template location

### 5. UV Package Management
**Decision**: Always use `uv add`, never `uv pip install`
**Reasoning**: Maintains lock file integrity, updates pyproject.toml automatically

### 6. TDD Workflow
**Decision**: Tests written BEFORE and alongside code (RED-GREEN-REFACTOR), not after
**Reasoning**: True TDD leads to better design, this template should enforce best practices

### 7. Automation Options
**Decision**: Provide examples for GitHub Actions, pre-commit hooks, AND manual scripts
**Reasoning**: Different team sizes and preferences need different approaches

### 8. Error KB Starter Content
**Decision**: Include common HTTP/network errors (timeout, permission denied, connection errors)
**Reasoning**: These are frequently encountered and often not properly handled with try-catch blocks

### 9. Tool Support
**Decision**: Support both Claude Code and GitHub Copilot
**Reasoning**: Teams use different tools, template should work with both

### 10. Output Logging
**Decision**: Detailed logs following standardized format, gitignored by default
**Reasoning**: Traceability and audit trail without cluttering repository

## Workflow Overview

### Stage 1: Environment Setup
1. Check/create UV virtual environment
2. Use `uv add` for packages
3. Reference: `uv-environment-setup.instructions.md`

### Stage 2: Requirements
1. Create requirement using template
2. Define problem, acceptance criteria, dependencies
3. Output: `docs/requirements/req-{name}.md`

### Stage 3: Threat Models & Diagrams
1. Generate threat model (STRIDE framework)
2. Generate architecture diagrams (Mermaid)
3. Reference relevant CodeGuard files
4. Output: `docs/diagrams/threat-model-{name}.md`, `docs/diagrams/architecture-{name}.md`
5. Human review → Approval

### Stage 4: Specifications
1. Generate spec from requirement
2. Include technical approach, security considerations
3. Reference CodeGuard files
4. Output: `docs/specifications/spec_{name}.md`
5. Auto-update INDEX.md and SPEC-CROSS-REFERENCE.md
6. Human review → Approval

### Stage 5: Code Generation (TDD)
1. **RED**: Write failing tests first
2. **GREEN**: Write minimal code to pass
3. **REFACTOR**: Improve code while keeping tests green
4. Apply relevant CodeGuard rules automatically
5. Follow docstring standards
6. Mirror directory structure in tests
7. Log execution details
8. Update error KB if self-fixes occur
9. Output: `src/{module}.py`, `test/test_{module}.py`
10. Automated security review
11. Human review → Approval

### Stage 6: Quality Review
1. Run ruff checks
2. Run pytest
3. Security review (CodeGuard compliance)
4. Post-test review
5. Update cross-reference table
6. Human approval

## Action Items Completed

- [x] Created folder structure
  - `docs/rules/`, `docs/diagrams/`, `docs/history/`
  - `.github/prompts/`, `.github/prompts/output-logs/`
  - `docs/output-logs/`

- [x] Moved existing files to `.archive/` folders
  - `.github/instructions/.archive/`
  - `.github/.archive/`
  - `docs/.archive/`

- [x] Created master documentation files
  - `docs/INDEX.md` - Master index
  - `docs/SPEC-CROSS-REFERENCE.md` - Cross-reference table
  - `docs/README.md` - Documentation hub overview

- [x] Created instruction files (with TODO markers for expansion)
  - `master-workflow.md`
  - `uv-environment-setup.instructions.md`
  - `tdd-workflow.instructions.md`
  - `threat-modeling.instructions.md`
  - `architecture-diagrams.instructions.md`
  - `claude-usage.instructions.md`
  - `copilot-usage.instructions.md`
  - `automation-setup.instructions.md`
  - `security-review.instructions.md`
  - `post-test-review.instructions.md`
  - `testcase.instructions.md`
  - `.github/instructions/README.md`

- [x] Created prompt files (with TODO markers for expansion)
  - `generate-spec-from-requirement.prompt.md`
  - `generate-code-from-spec.prompt.md`
  - `create-threat-model.prompt.md`
  - `create-architecture-diagram.prompt.md`
  - `.github/prompts/README.md`
  - `.github/prompts/output-logs/README.md`

- [x] Created rules files
  - `docs/rules/docstring-standards.md` - Complete with examples
  - `docs/rules/output-format.md` - Complete log format specification
  - `docs/rules/error-resolution-kb.md` - Starter KB with common errors
  - `docs/rules/README.md`

- [x] Created folder READMEs
  - `docs/diagrams/README.md`
  - `docs/history/README.md`
  - `docs/output-logs/README.md`

- [x] Saved this conversation to history

## Next Steps (For Template Users)

When using this template for a new project:

1. **Initial Setup**
   - Clone/use this template
   - Follow `uv-environment-setup.instructions.md`
   - Read `docs/README.md` and `docs/INDEX.md`

2. **Configure AI Assistant**
   - Claude Code: Already configured via CLAUDE.md files
   - GitHub Copilot: Update `.github/copilot-instructions.md`

3. **Create First Requirement**
   - Use `docs/templates/requirements-template.md`
   - Save to `docs/requirements/req-{name}.md`

4. **Follow Workflow**
   - Reference `.github/instructions/master-workflow.md`
   - Generate specifications, threat models, diagrams
   - Implement with TDD
   - Track in cross-reference table

5. **Customize Rules**
   - Modify `docs/rules/docstring-standards.md` for team preferences
   - Expand `docs/rules/error-resolution-kb.md` as project grows

6. **Setup Automation** (Optional)
   - Review `automation-setup.instructions.md`
   - Choose GitHub Actions, pre-commit hooks, or manual scripts

## References

- **Master Workflow**: `.github/instructions/master-workflow.md`
- **Documentation Index**: `docs/INDEX.md`
- **Cross-Reference Table**: `docs/SPEC-CROSS-REFERENCE.md`
- **CodeGuard Documentation**: https://project-codeguard.org/

---

**Impact**: This setup provides a complete, production-ready workflow template for specification-driven development with integrated security, comprehensive documentation, and AI assistant support. It can be used as-is or customized for specific project needs.

**Template Philosophy**:
- **Universal in `.github/`** - Works for any Python project
- **Specific in `docs/`** - Tailored to each project's needs
- **Security-first** - CodeGuard integrated throughout
- **AI-friendly** - Works with multiple AI assistants
- **Traceable** - Every decision and change is documented
