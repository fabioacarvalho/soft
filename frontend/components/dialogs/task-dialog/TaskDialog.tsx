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
import TaskName from './sub-components/TaskName';
import TaskDescription from './sub-components/TaskDescription';
import ClientList from './sub-components/ClientList';
import PriorityList from './sub-components/PriorityList';

export default function TaskDialog() {
    return (
        <Dialog>
            <DialogTrigger asChild>
                <Button variant="outline" className="w-full justify-start">
                    <BiTask className="mr-2" />
                    Add Task
                </Button>
            </DialogTrigger>
            <DialogContent className="sm:max-w-lg">
                <DialogHeader>
                    <DialogTitle>Add New Task</DialogTitle>
                    <DialogDescription>
                        Fill in the details below to create a new task.
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
                    <Button>Create Task</Button>
                </div>
            </DialogContent>
        </Dialog>
    );
}
