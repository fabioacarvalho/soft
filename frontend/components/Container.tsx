"use server";

import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar"
import { AppSidebar } from "@/components/sidebar"
import { cookies } from "next/headers"
import { Separator } from "@radix-ui/react-separator";

import Navbar from "@/components/navbar/Navbar";

export default async function Container({ children }: { children: React.ReactNode }) {
  const cookieStore = await cookies()
  const defaultOpen = cookieStore.get("sidebar_state")?.value === "true"
  
  return (
    <div className="h-screen flex">
        <SidebarProvider defaultOpen={defaultOpen}>
          <AppSidebar />
          <SidebarTrigger />
          <main className="flex flex-col w-full  px-4 mt-2 sm:px-6 lg:px-8">
            <Navbar />
            <Separator className="my-4 " />

            <div className="flex-1 overflow-y-auto container mx-auto px-4 mt-10 ">
              {children}
            </div>

          </main>
        </SidebarProvider>
    </div>
  );
}