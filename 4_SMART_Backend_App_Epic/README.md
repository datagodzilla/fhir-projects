# SMART Backend App - Epic

> **Status**: Coming Soon

A server-side application that authenticates against **Epic's FHIR API** using the **SMART Backend Services** specification (client credentials with JWT). Demonstrates system-level access, Bulk FHIR data export, and processing large datasets without user interaction.

## What Will Be Built

- SMART Backend Services authentication (client_credentials grant)
- JWT (JSON Web Token) creation and signing with RSA keys
- System-level FHIR access (no patient context required)
- Bulk FHIR export ($export operation) for population-level data
- NDJSON (Newline Delimited JSON) processing pipeline
- Automated data extraction and analysis scripts

## Key FHIR Concepts

| Concept | Description |
|---------|-------------|
| Backend Services | Server-to-server auth without user interaction |
| Client Credentials | OAuth2 grant type using JWT assertion |
| JWT / JWK | JSON Web Token signed with private key, public key registered with server |
| Bulk FHIR | `$export` operation for downloading large datasets |
| NDJSON | Newline Delimited JSON format for bulk data |
| System Scopes | `system/Patient.read`, `system/Observation.read`, etc. |

## Prerequisites

- Epic developer account with backend services app registered
- RSA key pair (public/private)
- Node.js 18+ or Python 3.x
- OpenSSL (for key generation)

## Tech Stack

Node.js or Python, SMART Backend Services, JWT, Epic FHIR API, Bulk FHIR

## License

MIT - see [LICENSE](../LICENSE)
