'use client';

import { FaRegEdit } from "react-icons/fa";
import { MdOutlineDelete } from "react-icons/md";

import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuSeparator,
    DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";

import { Button } from "../ui/button";
import { MoreHorizontal } from "lucide-react";
import { JSX } from "react";

type MenuItem = {
    icon: JSX.Element;
    label: string;
    className: string;
    separator?: undefined;
};

export default function TasksDropDown() {
    const menuItems: MenuItem[] = [
        {
            icon: <FaRegEdit className="size-4" />,
            label: "Edit Task",
            className: "",
        },
        {
            icon: <MdOutlineDelete className="size-4" />,
            label: "Delete Task",
            className: "text-red-600",
        },
    ]
    return (
        <div>
            <DropdownMenu>
                <DropdownMenuTrigger asChild>
                    <Button variant="ghost" className="h-8 w-8 p-0">
                        <MoreHorizontal className="h-4 w-4" />
                    </Button>
                </DropdownMenuTrigger>
                <DropdownMenuContent className="poppins">
                    {menuItems.map((item, index) => (
                        <div key={index}>
                            <DropdownMenuItem className={`flex items-center gap-1 p-1[10px] ${item.className}`}>
                                {item.icon}
                                <span>{item.label}</span>
                            </DropdownMenuItem>
                            {item.separator && <DropdownMenuSeparator key={index} />}
                        </div>
                    ))}
                </DropdownMenuContent>
            </DropdownMenu>
        </div>
    );
}