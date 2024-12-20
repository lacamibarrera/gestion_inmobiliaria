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

 Date: 10/12/2024 15:38:00
*/


-- ----------------------------
-- Table structure for gestion_inmuebles_solicitud
-- ----------------------------
DROP TABLE IF EXISTS "public"."gestion_inmuebles_solicitud";
CREATE TABLE "public"."gestion_inmuebles_solicitud" (
  "id" int8 NOT NULL GENERATED BY DEFAULT AS IDENTITY (
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1
),
  "mensaje" text COLLATE "pg_catalog"."default" NOT NULL,
  "estado" varchar(20) COLLATE "pg_catalog"."default" NOT NULL,
  "fecha_creacion" timestamptz(6) NOT NULL,
  "arrendador_id" int4 NOT NULL,
  "inmueble_id" int4 NOT NULL,
  "arrendatario_id" int4
)
;

-- ----------------------------
-- Records of gestion_inmuebles_solicitud
-- ----------------------------
INSERT INTO "public"."gestion_inmuebles_solicitud" VALUES (11, 'Me interesa este Inmueble favor contactar', 'Pendiente', '2024-12-10 00:48:41.061131-03', 2, 5, 3);

-- ----------------------------
-- Auto increment value for gestion_inmuebles_solicitud
-- ----------------------------
SELECT setval('"public"."gestion_inmuebles_solicitud_id_seq"', 11, true);

-- ----------------------------
-- Indexes structure for table gestion_inmuebles_solicitud
-- ----------------------------
CREATE INDEX "gestion_inmuebles_solicitud_arrendador_id_cb949520" ON "public"."gestion_inmuebles_solicitud" USING btree (
  "arrendador_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "gestion_inmuebles_solicitud_inmueble_id_06871793" ON "public"."gestion_inmuebles_solicitud" USING btree (
  "inmueble_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

-- ----------------------------
-- Primary Key structure for table gestion_inmuebles_solicitud
-- ----------------------------
ALTER TABLE "public"."gestion_inmuebles_solicitud" ADD CONSTRAINT "gestion_inmuebles_solicitud_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Foreign Keys structure for table gestion_inmuebles_solicitud
-- ----------------------------
ALTER TABLE "public"."gestion_inmuebles_solicitud" ADD CONSTRAINT "gestion_inmuebles_so_arrendador_id_cb949520_fk_auth_user" FOREIGN KEY ("arrendador_id") REFERENCES "public"."auth_user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "public"."gestion_inmuebles_solicitud" ADD CONSTRAINT "gestion_inmuebles_so_inmueble_id_06871793_fk_gestion_i" FOREIGN KEY ("inmueble_id") REFERENCES "public"."gestion_inmuebles_inmueble" ("id_inmueble") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;
