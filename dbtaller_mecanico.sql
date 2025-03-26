-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 26-03-2025 a las 07:48:21
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `dbtaller_mecanico`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `rfc` varchar(13) NOT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`id`, `nombre`, `telefono`, `rfc`, `email`) VALUES
(1, 'Bob Esponja Pantalones Cuadrados', '3326650118', 'BOBS891234ABC', 'bob@crustycangrejo.com'),
(2, 'Homer J Simpson', '00000000', 'HOMJ720315XYZ', 'homer@plantanuclear.com'),
(3, 'Pedro Picapiedra', '00000000', 'PEPI650789ROC', 'pedro@rocadura.com'),
(4, 'Rick Sánchez', '00000000', 'RICS567890POR', 'rick@gmail.com'),
(5, 'Don Ramon', '00000000', 'DORV420666NON', 'don.ramon@vecindad.mx');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `det_reparaciones`
--

CREATE TABLE `det_reparaciones` (
  `folio_detalle` int(11) NOT NULL,
  `folio` int(11) NOT NULL,
  `pieza_id` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL CHECK (`cantidad` > 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `piezas`
--

CREATE TABLE `piezas` (
  `id` int(11) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `stock` int(11) NOT NULL CHECK (`stock` >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `piezas`
--

INSERT INTO `piezas` (`id`, `descripcion`, `stock`) VALUES
(1, 'Llavenosa cromada', 8),
(2, 'Cepillada de fierro doble acción', 4),
(3, 'Bujía reversa con juego', 15),
(4, 'Tornillo sin fin pero con ganas', 12),
(5, 'Amortiguador de sacudidas prolongadas', 7),
(6, 'Piston lubricado a mano', 10),
(7, 'Eje con doble entrada', 5),
(8, 'Caja de bolas con rebote', 20),
(9, 'Palanca para meter duro y parejo', 6),
(10, 'Llave nuda reforzada', 9);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reparaciones`
--

CREATE TABLE `reparaciones` (
  `folio` int(11) NOT NULL,
  `matricula` varchar(20) NOT NULL,
  `fecha_entrada` date NOT NULL,
  `fecha_salida` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `usuario_id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `perfil` enum('Admin','Mecanico','Auxiliar') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`usuario_id`, `nombre`, `username`, `password`, `perfil`) VALUES
(1, 'Administrador General', 'admin', 'admin', 'Admin'),
(2, 'Uziel', 'uziel', 'uziel', 'Mecanico'),
(3, 'Rick Sánchez', 'rick', 'morty123', 'Admin'),
(4, 'Homero Simpson', 'homero', 'donut123', 'Mecanico'),
(5, 'Bob Esponja', 'bob', 'patricio123', 'Auxiliar'),
(6, 'Tony Stark', 'ironman', 'jarvis123', 'Admin'),
(7, 'Goku Son', 'kakaroto', 'vegeta123', 'Mecanico');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vehiculos`
--

CREATE TABLE `vehiculos` (
  `matricula` varchar(10) NOT NULL,
  `cliente_id` int(11) NOT NULL,
  `marca` varchar(50) NOT NULL,
  `modelo` varchar(50) NOT NULL,
  `color` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `vehiculos`
--

INSERT INTO `vehiculos` (`matricula`, `cliente_id`, `marca`, `modelo`, `color`) VALUES
('BAT-2024', 2, 'Wayne Industries', 'Batmóvil', 'Negro Mate'),
('DED-666', 4, 'Deadpool', 'Scooter', 'Rojo Sangre'),
('MAG-777', 5, 'Ricky Martin', 'Platillo Volador', 'Gris'),
('SPD-2024', 1, 'Stark Industries', 'Spider-Móvil', 'Rojo y Azul'),
('SUP-2024', 3, 'Nose', 'NOse', 'nose');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `det_reparaciones`
--
ALTER TABLE `det_reparaciones`
  ADD PRIMARY KEY (`folio_detalle`),
  ADD KEY `folio` (`folio`),
  ADD KEY `pieza_id` (`pieza_id`);

--
-- Indices de la tabla `piezas`
--
ALTER TABLE `piezas`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `reparaciones`
--
ALTER TABLE `reparaciones`
  ADD PRIMARY KEY (`folio`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`usuario_id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `vehiculos`
--
ALTER TABLE `vehiculos`
  ADD PRIMARY KEY (`matricula`),
  ADD KEY `cliente_id` (`cliente_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `det_reparaciones`
--
ALTER TABLE `det_reparaciones`
  MODIFY `folio_detalle` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `usuario_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `det_reparaciones`
--
ALTER TABLE `det_reparaciones`
  ADD CONSTRAINT `det_reparaciones_ibfk_1` FOREIGN KEY (`folio`) REFERENCES `reparaciones` (`folio`) ON DELETE CASCADE,
  ADD CONSTRAINT `det_reparaciones_ibfk_2` FOREIGN KEY (`pieza_id`) REFERENCES `piezas` (`id`);

--
-- Filtros para la tabla `vehiculos`
--
ALTER TABLE `vehiculos`
  ADD CONSTRAINT `vehiculos_ibfk_1` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
