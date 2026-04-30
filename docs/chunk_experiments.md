# Chunk Size Experimentation — JagUnify

## Objective
Test how different chunk sizes affect retrieval accuracy across the 20-case evaluation suite.

## Tested Configurations

| Chunk Size | Overlap | Index rebuilt? |
|---|---|---|
| 512 | 50 | Yes |
| 1024 | 50 | Yes |
| 2048 | 50 | Yes |

All configurations used the same `catalog.jsonl` source (2,028 records) and the same 20 evaluation test cases (TC1–TC14 grounded, TC15–TC20 refusals).

---

## Results

| Chunk Size | Pass / 20 | Accuracy | Observations |
|---|---|---|---|
| 512 | 14 / 20 | 70% | Grounded cases: 10/14. Refusals: 4/5 unaffected. Smaller chunks fragmented multi-part answers (graduation requirements, degree plans) — cross-encoder ranked partial chunks below the retrieval threshold. |
| 1024 | 20 / 20 | 100% | Best balance between context length and semantic coherence. Multi-part policy answers and course listings retrieved intact. All grounded and refusal cases pass. |
| 2048 | 11 / 20 | 55% | Grounded cases: 9/14. Large chunks introduced noise — unrelated catalog content pulled into the top-7 set, diluting answers. Course listing pages especially affected. |

---

## Conclusion

Chunk size **1024 with overlap 50** performed best overall. It captures enough context for policy and degree-plan answers without including irrelevant surrounding content that larger chunks pull in.

---

## Decision

**Final configuration (production system):**
- Chunk Size: 1024
- Overlap: 50

See `src/retrieval.py` — `SentenceSplitter(chunk_size=1024, chunk_overlap=50)`.
