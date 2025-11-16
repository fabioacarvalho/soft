import { Button } from '@/components/ui/button';
import { Label } from '@/components/ui/label';
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu';

import { IoIosArrowDown } from 'react-icons/io';
import { RiArrowDownDoubleFill } from 'react-icons/ri';
import { MdKeyboardDoubleArrowRight } from 'react-icons/md';
import { MdOutlineKeyboardDoubleArrowUp } from 'react-icons/md';
import { IconType } from 'react-icons/lib';
import { useState } from 'react';
import { IoMdCheckmark } from 'react-icons/io';

type ClientItem = {
    name: string;
    icon: IconType;
    textColor: string;
    backgroundColor: string;
};

const ClientItems: ClientItem[] = [
    {
        name: 'Low',
        icon: MdKeyboardDoubleArrowRight,
        textColor: 'text-green-700',
        backgroundColor: 'bg-green-100',
    },
    {
        name: 'Medium',
        icon: RiArrowDownDoubleFill,
        textColor: 'text-yellow-700',
        backgroundColor: 'bg-yellow-100',
    },
    {
        name: 'High',
        icon: MdOutlineKeyboardDoubleArrowUp,
        textColor: 'text-red-700',
        backgroundColor: 'bg-red-100',
    },
];

export default function ClientList() {
    const [selectedClient, setSelectedClient] = useState<ClientItem>(ClientItems[0]);

    function renderSelectedClient() {
        const Icon = selectedClient.icon;
        return (
            <div className="flex items-center gap-2">
                <div
                    className={`p-1 rounded-md items-center size-6 justify-center text-lg ${selectedClient.backgroundColor} ${selectedClient.textColor}`}
                >
                    <Icon />
                </div>
                <span>{selectedClient.name}</span>
                <IoIosArrowDown className="ml-2" />
            </div>
        );
    };


    return (
        <div>
            <Label className="opacity-75 text-sm font-medium mb-2">
                Client
            </Label>
            <DropdownMenu>
                <DropdownMenuTrigger asChild>
                    <Button
                        variant="outline"
                        className="w-full justify-start h-11"
                    >
                        {renderSelectedClient()}
                    </Button>
                </DropdownMenuTrigger>
                <DropdownMenuContent className="w-full">
                    {ClientItems.map((item) => {
                        const Icon = item.icon;
                        return (
                            <DropdownMenuItem
                                key={item.name}
                                onClick={() => setSelectedClient(item)}
                                className="flex items-center justify-between"
                            >
                                <div className="flex items-center gap-2">
                                    <div
                                        className={`p-1 rounded-md items-center size-6 justify-center text-lg ${item.backgroundColor} ${item.textColor}`}
                                    >
                                        <Icon />
                                    </div>
                                    <span>{item.name}</span>
                                </div>
                                {selectedClient.name === item.name && (
                                    <IoMdCheckmark className="text-green-600" />
                                )}
                            </DropdownMenuItem>
                        );
                    })}
                </DropdownMenuContent>
            </DropdownMenu>
        </div>
    );
}