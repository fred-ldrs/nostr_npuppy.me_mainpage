# npuppy.me - NOSTR Address Service

A web application that allows users to create friendly @npuppy.me addresses from their NOSTR npub keys.

## Overview

This service provides an easy way for NOSTR users to convert their complex npub keys into memorable, user-friendly @npuppy.me addresses, similar to how my.nostr.com operates.

## Core Features

- Convert complex NOSTR npub keys to memorable @npuppy.me addresses
- Manage multiple addresses through a user dashboard
- Secure authentication via email OTP (no password storage)
- Free service with optional donations via Lightning Network

## Technical Architecture

### Frontend
- Dark-themed minimalist interface
- Responsive design for mobile and desktop usage

### Backend
- **Framework**: Python with Flask/FastAPI
- **Database**: MariaDB
- **DNS**: Configuration for npuppy.me domain using the NOSTR `.well-known` standard with `nostr.json` file and appropriate DNS settings

## User Management

### User Authentication & Session Management
- ~~**Authentication Method**: Email OTP (One-Time Password) system~~
  - ~~6-digit code sent to user's email~~
  - ~~OTP valid for maximum 15 minutes~~
- ~~Session Duration: 10 minutes after successful OTP verification~~
- ~~Account Limits: Maximum 10 @npuppy.me addresses per registered email~~
- - **Account Limits**: Maximum 10 @npuppy.me addresses per registered user

**Aktualisierung:**  
Statt des OTP-Verfahrens wird nun ein einfaches Authentifizierungssystem verwendet:
- **Authentifizierung:** Nutzername und Passwort
- Die Zugangsdaten werden ausschließlich als Hashwert gespeichert
- Es werden keine personenbezogenen Daten wie E-Mail-Adressen gespeichert
- Ziel: einfache, datensparsame Implementierung

### Address Management
- Register and manage @npuppy.me addresses
- Update npub keys associated with existing addresses
- Self-service address management via user dashboard
- **Allocation Policy**: First come, first served basis

## Address Policies

### Format Guidelines
- **Characters Allowed**: Alphanumeric (a-z, 0-9)
- **Special Characters**: Periods (.), underscores (_), and hyphens (-)
- **Length**: 3-30 characters

### Content Restrictions
- No constitutionally prohibited names or hate speech
- Subject to moderation using existing public blocklists for inappropriate content
- No verification of npub ownership required

## Donation System

- **Implementation**: Subtle donation button in website footer
- **Payment Processing**: OpenNode API for Lightning Network payments (refer to OpenNode documentation)
- **User Experience**:
  - User-defined donation amounts
  - No account required for donations
  - No special rewards or tracking for donors

## Non-Functional Requirements

### Security
- Encrypted storage of email addresses
- No storage of additional personal data
- No password storage (OTP only)
- Protection against common web vulnerabilities

### Rate Limiting
- Maximum 5 OTP requests per email address per hour
- Maximum 20 address registrations per account per day
- IP-based rate limiting for unauthenticated requests (100 per hour)

### Performance & Reliability
- Fast address lookup and resolution
- Consistent service availability
- Scalable architecture from launch with ability to add additional domain endings in future

### Data Management
- Source code version control via GitHub
- Database backups implemented via standard backup procedures
- No long-term storage of personal user data beyond encrypted email addresses

## Development Roadmap

1. **Phase 1**: Foundation
   - Project structure setup
   - Database schema implementation
   - OTP authentication system

2. **Phase 2**: Core Functionality
   - npub to @npuppy.me conversion logic
   - User dashboard implementation
   - Address management features

3. **Phase 3**: Deployment & Integration
   - DNS configuration with .well-known implementation
   - NOSTR protocol integration
   - Production deployment

4. **Phase 4**: Enhancements
   - Performance optimizations
   - Additional user features
   - API for third-party integrations

## Getting Started

Development instructions coming soon...

Last updated: 2025-08-25 13:14:13 by fred-ldrs
```
