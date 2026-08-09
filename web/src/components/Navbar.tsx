"use client";

import React, { useState, useEffect } from 'react';
import { ShieldCheck, Moon, Sun, Menu } from 'lucide-react';
import { Button, buttonVariants } from '@/components/ui/button';
import { Sheet, SheetContent, SheetTrigger } from '@/components/ui/sheet';

export function Navbar() {
  const [isDark, setIsDark] = useState(false);

  useEffect(() => {
    const isDarkOS = window.matchMedia('(prefers-color-scheme: dark)').matches;
    setIsDark(isDarkOS);
    if (isDarkOS) document.documentElement.classList.add('dark');
  }, []);

  const toggleTheme = () => {
    if (isDark) {
      document.documentElement.classList.remove('dark');
      setIsDark(false);
    } else {
      document.documentElement.classList.add('dark');
      setIsDark(true);
    }
  };

  return (
    <header className="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container mx-auto px-4 flex h-16 items-center justify-between">
        <a href="/" className="flex items-center gap-2 font-bold text-xl">
          <ShieldCheck className="h-8 w-8 text-primary" />
          <span>Proof<span className="text-primary">Vault</span></span>
        </a>
        
        {/* Desktop Nav */}
        <nav className="hidden md:flex gap-6 items-center">
          <a href="#how-it-works" className="text-sm font-medium text-muted-foreground hover:text-foreground">How it Works</a>
          <a href="#features" className="text-sm font-medium text-muted-foreground hover:text-foreground">Features</a>
          <a href="#api" className="text-sm font-medium text-muted-foreground hover:text-foreground">API Docs</a>
          
          <Button variant="ghost" size="icon" onClick={toggleTheme}>
            {isDark ? <Sun className="h-5 w-5" /> : <Moon className="h-5 w-5" />}
          </Button>
          
          <Button>Connect Wallet</Button>
        </nav>

        {/* Mobile Nav */}
        <div className="md:hidden flex items-center gap-2">
          <Button variant="ghost" size="icon" onClick={toggleTheme}>
            {isDark ? <Sun className="h-5 w-5" /> : <Moon className="h-5 w-5" />}
          </Button>
          
          <Sheet>
            <SheetTrigger className={buttonVariants({ variant: "ghost", size: "icon" })}>
              <Menu className="h-6 w-6" />
            </SheetTrigger>
            <SheetContent side="right" className="w-[300px] flex flex-col gap-6 pt-12">
              <a href="#how-it-works" className="text-lg font-medium">How it Works</a>
              <a href="#features" className="text-lg font-medium">Features</a>
              <a href="#api" className="text-lg font-medium">API Docs</a>
              <div className="mt-auto pb-8">
                <Button className="w-full">Connect Wallet</Button>
              </div>
            </SheetContent>
          </Sheet>
        </div>
      </div>
    </header>
  );
}
