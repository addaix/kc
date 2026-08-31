# Ecosystem: prior art, external and internal

142 external entries across nine clusters and 43 in-fleet packages, with every licence read from the LICENSE file and, where an artifact ships, from inside it. Full tables and references: [`docs/detail/ecosystem-full.md`](detail/ecosystem-full.md). The verdict distribution is the finding — **9 depend on it, 23 wrap it, 79 study it and move on, 31 avoid** — and nothing in the field is adoptable whole.

## (a) External ecosystem

Only the adoptable rows. **Bold** licences block commercialisable code.

| Project | Licence | Verdict | Why |
|---|---|---|---|
| [GEPA](https://github.com/gepa-ai/gepa) | MIT | **depend** | Offline prompt-program optimisation; zero dependencies |
| [pyoxigraph](https://github.com/oxigraph/oxigraph) | MIT OR Apache-2.0 | **depend** | The only graph store not copyleft, source-available or abandoned; one maintainer, so seam it |
| [curies](https://github.com/biopragmatics/curies) | MIT | **depend** | Canonical identifiers; attribution without them is unfollowable |
| [NetworkX](https://github.com/networkx/networkx) | BSD-3 (`NOASSERTION`) | **depend** | Reachability over hierarchies and derivation chains; never persistence |
| [docling](https://github.com/docling-project/docling) | MIT, Linux Foundation | **depend** | Per-element page/bbox provenance: a place on a page, not a filename |
| [ir_datasets](https://github.com/allenai/ir_datasets) | Apache-2.0 (loader) | **depend** | TREC-format fetching with per-dataset access terms |
| [MTRAG](https://github.com/IBM/mt-rag-benchmark) | Apache-2.0 (incl. corpora) | **depend** | Human-written multi-turn conversations with unanswerable turns |
| [cerbos query-plan-adapters](https://github.com/cerbos/query-plan-adapters) | Apache-2.0 | **depend** | Policy AST → store predicate; **throws** on inexpressible operators, since dropping one over-grants |
| [MCP](https://github.com/modelcontextprotocol/modelcontextprotocol) + [`mcp`](https://github.com/modelcontextprotocol/python-sdk) | Apache-2.0 / MIT | **depend** | A URI-addressed subscribable namespace is a `dol` Mapping as a protocol — but no query primitive and no attribution model, so kc's query surface must be a *tool* |
| [graphiti-core](https://github.com/getzep/graphiti) | Apache-2.0 | wrap | Alone in saying a fact *was* true until March — but wants the whole retrieval path, and its vendor killed one OSS edition |
| [LlamaIndex](https://github.com/run-llama/llama_index) + readers | MIT | wrap | The only broad permissive catalogue; no owner, ACL or deletion detection |
| [DSPy](https://github.com/stanfordnlp/dspy) | MIT | wrap | Exited retrieval, so a `dspy.Module` can call `ir`; hard-depends on litellm |
| [prov](https://github.com/trungdong/prov) | MIT (PyPI: none) | wrap | Zero deps; an optional `kc[prov]` export, never kc's model |
| [OpenLineage](https://github.com/OpenLineage/OpenLineage) | Apache-2.0 (verified in wheel) | wrap | The vocabulary, not the client; DIRECT vs INDIRECT is its best idea |
| [pySHACL](https://github.com/RDFLib/pySHACL) + [rdflib](https://github.com/RDFLib/rdflib) | Apache-2.0 / BSD-3 | wrap | Path constraints pydantic cannot express; rdflib disqualified as storage (~1.89 KB/triple) |
| [airbyte-python-cdk](https://github.com/airbytehq/airbyte-python-cdk) | MIT | wrap | The incremental *engine* is MIT, in a different repo from the ELv2 catalogue |
| [dlt](https://github.com/dlt-hub/dlt) | Apache-2.0 | wrap | The permissive incremental-sync seam; keep its destinations away |
| [mcp-atlassian](https://github.com/sooperset/mcp-atlassian) | MIT (PyPI: none) | wrap | The Confluence/Jira normaliser, not the server |
| [SpiceDB](https://github.com/authzed/spicedb) | Apache-2.0 | wrap | Bulk APIs that **error** rather than truncate; a server, so take the client |
| [OpenFGA](https://github.com/openfga/openfga) | Apache-2.0, CNCF | wrap | Same seam, but `ListObjectsResponse` has no cursor or truncation flag: a long result silently becomes "you may see only these" |
| [Cerbos PDP](https://github.com/cerbos/cerbos) | Apache-2.0 | wrap | A condition AST for your own store — no N, no k; stateless, so ABAC only |
| [Open Policy Agent](https://github.com/open-policy-agent/opa) | Apache-2.0, CNCF graduated | wrap | UCAST: one dialect-neutral AST lowered into `vd`'s filters |
| [SEP-2640 ext-skills](https://github.com/modelcontextprotocol/experimental-ext-skills) | Apache-2.0 (Draft) | wrap | The emerging context-interchange standard — not A2A, not OASF; SHA-256 manifest |
| [Agent Skills spec](https://agentskills.io/specification) | Apache-2.0 | wrap | Own ~200 lines of validation; its missing provenance model is kc's hole |
| [llms.txt v2](https://llmstxt.org) | Apache-2.0 | wrap | MCP serves agents that connect; llms.txt those that only fetch |
| [EnterpriseRAG-Bench](https://github.com/onyx-dot-app/EnterpriseRAG-Bench) | MIT | wrap | Shaped like kc's problem (Conflicting Info / Completeness / Info Not Found), but LLM-generated and competitor-published |
| [BEIR](https://github.com/beir-cellar/beir), [FreshStack](https://github.com/fresh-stack/freshstack) | Apache-2.0 code; **BEIR's datasets grant nothing**, FreshStack's are CC BY-SA | wrap | BEIR's qrels format (the bundle includes MS MARCO); FreshStack's nugget-level qrels over corpora that cannot be redistributed |
| [TechQA](https://github.com/IBM/techqa), [CUAD](https://huggingface.co/datasets/theatticusproject/cuad) | Apache-2.0 (HF card only); CC BY-4.0 (card metadata) | wrap | The only clean supply of real organisational writing — TechNotes with unanswerable questions, contracts with span-level gold testing *attribution*. Both licences rest on metadata fields |

**Refusals whose reason is instructive.**

| Project | Licence / state | The lesson |
|---|---|---|
| [Singer taps](https://github.com/singer-io) | **AGPL-3.0** | The protocol lib, SDK and Meltano are permissive, every singer-io tap is AGPL, and so is `MeltanoLabs/tap-salesforce` by fork lineage — "use the fork" is no mitigation |
| [owlready2](https://bitbucket.org/jibalamy/owlready2) | **LGPL-3.0 shipping an AGPL Pellet** | Disclosed by no metadata anywhere; found only in the sdist |
| [PyAirbyte](https://github.com/airbytehq/PyAirbyte) | **ELv2**; PyPI declares **no licence** | Metadata concealing a source-available licence |
| [OpenMetadata](https://github.com/open-metadata/OpenMetadata) | Repo Apache-2.0, **wheel is a Collate CLA** | Its non-compete covers kc's space and terminates on breach |
| [Memgraph](https://github.com/memgraph/memgraph), [Morphik](https://github.com/morphik-org/morphik-core) | **BSL / BUSL-1.1** | One grant forbids what a shipped kc does; the other expires at US$2,000/month revenue, terminating when kc starts working |
| [MS MARCO](https://microsoft.github.io/msmarco/), [anthropics/skills](https://github.com/anthropics/skills) | **Non-commercial** (HF says `cc-by-sa-4.0`); **no root LICENSE** | Metadata flatly wrong about the dataset most dense retrievers trained on; a 172.8k-star skills source with no grant. kc must demand a licence per ingested item |
| [neo4j driver](https://github.com/neo4j/neo4j-python-driver), [kglab](https://github.com/DerwenAI/kglab) | Permissive over a **GPL-3.0 server** / **GPL-2.0 igraph** | Transitive closure decides: a bundled application sets your licence |
| [Kuzu](https://github.com/kuzudb/kuzu), [Quivr](https://github.com/The-Vibe-Company/Quivr), [Cognita](https://github.com/truefoundry/cognita), [Verba](https://github.com/weaviate/Verba), [oso](https://github.com/osohq/oso), [Letta](https://github.com/letta-ai/letta) | Permissive; archived, orphaned or deprecated | 39.4k stars is a monument, not a signal: two reference RAG frameworks archived by their own sponsors, oso 2.5 years without a release on the security path, Letta's upstream calling its own source not-for-production |

**The licence landscape.** Package metadata disagrees with the LICENSE file often enough to change a verdict: reading the file — and, where an artifact ships, the licence *inside it* — changed the answer eleven times, three of which would otherwise have put an unusable licence into a commercialisable product (OpenMetadata's repo is Apache-2.0; its wheel is a Collate CLA). The expected AGPL is absent from the provenance cluster, sitting instead in applications with a paid cloud — Basic Memory, Khoj, where §13 fires on *network interaction*, so a hosted kc linking either owes complete source to every user — and in the Singer taps. **Source-available is the larger, growing risk**: seven equally unusable blockers, two relicensed *from* permissive terms.

**Every project bundling its own vector store also runs a paid cloud** — mem0, cognee, Zep, Basic Memory, txtai, Morphik, SurfSense, Onyx, Dify, RAGFlow, Open WebUI, Mastra — so bundling is the moat, and "adopt the framework" and "keep the fleet's own storage" are mutually exclusive. And **the paywall lands exactly on the two capabilities kc would need**: Onyx open-sourced all 55 connectors while fencing its ACL mirror and query-time censoring in a proprietary `ee/`; SurfSense fenced its connectors behind BUSL; Nango's OAuth engine is ELv2; Mastra's carve-out runs through `auth/ee`. Fetching content is commoditised; knowing who may see it, and holding the credentials to keep asking, is not.

## (b) What the profiled brains actually are

Re-checked against primary sources at fixed commits. The profile table's fifth row, the publisher's own product, is absent by construction: no repository, no package, no source, so nothing about it can be verified — which is that row's finding.

| System | Confirmed | Refuted | Unverifiable |
|---|---|---|---|
| **mem0** | Append-only, and more so than claimed (the ADD/UPDATE/DELETE loop is orphaned); scopes are filters, not authorisation | Decay (`decay=True` **raises** in OSS); "no keyword or entity signals" (the ranker is hybrid); "no correction path" | Its 92.5 LoCoMo / 94.4 LongMemEval; third parties cluster at 61–63% |
| **Zep / Graphiti** | Four timestamps per edge on two axes; contradiction detection scoped to one top-10 search; no decay | "Expire, never delete" (`DETACH DELETE` at four granularities); invalidated edges return **by default**; "sub-second" (paper: 2.58–3.20 s) | Model calls and latency per episode; published by nobody |
| **Letta** | The unit is literally a reserved section of the context window; memory and agent services are one component | "The licence changed" (Apache-2.0 throughout); "inseparable from the agent loop" — false at the data layer | Why the server was archived; how Cloud stores state; any independent benchmark |
| **DIY: Markdown + git** | Serve is lexical (bundled ripgrep); the path *is* the schema; citations are free; compaction never prunes the corpus | "No connectors" (MCP and hooks ship); "inherits CI" — 23.0% of a 356-repo sample carries stale references | **Lexical vs dense recall on a real Markdown corpus — the number kc needs, measured by nobody** |
| **Gorgias Cortex** | dbt into BigQuery with **native** `VECTOR_SEARCH`; BM25 lookup at ~8 ms, recall@10 = 0.88; maintenance emits PRs | "~12k typed nodes with typed edges" is one frame of a system reshaped twice in six months; most reads are agent-written SQL | Whether retrieval is ACL-filtered per asker; what maintenance costs |

**Component versus application.** mem0 bundles an extraction prompt, an embedder, ~25 vector backends, an entity store and paid-feature telemetry; Graphiti is a library over an application (Neo4j/FalkorDB/Neptune) whose write cost is O(entities + edges) LLM calls; Zep ships nothing; Letta's Python server was **deleted from `main`** on 2026-08-15; DIY is a pattern over git and ripgrep; Cortex has no repository. **Two of the five are libraries, three have no library at any tier, and none is a component at the grain a facade needs** — neither mem0 nor Graphiti gives you its ranker without its extractor. The genuine components live one layer down: the grain `vd` and `ef` already face.

## (c) Does a facade over these make sense?

**The `vd` disanalogy.** Every `vd` backend implements the *same primitive* — approximate nearest neighbour over a fixed-dimension vector under a named metric — and differs only in syntax, so translation is lossless. These five agree about nothing at that level, starting with what a memory *is*: an LLM-extracted sentence (mem0), a typed edge with four timestamps (Graphiti), a prompt segment never retrieved because it is always present (Letta), a lexical span at `path:line` (DIY), a BigQuery row routing a human review (Cortex). An empty result means five incompatible things. Both shapes fail: **the union** is a dispatch table with five type systems glued to it; **the intersection** is store text / retrieve text, which is `ef` plus a `MutableMapping`.

**The in-fleet cautionary precedent is `ayn`** — the same shape one domain over, now with no `tests/`, searchers returning `[]`, three controllers literally `pass`, zero consumers. What separates it from `vd` is five checkable properties: same primitive, a real consumer calling through, adapters that connect, a vocabulary rather than a shrug for "cannot do that", an escape hatch. **`aix` is no precedent either** — one backend, litellm, itself the aggregator.

**Verdict: face capture and retrieval, not whole systems.** They generalise because they are *verbs*: a lossy `ingest` returning a receipt **and** a verbatim `put`; retrieval with capability checked at the boundary and able to **fail the call**. Representation and maintenance are *nouns and policies* — `prune()` is nothing on DIY, a pull request on Cortex, a `DETACH DELETE` on Graphiti — so declare representation, and model maintenance as a registry of named policies.

## (d) Internal prior art

Forty-three packages surveyed by reading source, running test suites and importing public surfaces. **Nearly every capability a "knowledge context layer" implies is already built, tested, published, and mostly consumed in production here.**

| Capability | Owner | State |
|---|---|---|
| Persistence, namespacing, codecs, caching, composition | `dol` | Shipped — zero deps, 86 dependents |
| Content-addressed blobs (`ContentRef`, `ContentAddressedStore`) | `dol.content` | Shipped, wire-compatible with zodal's TS `ContentRef` |
| Record/CRUD/query layer (filter/sort/paginate) | `dol` | **Designed-but-unbuilt** — [dol#80](https://github.com/i2mint/dol/issues/80) OPEN; building it in kc duplicates a planned feature |
| Segmentation, 6-provider embedding, content-addressed invalidation, staleness/refresh, reranking, eval | `ef` | Shipped, consumed |
| ~15 vector backends, filter AST, canonical score contract, RRF + BM25 | `vd` | Shipped — the fleet's best facade precedent |
| Corpus contract; federated `discover` with per-source calibrated abstention before weighted RRF; attribution as `(source, artifact_id)`; disclosure; traversal; eval; MCP/CLI | `ir` | Shipped, daily use, 19.3k LOC — **the layer most people reaching for "kc" are describing** |
| Agentic loop: six injected role Protocols, budget governance, the back-edge | `raglab` | Shipped, zero consumers; a source is any `callable(query, **params) -> Sequence[ir.SearchHit]` |
| Uniform attributed catalog + pluggable search + MCP (`Card`, `Catalog`) | `toolery` | Shipped — **kc's stated unit and kc's stated shape** |
| PROV-O `Provenance`, W3C-Web-Annotation `Annotation`, `OpLog`/replay | `lacing` | Shipped, live in production |
| Transcript capture with egress scrubbing that **raises**; freshness predicates | `openloops` | Shipped, daily use |
| Source → markdown (doc sites, code, ~26 formats) | `contaix` + `dn` | Shipped, thinly tested — zero unit tests, two live bugs |
| GitHub as data; URL→bytes with cache; LLM access; MCP with a per-call middleware chokepoint; credentials; kind resolution | `hubcap`/`ge`, `graze`, `aix`, `py2mcp`, `config2py`, `i2.castgraph` | Shipped |

**Dependency direction: BESIDE.** The test is one sentence — *a correct position requires no published package to change*. BELOW fails four times (`dol` declares `dependencies = []` on purpose and gates PRs on an 89-dependent ledger; `ef`'s boundary forbids absorbing orchestration; `ir` is offline-by-default; `vd` would gain its first non-pyyaml dependency). ABOVE fails twice, both as "duplicate an assembly that already exists": `ir` *is* ef+vd with a corpus contract, `raglab` *is* ir with a control loop, `toolery` occupies the remaining slot. BESIDE passes: base edges to `dol`, `config2py`, `lkj`, `i2`, `aix` (**never `oa`**) and `py2mcp`, with `ef`/`vd` **transitive only through `ir`** — a direct `kc → vd` edge is evidence kc is redoing ef's or ir's job.

**The gaps, ranked — and the gap is small.** (1) **Access control, the only unclaimed one**: a grep across `ir`, `raglab` and `contaix` for `acl`/`permission`/`authoriz`/`tenant`/`principal` returns nothing, `lacing.ArtifactStore` says the access calculus is deliberately absent and belongs to a wrapping facade, and the seam is free because `filter` pre-filters before ranking in all three modes. (2) **Write/consolidation with bi-temporal validity** — claimed by [raglab#6](https://github.com/thorwhalen/raglab/issues/6), because raglab is the only layer that sees purpose; **close the loser**. (3) **Shared multi-user storage** — `STORAGE_BACKENDS = ('local',)`; unifying behind `vd.Collection` is [ir#28](https://github.com/i2mint/ir/issues/28), OPEN and deferred, fixable there with no new package. (4–6) **Fetch provenance** belongs upstream in `graze`, **connectors** are a to-do list, **async** is a decision.

## (e) What kc should compose rather than rebuild

- Storage, namespacing, codecs, caching; the record/query facade; content-addressed blobs → **`dol`** / `dol.content` (query layer = dol#80)
- Chunkers, embedders, embedding caches, the indexing/invalidation core, refresh, staleness → **`ef`** — two invalidation cores exist; a third is the predictable failure
- Vector adapters, filter language, score normalisation, rank fusion → **`vd`**, through `ef`/`ir`, never directly
- Retrieval, federation, citation identity, disclosure, abstention, traversal, eval, coverage → **`ir`**; the planner/evaluator loop and purpose-indexed memory → **`raglab`**
- Source → markdown → **`contaix`**/**`dn`**; GitHub as data → **`hubcap`**/**`ge`** (never the fourth GitHub client); URL fetch-cache → **`graze`**; Drive/Dropbox/SSH/Redis/Dynamo/SQL → the `dols` adapters; transcript capture → **`openloops`**
- MCP server, OAuth, audit middleware → **`py2mcp`** (never the third MCP path); `.mcpb` bundling → **`coact.publish`**; LLM calls → **`aix`**, not `oa`; credentials → **`config2py`**; kind resolution → **`i2.castgraph`**; plugin registry → **`skill.registry.Registry`**
- Provenance/annotation vocabulary → **`lacing`** — say what kc's model has that `lacing.Provenance` does not; if "nothing", build it there
- The uniform attributed catalog with pluggable search and MCP → **`toolery`**

## (f) The strongest argument that kc should not exist

**At full strength.** Every component of a knowledge-context layer is already built, tested and, where it matters, running in production here. Retrieval, federation, attribution identity, abstention, disclosure, traversal and coverage diagnostics are `ir` — 19.3k LOC, 430 tests, daily use. Ingest and content-addressed invalidation are `ef`; the vector backends and the contracts that make fusion work are `vd`; the agentic loop is `raglab`; provenance is `lacing`; chat capture with egress scrubbing is `openloops`; the audited MCP surface is `py2mcp`; the record/query layer is dol#80. The uniform attributed catalog with pluggable search and an MCP surface — **kc's stated unit and kc's stated shape** — is already shipped as `toolery.Card`/`Catalog`. Of the six remaining gaps, two are claimed by open issues, one belongs upstream, one is a to-do list, one is a decision. **That leaves exactly one unclaimed capability — access control — and it is a filter-field convention plus an enforcement wrapper over a pre-filter seam `ir` already applies. A convention plus a wrapper is a module, not a platform.** The fleet holds a fresh example of ignoring this (`ayn`) and a precedent for choosing not to build, ADR-013: *if you cannot state in one sentence which existing daily habit the thing displaces, do not build it.* Two exceptions raise the bar further: kc cannot be cheaply removed (already published at 0.0.8), and its failure mode is silent — a retrieval layer answering "nothing relevant" is the falsely-clean-slate failure the risk register calls worse than no ledger at all. And the fleet's last capture-discipline problem, a 100% miss rate over 8 of 8 sessions, was fixed **with prose, not with a store**.

**The strongest rebuttal.** Access control is not a feature; it is a *position*. Enforced anywhere but the retriever/store boundary it leaks through every facade above it, so it cannot be retrofitted into `ir` without `ir` becoming what it has declared it is not, and cannot be bolted onto four layers without four of them disagreeing. What no package owns and no issue claims is the *chokepoint*: where a principal, a policy and an attribution stamp are applied once, below which every retrieval path already funnels — `lacing.ArtifactStore` says exactly this in its docstring. The fleet's pieces are personal rather than organisational for exactly one reason (`STORAGE_BACKENDS = ('local',)`), so *access contract + shared addressability* is what makes a very good personal stack organisational.

**Verdict.** The gap is real but narrow: **kc's defensible v1 is a contract, not a platform** — a filter-field convention plus an enforcement wrapper at the retriever boundary, carrying a freshness envelope, BESIDE the stack and requiring no published package to change. Adding adapters over mem0/Zep/Graphiti before that contract is consumed by something real makes it `ayn`. Three preconditions gate the first commit, none of them code: name the single operation mem0/Zep/Letta all implement, with its identity, time and attribution models; decide raglab#6 and close the loser; write the kill criterion. Otherwise the right outcome is an access-control type emitted by `ir`, `contaix`, `hubcap` and `dn`, a patch to ir#28, and no new package at all.
