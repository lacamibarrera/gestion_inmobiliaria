/*
 Navicat Premium Data Transfer

 Source Server         : localhost_5432
 Source Server Type    : PostgreSQL
 Source Server Version : 160004 (160004)
 Source Host           : localhost:5432
 Source Catalog        : gestion_inmuebles
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 160004 (160004)
 File Encoding         : 65001

 Date: 10/12/2024 15:37:45
*/


-- ----------------------------
-- Table structure for gestion_inmuebles_inmueble
-- ----------------------------
DROP TABLE IF EXISTS "public"."gestion_inmuebles_inmueble";
CREATE TABLE "public"."gestion_inmuebles_inmueble" (
  "id_inmueble" int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY (
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1
),
  "nombre" varchar(200) COLLATE "pg_catalog"."default" NOT NULL,
  "descripcion" text COLLATE "pg_catalog"."default" NOT NULL,
  "m2_construidos" float8 NOT NULL,
  "m2_terreno" float8 NOT NULL,
  "estacionamientos" int4 NOT NULL,
  "habitaciones" int4 NOT NULL,
  "banos" int4 NOT NULL,
  "direccion" varchar(300) COLLATE "pg_catalog"."default" NOT NULL,
  "precio_mensual" numeric(12,2) NOT NULL,
  "estado" varchar(20) COLLATE "pg_catalog"."default" NOT NULL,
  "imagen_url" varchar(300) COLLATE "pg_catalog"."default",
  "fecha_creacion" timestamptz(6) NOT NULL,
  "ultima_modificacion" timestamptz(6) NOT NULL,
  "id_comuna_id" int4 NOT NULL,
  "id_region_id" int4 NOT NULL,
  "tipo_inmueble" text COLLATE "pg_catalog"."default" NOT NULL,
  "usuario_id" int4 NOT NULL
)
;

-- ----------------------------
-- Records of gestion_inmuebles_inmueble
-- ----------------------------
INSERT INTO "public"."gestion_inmuebles_inmueble" VALUES (6, 'Departamento En Concepcion', 'Departamento de 3 Dormitorios, Amplios Ventanales, con Sol de Tarde', 90, 90, 2, 3, 2, 'O''higgins 1528', 650000.00, 'DISPONIBLE', 'https://www.maudierpropiedades.cl/wp-content/uploads/2020/12/20201216_164900.jpg', '2024-12-10 01:08:30.517742-03', '2024-12-10 01:08:30.517742-03', 171, 10, 'DEPARTAMENTO', 4);
INSERT INTO "public"."gestion_inmuebles_inmueble" VALUES (5, 'Oficina en Providencia', 'Hermosa oficina en Santiago, Sector Empresarial, central, amplio y cómodo.', 70, 70, 1, 2, 2, 'Avenida Pedro de Valdivia 598', 300000.00, 'DISPONIBLE', 'https://www.bienesonline.com/chile/photos/arriendo-oficina-providencia-metro-pedro-de-valdivia-14254099520.jpg', '2024-12-09 23:35:43.771761-03', '2024-12-09 23:35:43.771761-03', 295, 16, 'OFICINA', 3);
INSERT INTO "public"."gestion_inmuebles_inmueble" VALUES (4, 'Casa en la Playa', 'Hermosa Casa en la Playa para Disfrutar de Tus Vacaciones, a dos cuadras de la playa.', 70, 150, 2, 3, 2, 'Avenida del Mar', 500000.00, 'NO_DISPONIBLE', 'https://cf.bstatic.com/xdata/images/hotel/max1024x768/419091128.jpg?k=5089014a66fb06bc61d0418617c2d29e2fd5026f535c9a91a19085513cad3321&o=&hp=1', '2024-12-08 22:50:42.821103-03', '2024-12-10 12:42:28.842196-03', 49, 6, 'CASA', 3);
INSERT INTO "public"."gestion_inmuebles_inmueble" VALUES (7, 'Bodega en Hualpen', 'Arriendo amplia bodega en la Comuna de Hualpen para Comerciantes', 50, 50, 1, 1, 1, 'Colon 9840', 1000000.00, 'DISPONIBLE', 'https://www.todogalpon.cl/wp-content/uploads/2023/07/foto10.webp', '2024-12-10 12:47:41.381519-03', '2024-12-10 12:47:41.381519-03', 173, 10, 'BODEGA', 3);

-- ----------------------------
-- Auto increment value for gestion_inmuebles_inmueble
-- ----------------------------
SELECT setval('"public"."gestion_inmuebles_inmueble_id_inmueble_seq"', 7, true);

-- ----------------------------
-- Indexes structure for table gestion_inmuebles_inmueble
-- ----------------------------
CREATE INDEX "gestion_inmuebles_inmueble_id_comuna_id_311e6367" ON "public"."gestion_inmuebles_inmueble" USING btree (
  "id_comuna_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "gestion_inmuebles_inmueble_id_region_id_231e9dad" ON "public"."gestion_inmuebles_inmueble" USING btree (
  "id_region_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "gestion_inmuebles_inmueble_usuario_id_8da0461c" ON "public"."gestion_inmuebles_inmueble" USING btree (
  "usuario_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table gestion_inmuebles_inmueble
-- ----------------------------
ALTER TABLE "public"."gestion_inmuebles_inmueble" ADD CONSTRAINT "gestion_inmuebles_inmueble_pkey" PRIMARY KEY ("id_inmueble");

-- ----------------------------
-- Foreign Keys structure for table gestion_inmuebles_inmueble
-- ----------------------------
ALTER TABLE "public"."gestion_inmuebles_inmueble" ADD CONSTRAINT "gestion_inmuebles_in_id_comuna_id_311e6367_fk_gestion_i" FOREIGN KEY ("id_comuna_id") REFERENCES "public"."gestion_inmuebles_comuna" ("id_comuna") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."gestion_inmuebles_inmueble" ADD CONSTRAINT "gestion_inmuebles_in_id_region_id_231e9dad_fk_gestion_i" FOREIGN KEY ("id_region_id") REFERENCES "public"."gestion_inmuebles_region" ("id_region") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."gestion_inmuebles_inmueble" ADD CONSTRAINT "gestion_inmuebles_inmueble_usuario_id_8da0461c_fk_auth_user_id" FOREIGN KEY ("usuario_id") REFERENCES "public"."auth_user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
