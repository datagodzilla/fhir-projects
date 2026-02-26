# SMART Patient App - Epic

> **Status**: Coming Soon

A browser-based patient portal that authenticates against **Epic's FHIR sandbox** using the **SMART on FHIR** launch framework. Demonstrates OAuth2 authorization code flow, token management, and reading clinical data from a simulated EHR.

## What Will Be Built

- SMART on FHIR standalone launch flow (OAuth2 authorization code)
- Epic sandbox registration and app configuration
- Patient context selection and token exchange
- Reading Patient, Condition, Observation, and MedicationRequest resources
- Clinical data dashboard with vitals, problem list, and medications
- Token refresh and session management

## Key FHIR Concepts

| Concept | Description |
|---------|-------------|
| SMART on FHIR | Authorization framework for EHR-connected apps |
| OAuth2 | Authorization code grant with PKCE |
| EHR Launch | App launched from within the EHR context |
| Standalone Launch | App launches independently, user selects patient |
| Scopes | `patient/Patient.read`, `patient/Observation.read`, etc. |
| fhirclient.js | JavaScript SMART on FHIR client library |

## Prerequisites

- Epic developer account ([open.epic.com](https://open.epic.com))
- App registered in Epic App Orchard sandbox
- Modern web browser
- Local HTTPS server (required for OAuth2 redirect)

## Tech Stack

HTML/CSS/JavaScript, fhirclient.js, SMART on FHIR, Epic Sandbox

## License

MIT - see [LICENSE](../LICENSE)
