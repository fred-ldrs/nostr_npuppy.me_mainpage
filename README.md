# npuppy.me - NOSTR Address Service

A web application that allows users to create friendly @npuppy.me addresses from their NOSTR npub keys.

## Overview

This service provides an easy way for NOSTR users to convert their complex npub keys into memorable, user-friendly @npuppy.me addresses, similar to how my.nostr.com operates.

## Core Features

- Convert complex NOSTR npub keys to memorable @npuppy.me addresses
- Manage multiple addresses through a user dashboard
- Secure authentication via username and password (no personal data required)
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

**Update:**  
Authentication now uses a simple username and password system:
- **Authentication:** Users create an account with a unique username and password.
- **Password Storage:** Passwords are stored only as secure cryptographic hashes (e.g., bcrypt, scrypt, or argon2). Plaintext passwords are never stored or logged.
- **Privacy:** No personally identifiable information (such as email address) is required or stored.
- **Session Management:** Secure sessions are created after login (via signed cookies or JWTs). Sessions have a reasonable timeout for security.
- **Account Limits:** Each user account can manage up to 10 @npuppy.me addresses via their dashboard.

#### Registration & Login Workflow

1. **Registration**
   - User chooses a unique username and password.
   - The password is hashed and only the hash is stored in the database.
   - No email or other personal data is requested or retained.

2. **Login**
   - User logs in with their username and password.
   - The submitted password is hashed and compared with the stored hash.
   - On successful authentication, a secure session is created.

3. **Session Management**
   - Sessions use signed cookies or JWTs.
   - Session tokens contain no personal data.
   - Sessions expire after a reasonable period of inactivity.

4. **Account Limits**
   - Each account can manage up to 10 @npuppy.me addresses.

#### Security Considerations

- Passwords are stored using strong, industry-standard password hashing algorithms.
- No personal data (such as email addresses) is collected or stored.
- Usernames must be unique and meet the address format guidelines.
- Sensitive operations require user authentication.
- Registration and login endpoints are rate-limited and protected against brute-force attacks.

### Address Management

- Register and manage @npuppy.me addresses
- Update npub keys associated with existing addresses
- Self-service address management via user dashboard
- **Allocation Policy:** First come, first served basis

## Address Policies

### Format Guidelines
- **Characters Allowed:** Alphanumeric (a-z, 0-9)
- **Special Characters:** Periods (.), underscores (_), and hyphens (-)
- **Length:** 3-30 characters

### Content Restrictions
- No constitutionally prohibited names or hate speech
- Subject to moderation using existing public blocklists for inappropriate content
- No verification of npub ownership required

## Donation System

- **Implementation:** Subtle donation button in website footer
- **Payment Processing:** OpenNode API for Lightning Network payments (refer to OpenNode documentation)
- **User Experience:**
  - User-defined donation amounts
  - No account required for donations
  - No special rewards or tracking for donors

## Non-Functional Requirements

### Security
- Passwords stored as cryptographic hashes only
- No storage of additional personal data
- Protection against common web vulnerabilities

### Rate Limiting
- Rate limiting for registration and authentication endpoints to prevent abuse
- Maximum 20 address registrations per account per day
- IP-based rate limiting for unauthenticated requests

### Performance & Reliability
- Fast address lookup and resolution
- Consistent service availability
- Scalable architecture from launch with ability to add additional domain endings in future

### Data Management
- Source code version control via GitHub
- Database backups implemented via standard backup procedures
- No long-term storage of personal user data

## Development Roadmap

1. **Phase 1**: Foundation
   - Project structure setup
   - Database schema implementation
   - Username/password authentication system

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

Last updated: 2025-08-26 04:45:44 by fred-ldrs
