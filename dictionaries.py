monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    6: "June"
}

print(monthConversions["Feb"])
print(monthConversions.get("Luv", "Not a valid Key"))
print(monthConversions.get(6))
