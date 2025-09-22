import {User, Settings, LogOut, Bell, Search, Menu} from "lucide-react";  
import {NavLink} from "react-router-dom";  
  
import {Avatar, AvatarFallback, AvatarImage} from "@/components/ui/avatar";  
import {  
    DropdownMenu,  
    DropdownMenuContent,  
    DropdownMenuItem,  
    DropdownMenuLabel,  
    DropdownMenuSeparator,  
    DropdownMenuTrigger  
} from "@/components/ui/dropdown-menu";  
import {Button} from "@/components/ui/button";  
import {UseUser} from "@/Context/UserContext.tsx";  
import {Loader} from "@/components/Loader.tsx";  
  
interface TopNavbarProps {  
    onMenuClick: () => void;  
}  
  
export function TopNavbar({onMenuClick}: TopNavbarProps) {  
    const {state, dispatch} = UseUser()  
    const {user, isAuthenticated, isLoading} = state  
  
    if (isLoading) {  
        return <Loader />  
    }  
  
  
    return (  
        <header className="h-16 bg-background border-b border-border px-4 md:px-6 flex items-center justify-between">  
            <Button  
                variant="ghost"  
                size="icon"  
                onClick={onMenuClick}  
                className="md:hidden"  
            >  
                <Menu className="w-5 h-5" />  
            </Button>  
            <div className="hidden md:flex items-center justify-center flex-1">  
                <h1 className="text-lg font-semibold text-foreground">  
                    Penguin Facts API Dashboard  
                </h1>  
            </div>  
  
  
            {/* Right section - Auth & User */}  
            <div className="flex items-center space-x-2 md:space-x-4 flex-1 justify-end">  
                {/* Notifications */}  
                {isAuthenticated && (  
                    <Button variant="ghost" size="icon" className="relative">  
                        <Bell className="w-5 h-5"/>  
                        <span className="absolute -top-1 -right-1 w-2 h-2 bg-destructive rounded-full"></span>  
                    </Button>  
                )}  
  
                {/* Auth section */}  
                {!isAuthenticated ? (  
                    <div className="flex items-center space-x-1 md:space-x-2">  
                        <NavLink to="/login">  
                            <Button  
                                variant="ghost"  
                                className="text-muted-foreground hover:text-foreground"  
                            >  
                                Log In  
                            </Button>  
                        </NavLink>  
  
                        <NavLink to="/register">  
                            <Button  
                                className="bg-gradient-arctic hover:opacity-90 text-primary border-0"  
                                size="sm"  
                            >  
                                Sign Up  
                            </Button>  
                        </NavLink>  
                    </div>  
                ) : (  
                    <DropdownMenu>  
                        <DropdownMenuTrigger asChild>  
                            <Button variant="ghost" className="relative h-8 w-8 rounded-full">  
                                <Avatar className="h-8 w-8 ring-2 ring-arctic/20">  
                                    {/*<AvatarImage src={user.avatar} alt={user.name}/>*/}  
                                    <AvatarFallback className="bg-gradient-arctic text-primary font-medium">  
                                        {user.firstName[0].charAt(0).toUpperCase()}{user.lastName[0].charAt(0).toUpperCase()}  
                                    </AvatarFallback>  
                                </Avatar>  
                            </Button>  
                        </DropdownMenuTrigger>  
                        <DropdownMenuContent className="w-56" align="end" forceMount>  
                            <DropdownMenuLabel className="font-normal">  
                                <div className="flex flex-col space-y-1">  
                                    <p className="text-sm font-medium leading-none">{user.firstName}</p>  
                                    <p className="text-xs leading-none text-muted-foreground">  
                                        {user.email}  
                                    </p>  
                                </div>  
                            </DropdownMenuLabel>  
                            <DropdownMenuSeparator/>                            <DropdownMenuItem>                                <User className="mr-2 h-4 w-4"/>  
                                <span>Profile</span>  
                            </DropdownMenuItem>  
                            <DropdownMenuItem>                                <Settings className="mr-2 h-4 w-4"/>  
                                <span>Settings</span>  
                            </DropdownMenuItem>  
                            <DropdownMenuSeparator/>                            <DropdownMenuItem onClick={() => {}}>  
                                <LogOut className="mr-2 h-4 w-4"/>  
                                <span>Log out</span>  
                            </DropdownMenuItem>  
                        </DropdownMenuContent>  
                    </DropdownMenu>  
                )}  
            </div>  
        </header>  
    );  
}