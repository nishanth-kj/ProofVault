# ProofVault

ProofVault is an Enterprise Blockchain Document Verification SaaS. This platform allows organizations to cryptographically hash important documents (transcripts, degrees, legal contracts) and anchor those hashes onto the Solana blockchain for immutable, decentralized verification.

## Project Structure

ProofVault is designed as a monorepo containing several distinct services:

- `/api`: The Python FastAPI backend handling business logic, database interaction, and blockchain coordination.
- `/web`: The Next.js frontend application providing the user interface for document upload, management, and verification.
- *(Future)* `/contracts`: Solana Anchor smart contracts to handle the on-chain hashing logic.

## Key Features

1. **Document Hashing**: Client-side or server-side hashing of files to ensure privacy (only the hash touches the blockchain).
2. **Blockchain Anchoring**: Immutably storing document hashes on Solana for low-cost, high-speed verification.
3. **Organization Management**: Multi-tenant architecture for different organizations to issue documents.
4. **Verification Portal**: A public-facing UI where third parties can upload a document and instantly verify its authenticity against the blockchain.

## Getting Started

Please explore the `docs` directory for detailed documentation on each subsystem:
- [API Architecture](api/architecture.md): Detailed breakdown of the technical design and backend conventions.
- [API Setup](api/setup.md): Instructions for running the backend locally.
- [Web Setup](web/setup.md): Instructions for running the frontend locally.
