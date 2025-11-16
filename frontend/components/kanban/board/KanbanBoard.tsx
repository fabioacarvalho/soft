import SingleBoard from './SingleBoard';
import { Board } from "@/types/board";


export default function KanbanBoard() {
    const boards: Board[] = [
        { name: 'To-Do', createdAt: new Date(), updatedAt: new Date(), tasks: ['a', 'b'] },
        { name: 'In Progress', createdAt: new Date(), updatedAt: new Date(), tasks: ['a',] },
        { name: 'Waiting', createdAt: new Date(), updatedAt: new Date(), tasks: ['a', 'b'] },
        { name: 'Done', createdAt: new Date(), updatedAt: new Date(), tasks: ['a', 'b', 'c'] },
    ];
    return (
        <div className="h-full rounded-2-xl flex mt-4 gap-3 ">
            {boards.map((board, index) => (
                <SingleBoard key={index} board={board} />
            ))}
        </div>
    );
}