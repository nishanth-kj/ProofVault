import { ShieldCheck } from 'lucide-react';

export function Footer() {
  return (
    <footer className="border-t py-6 mt-auto bg-background">
      <div className="container mx-auto px-4 flex flex-col items-center justify-between gap-6 md:flex-row">
        <div className="flex items-center gap-2 font-bold text-xl">
          <ShieldCheck className="h-6 w-6 text-primary" />
          <span>ProofVault</span>
        </div>
        
        <div className="flex gap-6 text-sm text-muted-foreground">
          <a href="#" className="hover:text-foreground transition-colors">Privacy Policy</a>
          <a href="#" className="hover:text-foreground transition-colors">Terms of Service</a>
          <a href="#" className="hover:text-foreground transition-colors">GitHub</a>
          <a href="#" className="hover:text-foreground transition-colors">Twitter</a>
        </div>
      </div>
    </footer>
  );
}
