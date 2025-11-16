import { Separator } from "@radix-ui/react-separator";

type TaskCard = {
    label: string;
    value: number;
}

export default function TasksStats() {
    const statisticCards: TaskCard[] = [
        { label: "total", value: 128 },
        { label: "in progress", value: 64 },
        { label: "done", value: 32 },
    ];
    return (
        <div className="flex flex-col gap2">
            <span className="font-bold text-xl">Tasks</span>

            <div className="grid grid-cols-2 gap-3 mt-3">
                {statisticCards.map((statCard, index) => (
                    <SingleCard key={index} statCard={statCard} />
                ))}
            </div>
        </div>
    );
}

function SingleCard({ statCard }: { statCard: TaskCard }) {
    return (
        <div className="p-3 bg-gray-100 rounded-xl">
            <span className="text-gray-600 text-[12px]">
                {statCard.label.toUpperCase()}
            </span>

            <div className="flex gap-2 mt-1 items-center">
                <Separator orientation="vertical" className="w-1 h-4 bg-primary" />
                <span className="font-bold text-lg">{statCard.value}</span>
            </div>
        </div>
    );
}