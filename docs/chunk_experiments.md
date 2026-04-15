# Chunk Size Experimentation — JagUnify

## Objective
Test how different chunk sizes affect retrieval accuracy in the RAG pipeline.

## Tested Configurations
- Chunk Size: 512 | Overlap: 50
- Chunk Size: 1024 | Overlap: 100
- Chunk Size: 2048 | Overlap: 200

## Results Summary

| Chunk Size | Accuracy (20 test cases) | Observations |
|-----------|--------------------------|-------------|
| 512 | Medium | More precise chunks but sometimes misses context |
| 1024 | High | Best balance between context and precision |
| 2048 | Low | Too much noise, less accurate retrieval |

## Conclusion
Chunk size **1024 with overlap 100** performed best overall. It provided enough context without introducing too much irrelevant information.

## Decision
Use:
- Chunk Size: 1024
- Overlap: 100

for the final system.
