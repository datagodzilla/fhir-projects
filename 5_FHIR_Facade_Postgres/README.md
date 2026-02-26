# FHIR Facade on PostgreSQL

> **Status**: Coming Soon

A custom **FHIR server** built with the **HAPI FHIR (Java)** framework that maps data from a **PostgreSQL** relational database to FHIR resources. Demonstrates how to expose existing clinical data as a standards-compliant FHIR API without migrating the underlying database.

## What Will Be Built

- HAPI FHIR server (Java/Spring Boot) with custom resource providers
- PostgreSQL database schema for clinical data
- Data mapping layer: SQL rows to FHIR Patient, Encounter, Observation resources
- FHIR REST API serving data from PostgreSQL
- Search parameter implementation (name, date, identifier)
- Custom FHIR operations
- Database migration scripts

## Key FHIR Concepts

| Concept | Description |
|---------|-------------|
| FHIR Facade | FHIR API layer over existing non-FHIR data |
| Resource Provider | Java class that handles CRUD for a resource type |
| IResourceProvider | HAPI FHIR interface for implementing resource operations |
| Search Parameters | Custom search logic mapping FHIR params to SQL queries |
| CapabilityStatement | Auto-generated from registered providers |
| Interceptors | Request/response hooks for logging, auth, validation |

## Prerequisites

- Java 17+ (JDK)
- Maven 3.8+
- PostgreSQL 14+
- Docker (optional, for containerized Postgres)

## Tech Stack

Java, Spring Boot, HAPI FHIR Server, PostgreSQL, Maven, Docker

## License

MIT - see [LICENSE](../LICENSE)
