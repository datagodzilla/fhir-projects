# FHIR Projects - Build 5 FHIR Applications

A portfolio of five healthcare interoperability applications built with **HL7 FHIR R4**, progressing from basic REST API clients to SMART on FHIR-authenticated apps and server-side implementations. Each project is a self-contained application that demonstrates real-world FHIR integration patterns.

## Introduction: Understanding FHIR R4 Resources

Before diving into the applications, explore the **FHIR R4 Resource Hierarchy** - an interactive visualization of all 264 nodes in the FHIR R4 (4.0.1) specification.

[![Explore FHIR R4 Hierarchy](https://img.shields.io/badge/Explore-FHIR_R4_Resource_Hierarchy-40B5AD?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJ3aGl0ZSI+PHBhdGggZD0iTTEyIDJMMyA3bDkgNSA5LTV6TTMgMTdsOSA1IDktNXoiLz48L3N2Zz4=&logoColor=white)](https://datagodzilla.github.io/fhir-projects/fhir_r4_hierarchy.html)

This single-file interactive tool provides four complementary views of the FHIR R4 specification:

| View | Description |
|------|-------------|
| **By Module** | Resources grouped by FHIR specification layers (L1 Foundation through L6 Specialized) |
| **By Category** | Resources grouped by HL7 categories: Foundation, Base, Clinical, Financial, Specialized |
| **By Inheritance (Table)** | Type hierarchy showing `extends` relationships (Base → Element, Resource → DomainResource) |
| **Inheritance Tree** | Interactive D3.js node-link tree with click-to-expand, zoom, pan, and search |

**Key stats**: 143 Resources, 38 Datatypes, 57 Normative elements, 140+ DomainResource types. Click any resource name to open its HL7 FHIR R4 specification page.

## Applications

| # | Application | Description | Tech Stack | Status |
|---|------------|-------------|------------|--------|
| 1 | [Patient Management Application](1_Patient_Management_Application/) | CRUD operations on FHIR Patient resources with search, pagination, visit history, and appointment calendar | HTML/CSS/JS, HAPI FHIR R4 | Complete |
| 2 | [SMART Patient App - Epic](2_SMART_Patient_App_Epic/) | OAuth2-authenticated patient portal using SMART on FHIR launch against Epic sandbox | HTML/CSS/JS, SMART on FHIR, Epic | Coming Soon |
| 3 | [SMART Patient App - Cerner](3_SMART_Patient_App_Cerner/) | EHR-launched patient app with write-back capabilities against Cerner sandbox | HTML/CSS/JS, SMART on FHIR, Cerner | Coming Soon |
| 4 | [SMART Backend App - Epic](4_SMART_Backend_App_Epic/) | Backend service with JWT authentication, Bulk FHIR data export from Epic | Node.js/Python, SMART Backend Services | Coming Soon |
| 5 | [FHIR Facade on Postgres](5_FHIR_Facade_Postgres/) | Custom FHIR server facade mapping PostgreSQL data to FHIR resources using HAPI FHIR (Java) | Java, HAPI FHIR Server, PostgreSQL | Coming Soon |

## Learning Progression

```
App 1: FHIR REST Basics          App 2: SMART on FHIR (Epic)     App 3: SMART on FHIR (Cerner)
  - Patient CRUD                   - OAuth2 Authorization           - EHR Launch Flow
  - Search & Pagination            - SMART Launch                   - Write-back Operations
  - Bundle Processing              - Token Management               - Multi-vendor Patterns
         |                                |                                |
         v                                v                                v
                    App 4: Backend Services               App 5: FHIR Server
                      - JWT / Client Credentials            - HAPI FHIR (Java)
                      - Bulk FHIR Export                    - PostgreSQL Mapping
                      - System-level Access                 - Custom Operations
```

## Tech Stack

| Technology | Used In | Purpose |
|-----------|---------|---------|
| **FHIR R4** | All apps | HL7 healthcare interoperability standard |
| **HAPI FHIR** | Apps 1, 5 | Public test server (App 1), Java FHIR server (App 5) |
| **HTML/CSS/JavaScript** | Apps 1-3 | Browser-based FHIR clients |
| **SMART on FHIR** | Apps 2-4 | OAuth2-based authorization for EHR access |
| **Epic Sandbox** | Apps 2, 4 | Epic's FHIR test environment |
| **Cerner Sandbox** | App 3 | Cerner's FHIR test environment |
| **Node.js / Python** | App 4 | Backend service implementation |
| **Java** | App 5 | HAPI FHIR server customization |
| **PostgreSQL** | App 5 | Relational database mapped to FHIR resources |

## Prerequisites

- Modern web browser (Chrome, Firefox, Edge)
- Python 3.x (for local HTTP server)
- Git
- For Apps 2-3: Epic/Cerner developer account
- For App 4: Node.js or Python 3.x
- For App 5: Java 17+, Maven, PostgreSQL

## Quick Start

```bash
# Clone the repository
git clone https://github.com/datagodzilla/fhir-projects.git
cd fhir-projects

# Run App 1 - Patient Management Application
cd 1_Patient_Management_Application
python3 -m http.server 8080
# Open http://localhost:8080 in your browser
```

## FHIR Resources Used

| Resource | App 1 | App 2 | App 3 | App 4 | App 5 |
|----------|-------|-------|-------|-------|-------|
| Patient | CRUD | Read | Read/Write | Bulk | CRUD |
| Encounter | Read | Read | Read | Bulk | CRUD |
| Appointment | Read | - | - | - | CRUD |
| Observation | - | Read | Read | Bulk | CRUD |
| Condition | - | Read | Read | Bulk | CRUD |
| MedicationRequest | - | Read | Read | Bulk | - |

## Project Structure

```
fhir-projects/
├── README.md
├── .gitignore
├── LICENSE
├── fhir_r4_hierarchy.html               # Interactive FHIR R4 resource hierarchy explorer
├── 1_Patient_Management_Application/    # Complete
├── 2_SMART_Patient_App_Epic/            # Coming Soon
├── 3_SMART_Patient_App_Cerner/          # Coming Soon
├── 4_SMART_Backend_App_Epic/            # Coming Soon
└── 5_FHIR_Facade_Postgres/             # Coming Soon
```

Each application directory contains:
- `README.md` - Setup instructions and documentation
- Application source code (HTML/JS or language-specific)
- `assets/` - Screenshots and visual assets
- `docs/` - Architecture docs, requirements, blog posts
- `scripts/` - Utility scripts

## Acknowledgments

These projects are inspired by the [Medblocks](https://medblocks.com/) "Build 5 FHIR Applications in 10 Weeks" bootcamp course, adapted and extended with original implementations, documentation, and architectural analysis.

## License

MIT License - see [LICENSE](LICENSE) for details.
