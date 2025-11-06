# Project-Specific Claude Instructions

This project uses the CodeGuard plugin for AI-assisted secure code generation.

## Security Framework

**Plugin:** `codeguard-security@project-codeguard`
**Update command:** `/plugin update codeguard-security@project-codeguard`
**Source:** https://github.com/project-codeguard/rules
**Documentation:** https://project-codeguard.org/

### About CodeGuard

Project CodeGuard is an open-source security framework from Cisco that embeds secure-by-default practices into AI coding workflows. It provides comprehensive security rules across 8 domains that guide AI assistants to generate more secure code automatically.

### Security Coverage

- Cryptography (algorithms, key management, certificate validation)
- Input validation (SQL injection, XSS, command injection prevention)
- Authentication (MFA, OAuth/OIDC, session management)
- Authorization (RBAC/ABAC, access control)
- Supply chain security
- Cloud security
- Platform security
- Data protection
