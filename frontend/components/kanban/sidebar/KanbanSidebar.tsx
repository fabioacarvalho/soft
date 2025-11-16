import { Card } from "@/components/ui/card";
import CircularProgress from "./CircularProgress";
import TasksStats from "./TasksStats";
// import SelectionDropDown from "@/components/drop-downs/selection-drop-down";

export default function KanbanSidebar() {
    return (
        <Card className="shadow-none p-6 rounded-3-md max-h-[640px] overflow-hidden">
            <div className="flex flex-col gap-0">
                {/* <SelectionDropDown /> */}
                <CircularProgress />
                <TasksStats />
            </div>
        </Card>
    );
}
