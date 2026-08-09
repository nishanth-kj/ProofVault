import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { FileText, Lock, Search } from 'lucide-react';

export function Features() {
  return (
    <section id="how-it-works" className="bg-muted/50 py-12">
      <div className="container mx-auto px-4 space-y-12">
        <div className="text-center space-y-4">
          <h2 className="text-3xl font-bold tracking-tight sm:text-4xl">How It Works</h2>
          <p className="text-muted-foreground mx-auto max-w-[600px] md:text-lg">
            Our platform secures your documents using state-of-the-art cryptography and decentralized ledgers.
          </p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <Card className="bg-background border-border/50 transition-all hover:shadow-lg hover:-translate-y-1 cursor-default">
            <CardHeader>
              <div className="mb-4 inline-flex h-12 w-12 items-center justify-center rounded-lg bg-primary/10">
                <FileText className="h-6 w-6 text-primary" />
              </div>
              <CardTitle>1. Hash Generation</CardTitle>
            </CardHeader>
            <CardContent className="text-muted-foreground">
              We generate a unique SHA-256 cryptographic hash of your document locally. The file never leaves your device.
            </CardContent>
          </Card>

          <Card className="bg-background border-border/50 transition-all hover:shadow-lg hover:-translate-y-1 cursor-default">
            <CardHeader>
              <div className="mb-4 inline-flex h-12 w-12 items-center justify-center rounded-lg bg-primary/10">
                <Lock className="h-6 w-6 text-primary" />
              </div>
              <CardTitle>2. Blockchain Anchoring</CardTitle>
            </CardHeader>
            <CardContent className="text-muted-foreground">
              The hash is permanently recorded on the Solana blockchain along with metadata like the issuer's public key.
            </CardContent>
          </Card>

          <Card className="bg-background border-border/50 transition-all hover:shadow-lg hover:-translate-y-1 cursor-default">
            <CardHeader>
              <div className="mb-4 inline-flex h-12 w-12 items-center justify-center rounded-lg bg-primary/10">
                <Search className="h-6 w-6 text-primary" />
              </div>
              <CardTitle>3. Instant Verification</CardTitle>
            </CardHeader>
            <CardContent className="text-muted-foreground">
              Anyone with the file can drag-and-drop it into ProofVault. We re-hash it and check the blockchain for a match instantly.
            </CardContent>
          </Card>
        </div>
      </div>
    </section>
  );
}
