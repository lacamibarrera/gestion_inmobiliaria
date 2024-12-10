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

 Date: 10/12/2024 15:38:12
*/


-- ----------------------------
-- Table structure for gestion_inmuebles_userprofile
-- ----------------------------
DROP TABLE IF EXISTS "public"."gestion_inmuebles_userprofile";
CREATE TABLE "public"."gestion_inmuebles_userprofile" (
  "id" int8 NOT NULL GENERATED BY DEFAULT AS IDENTITY (
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1
),
  "tipo" varchar(20) COLLATE "pg_catalog"."default" NOT NULL,
  "rut" varchar(12) COLLATE "pg_catalog"."default" NOT NULL,
  "direccion" varchar(300) COLLATE "pg_catalog"."default" NOT NULL,
  "telefono" varchar(12) COLLATE "pg_catalog"."default" NOT NULL,
  "fecha_registro" timestamptz(6) NOT NULL,
  "user_id" int4 NOT NULL
)
;

-- ----------------------------
-- Records of gestion_inmuebles_userprofile
-- ----------------------------
INSERT INTO "public"."gestion_inmuebles_userprofile" VALUES (1, 'ARRENDATARIO', '16.009.911-9', 'Río Maullin 5337, Denavi Sur Talcahuano', '987473788', '2024-12-08 21:10:31.142094-03', 2);
INSERT INTO "public"."gestion_inmuebles_userprofile" VALUES (3, 'ARRENDADOR', '000556-5', 'asdaskljaskld', '1215465', '2024-12-10 00:59:21.753317-03', 4);
INSERT INTO "public"."gestion_inmuebles_userprofile" VALUES (2, 'ARRENDADOR', '7.398.688-5', 'El Chequen 434', '788954', '2024-12-08 21:42:18.581244-03', 3);

-- ----------------------------
-- Auto increment value for gestion_inmuebles_userprofile
-- ----------------------------
SELECT setval('"public"."gestion_inmuebles_userprofile_id_seq"', 3, true);

-- ----------------------------
-- Uniques structure for table gestion_inmuebles_userprofile
-- ----------------------------
ALTER TABLE "public"."gestion_inmuebles_userprofile" ADD CONSTRAINT "gestion_inmuebles_userprofile_user_id_key" UNIQUE ("user_id");

-- ----------------------------
-- Primary Key structure for table gestion_inmuebles_userprofile
-- ----------------------------
ALTER TABLE "public"."gestion_inmuebles_userprofile" ADD CONSTRAINT "gestion_inmuebles_userprofile_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Foreign Keys structure for table gestion_inmuebles_userprofile
-- ----------------------------
ALTER TABLE "public"."gestion_inmuebles_userprofile" ADD CONSTRAINT "gestion_inmuebles_userprofile_user_id_daf7fd0c_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "public"."auth_user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE INITIALLY DEFERRED;