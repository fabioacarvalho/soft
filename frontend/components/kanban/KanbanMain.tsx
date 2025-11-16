import { Card } from "@/components/ui/card";
import KanbanBoard from "@/components/kanban/board/KanbanBoard";
import KanbanAreaHeader from "@/components/kanban/header/KanbanAreaHeader";

export default function KanbanMain() {
    return (
        <Card className="shadow-none p-7 rounded-3-md px-7 flex-col gap-8 ">
            <KanbanAreaHeader />
            <KanbanBoard />
        </Card>
    );
}