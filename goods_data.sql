#
# TABLE STRUCTURE FOR: goods
#

DROP TABLE IF EXISTS `goods`;

CREATE TABLE `goods` (
  `GId` int(8) NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `Cost` float NOT NULL,
  PRIMARY KEY (`GId`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;

INSERT INTO goods (GId, Name, Cost) VALUES 
(1, 'Butter', '14.33'),
(2, 'Salad', '11.97'),
(3, 'Pizza', '13.66'),
(4, 'Burger', '4.54'),
(5, 'Hotdog', '7.47'),
(6, 'Smoked salmon', '2.18'),
(7, 'French Fries', '1.85'),
(8, 'Waffle', '3.04'),
(9, 'Ice cream', '14.21'),
(10, 'Pancake', '11.89'),
(11, 'Pie', '6.09'),
(12, 'Cheese', '2.49'),
(13, 'Pasta', '12.82'),
(14, 'Donuts', '4.34'),
(15, 'Tuna', '6.1'),
(16, 'Egg', '8.11'),
(17, 'Sandwich', '8.03'),
(18, 'Honey', '4.93'),
(19, 'Mayonnaise', '14.02'),
(20, 'Noodles', '10.76'),
(21, 'Meatball', '15.2'),
(22, 'Milk', '15.32'),
(23, 'Bread', '4.45'),
(24, 'Yogurt', '9.26'),
(25, 'Chocolate', '1.83'),
(26, 'Dosa', '7.74'),
(27, 'Bacon', '6.22'),
(28, 'Biryani', '8.25'),
(29, 'Taco', '2.05'),
(30, 'Grilled chicken', '1.62');


