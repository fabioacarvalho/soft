import { useTheme } from "next-themes";

export default function Searchbar() {
    const { theme } = useTheme();
    
    const bgColor = theme === 'dark' ? 'bg-transparent' : 'bg-white';
    return (
        <div className="w-full max-w-md mx-auto">
            <input
                type="text"
                placeholder="Search..."
                className={`${bgColor} w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500`}
            />
        </div>
    )
}