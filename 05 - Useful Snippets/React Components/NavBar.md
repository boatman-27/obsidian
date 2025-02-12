```JSX
import { useState } from "react";
import { NavLink, useLocation } from "react-router-dom";
import { logout } from "../services/apiAccount";
import { useUser } from "../contexts/UserContext";
  
function Navbar() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const { accountStatus, user } = useUser();
  const location = useLocation();
  
  const handleToggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  const navLinks =
    user?.userrole === "student"
      ? [
          { to: "/quiz/previous-results", label: "Previous Sessions Results" },
          { to: "/account/edit-profile", label: "Account" },
          { to: "/chatbot", label: "Ask a Question" },
          { to: "/contact", label: "Contact Us" },
        ]
      : [{ to: "/admin/manage-site", label: "Manage Site" }];
  return (
    <nav className="border-gray-200 bg-white dark:bg-gray-900 w-full py-2">
      <div className="flex items-center justify-between px-4">
        {/* Logo Section */}
        <NavLink
          to="/"
          className="flex items-center space-x-3 rtl:space-x-reverse flex-shrink-0"
        >
          <img
            src="/maths2.png"
            className="h-10 w-auto sm:h-20"
            alt="Maths Logo"
          />
          <span className="self-center whitespace-nowrap text-md sm:text-2xl font-semibold dark:text-white">
            Practice your Maths Skills
          </span>
        </NavLink>

        {/* Toggle Menu Button */}
        <button
          data-collapse-toggle="navbar-default"
          type="button"
          className="inline-flex h-10 w-10 items-center justify-center rounded-lg p-2 text-sm text-gray-500 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 md:hidden dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
          aria-controls="navbar-default"
          aria-expanded={isMenuOpen}
          onClick={handleToggleMenu}
        >
          <span className="sr-only">Open main menu</span>
          <svg
            className="h-5 w-5"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 17 14"
          >
            <path
              stroke="currentColor"
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M1 1h15M1 7h15M1 13h15"
            />
          </svg>
        </button>

        {/* Navigation Links */}
        {accountStatus ? (
          <div
            className={`${
              isMenuOpen ? "block" : "hidden"
            } w-full md:block md:w-auto`}
            id="navbar-default"
          >
            <div className="flex items-center justify-between space-x-4">
              <ul className="flex flex-row flex-wrap space-x-4 font-medium rtl:space-x-reverse dark:text-white">
                {navLinks.map((link) => (
                  <li key={link.to}>
                    <NavLink
                      to={link.to}
                      className={`block px-3 py-2 text-gray-900 hover:text-custom-pink ${
                        location.pathname.includes(link.to)
                          ? "dark:text-custom-pink"
                          : "text-white"
                      }`}
                    >
                      {link.label}
                    </NavLink>
                  </li>
                ))}
              </ul>
              <button
                type="button"
                className="ml-4 rounded-lg bg-custom-pink px-4 py-2 text-white hover:bg-primary-800"
                onClick={logout}
              >
                Sign Out
              </button>
            </div>
          </div>
        ) : (
          <button
            type="button"
            className="ml-4 rounded-lg bg-custom-pink px-4 py-2 text-white hover:bg-primary-800"
          >
            <NavLink to="/account/login">Sign In</NavLink>
          </button>
        )}
      </div>
    </nav>
  );
}
export default Navbar;
```