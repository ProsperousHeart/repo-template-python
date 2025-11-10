# Workflow Usage Guide: Practical Examples

**Date**: 2025-11-09
**Related**: [Setup Conversation](2025-11-09-setup-conversation.md)
**Purpose**: Provide step-by-step examples of using the documentation-driven development workflows

## 🎯 Overview

This guide shows practical examples of executing the complete workflow from requirements through code generation using the prompts and instructions created in this template.

## 📋 Table of Contents

1. [Complete Workflow Example](#complete-workflow-example-user-authentication)
2. [Using Workflow Orchestration Prompts](#using-workflow-orchestration-prompts)
3. [Using Individual Prompts](#using-individual-prompts)
4. [Quality Review at Each Stage](#quality-review-at-each-stage)
5. [Troubleshooting Common Issues](#troubleshooting-common-issues)

---

## Complete Workflow Example: User Authentication

Let's walk through implementing a user authentication feature from scratch.

### Stage 0: Environment Setup

**Prompt:**

```
Check the UV environment following .github/instructions/uv-environment-setup.instructions.md.
If environment doesn't exist, create it.
```

**Expected outcome:**

- ✅ UV environment exists
- ✅ Ready to use `uv add` for packages

---

### Stage 1: Requirements → Specification

**Using orchestration prompt (recommended):**

```
Execute the workflow-requirements-to-spec prompt for docs/requirements/req-user-auth.md with threat model scope per-requirement
```

This single command will:

1. ✅ Generate `docs/specifications/spec_ser-auth.md`
2. ✅ Create `docs/diagrams/threat-model_user-auth.md`
3. ✅ Create `docs/diagrams/architecture_user-auth.md`
4. ✅ Run specification quality review
5. ✅ Update cross-reference table and index
6. ✅ Create execution log

**Expected output summary:**

```
✅ Requirements → Specification Workflow Complete

📁 Files Created:
- [docs/specifications/spec_user-auth.md](../specifications/spec_user-auth.md)
- [docs/diagrams/threat-model_user-auth.md](../diagrams/threat-model_user-auth.md)
- [docs/diagrams/architecture-user-auth.md](../diagrams/architecture_user-auth.md)

📝 Files Updated:
- [docs/SPEC-CROSS-REFERENCE.md](../SPEC-CROSS-REFERENCE.md)
- [docs/INDEX.md](../INDEX.md)

🔒 CodeGuard Files Referenced:
- [codeguard-0-authentication-mfa.instructions.md](../../.github/instructions/codeguard-0-authentication-mfa.instructions.md)
- [codeguard-0-input-validation-injection.instructions.md](../../.github/instructions/codeguard-0-input-validation-injection.instructions.md)
- [codeguard-0-session-management-and-cookies.instructions.md](../../.github/instructions/codeguard-0-session-management-and-cookies.instructions.md)

📋 Quality Review: ✅ PASSED

⏳ Next Step: Human review and approval
```

**Human review checkpoint**: Review the generated files and approve to proceed.

---

### Stage 2: Specification → Code

**Using orchestration prompt (recommended):**

```
Execute the workflow-spec-to-code prompt for docs/specifications/spec_user-auth.md
```

This single command will:

1. ✅ Implement code using TDD (RED-GREEN-REFACTOR cycles)
2. ✅ Generate tests before code
3. ✅ Apply CodeGuard security rules
4. ✅ Run security review
5. ✅ Run quality validation (pytest, coverage, ruff)
6. ✅ Update documentation
7. ✅ Create execution log

**Expected output summary:**

```
✅ Specification → Code Workflow Complete

📁 Files Created:
- src/auth/login.py
- src/auth/session.py
- test/test_auth/test_login.py
- test/test_auth/test_session.py

🧪 Test Results:
- Total tests: 24
- Passed: 24 ✅
- Coverage: 94%

🔒 CodeGuard Files Applied:
- [codeguard-0-authentication-mfa.instructions.md](../../.github/instructions/codeguard-0-authentication-mfa.instructions.md)
- [codeguard-0-input-validation-injection.instructions.md](../../.github/instructions/codeguard-0-input-validation-injection.instructions.md)
- [codeguard-0-session-management-and-cookies.instructions.md](../../.github/instructions/codeguard-0-session-management-and-cookies.instructions.md)

📋 Quality Review: ✅ PASSED
🔒 Security Review: ✅ PASSED

⏳ Next Step: Human code review and approval
```

---

## Using Workflow Orchestration Prompts

### Benefits

- 🚀 **Fast**: Single command runs entire workflow
- ✅ **Complete**: Includes all quality gates
- 📋 **Traceable**: Creates comprehensive logs
- 🔒 **Secure**: Automatically applies CodeGuard

### Requirements → Specification Workflow

**Prompt file**: [workflow-requirements-to-spec.prompt.md](../../.github/prompts/workflow-requirements-to-spec.prompt.md)

**Usage with Claude Code:**

```
Execute the workflow-requirements-to-spec prompt for docs/requirements/req-{name}.md with threat model scope {per-requirement|high-level-aggregate|grouped-by-feature}
```

**Usage with GitHub Copilot:**

```
@workspace Follow @.github/prompts/workflow-requirements-to-spec.prompt.md to generate complete specification from @docs/requirements/req-{name}.md
```

**What it does:**

1. Generates specification
2. Creates threat model
3. Creates architecture diagram
4. Runs [specification quality review](../../.github/instructions/quality-checklists.md)
5. Updates [cross-reference table](../SPEC-CROSS-REFERENCE.md)
6. Creates execution log

### Specification → Code Workflow

**Prompt file**: [workflow-spec-to-code.prompt.md](../../.github/prompts/workflow-spec-to-code.prompt.md)

**Usage with Claude Code:**

```
Execute the workflow-spec-to-code prompt for docs/specifications/spec_{name}.md
```

**Usage with GitHub Copilot:**

```
@workspace Follow @.github/prompts/workflow-spec-to-code.prompt.md to implement @docs/specifications/spec_{name}.md
```

**What it does:**

1. Reviews specification
2. Implements using [TDD workflow](../../.github/instructions/tdd-workflow.instructions.md)
3. Runs [security review](../../.github/instructions/security-review.instructions.md)
4. Runs [quality validation](../../.github/instructions/quality-checklists.md)
5. Conducts [post-test review](../../.github/instructions/post-test-review.instructions.md)
6. Updates documentation
7. Creates execution log

---

## Using Individual Prompts

### When to Use Individual Prompts

- 🎯 **Specific task**: Only need one operation
- 🔄 **Iterating**: Regenerating one component
- 📚 **Learning**: Understanding each step

### Generate Specification

**Prompt file**: [generate-spec-from-requirement.prompt.md](../../.github/prompts/generate-spec-from-requirement.prompt.md)

```
Use the generate-spec-from-requirement prompt for docs/requirements/req-{name}.md
```

**Outputs**:

- `docs/specifications/spec_{name}.md`
- Updates to [cross-reference table](../SPEC-CROSS-REFERENCE.md)

### Create Threat Model

**Prompt file**: [create-threat-model.prompt.md](../../.github/prompts/create-threat-model.prompt.md)

```
Use the create-threat-model prompt for docs/requirements/req-{name}.md with scope per-requirement
```

**Outputs**:

- `docs/diagrams/threat-model-{name}.md`
- STRIDE analysis
- CodeGuard references

### Create Architecture Diagram

**Prompt file**: [create-architecture-diagram.prompt.md](../../.github/prompts/create-architecture-diagram.prompt.md)

```
Use the create-architecture-diagram prompt for docs/specifications/spec_{name}.md
```

**Outputs**:

- `docs/diagrams/architecture-{name}.md`
- Mermaid diagrams
- Security annotations

### Generate Code with TDD

**Prompt file**: [generate-code-from-spec.prompt.md](../../.github/prompts/generate-code-from-spec.prompt.md)

```
Use the generate-code-from-spec prompt for docs/specifications/spec_{name}.md
```

**Outputs**:

- Source files in `src/`
- Test files in `test/`
- Execution log with TDD cycles documented

---

## Quality Review at Each Stage

### Requirements Stage Quality Review

**Reference**: [Quality Checklists - Requirements Stage](../../.github/instructions/quality-checklists.md#requirements-stage-quality-checklist)

**Prompt:**

```
Conduct requirements stage quality review for docs/requirements/req-{name}.md following .github/instructions/quality-checklists.md
```

**Key checks:**

- ✅ Problem statement clear
- ✅ Acceptance criteria measurable
- ✅ Dependencies identified
- ✅ Security considerations noted

### Specification Stage Quality Review

**Reference**: [Quality Checklists - Specification Stage](../../.github/instructions/quality-checklists.md#specification-stage-quality-checklist)

**Prompt:**

```
Conduct specification stage quality review for docs/specifications/spec_{name}.md following .github/instructions/quality-checklists.md
```

**Key checks:**

- ✅ Architecture defined
- ✅ TDD planning complete
- ✅ Threat model created
- ✅ CodeGuard files referenced
- ✅ Filename includes `-tdd` suffix

### Code Generation Stage Quality Review

**Reference**: [Quality Checklists - Code Generation Stage](../../.github/instructions/quality-checklists.md#code-generation-tdd-stage-quality-checklist)

**Prompt:**

```
Conduct code generation stage quality review for src/{module}/ following .github/instructions/quality-checklists.md
```

**Key checks:**

- ✅ All tests pass
- ✅ Coverage ≥ 90%
- ✅ Ruff checks pass
- ✅ Docstrings follow [standards](../rules/docstring-standards.md)
- ✅ CodeGuard compliance verified

**Manual commands:**

```bash
# Run tests
pytest -v

# Check coverage
pytest --cov=src --cov-report=term

# Run ruff
ruff check src/ test/
ruff format src/ test/
```

---

## Troubleshooting Common Issues

### Issue: Quality Review Fails

**Symptom:**

```
❌ Quality review failed: Test coverage only 65% (threshold 90%)
```

**Solution:**

```bash
# Identify uncovered lines
pytest --cov=src --cov-report=html
open htmlcov/index.html

# Add tests for missing scenarios
# Re-run quality review
```

### Issue: Security Review Fails

**Symptom:**

```
❌ Security review failed: Hardcoded credential found
```

**Solution:**

1. Review relevant [CodeGuard file](../../.github/instructions/)
2. Move credentials to environment variables
3. Update code to use `os.getenv()`
4. Add to [error resolution KB](../rules/error-resolution-kb.md)
5. Re-run security review

### Issue: Tests Fail After Refactoring

**Symptom:**
Tests pass in GREEN but fail after REFACTOR phase

**Solution:**

1. Review changes made during refactoring
2. Ensure logic hasn't changed
3. Check test expectations are still valid
4. Add debug logging temporarily
5. Request human guidance if stuck

### Issue: Prompt Not Executing

**Symptom:**
AI doesn't recognize the prompt reference

**Solution:**

```
Read .github/prompts/{prompt-file}.prompt.md and execute that prompt for {target-file}
```

---

## Quick Reference

### Workflow Orchestration

```bash
# Requirements → Specification (complete)
Execute workflow-requirements-to-spec prompt for docs/requirements/{name}.md with scope per-requirement

# Specification → Code (complete)
Execute workflow-spec-to-code prompt for docs/specifications/spec_{name}.md
```

### Individual Operations

```bash
# Generate specification
Use generate-spec-from-requirement prompt for docs/requirements/{name}.md

# Create threat model
Use create-threat-model prompt for docs/requirements/{name}.md with scope per-requirement

# Create architecture diagram
Use create-architecture-diagram prompt for docs/specifications/spec_{name}.md

# Generate code with TDD
Use generate-code-from-spec prompt for docs/specifications/spec_{name}.md
```

### Quality Reviews

```bash
# Requirements quality review
Conduct requirements stage quality review for docs/requirements/{name}.md following .github/instructions/quality-checklists.md

# Specification quality review
Conduct specification stage quality review for docs/specifications/spec_{name}.md following .github/instructions/quality-checklists.md

# Code quality review
Conduct code generation stage quality review for src/{module}/ following .github/instructions/quality-checklists.md
```

### Manual Quality Checks

```bash
# Run all tests
pytest -v

# Check coverage with report
pytest --cov=src --cov-report=term --cov-report=html

# Ruff linting
ruff check src/ test/

# Ruff formatting
ruff format src/ test/

# Combined check
pytest -v && pytest --cov=src && ruff check src/ test/
```

---

## Related Documentation

- [Setup Conversation](2025-11-09-setup-conversation.md) - Why this structure exists
- [Master Workflow](../../.github/instructions/master-workflow.md) - Complete workflow overview
- [Quality Checklists](../../.github/instructions/quality-checklists.md) - All stage checklists
- [All Workflow Prompts](../../.github/prompts/) - Orchestration and individual prompts
- [TDD Workflow](../../.github/instructions/tdd-workflow.instructions.md) - RED-GREEN-REFACTOR process
- [Output Format](../rules/output-format.md) - Log format specification

---

**Last Updated**: 2025-11-09
