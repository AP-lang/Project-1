drop table painting;
drop table painter;
CREATE TABLE PAINTER (
     PAINTER_NUM     	INT  Primary Key,
     PAINTER_LNAME	  CHAR(50)  NOT NULL,
     PAINTER_FNAME    CHAR(50),
     PAINTER_ORIGIN   CHAR(25),
     PAINTER_DOB	  DATE
);
CREATE TABLE PAINTING (
   PAINTING_NUM     INT PRIMARY KEY,
   PAINTING_TITLE   CHAR(50),
   PAINTING_VALUE   NUMBER(11,2),
   PAINTER_NUM  int   REFERENCES PAINTER
);
INSERT INTO PAINTER VALUES
(123,'Vecelli','Titian', 'Italy', '1-Jan-1485');
INSERT INTO PAINTER VALUES 
(126,'O''Keeffe','Georgia', 'United States','15-Nov-1887');
INSERT INTO PAINTER VALUES
(130,'Van Gogh','Vincent', 'Netherlands', '30-Mar-1853');
INSERT INTO PAINTER VALUES
(133,'van Rijn','Rembrandt','Netherlands', '15-Jul-1606');
INSERT INTO PAINTER VALUES
(136,'Picasso','Pablo', 'Spain', '25-Oct-1881');
INSERT INTO PAINTER VALUES
(139,'Monet','Claude', 'France', '14-Nov-1840');
INSERT INTO PAINTER VALUES
(142,'Warhol', 'Andy', 'United States', '6-Aug-1928');
INSERT INTO PAINTER VALUES
(145,'Renior','Pierre-Auguste', 'France', '25-Feb-1841');
INSERT INTO PAINTER VALUES
(146,'da Vinci','Leonardo', 'Italy', '15-Apr-1452');
INSERT INTO PAINTER VALUES
(148,'di Lodovico Buonarrotu Simoni','Michelangelo', 'Italy', '6-Mar-1475');

INSERT INTO PAINTING VALUES
(10,'Mona Lisa', 700000000,146);
INSERT INTO PAINTING VALUES
(20,'Portrait of Marten Soolmans',201832.57,133);
INSERT INTO PAINTING VALUES
(30,'Salvator Mundi', 450300000,146);
INSERT INTO PAINTING VALUES
(40,'Les Femmes d''Alger', 187000000,136);
INSERT INTO PAINTING VALUES
(50,'The Dream', 155000000,136);
INSERT INTO PAINTING VALUES
(60,'Eight Elvises', 100000000,142);
INSERT INTO PAINTING VALUES
(70, 'Diana and Actaeon', 91000000,123);
INSERT INTO PAINTING VALUES
(80, 'Portrait of Doctor Gachet', 82500000,130);
INSERT INTO PAINTING VALUES
(90, 'Le bassin aux nympheas', 80600000,139);
INSERT INTO PAINTING VALUES
(100, 'Le moulin de la Galette', 78100000,145);
INSERT INTO PAINTING VALUES
(110, 'Self-portrait with bandaged ear', 90000000,130);
INSERT INTO PAINTING VALUES
(120, 'The Last Supper', 0,146);
INSERT INTO PAINTING VALUES
(130, 'the Starry Night', 0,130);
INSERT INTO PAINTING VALUES
(140, 'Creation of Adam', 0,148);
INSERT INTO PAINTING VALUES
(150, 'Water Lilies', 0,139);
INSERT INTO PAINTING VALUES
(160, 'The Night Watch', 0,133);

Commit;
Select * from Painter;
Select * from Painting;



