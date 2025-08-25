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
- OTP
  - User registration and authentication via email OTP (no password storage)
  - User account / dashboard acess via email OTP (no password storage)
  - OTP code: valid for maximum 15 minutes, 6-digit code 
- Conversion of NOSTR npub keys to @npuppy.me addresses
- User dashboard for managing multiple addresses
- No Verification of npub ownership (Reason: would required that user put his nsec into the system - otherwise no possiblity for Verification of npub ownership)
- DNS integration for proper NOSTR address resolution

### User Authentication & Session Management
- **Authentication Method**: Email OTP (One-Time Password) system
  - 6-digit code sent to user's email
  - OTP valid for maximum 15 minutes
- **Session Duration**: 10 minutes after successful OTP verification
- **Account Limits**: Maximum 10 @npuppy.me addresses per registered email

### Address Management
- **Address Ownership**: Users can register and manage their own @npuppy.me addresses
- **Key Updates**: Users can update the npub key associated with their existing @npuppy.me address
- **Address Restrictions**:
  - No constitutionally prohibited names or hate speech
  - Subject to moderation for inappropriate content

### Address Format Guidelines
- **Character Support**: Standard alphanumeric characters (a-z, 0-9)
- **Special Characters**: Limited set including periods (.), underscores (_), and hyphens (-)
- **Length**: Minimum 3, maximum 30 characters

### Donation System
- **Placement**: Subtle donation button placed in the footer of the website
- **Payment Processing**: Integration with OpenNode API for Lightning Network payments
- **User Experience**:
  - Users can freely choose donation amount
  - No account required for donations
  - No tracking or special rewards for donors
- **Technical Integration**:
  - Direct OpenNode API integration
  - Minimal frontend implementation (button only)
  - Payment processing handled entirely by OpenNode

### Non-Functional Requirements
- Security: Secure handling of user data and NOSTR keys
- Performance: Fast address lookup and resolution
- Scalability: Support for growing user base
- Reliability: Consistent service availability
- The service is free for the user. but the user is free to donate

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

Development instructions coming soon...

Last updated: 2025-08-25 12:46:04 by fred-ldrs
