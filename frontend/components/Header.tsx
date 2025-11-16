import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar"
import { AppSidebar } from "@/components/sidebar"

export default function Header() {
  return (
    <SidebarProvider>
      <AppSidebar />
        <SidebarTrigger />
    </SidebarProvider>
  )
}