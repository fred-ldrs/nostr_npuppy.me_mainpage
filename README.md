# npuppy.me - NOSTR Address Service

A web application that allows users to create friendly @npuppy.me addresses from their NOSTR npub keys.

## Overview

This service provides an easy way for NOSTR users to convert their complex npub keys into memorable, user-friendly @npuppy.me addresses, similar to how my.nostr.com operates.

## Requirements

### Technical Requirements
- **Backend**: Python with Flask/FastAPI
- **Database**: MariaDB
- **Authentication**: Email OTP (One-Time Password) system
- **Design**: Dark-themed minimalist interface
- **Infrastructure**: DNS configuration for npuppy.me domain

### Functional Requirements
- User registration and authentication via email OTP (no password storage)
- Conversion of NOSTR npub keys to @npuppy.me addresses
- User dashboard for managing multiple addresses
- Verification of npub ownership
- DNS integration for proper NOSTR address resolution

### Non-Functional Requirements
- Security: Secure handling of user data and NOSTR keys
- Performance: Fast address lookup and resolution
- Scalability: Support for growing user base
- Reliability: Consistent service availability

## Development Roadmap

1. **Phase 1**: Basic setup and authentication
   - Initial project structure
   - Database schema implementation
   - OTP email authentication system

2. **Phase 2**: Core functionality
   - npub to @npuppy.me conversion logic
   - User dashboard
   - Address management features

3. **Phase 3**: Integration and deployment
   - DNS configuration
   - NOSTR protocol integration
   - Production deployment

4. **Phase 4**: Enhancements and additional features
   - Performance optimizations
   - Additional user features
   - API for third-party integrations

## Getting Started

Development instructions coming soon..."
