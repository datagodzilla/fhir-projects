# SMART Patient App - Cerner

> **Status**: Coming Soon

A browser-based patient app that launches from **Cerner's EHR sandbox** using the SMART on FHIR EHR launch flow. Demonstrates multi-vendor FHIR patterns, write-back operations, and the differences between Epic and Cerner FHIR implementations.

## What Will Be Built

- SMART on FHIR EHR launch flow (app launched from within Cerner)
- Cerner sandbox registration and configuration
- Reading and writing Patient data (write-back to EHR)
- Handling vendor-specific FHIR implementation differences
- Clinical data display with patient context from EHR launch
- Comparison of Epic vs. Cerner FHIR behavior

## Key FHIR Concepts

| Concept | Description |
|---------|-------------|
| EHR Launch | App launched from the EHR with pre-selected patient context |
| Write-back | Creating/updating resources in the EHR via FHIR API |
| Vendor Differences | Handling Epic vs. Cerner implementation variations |
| US Core Profiles | Standardized FHIR profiles for US healthcare |
| CapabilityStatement | Querying server capabilities to adapt behavior |

## Prerequisites

- Cerner developer account ([code.cerner.com](https://code.cerner.com))
- App registered in Cerner Code sandbox
- Modern web browser

## Tech Stack

HTML/CSS/JavaScript, fhirclient.js, SMART on FHIR, Cerner Sandbox

## License

MIT - see [LICENSE](../LICENSE)
