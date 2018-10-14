import pandas as pd

CATEGORIES: pd.DataFrame = pd.DataFrame([
    [1, "Restaurants, cafe, fast food", "restaurant"],
    [2, "Chocolate, cookies, candy, ice cream", "chocolate"],
    [3, "Chips, snacks, nuts, fruit, gum, cereal, yogurt, soups", "chips"],
    [4, "Seasoning, condiments, ketchup", "seasoning"],
    [5, "Pet food", "petfood"],
    [6, "Alcohol", "alcohol"],
    [7, "Coffee, tea", "coffee"],
    [8, "Soda, juice, milk, energy drinks, water", "soda"],
    [9, "Cars, automobiles (car sales, auto parts, car insurance, car repair, gas, motor oil, etc.)", "cars"],
    [10, "Electronics (computers, laptops, tablets, cellphones, TVs, etc.)", "electronics"],
    [11, "Phone, TV and internet service providers", "phone_tv_internet_providers"],
    [12, "Financial services (banks, credit cards, investment firms, etc.)", "financial"],
    [13, "Education (universities, colleges, kindergarten, online degrees, etc.)", "education"],
    [14, "Security and safety services (anti-theft, safety courses, etc.)", "security"],
    [15, "Software (internet radio, streaming, job search website, grammar correction, travel planning, etc.)",
     "software"],
    [16, "Other services (dating, tax, legal, loan, religious, printing, catering, etc.)", "other_service"],
    [17, "Beauty products and cosmetics (deodorants, toothpaste, makeup, hair products, laser hair removal, etc.)",
     "beauty"],
    [18, "Healthcare and medications (hospitals, health insurance, allergy, cold remedy, home tests, vitamins)",
     "healthcare"],
    [19, "Clothing and accessories (jeans, shoes, eye glasses, handbags, watches, jewelry)", "clothing"],
    [20, "Baby products (baby food, sippy cups, diapers, etc.)", "baby"],
    [21, "Games and toys (including video and mobile games)", "game"],
    [22, "Cleaning products (detergents, fabric softeners, soap, tissues, paper towels, etc.)", "cleaning"],
    [23, "Home improvements and repairs (furniture, decoration, lawn care, plumbing, etc.)", "home_improvement"],
    [24, "Home appliances (coffee makers, dishwashers, cookware, vacuum cleaners, heaters, music players, etc.)",
     "home_appliance"],
    [25, "Vacation and travel (airlines, cruises, theme parks, hotels, travel agents, etc.)", "travel"],
    [26, "Media and arts (TV shows, movies, musicals, books, audio books, etc.)", "media"],
    [27, "Sports equipment and activities", "sports"],
    [28, "Shopping (department stores, drug stores, groceries, etc.)", "shopping"],
    [29, "Gambling (lotteries, casinos, etc.)", "gambling"],
    [30, "Environment, nature, pollution, wildlife", "environment"],
    [31, "Animal rights, animal abuse", "animal_right"],
    [32, "Human rights", "human_right"],
    [33, "Safety, safe driving, fire safety", "safety"],
    [34, "Smoking, alcohol abuse", "smoking_alcohol_abuse"],
    [35, "Domestic violence", "domestic_violence"],
    [36, "Self esteem, bullying, cyber bullying", "self_esteem"],
    [37, "Political candidates (support or opposition)", "political"],
    [38, "Charities", "charities"],
    [39, "Unclear", "unclear"]], columns=['label', 'description', 'text'])
