-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 16-10-2021 a las 16:58:20
-- Versión del servidor: 10.4.20-MariaDB
-- Versión de PHP: 8.0.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_prediccion`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `animales`
--

CREATE TABLE `animales` (
  `Id_animal` int(11) NOT NULL,
  `Nombre_animal` char(50) NOT NULL,
  `Id_tipo_animal` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `animales`
--

INSERT INTO `animales` (`Id_animal`, `Nombre_animal`, `Id_tipo_animal`) VALUES
(1, 'Gato', 1),
(2, 'Tigre', 1),
(3, 'Cocodrilo', 2),
(4, 'Hormiga', 3),
(5, 'Lobo', 4),
(6, 'Leon', 1),
(7, 'Cucaracha', 3),
(8, 'Betta', 5),
(9, 'Rata', 6),
(10, 'Mono', 7),
(11, 'Gorila', 7);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `caracteristicas`
--

CREATE TABLE `caracteristicas` (
  `Id_caracteristica` int(11) NOT NULL,
  `Nombre_caracteristica` char(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `caracteristicas`
--

INSERT INTO `caracteristicas` (`Id_caracteristica`, `Nombre_caracteristica`) VALUES
(1, 'Pequeño'),
(2, 'Domestico'),
(3, 'Peligroso'),
(4, 'Grande'),
(5, 'Lindo'),
(6, 'Tranquilo'),
(7, 'Verde'),
(8, 'Carnivoro'),
(9, 'Nocturno'),
(10, 'Independiente'),
(11, 'Fuerte'),
(12, 'Feo'),
(13, 'Agresivo'),
(14, 'Trabajador'),
(15, 'Jugueton'),
(16, 'Agil'),
(17, 'Blanco');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `caracteristicas_animales`
--

CREATE TABLE `caracteristicas_animales` (
  `Id_caracteristica_animal` int(11) NOT NULL,
  `Id_animal` int(11) NOT NULL,
  `Id_caracteristica` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `caracteristicas_animales`
--

INSERT INTO `caracteristicas_animales` (`Id_caracteristica_animal`, `Id_animal`, `Id_caracteristica`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 2, 3),
(4, 3, 4),
(5, 3, 3),
(6, 1, 5),
(7, 1, 6),
(8, 4, 1),
(9, 2, 4),
(10, 3, 7),
(11, 5, 8),
(12, 5, 9),
(13, 1, 10),
(14, 6, 4),
(15, 6, 11),
(16, 7, 12),
(17, 8, 13),
(18, 4, 14),
(19, 9, 1),
(20, 9, 12),
(21, 2, 13),
(22, 1, 15),
(23, 10, 16),
(24, 1, 17),
(25, 11, 4),
(26, 11, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_animal`
--

CREATE TABLE `tipo_animal` (
  `Id_tipo_animal` int(11) NOT NULL,
  `Nombre_tipo_animal` char(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tipo_animal`
--

INSERT INTO `tipo_animal` (`Id_tipo_animal`, `Nombre_tipo_animal`) VALUES
(1, 'Felino'),
(2, 'Reptil'),
(3, 'Insecto'),
(4, 'Canino'),
(5, 'Pez'),
(6, 'Roedor'),
(7, 'Primate');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `animales`
--
ALTER TABLE `animales`
  ADD PRIMARY KEY (`Id_animal`),
  ADD KEY `Id_tipo_animal` (`Id_tipo_animal`);

--
-- Indices de la tabla `caracteristicas`
--
ALTER TABLE `caracteristicas`
  ADD PRIMARY KEY (`Id_caracteristica`);

--
-- Indices de la tabla `caracteristicas_animales`
--
ALTER TABLE `caracteristicas_animales`
  ADD PRIMARY KEY (`Id_caracteristica_animal`),
  ADD KEY `Id_animal` (`Id_animal`),
  ADD KEY `Id_caracteristica` (`Id_caracteristica`);

--
-- Indices de la tabla `tipo_animal`
--
ALTER TABLE `tipo_animal`
  ADD PRIMARY KEY (`Id_tipo_animal`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `animales`
--
ALTER TABLE `animales`
  ADD CONSTRAINT `Id_tipo_animal` FOREIGN KEY (`Id_tipo_animal`) REFERENCES `tipo_animal` (`Id_tipo_animal`);

--
-- Filtros para la tabla `caracteristicas_animales`
--
ALTER TABLE `caracteristicas_animales`
  ADD CONSTRAINT `Id_animal` FOREIGN KEY (`Id_animal`) REFERENCES `animales` (`Id_animal`),
  ADD CONSTRAINT `Id_caracteristica` FOREIGN KEY (`Id_caracteristica`) REFERENCES `caracteristicas` (`Id_caracteristica`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
