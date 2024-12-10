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

 Date: 10/12/2024 15:37:15
*/


-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS "public"."django_content_type";
CREATE TABLE "public"."django_content_type" (
  "id" int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY (
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1
),
  "app_label" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "model" varchar(100) COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO "public"."django_content_type" VALUES (1, 'admin', 'logentry');
INSERT INTO "public"."django_content_type" VALUES (2, 'auth', 'permission');
INSERT INTO "public"."django_content_type" VALUES (3, 'auth', 'group');
INSERT INTO "public"."django_content_type" VALUES (4, 'auth', 'user');
INSERT INTO "public"."django_content_type" VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO "public"."django_content_type" VALUES (6, 'sessions', 'session');
INSERT INTO "public"."django_content_type" VALUES (7, 'gestion_inmuebles', 'comuna');
INSERT INTO "public"."django_content_type" VALUES (8, 'gestion_inmuebles', 'region');
INSERT INTO "public"."django_content_type" VALUES (9, 'gestion_inmuebles', 'tipoinmueble');
INSERT INTO "public"."django_content_type" VALUES (10, 'gestion_inmuebles', 'inmueble');
INSERT INTO "public"."django_content_type" VALUES (11, 'gestion_inmuebles', 'userprofile');
INSERT INTO "public"."django_content_type" VALUES (12, 'gestion_inmuebles', 'solicitud');
INSERT INTO "public"."django_content_type" VALUES (13, 'gestion_inmuebles', 'gestionsolicitud');

-- ----------------------------
-- Auto increment value for django_content_type
-- ----------------------------
SELECT setval('"public"."django_content_type_id_seq"', 13, true);

-- ----------------------------
-- Uniques structure for table django_content_type
-- ----------------------------
ALTER TABLE "public"."django_content_type" ADD CONSTRAINT "django_content_type_app_label_model_76bd3d3b_uniq" UNIQUE ("app_label", "model");

-- ----------------------------
-- Primary Key structure for table django_content_type
-- ----------------------------
ALTER TABLE "public"."django_content_type" ADD CONSTRAINT "django_content_type_pkey" PRIMARY KEY ("id");
