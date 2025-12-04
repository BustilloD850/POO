-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 03-12-2025 a las 17:28:04
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_cochecitos`
--
CREATE DATABASE IF NOT EXISTS `bd_cochecitos` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `bd_cochecitos`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `camiones`
--

CREATE TABLE `camiones` (
  `id_camion` int(100) NOT NULL,
  `marca` varchar(100) NOT NULL,
  `color` varchar(100) NOT NULL,
  `modelo` varchar(100) NOT NULL,
  `velocidad` int(100) NOT NULL,
  `caballaje` int(100) NOT NULL,
  `plazas` int(100) NOT NULL,
  `eje` int(100) NOT NULL,
  `capacidadCarga` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `camiones`
--

INSERT INTO `camiones` (`id_camion`, `marca`, `color`, `modelo`, `velocidad`, `caballaje`, `plazas`, `eje`, `capacidadCarga`) VALUES
(1, 'MERCEDES-BENZ', 'BLANCO', '1970', 130, 400, 24, 2, 2500),
(2, 'INTERNATIONAL', 'BLANCO', '2005', 190, 400, 2, 1, 4000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `camionetas`
--

CREATE TABLE `camionetas` (
  `id_camionetas` int(100) NOT NULL,
  `marca` varchar(100) NOT NULL,
  `color` varchar(100) NOT NULL,
  `modelo` varchar(100) NOT NULL,
  `velocidad` int(100) NOT NULL,
  `caballaje` int(100) NOT NULL,
  `plazas` int(100) NOT NULL,
  `traccion` varchar(100) NOT NULL,
  `cerrada` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `camionetas`
--

INSERT INTO `camionetas` (`id_camionetas`, `marca`, `color`, `modelo`, `velocidad`, `caballaje`, `plazas`, `traccion`, `cerrada`) VALUES
(1, 'RENAULT', 'VERDE', '2020', 190, 120, 5, 'TRASERA', 0),
(2, 'VOLKSWAGEN', 'AZUL', '2020', 220, 290, 5, 'TRASERA', 0),
(3, 'LAMBORGHINI', 'AMARILLO', '2019', 260, 340, 5, 'TRASERA', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `coches`
--

CREATE TABLE `coches` (
  `id` int(100) NOT NULL,
  `marca` varchar(100) NOT NULL,
  `color` varchar(100) NOT NULL,
  `modelo` varchar(100) NOT NULL,
  `velocidad` int(100) NOT NULL,
  `caballaje` int(100) NOT NULL,
  `plazas` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `coches`
--

INSERT INTO `coches` (`id`, `marca`, `color`, `modelo`, `velocidad`, `caballaje`, `plazas`) VALUES
(2, 'MAZDA', 'NEGRO', '2015', 250, 190, 2),
(4, 'LAMBORGHINI', 'NARANJA', '2011', 336, 340, 2);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `camiones`
--
ALTER TABLE `camiones`
  ADD PRIMARY KEY (`id_camion`);

--
-- Indices de la tabla `camionetas`
--
ALTER TABLE `camionetas`
  ADD PRIMARY KEY (`id_camionetas`);

--
-- Indices de la tabla `coches`
--
ALTER TABLE `coches`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `camiones`
--
ALTER TABLE `camiones`
  MODIFY `id_camion` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `camionetas`
--
ALTER TABLE `camionetas`
  MODIFY `id_camionetas` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `coches`
--
ALTER TABLE `coches`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
