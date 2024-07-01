-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 01 Tem 2024, 15:04:54
-- Sunucu sürümü: 10.4.32-MariaDB
-- PHP Sürümü: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `srntodolistdb`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `logs`
--

CREATE TABLE `logs` (
  `Id` int(11) NOT NULL,
  `LogMessage` text NOT NULL,
  `LogDate` datetime NOT NULL,
  `UserID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `tasklist`
--

CREATE TABLE `tasklist` (
  `Id` int(11) NOT NULL,
  `ListName` varchar(32) NOT NULL,
  `CreatedDate` date NOT NULL,
  `UserID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `tasks`
--

CREATE TABLE `tasks` (
  `Id` int(11) NOT NULL,
  `TaskName` varchar(32) NOT NULL,
  `Status` int(11) NOT NULL,
  `CompletedDate` date DEFAULT NULL,
  `ListID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `users`
--

CREATE TABLE `users` (
  `Id` int(11) NOT NULL,
  `Number` varchar(11) NOT NULL,
  `Username` varchar(32) NOT NULL,
  `Password` varchar(200) NOT NULL,
  `Name` varchar(32) NOT NULL,
  `Surname` varchar(32) NOT NULL,
  `CreatedDate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `logs`
--
ALTER TABLE `logs`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `LogTypeID` (`UserID`);

--
-- Tablo için indeksler `tasklist`
--
ALTER TABLE `tasklist`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `UserID` (`UserID`);

--
-- Tablo için indeksler `tasks`
--
ALTER TABLE `tasks`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `ListID` (`ListID`);

--
-- Tablo için indeksler `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`Id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `logs`
--
ALTER TABLE `logs`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=225;

--
-- Tablo için AUTO_INCREMENT değeri `tasklist`
--
ALTER TABLE `tasklist`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=89;

--
-- Tablo için AUTO_INCREMENT değeri `tasks`
--
ALTER TABLE `tasks`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=289;

--
-- Tablo için AUTO_INCREMENT değeri `users`
--
ALTER TABLE `users`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- Dökümü yapılmış tablolar için kısıtlamalar
--

--
-- Tablo kısıtlamaları `logs`
--
ALTER TABLE `logs`
  ADD CONSTRAINT `logs_ibfk_2` FOREIGN KEY (`UserID`) REFERENCES `users` (`Id`);

--
-- Tablo kısıtlamaları `tasklist`
--
ALTER TABLE `tasklist`
  ADD CONSTRAINT `tasklist_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `users` (`Id`);

--
-- Tablo kısıtlamaları `tasks`
--
ALTER TABLE `tasks`
  ADD CONSTRAINT `tasks_ibfk_1` FOREIGN KEY (`ListID`) REFERENCES `tasklist` (`Id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
