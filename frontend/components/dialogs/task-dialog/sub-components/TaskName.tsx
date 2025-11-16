import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";
import { FaCircleExclamation } from "react-icons/fa6";

export default function TaskName() {
    return (
        <div className="flex flex-col gap-2">
            <Label htmlFor="task-name" className="opacity-75 text-sm font-medium">
                Task Name
            </Label>
            <Input
                id="task-name"
                type="text"
                placeholder="Enter task name"
                required
                className="h-11"
            />

            <div className="text-red-500 text-[12px] flex items-center gap-1">
                <FaCircleExclamation />
                <span>Task field is required.</span>
            </div>
        </div>
    );
}