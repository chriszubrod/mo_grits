CREATE DATABASE mogrits;

USE mogrits;

CREATE TABLE period (
	id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
	name VARCHAR(20) NOT NULL,
	description VARCHAR(255) NOT NULL
)

INSERT INTO period (name, description)
VALUES ('breakfast', 'Meal period between 7AM and 11AM');
INSERT INTO period (name, description)
VALUES ('lunch', 'Meal period between 11AM and 3PM.');
INSERT INTO period (name, description)
VALUES ('dinner', 'Meal period between 3PM and 10PM.');
INSERT INTO period (name, description)
VALUES ('bar', 'Drinks prepared for any meal period.');

SELECT * FROM period;

CREATE TABLE menu (
	id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
	period_id INT NOT NULL,
	name VARCHAR(1000) NOT NULL,
	description VARCHAR(1000) NOT NULL,
	price DECIMAL(18,2) NOT NULL
)

INSERT INTO menu (period_id, name, description, price)
VALUES (1, 'Waffle Grits', 'Perfect start to your morning with Waffle Grits with your choice of Bacon and Cheddar, Jalapeno and Monterey Jack Cheese or Gruyere and Ham.', 7.00);
INSERT INTO menu (period_id, name, description, price)
VALUES (1, 'Grits Cakes with Poached Eggs and Country Gravy', 'Prepared with the paring knife, round cookie cutter and a pizza wheel...you will not want to miss the excitement of this presentation.', 7.00);
INSERT INTO menu (period_id, name, description, price)
VALUES (1, 'Buttermilk Grits with Pear-Granola', 'A sweet start to your day with a rich buttermilk flavor topped with pear-granola.', 7.00);
INSERT INTO menu (period_id, name, description, price)
VALUES (1, 'Bacon-and-Cheddar Grits Quiche', 'Try with cheese to the edges of a warm, bacony grits crusted quiche.', 7.00);
INSERT INTO menu (period_id, name, description, price)
VALUES (1, 'Blackberry-Yogurt Grits', 'Sweet and savory buttermilk grits topped with blackberry jam, blackberries, toasted almonds and a honey drizzle.', 7.00);
INSERT INTO menu (period_id, name, description, price)
VALUES (1, 'Hatch Chile Grits Breakfast Bowl', 'Creamy grits topped with a fried egg, and a chile spice.', 7.00);

INSERT INTO menu (period_id, name, description, price)
VALUES (2, 'Cheesy Grits-and-Ale Soup', 'Rich and hearty beer-cheese soup, with stone-ground grits. Topped with sharp Cheddar cheese and Garlic Pumpernickel Croutons. Pairs well with a brown ale from Newcastle or Sierra Nevada.', 10.00);
INSERT INTO menu (period_id, name, description, price)
VALUES (2, 'Chicken Chili Pot Pie', 'Poblano chiles and butternut squash topped with puffed, cheesy grits.', 10.00);
INSERT INTO menu (period_id, name, description, price)
VALUES (2, 'Smoked Gouda and Andouille Grits', 'A little more Cajun, prepared with Andouille sausage and rich smoked Gouda.', 10.00);
INSERT INTO menu (period_id, name, description, price)
VALUES (2, 'Creamy Parmesan Grits', 'Parmigiano-Reggiano cheese, adding a nutty flavor and an earthy depth.', 10.00);
INSERT INTO menu (period_id, name, description, price)
VALUES (2, 'Cheese Grits and Roasted Tomatoes', 'Versatile roasted tomatoes, paired with a salad and shaved grilled filet.', 10.00);

INSERT INTO menu (period_id, name, description, price)
VALUES (3, 'Italian-Style Grits and Greens with Pulled Pork and Mushrooms', 'Creamy grits and greens with pulled port and garlicky sauteed mushrooms.', 15.00);
INSERT INTO menu (period_id, name, description, price)
VALUES (3, 'Pan-Seared Shrimp with Chive Grits and Salsa Verde', 'A lowcounty classis with fresh shrimp and creamy, yellow stoneground grits.', 15.00);
INSERT INTO menu (period_id, name, description, price)
VALUES (3, 'Caramelized Onion and Pancetta Grits', 'You do not want to miss this pairing of Caramelized Onion and the Italian Pancetta.', 15.00);
INSERT INTO menu (period_id, name, description, price)
VALUES (3, 'Company Pot Roast with Creamy Muchroom Grits', 'Bacon, garlic and red wine imbue humble chuck roast over creamy muchroom grits.', 15.00);
INSERT INTO menu (period_id, name, description, price)
VALUES (3, 'Country Ham and Gouda Grit Cakes with Tomato Gravy', 'Grit cakes are browned in a skillet and topped with country ham and tomato gravy slow prepared overnight.', 15.00);
INSERT INTO menu (period_id, name, description, price)
VALUES (3, 'Pimiento Cheese and Brisket Grits', 'Sliced brisket and mixed with fresh pimiento cheese.', 15.00);

INSERT INTO menu (period_id, name, description, price)
VALUES (4, 'The Hurricane', 'One of New Orleans most famous cocktails.', 3.00);
INSERT INTO menu (period_id, name, description, price)
VALUES (4, 'Pimms Cup', 'In the 1940s, owner of the Napoleon House in the French Quarter created this New Orleans staple.', 3.00);
INSERT INTO menu (period_id, name, description, price)
VALUES (4, 'Ramos Gin Fizz', 'Invented by Henry C. Ramos in 1888, and made famous by The Roosevelt Hotel.', 3.00);
INSERT INTO menu (period_id, name, description, price)
VALUES (4, 'New Orleans Daiquiri', 'Classic Cuban cocktail with a Creole twist.', 3.00);
INSERT INTO menu (period_id, name, description, price)
VALUES (4, '2015 Truchard Chardonnay', 'Napa Valley, CA', 3.00);
INSERT INTO menu (period_id, name, description, price)
VALUES (4, '2013 Melville Viognier', 'Santa Barbara County, CA', 3.00);
INSERT INTO menu (period_id, name, description, price)
VALUES (4, 'Rose City Red Ale', 'Alameda Brewhouse, Portland, OR', 3.00);
INSERT INTO menu (period_id, name, description, price)
VALUES (4, 'Cream Ale', 'Anderson Craft Ales, London, ON', 3.00);
INSERT INTO menu (period_id, name, description, price)
VALUES (4, 'Burly Goat Doppelbock', 'Granville Island Brewing, Vancouver, BC', 3.00);
INSERT INTO menu (period_id, name, description, price)
VALUES (4, '4 Mile Pale Ale', '4 Mile Brewing Company, Victoria, BC', 3.00);
INSERT INTO menu (period_id, name, description, price)
VALUES (4, 'Class V', 'Whitewater Brewing Company, Ottawa, ON', 3.00);

SELECT * FROM menu;