'use client';

import { Label } from "@radix-ui/react-dropdown-menu";
import { Textarea } from "@/components/ui/textarea";
import { FaCircleExclamation } from "react-icons/fa6";
import { ChangeEvent, useState } from "react";

export default function TaskDescription() {

    const [textCounter, setTextCounter] = useState(0);
    
    function handleTextChange(event: ChangeEvent<HTMLTextAreaElement>) {
        const inputText = event.target.value;
        if (inputText.length > 200) {
            return; // Prevent input if it exceeds 200 characters
        }
        setTextCounter(inputText.length);
    }

    return (
        <div className="flex flex-col gap-2 mt-4">
            <Label className="opacity-75 text-sm font-medium">
                Task Description
            </Label>
            <Textarea
                id="task-description"
                placeholder="Enter task description"
                className="resize-none"
                value={textCounter}
                onChange={handleTextChange}
            />

            <div className="flex justify-between items-center">
                <div className="text-red-500 text-[12px] flex items-center gap-1">
                    <FaCircleExclamation />
                    <span>Task description is recommended.</span>
                </div>
                <div className="text-sm text-gray-500">
                    {textCounter}/200 Caracters
                </div>
            </div>

        </div>
    );
}