-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 26-05-2021 a las 20:31:27
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
-- Base de datos: `db_farmacia_5`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_clientes`
--

CREATE TABLE `tbl_clientes` (
  `ID_CLIENTE` int(11) NOT NULL,
  `NOMBRE` varchar(200) NOT NULL,
  `APELLIDO` varchar(100) NOT NULL,
  `EDAD` varchar(50) NOT NULL,
  `CUIDAD` varchar(100) NOT NULL,
  `DIRECCION` varchar(100) NOT NULL,
  `TELEFONO` int(50) NOT NULL,
  `FECHA` date NOT NULL,
  `ID_PRODUCTOS` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_descuentos_adulto_mayor`
--

CREATE TABLE `tbl_descuentos_adulto_mayor` (
  `ID_DESCUENTO` int(11) NOT NULL,
  `NOMBRE` varchar(100) NOT NULL,
  `APELLIDO` varchar(100) NOT NULL,
  `EDAD` varchar(50) NOT NULL,
  `DIRECCION` varchar(200) NOT NULL,
  `PUNTOS` double NOT NULL,
  `TELEFONO` int(100) NOT NULL,
  `FECHA` date NOT NULL,
  `PRECIO` int(100) NOT NULL,
  `IDENTIDAD` int(100) NOT NULL,
  `SEXO` varchar(30) NOT NULL,
  `ID_PRODUCTOS` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_facturas`
--

CREATE TABLE `tbl_facturas` (
  `ID_FACTURA` int(11) NOT NULL,
  `CODIGO_FARMACIA` double NOT NULL,
  `RAZON_SOCIAL` varchar(150) NOT NULL,
  `DEPARTAMENTO` varchar(100) NOT NULL,
  `COLONIA` varchar(100) NOT NULL,
  `CORREO` varchar(200) NOT NULL,
  `TELEFONO` int(50) NOT NULL,
  `TOTAL` double NOT NULL,
  `ID_PRODUCTOS` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_medicamentos`
--

CREATE TABLE `tbl_medicamentos` (
  `ID_MEDICAMENTO` int(11) NOT NULL,
  `PRESENTACION` varchar(150) NOT NULL,
  `FORMA` varchar(150) NOT NULL,
  `MARCA_PRODUCTO` varchar(100) NOT NULL,
  `CANTIDAD` varchar(200) NOT NULL,
  `ID_PRODUCTOS` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_productos`
--

CREATE TABLE `tbl_productos` (
  `ID_PRODUCTO` int(11) NOT NULL,
  `PRODUCTO` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_recetas`
--

CREATE TABLE `tbl_recetas` (
  `ID_RECETA` int(11) NOT NULL,
  `NOMBRE_PACIENTE` varchar(100) NOT NULL,
  `APELLIDO` varchar(100) NOT NULL,
  `DIRECCION` varchar(100) NOT NULL,
  `GENERO` varchar(100) NOT NULL,
  `TELEFONO` int(50) NOT NULL,
  `CODIGO` double NOT NULL,
  `ID_PRODUCTO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_registros`
--

CREATE TABLE `tbl_registros` (
  `ID_REGISTRO` int(11) NOT NULL,
  `NOMBRE_EMPRESA` varchar(200) NOT NULL,
  `DIRECCION` varchar(150) NOT NULL,
  `TELEFONO` int(100) NOT NULL,
  `CORREO` varchar(150) NOT NULL,
  `MEDICO_GENERAL` varchar(100) NOT NULL,
  `ID_PRODUCTO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tbl_clientes`
--
ALTER TABLE `tbl_clientes`
  ADD PRIMARY KEY (`ID_CLIENTE`),
  ADD KEY `FK_PRODUCTO_CLIENTES` (`ID_PRODUCTOS`);

--
-- Indices de la tabla `tbl_descuentos_adulto_mayor`
--
ALTER TABLE `tbl_descuentos_adulto_mayor`
  ADD PRIMARY KEY (`ID_DESCUENTO`),
  ADD KEY `FK_PRODUCTO_DESCUENTOS_ADULTOS_MAYOR` (`ID_PRODUCTOS`);

--
-- Indices de la tabla `tbl_facturas`
--
ALTER TABLE `tbl_facturas`
  ADD PRIMARY KEY (`ID_FACTURA`),
  ADD KEY `FK_PRODUCTO_FACTURAS` (`ID_PRODUCTOS`);

--
-- Indices de la tabla `tbl_medicamentos`
--
ALTER TABLE `tbl_medicamentos`
  ADD PRIMARY KEY (`ID_MEDICAMENTO`),
  ADD KEY `FK_PRDUCTO_MEDICAMENTOS` (`ID_PRODUCTOS`);

--
-- Indices de la tabla `tbl_productos`
--
ALTER TABLE `tbl_productos`
  ADD PRIMARY KEY (`ID_PRODUCTO`);

--
-- Indices de la tabla `tbl_recetas`
--
ALTER TABLE `tbl_recetas`
  ADD PRIMARY KEY (`ID_RECETA`),
  ADD KEY `FK_PRODUCTO_RECETAS` (`ID_PRODUCTO`);

--
-- Indices de la tabla `tbl_registros`
--
ALTER TABLE `tbl_registros`
  ADD PRIMARY KEY (`ID_REGISTRO`),
  ADD KEY `FK_PRODUCTO_REGISTROS` (`ID_PRODUCTO`);

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
-- AUTO_INCREMENT de la tabla `tbl_recetas`
--
ALTER TABLE `tbl_recetas`
  MODIFY `ID_RECETA` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tbl_registros`
--
ALTER TABLE `tbl_registros`
  MODIFY `ID_REGISTRO` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `tbl_clientes`
--
ALTER TABLE `tbl_clientes`
  ADD CONSTRAINT `FK_PRODUCTO_CLIENTES` FOREIGN KEY (`ID_PRODUCTOS`) REFERENCES `tbl_productos` (`ID_PRODUCTO`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `tbl_descuentos_adulto_mayor`
--
ALTER TABLE `tbl_descuentos_adulto_mayor`
  ADD CONSTRAINT `FK_PRODUCTO_DESCUENTOS_ADULTO_MAYOR` FOREIGN KEY (`ID_PRODUCTOS`) REFERENCES `tbl_productos` (`ID_PRODUCTO`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `tbl_facturas`
--
ALTER TABLE `tbl_facturas`
  ADD CONSTRAINT `FK_PRODUCTO_FACTURAS` FOREIGN KEY (`ID_PRODUCTOS`) REFERENCES `tbl_productos` (`ID_PRODUCTO`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `tbl_medicamentos`
--
ALTER TABLE `tbl_medicamentos`
  ADD CONSTRAINT `FK_PRODUCTO_MEDICAMENTOS` FOREIGN KEY (`ID_PRODUCTOS`) REFERENCES `tbl_productos` (`ID_PRODUCTO`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `tbl_recetas`
--
ALTER TABLE `tbl_recetas`
  ADD CONSTRAINT `FK_PRODUCTO_RECETAS` FOREIGN KEY (`ID_PRODUCTO`) REFERENCES `tbl_productos` (`ID_PRODUCTO`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `tbl_registros`
--
ALTER TABLE `tbl_registros`
  ADD CONSTRAINT `FK_PRODUCTO_REGISTROS` FOREIGN KEY (`ID_PRODUCTO`) REFERENCES `tbl_productos` (`ID_PRODUCTO`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
