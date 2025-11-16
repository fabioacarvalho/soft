"use client";

import { Button } from "@/components/ui/button"
import { Separator } from "@/components/ui/separator"
import Searchbar from "./Searchbar";
import { DarkModeButton } from "@/components/DarkModeButton";

export default function Navbar() {
    return (
        <nav className="poppins p-4 flex justify-between items-center">
            
            <div className="flex items-center gap-16">
                <Searchbar />
            </div>
            <div className="flex items-center gap-5">
                <DarkModeButton />
                <Separator orientation="vertical" className="h-6" />
                <Button variant="outline" className="rounded-3-md h-10">New Deal</Button>
            </div>
        </nav>
    )
}