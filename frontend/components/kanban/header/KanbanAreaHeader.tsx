import {Button } from "@/components/ui/button";
import { MdOutlineSortByAlpha } from "react-icons/md";
import SortingDropDown from "@/components/drop-downs/sorting-drop-down";
import TaskDialog from "@/components/dialogs/task-dialog/TaskDialog";

export default function KanbanAreaHeader() {
    return (
        <div className="flex justify-between items-center">
            <div className="flex gap-3 items-center">
                <span className="text-2-xl font-bold">Pipeline</span>

            </div>

            <div className="flex items-center gap-2">
                <div className="flex items-center gap-1">
                    <MdOutlineSortByAlpha className="text-xl text-gray-500" />
                    <span className="text-gray-500 text-sm">Sort</span>
                </div>

                <SortingDropDown />

                <div>
                    <TaskDialog />
                </div>
                {/* <Button className="rounded-md px-4" variant="outline" size="sm">New Deal</Button> */}
            </div>
        </div>
    );
}