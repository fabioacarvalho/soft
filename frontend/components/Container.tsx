"use server";

import { Header } from "./Header";
import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar"
import { AppSidebar } from "@/components/sidebar"
import { cookies } from "next/headers"
import { Separator } from "@radix-ui/react-separator";

export default async function Container({ children }: { children: React.ReactNode }) {
  const cookieStore = await cookies()
  const defaultOpen = cookieStore.get("sidebar_state")?.value === "true"
  
  return (
    <div>
        <SidebarProvider defaultOpen={defaultOpen}>
          <AppSidebar />
          <SidebarTrigger />
          <main className=" w-full max-w-7xl px-4 mt-2 sm:px-6 lg:px-8">
            <Header />
            <Separator className="my-4 " />

            <div className="container mx-auto px-4 mt-10">
              {children}
            </div>

          </main>
        </SidebarProvider>
    </div>
  );
}