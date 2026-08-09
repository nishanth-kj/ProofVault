import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "ProofVault | Enterprise Blockchain Verification",
  description: "Unforgeable Document Verification on the Solana Blockchain.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-background text-foreground antialiased">
        {children}
      </body>
    </html>
  );
}
