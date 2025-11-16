import Container from "@/components/Container";
import KanbanMain from "@/components/kanban/KanbanMain";
import { BusinessHeader } from "@/components/BusinessHeader";
import KanbanSidebar from "@/components/kanban/sidebar/KanbanSidebar";

export default function Business() {
  return (
    <Container>
      <div>
        <BusinessHeader />
        <KanbanMain />
        {/* <KanbanSidebar /> */}
      </div>
    </Container>
  );
}
