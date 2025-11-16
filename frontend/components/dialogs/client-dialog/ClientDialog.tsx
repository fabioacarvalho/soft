import { Button } from '@/components/ui/button';
import {
    Dialog,
    DialogContent,
    DialogDescription,
    DialogHeader,
    DialogTitle,
    DialogTrigger,
} from '@/components/ui/dialog';

import { Separator } from '@radix-ui/react-separator';

import { BiTask } from 'react-icons/bi';
import TaskName from './sub-components/ClientName';
import TaskDescription from './sub-components/ClientDescription';
import ClientList from './sub-components/ClientList';
import PriorityList from './sub-components/PriorityList';
import { FaBuildingUser } from "react-icons/fa6";


export default function ClientDialog() {
    return (
        <Dialog>
            <DialogTrigger asChild>
                <Button variant="outline" className="w-full justify-start">
                    <FaBuildingUser className="mr-2" />
                    Add Client
                </Button>
            </DialogTrigger>
            <DialogContent className="sm:max-w-lg">
                <DialogHeader>
                    <DialogTitle>Add New Client</DialogTitle>
                    <DialogDescription>
                        Fill in the details below to create a new Client.
                    </DialogDescription>
                </DialogHeader>

                <div className="flex flex-col gap-4 mt-4">
                    <TaskName />
                    <TaskDescription />
                    <ClientList />
                    <PriorityList />
                </div>

                <Separator className="my-4" />

                <div className="flex justify-end">
                    <Button>Create Client</Button>
                </div>
            </DialogContent>
        </Dialog>
    );
}
