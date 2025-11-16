'use client';
import { CheckIcon, ChevronsUpDownIcon } from "lucide-react"
 
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import {
  Command,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
} from "@/components/ui/command"
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"

import {
  Card,
  CardAction,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { useState } from "react";
import { DarkModeButton } from "@/components/DarkModeButton";

const companys = [
  {
    value: "denso",
    label: "Denso do Brasil",
  },
  {
    value: "banco_do_brasil",
    label: "Banco do Brasil",
  },
  {
    value: "brunander",
    label: "Banco Brunander",
  },
  {
    value: "remix",
    label: "Remix",
  },
  {
    value: "astro",
    label: "Astro",
  },
]

export default function LoginPage() {
  const [open, setOpen] = useState(false)
  const [value, setValue] = useState("")

  return (
    <div className="min-h-screen flex items-center justify-center">
      <div className="fixed top-4 right-4 px-4 py-2 ">
        <DarkModeButton />
      </div>
      <Card className="w-full max-w-xl">
        <CardHeader>
          <CardTitle>Login to your account</CardTitle>
          <CardDescription>
            Enter your email below to login to your account
          </CardDescription>
          <CardAction>
            <Button variant="link">Sign Up</Button>
          </CardAction>
        </CardHeader>
        <CardContent>
          <form>
            <div className="flex flex-col gap-6">
              <div className="grid gap-2">
                <Label htmlFor="company">Company</Label>
                <Popover open={open} onOpenChange={setOpen}>
                  <PopoverTrigger asChild>
                    <Button
                      variant="outline"
                      role="combobox"
                      aria-expanded={open}
                      className="justify-between"
                    >
                      {value
                        ? companys.find((company) => company.value === value)?.label
                        : "Select company..."}
                      <ChevronsUpDownIcon className="ml-2 h-4 w-4 shrink-0 opacity-50" />
                    </Button>
                  </PopoverTrigger>
                  <PopoverContent className=" p-0">
                    <Command>
                      <CommandInput placeholder="Search framework..." />
                      <CommandList>
                        <CommandEmpty>No Company found.</CommandEmpty>
                        <CommandGroup>
                          {companys.map((company) => (
                            <CommandItem
                              key={company.value}
                              value={company.value}
                              onSelect={(currentValue) => {
                                setValue(currentValue === value ? "" : currentValue)
                                setOpen(false)
                              }}
                            >
                              <CheckIcon
                                className={cn(
                                  "mr-2 h-4 w-4",
                                  value === company.value ? "opacity-100" : "opacity-0"
                                )}
                              />
                              {company.label}
                            </CommandItem>
                          ))}
                        </CommandGroup>
                      </CommandList>
                    </Command>
                  </PopoverContent>
                </Popover>
              </div>
              <div className="grid gap-2">
                <Label htmlFor="email">Email</Label>
                <Input
                  id="email"
                  type="email"
                  placeholder="m@example.com"
                  required
                />
              </div>
              <div className="grid gap-2">
                <div className="flex items-center">
                  <Label htmlFor="password">Password</Label>
                  <a
                    href="#"
                    className="ml-auto inline-block text-sm underline-offset-4 hover:underline"
                  >
                    Forgot your password?
                  </a>
                </div>
                <Input id="password" type="password" required />
              </div>
            </div>
          </form>
        </CardContent>
        <CardFooter className="flex-col gap-2">
          <Button type="submit" className="w-full">
            Login
          </Button>
          <Button variant="outline" className="w-full">
            Login with Google
          </Button>
        </CardFooter>
      </Card>
    </div>

    // <div className="min-h-screen flex items-center justify-center">
    //   <div className="bg-white p-8 rounded-lg shadow-md w-full max-w-md">
    //     <h2 className="text-2xl font-semibold mb-6 text-center">Login</h2>

    //     {error && (
    //       <p className="text-red-500 text-sm mb-4 text-center">{error}</p>
    //     )}

    //     <form onSubmit={handleSubmit} className="flex flex-col space-y-4">
    //       <input
    //         type="email"
    //         placeholder="Email"
    //         value={email}
    //         onChange={(e) => setEmail(e.target.value)}
    //         className="border rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
    //       />
    //       <input
    //         type="password"
    //         placeholder="Password"
    //         value={password}
    //         onChange={(e) => setPassword(e.target.value)}
    //         className="border rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
    //       />

    //       <div className="flex justify-between mt-4">
    //         <button
    //           type="button"
    //           onClick={handleCancel}
    //           className="bg-gray-300 text-gray-700 px-4 py-2 rounded-lg hover:bg-gray-400"
    //         >
    //           Cadastrar
    //         </button>
    //         <button
    //           type="submit"
    //           className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
    //         >
    //           Login
    //         </button>
    //       </div>

    //       <div className="flex justify-between mt-4">
    //         <span className='text-sm text-muted-foreground'>
    //           Use o e-mail: <strong>carlosmotta@example.com</strong> e a senha: <strong>admin</strong> para acessar, ou, faça o cadastro de novo usuário.
    //         </span>
    //       </div>
    //     </form>
    //   </div>
    // </div>
  );
}