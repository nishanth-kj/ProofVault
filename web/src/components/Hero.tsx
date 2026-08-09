import { Button } from '@/components/ui/button';

export function Hero() {
  return (
    <section className="container mx-auto px-4 flex flex-col items-center justify-center space-y-6 min-h-[calc(100vh-4rem)] text-center">
      <div className="space-y-4">
        <h1 className="text-4xl font-extrabold tracking-tight sm:text-5xl md:text-6xl lg:text-7xl">
          The standard for <br />
          <span className="text-primary">Document Authenticity</span>
        </h1>
        <p className="mx-auto max-w-[700px] text-muted-foreground md:text-xl leading-relaxed">
          Instantly verify academic records, legal contracts, and enterprise documents on the Solana blockchain with zero-knowledge proofs.
        </p>
      </div>
      
      <div className="flex flex-col sm:flex-row gap-4">
        <Button size="lg" className="h-12 px-8 text-base">Issue a Document</Button>
        <Button size="lg" variant="outline" className="h-12 px-8 text-base">Verify Document</Button>
      </div>
    </section>
  );
}
