BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Sales" (
	"ID"	INTEGER NOT NULL,
	"amount"	REAL NOT NULL,
	"salesDate"	TEXT NOT NULL,
	"region"	TEXT NOT NULL,
	PRIMARY KEY("ID" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Region" (
	"code"	TEXT NOT NULL,
	"name"	TEXT NOT NULL,
	PRIMARY KEY("code")
);
CREATE TABLE IF NOT EXISTS "ImportedFiles" (
	"fileName"	TEXT NOT NULL,
	PRIMARY KEY("fileName")
);
INSERT INTO "Region" VALUES ('w','West');
INSERT INTO "Region" VALUES ('e','East');
INSERT INTO "Region" VALUES ('n','North');
INSERT INTO "Region" VALUES ('s','South');
COMMIT;
