/*
  Warnings:

  - You are about to drop the column `time` on the `Disease_Frequency` table. All the data in the column will be lost.
  - You are about to drop the column `time` on the `Drug_Sales` table. All the data in the column will be lost.
  - Added the required column `frequency` to the `Disease_Frequency` table without a default value. This is not possible if the table is not empty.
  - Added the required column `salesCount` to the `Drug_Sales` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "Disease_Frequency" DROP COLUMN "time",
ADD COLUMN     "frequency" INTEGER NOT NULL;

-- AlterTable
ALTER TABLE "Drug_Sales" DROP COLUMN "time",
ADD COLUMN     "salesCount" INTEGER NOT NULL;

-- CreateTable
CREATE TABLE "Disease_Freq" (
    "ID" SERIAL NOT NULL,
    "Date" TEXT,
    "Count" BIGINT,
    "Region ID" BIGINT,
    "Disease ID" BIGINT,
    "Disease" TEXT,
    "Region" TEXT,

    CONSTRAINT "Disease_Freq_pkey" PRIMARY KEY ("ID")
);

-- CreateTable
CREATE TABLE "Delhi" (
    "ID" SERIAL NOT NULL,
    "Date" TEXT,
    "Count" BIGINT,
    "Region ID" BIGINT,
    "Disease ID" BIGINT,
    "Disease" TEXT,
    "Region" TEXT,

    CONSTRAINT "Delhi_pkey" PRIMARY KEY ("ID")
);

-- CreateTable
CREATE TABLE "Kolkata" (
    "ID" SERIAL NOT NULL,
    "Date" TEXT,
    "Count" BIGINT,
    "Region ID" BIGINT,
    "Disease ID" BIGINT,
    "Disease" TEXT,
    "Region" TEXT,

    CONSTRAINT "Kolkata_pkey" PRIMARY KEY ("ID")
);

-- CreateTable
CREATE TABLE "Pune" (
    "ID" SERIAL NOT NULL,
    "Date" TEXT,
    "Count" BIGINT,
    "Region ID" BIGINT,
    "Disease ID" BIGINT,
    "Disease" TEXT,
    "Region" TEXT,

    CONSTRAINT "Pune_pkey" PRIMARY KEY ("ID")
);
