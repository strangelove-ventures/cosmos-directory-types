#!/usr/bin/env node

import fs from "fs/promises";
import path from "path";
import { InputData, jsonInputForTargetLanguage, quicktype } from "quicktype-core";

const cwd = (...args) => path.resolve(process.cwd(), ...args);

const ls = async (...args) => {
  const directory = cwd(...args);
  const names = await fs.readdir(directory, { encoding: "utf-8" });
  const paths = names.map((name) => path.resolve(directory, name));
  return paths;
};

const lsf = async (...args) => {
  const paths = await ls(...args);
  const files = await Promise.all(paths.map((p) => fs.readFile(p, { encoding: "utf-8" })));
  return files;
};

const generate = async ({ lang = "", ext = "" }) => {
  const jsonInput = jsonInputForTargetLanguage(lang);

  await jsonInput.addSource({ name: "AllChainsData", samples: await lsf("samples/chains") });
  await jsonInput.addSource({ name: "ChainData", samples: await lsf("samples/chain") });
  await jsonInput.addSource({ name: "AllValidatorsData", samples: await lsf("samples/validators") });
  await jsonInput.addSource({ name: "ValidatorData", samples: await lsf("samples/validator") });
  await jsonInput.addSource({ name: "ChainValidatorsData", samples: await lsf("samples/chain-validators") });

  const inputData = new InputData();
  inputData.addInput(jsonInput);

  const { lines } = await quicktype({
    alphabetizeProperties: true,
    checkProvenance: true,
    combineClasses: true,
    inputData,
    lang,
  });

  const destination = cwd(`dist/generated.${ext.replace(/^\./, "")}`);
  const contents = lines.concat("").join("\n");
  await fs.writeFile(destination, contents, { encoding: "utf-8" });
};

const build = async () => {
  const langs = [
    { lang: "go", ext: ".go" },
    { lang: "python", ext: ".py" },
    { lang: "rust", ext: ".rs" },
    { lang: "typescript", ext: ".ts" },
  ];

  await Promise.all(langs.map((args) => generate(args)));
};

void build();
