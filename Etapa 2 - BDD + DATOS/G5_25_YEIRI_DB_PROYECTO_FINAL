-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-06-2021 a las 17:37:22
-- Versión del servidor: 10.4.18-MariaDB
-- Versión de PHP: 7.4.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `db_cine`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_clientes`
--

CREATE TABLE `tbl_clientes` (
  `ID_CLIENTE` int(11) NOT NULL,
  `NOMBRE` varchar(200) NOT NULL,
  `APELLIDO` varchar(200) NOT NULL,
  `EDAD` varchar(150) NOT NULL,
  `TELEFONO` int(100) NOT NULL,
  `DIRECCION` varchar(200) NOT NULL,
  `SEXO` varchar(50) NOT NULL,
  `IDENTIDAD` int(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_descuentos_adulto_mayor`
--

CREATE TABLE `tbl_descuentos_adulto_mayor` (
  `ID_DESCUENTO` int(11) NOT NULL,
  `DESCUENTO` int(200) NOT NULL,
  `PUNTOS` int(150) NOT NULL,
  `CLIENTE` varchar(200) NOT NULL,
  `PRODUCTO` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_facturas`
--

CREATE TABLE `tbl_facturas` (
  `ID_FACTURA` int(11) NOT NULL,
  `CODIGO_FARMACIA` int(200) NOT NULL,
  `FECHA` date NOT NULL,
  `DEPARTAMENTO` varchar(200) NOT NULL,
  `TOTAL` int(150) NOT NULL,
  `PRODUCTO` varchar(200) NOT NULL,
  `REGISTRO` varchar(200) NOT NULL,
  `CLIENTE` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_medicamentos`
--

CREATE TABLE `tbl_medicamentos` (
  `ID_MEDICAMENTO` int(11) NOT NULL,
  `CANTIDAD` int(200) NOT NULL,
  `FORMA` varchar(150) NOT NULL,
  `PRECIO` int(150) NOT NULL,
  `PRODUCTO` varchar(200) NOT NULL,
  `CLIENTE` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_productos`
--

CREATE TABLE `tbl_productos` (
  `ID_PRODUCTO` int(11) NOT NULL,
  `VALOR_PRODUCTO` int(200) NOT NULL,
  `PRODUCTO` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_registros_farmacia`
--

CREATE TABLE `tbl_registros_farmacia` (
  `ID_REGISTRO` int(11) NOT NULL,
  `NOMBRE_FARMACIA` varchar(200) NOT NULL,
  `UBICACION` varchar(200) NOT NULL,
  `TELEFONO_FARMCIA` int(150) NOT NULL,
  `CORREO` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tbl_clientes`
--
ALTER TABLE `tbl_clientes`
  ADD PRIMARY KEY (`ID_CLIENTE`);

--
-- Indices de la tabla `tbl_descuentos_adulto_mayor`
--
ALTER TABLE `tbl_descuentos_adulto_mayor`
  ADD PRIMARY KEY (`ID_DESCUENTO`),
  ADD KEY `FK_DESCUENTOS_ADULTO_MATOR_PRODUCTO` (`PRODUCTO`),
  ADD KEY `FK_DESCUENTOS_ADULTO_MAYOR_CLIENTE` (`CLIENTE`);

--
-- Indices de la tabla `tbl_facturas`
--
ALTER TABLE `tbl_facturas`
  ADD PRIMARY KEY (`ID_FACTURA`),
  ADD KEY `FK_FACTURAS_PRODUCTO` (`PRODUCTO`),
  ADD KEY `FK_FACTURAS_REGISTRO` (`REGISTRO`),
  ADD KEY `FK_FACTURAS_CLIENTE` (`CLIENTE`);

--
-- Indices de la tabla `tbl_medicamentos`
--
ALTER TABLE `tbl_medicamentos`
  ADD PRIMARY KEY (`ID_MEDICAMENTO`),
  ADD KEY `FK_MEDICAMENTOS_PRODUCTO` (`PRODUCTO`),
  ADD KEY `FK_MEDICAMENTOS_CLIENTE` (`CLIENTE`);

--
-- Indices de la tabla `tbl_productos`
--
ALTER TABLE `tbl_productos`
  ADD PRIMARY KEY (`ID_PRODUCTO`),
  ADD KEY `FK_PRODUCTOS_PRODUCTO` (`PRODUCTO`);

--
-- Indices de la tabla `tbl_registros_farmacia`
--
ALTER TABLE `tbl_registros_farmacia`
  ADD PRIMARY KEY (`ID_REGISTRO`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `tbl_clientes`
--
ALTER TABLE `tbl_clientes`
  MODIFY `ID_CLIENTE` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tbl_descuentos_adulto_mayor`
--
ALTER TABLE `tbl_descuentos_adulto_mayor`
  MODIFY `ID_DESCUENTO` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tbl_facturas`
--
ALTER TABLE `tbl_facturas`
  MODIFY `ID_FACTURA` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tbl_medicamentos`
--
ALTER TABLE `tbl_medicamentos`
  MODIFY `ID_MEDICAMENTO` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tbl_productos`
--
ALTER TABLE `tbl_productos`
  MODIFY `ID_PRODUCTO` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tbl_registros_farmacia`
--
ALTER TABLE `tbl_registros_farmacia`
  MODIFY `ID_REGISTRO` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `tbl_descuentos_adulto_mayor`
--
ALTER TABLE `tbl_descuentos_adulto_mayor`
  ADD CONSTRAINT `FK_CLIENTES_DESCUENTOS_ADULTO_MAYOR` FOREIGN KEY (`ID_DESCUENTO`) REFERENCES `tbl_clientes` (`ID_CLIENTE`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_PRODUCTOS_DESCUENTOS_ADULTO_MAYOR` FOREIGN KEY (`ID_DESCUENTO`) REFERENCES `tbl_productos` (`ID_PRODUCTO`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `tbl_facturas`
--
ALTER TABLE `tbl_facturas`
  ADD CONSTRAINT `FK_CLIENTES_FACTURAS` FOREIGN KEY (`ID_FACTURA`) REFERENCES `tbl_clientes` (`ID_CLIENTE`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_PRODUCTOS_FACTURAS` FOREIGN KEY (`ID_FACTURA`) REFERENCES `tbl_productos` (`ID_PRODUCTO`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_REGISTROS_FARMACIA_FACTURAS` FOREIGN KEY (`ID_FACTURA`) REFERENCES `tbl_registros_farmacia` (`ID_REGISTRO`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `tbl_medicamentos`
--
ALTER TABLE `tbl_medicamentos`
  ADD CONSTRAINT `FK_CLIENTES_MENDICAMENTOS` FOREIGN KEY (`ID_MEDICAMENTO`) REFERENCES `tbl_clientes` (`ID_CLIENTE`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_PRODUCTOS_MEDICAMENTOS` FOREIGN KEY (`ID_MEDICAMENTO`) REFERENCES `tbl_productos` (`ID_PRODUCTO`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
