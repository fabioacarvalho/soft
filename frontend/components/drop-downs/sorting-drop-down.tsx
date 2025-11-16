'use client';

import * as React from 'react';

import { Button } from '../ui/button';
import {
    DropdownMenu,
    DropdownMenuCheckboxItem,
    DropdownMenuContent,
    DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu';

import { IoMdArrowDown } from 'react-icons/io';
import { IoMdArrowUp } from 'react-icons/io';

const options = ["A-Z", "Z-a"];

export default function SortingDropDown() {
    const [selectedOption, setSelectedOption] = React.useState<string>("A-Z");

    return (
        <DropdownMenu>
            <DropdownMenuTrigger asChild>
                <Button variant="ghost" className="rounded-md px-3 min-w-[80px] justify-between">
                    {selectedOption === "A-Z" ? <IoMdArrowDown /> : <IoMdArrowUp />}
                    <span className="text-sm">{selectedOption}</span>
                </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent className="w-40">
                {options.map((option) => (
                    <DropdownMenuCheckboxItem
                        key={option}
                        checked={selectedOption === option}
                        onCheckedChange={() => setSelectedOption(option)}
                    >
                        {option}
                    </DropdownMenuCheckboxItem>
                ))}
            </DropdownMenuContent>
        </DropdownMenu>
    );
}