-- Schema mydb
CREATE SCHEMA IF NOT EXISTS mydb DEFAULT CHARACTER SET utf8mb3 ;
USE mydb ;

-- Table mydb.Abogado
CREATE TABLE IF NOT EXISTS mydb.Abogado (
  DNI INT NOT NULL,
  NombreA VARCHAR(45) NULL,
  Contraseña VARCHAR(45) NULL,
  PRIMARY KEY (DNI))
ENGINE = InnoDB;


-- Table mydb.Cliente
CREATE TABLE IF NOT EXISTS mydb.Cliente (
  IDCliente INT NOT NULL AUTO_INCREMENT,
  Nombre VARCHAR(25) NOT NULL,
  Apellido VARCHAR(25) NOT NULL,
  DNIC INT(10) NOT NULL,
  Direccion VARCHAR(45) NOT NULL,
  Telefono VARCHAR(25) NOT NULL,
  Mail VARCHAR(45) NOT NULL,
  AbogadoDNI INT NOT NULL,
  PRIMARY KEY (IDCliente),
  INDEX fkClienteAbogadoidx (AbogadoDNI ASC),
  CONSTRAINT fkClienteAbogado
    FOREIGN KEY (AbogadoDNI)
    REFERENCES mydb.Abogado (DNI)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-
-- Table mydb.Casos
CREATE TABLE IF NOT EXISTS mydb.Casos (
  IDCaso INT NOT NULL AUTO_INCREMENT,
  Tipo VARCHAR(25) NOT NULL,
  FechaInicio DATE NOT NULL,
  FechaFin DATE NULL,
  Motivo TEXT,
  ClienteIDCliente INT NOT NULL,
  PRIMARY KEY (IDCaso),
  INDEX fkCasosCliente1idx (ClienteIDCliente ASC),
  CONSTRAINT fkCasosCliente1
    FOREIGN KEY (ClienteIDCliente)
    REFERENCES mydb.Cliente (IDCliente)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- Table mydb.Etapa
CREATE TABLE IF NOT EXISTS mydb. Etapa (
  IDEtapa INT NOT NULL AUTO_INCREMENT,
  Firma BLOB NOT NULL,
  FechaFirma DATE NOT NULL,
  LugarFirma VARCHAR(35) NOT NULL,
  FechaInicioE3 DATE NOT NULL,
  FechaComisionMedica DATE NOT NULL,
  FechaCierreE3 DATE NOT NULL,
  PresentaProntoDespacho VARCHAR(2) NOT NULL,
  FechaDictamen DATE NOT NULL,
  FechaConciliación DATE NOT NULL,
  EtapaInicio BIT(1) NOT NULL,
  FechaInicio DATE NOT NULL,
  EtapaIntermedia BIT(1) NOT NULL,
  FechaIntermedia DATE NOT NULL,
  EtapaFinal BIT(1) NOT NULL,
  FechaFinal DATE NOT NULL,
  PRIMARY KEY (IDEtapa))
ENGINE = InnoDB;



-- Table mydb.CasosEtapa
CREATE TABLE IF NOT EXISTS mydb.CasosEtapa (
  IDCasosEtapa INT NOT NULL AUTO_INCREMENT,
  CasosIDCaso INT NOT NULL,
  EtapaIDEtapa INT NOT NULL,
  PRIMARY KEY (IDCasosEtapa),
  INDEX fkCasosEtapaCasos1idx (CasosIDCaso ASC),
  INDEX fkCasosEtapaEtapa1idx (EtapaIDEtapa ASC),
  CONSTRAINT fkCasosEtapaCasos1
    FOREIGN KEY (CasosIDCaso)
    REFERENCES mydb.Casos (IDCaso)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fkCasosEtapaEtapa1
    FOREIGN KEY (EtapaIDEtapa)
    REFERENCES mydb.Etapa (IDEtapa)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;



