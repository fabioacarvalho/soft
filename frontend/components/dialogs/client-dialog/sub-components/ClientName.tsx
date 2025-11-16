import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";
import { FaCircleExclamation } from "react-icons/fa6";

export default function ClientName() {
    return (
        <div className="flex flex-col gap-2">
            <Label htmlFor="client-name" className="opacity-75 text-sm font-medium">
                Client Name
            </Label>
            <Input
                id="client-name"
                type="text"
                placeholder="Enter client name"
                required
                className="h-11"
            />

            <div className="text-red-500 text-[12px] flex items-center gap-1">
                <FaCircleExclamation />
                <span>Client field is required.</span>
            </div>
        </div>
    );
}