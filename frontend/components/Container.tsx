"use client";

export default function Container({ children }: { children: React.ReactNode }) {
  
  return (
    <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-4">
        <div className="container mx-auto px-4">{children}</div>
    </div>
  );
}