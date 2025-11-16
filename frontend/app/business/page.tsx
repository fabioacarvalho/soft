import Container from "@/components/Container";
import KanbanMain from "@/components/kanban/KanbanMain";
import { BusinessHeader } from "@/components/BusinessHeader";
import KanbanSidebar from "@/components/kanban/sidebar/KanbanSidebar";

export default function Business() {
  return (
    <Container>
      <div>
        <BusinessHeader />
        <h1 className="text-4xl font-bold text-zinc-900 dark:text-zinc-100">
          Welcome to the Business Page
        </h1>
        <p className="mt-4 text-zinc-700 dark:text-zinc-300">
          This is a protected page. You are successfully authenticated!
        </p>
        <KanbanMain />
        {/* <KanbanSidebar /> */}
      </div>
    </Container>
  );
}
