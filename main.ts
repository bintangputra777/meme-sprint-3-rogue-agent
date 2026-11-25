// Entry for the make.fun bounty "Meme Sprint 3: AI Agent Goes Rogue"
// (u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6).
//
// The program writes the pre-rendered meme image held in this repository
// (assets/entry.png, 1024x1024 PNG) to /output/entry.png. It is the simplest
// program the brief allows: a deterministic copy of an image the repository
// holds. No network, no randomness, no environment input — every run writes
// the same bytes. Before copying it verifies the source is a whole PNG of
// the size the gate requires, so a broken asset fails loudly instead of
// silently producing an invalid entry.
import { copyFileSync, existsSync, mkdirSync, readFileSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot: string = dirname(fileURLToPath(import.meta.url));
const source: string = join(repoRoot, "assets", "entry.png");
const output: string = "/output/entry.png";

// Gate check, mirrored from the bounty rules: a whole PNG, 1024x1024,
// at most 1 MiB. PNG signature + IHDR width/height read from the header.
if (!existsSync(source)) {
  throw new Error(`missing entry image: ${source}`);
}
const header: Buffer = readFileSync(source).subarray(0, 33);
const pngSignature: Buffer = Buffer.from([
  0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a,
]);
if (!header.subarray(0, 8).equals(pngSignature)) {
  throw new Error("entry image is not a PNG");
}
const width: number = header.readUInt32BE(16);
const height: number = header.readUInt32BE(20);
if (width !== 1024 || height !== 1024) {
  throw new Error(`entry image must be 1024x1024, got ${width}x${height}`);
}
if (statSync(source).size > 1_048_576) {
  throw new Error("entry image exceeds the 1 MiB gate");
}

mkdirSync(dirname(output), { recursive: true });
copyFileSync(source, output);
