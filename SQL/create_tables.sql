#
# TABLE STRUCTURE FOR: users
#

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `UId` int(8) NOT NULL AUTO_INCREMENT,
  `Email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Password` char(64) COLLATE utf8mb4_unicode_ci NOT NULL,
  `UserType` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `LastName` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `FirstName` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `IsDriving` tinyint(1) DEFAULT 0,
  PRIMARY KEY (`UId`),
  UNIQUE KEY `Uniq_Email` (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# TABLE STRUCTURE FOR: goods
#

DROP TABLE IF EXISTS `goods`;

CREATE TABLE `goods` (
  `GId` int(8) NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Cost` float NOT NULL,
  PRIMARY KEY (`GId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# TABLE STRUCTURE FOR: deliveries
#

DROP TABLE IF EXISTS `deliveries`;

CREATE TABLE `deliveries` (
  `DId` int(8) NOT NULL AUTO_INCREMENT,
  `CustomerId` int(8) NOT NULL,
  `DriverId` int(8) DEFAULT NULL,
  `Status` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `PickupLocation` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `DropLocation` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `PlacedTime` datetime DEFAULT current_timestamp(),
  `PickupTime` datetime DEFAULT NULL,
  `DropoffTime` datetime DEFAULT NULL,
  `Rating` int(1) DEFAULT NULL,
  PRIMARY KEY (`DId`),
  KEY `fk_customer` (`CustomerId`),
  KEY `fk_driver` (`DriverId`),
  CONSTRAINT `fk_customer` FOREIGN KEY (`CustomerId`) REFERENCES `users` (`UId`),
  CONSTRAINT `fk_driver` FOREIGN KEY (`DriverId`) REFERENCES `users` (`UId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# TABLE STRUCTURE FOR: deliveryItems
#

DROP TABLE IF EXISTS `deliveryItems`;

CREATE TABLE `deliveryItems` (
  `DId` int(8) NOT NULL,
  `GId` int(8) NOT NULL,
  `Quantity` int(3) NOT NULL,
  PRIMARY KEY (`DId`,`GId`),
  KEY `fk_good` (`GId`),
  CONSTRAINT `fk_delivery` FOREIGN KEY (`DId`) REFERENCES `deliveries` (`DId`),
  CONSTRAINT `fk_good` FOREIGN KEY (`GId`) REFERENCES `goods` (`GId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;