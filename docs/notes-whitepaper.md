# Notes on the "company brain" whitepaper

**Source and reading rules.** A ~40-page whitepaper from a vendor selling a team documentation product with an AI layer on top. It is marketing: the vendor popularised the category label, ran the survey it cites, chose which competitors to profile, and closes by showing its own product as one configuration of its own taxonomy. Claims carry a tag — `[evidence]`, `[vendor claim]`, `[folklore]` (repeated everywhere, sourced nowhere); unmarked sentences are *ours*. The survey (~149 self-recruited respondents, no sampling frame published) is `[vendor claim]` at best. What survives: the **taxonomy**, the **failure-mode inventory**, the **architecture profiles**. The category's claim is a layer reading across the systems a company already uses and answering from them, for people *and* agents — a redefinition making the category about **retrieval and upkeep**, not storage.

---

## The problem, as claimed

### The human half

| Claim | Tag and what's wrong with it |
|---|---|
| Knowledge sits in several systems at once (wiki, drives, chat, email) | `[vendor claim]` — multi-select summing ~312%, with "two or more systems" offered as a peer of the options it summarises. Only defensible reading: most respondents tick more than one box |
| Docs decay in a loop: written → relied on → reality moves → one wrong answer kills trust → someone forks a copy elsewhere | `[folklore]` — no decay half-life, no duplication rate, no trust measurement. The interesting direction (distrust *causes* fragmentation) is the unevidenced part |
| Interrupting a colleague costs them ~20 minutes of focus | `[folklore]` — the figure comes from task-resumption research on interrupting a *primary task*, not on answering a doc question. Borrowed, not derived |
| A shared layer takes "I need to know" from hours to seconds | `[folklore]` — no baseline, no task definition; the oldest line in the KM sales deck |
| A team brain is harder than a personal second brain | `[folklore]` as stated — though the real mechanisms (per-user permissions, contradicting sources, who owns upkeep) appear later only as survey worries |

### The agent half — the genuinely useful part

Same corpus, same rot, a different failure function: humans silently supply a judgement layer agents lack. Severities are `[folklore]`, but the taxonomy is a gift and every row is independently testable.

| Failure | Human cost | Agent cost |
|---|---|---|
| Tribal knowledge | a costly wait | the fact exists nowhere, and the hole is invisible |
| Missing caveat | one misapplied rule, caught on the spot | the rule applied uniformly at machine rate — an omission becomes policy |
| Conflicting channels | cross-checks the two versions | serves whichever ranks highest, as truth |
| Stale page | senses the page is old | 2024 and yesterday arrive with identical confidence |
| Silent teams | knows whom to ask | whole teams are invisible |
| Doc debt | drowns slowly | each stale page is a landmine |

Two claims worth carrying: **retrieval transfers authority from container to content** — a speculative draft is harmless while nobody finds it, authoritative the moment it is indexed `[folklore]`, one interviewee's hypothetical and the most actionable idea in the document; and **AI made bad documents expensive by finally finding them** `[vendor claim]`, an anecdote rather than a rate, but the mechanism holds.

---

## The four-component decomposition

Their skeleton: every brain is these four boxes with four options each `[vendor claim]` — basis "we looked inside a dozen", no list, no inclusion criteria, no method.

| Component | Options offered | What it actually decides |
|---|---|---|
| **Capture** | scheduled pulls · event capture · agent ingestion (LLM distils, stores a summary) · inference-time retrieval (store nothing) | freshness vs cost vs noise — and, buried in "agent ingestion", whether the write path is lossy |
| **Represent** | plain files · documents (owners + permissions) · vector index · knowledge graph | which questions become answerable later |
| **Maintain** ("dreaming and pruning") | consolidation runs · time decay · drift detection · human review queues | who owns truth, and how staleness gets noticed at all |
| **Serve** | chat with citations · hybrid search · headless API/MCP · purpose-built apps | who the caller is — three of these are surfaces and one is the engine |

**Real seams.** Capture and serve are genuine, and the chapter's best idea is that staleness has three independent causes — *age*, *disuse*, *contradiction with a live system* — each needing its own detector. That some systems deliberately run a human-readable tier *plus* a dense agent-only tier `[vendor claim]` is the true finding, and it contradicts the single-select picker they close with.

**Where it leaks.**
- *Capture is two axes in one row.* Pull-vs-push is **transport**, distil-vs-verbatim is **lossiness**; fusing them hides the only irreversible decision in the write path.
- *"Inference-time retrieval" is not a capture option* — it is the absence of capture, and picking it turns the other three rows into no-ops.
- *Representation is not a peer.* A graph forces entity extraction upstream and traversal downstream; plain files make drift detection nearly impossible. The pivot, not a column.
- *The maintenance row mixes three kinds of thing.* Consolidation and decay are **actions**, drift detection a **detector** that only flags, review queues an **authorisation policy** over what the others propose — detection / action / authority in one word.
- *"Users only touch the serve layer"* is contradicted by their own review queue, an inbox a human works daily.
- *The picker implies 4⁴ = 256 systems*, most incoherent — and their own selection takes the cheapest option in every row while the adjacent caption claims a capability it does not include.

**The missing fifth component: evaluation.** Nothing measures whether the brain answers correctly, so every decay policy is unfalsifiable and every capture choice is taste. Also missing: a **return arrow** (nothing writes a correction back to the stale source) and **conflict/identity resolution** — two sources disagreeing, one entity under two names — assumed away entirely.

---

## Real architectures from the field

| System | Capture | Represent | Maintain | Serve | The distinctive bet |
|---|---|---|---|---|---|
| **mem0** (OSS + hosted) | app-triggered `add()`; an LLM decides what to keep; no connector fleet `[vendor claim]` | vector index of atomic scoped facts (user/agent/session/org); no human-readable tier | append-only; staleness handled at *search* time by recency/frequency decay; no consolidation, drift check or review `[vendor claim]` | headless: SDKs + hosted MCP, hybrid ranking. No chat, no app | lossy on write, corrective on read — never resolve a contradiction, just rank one above the other |
| **Zep / Graphiti** (OSS engine + service) | push "episodes"; extraction plus contradiction adjudication per episode `[vendor claim]` | bi-temporal knowledge graph: episodes → typed entities/edges → communities; validity time *and* belief time | contradiction-driven invalidation only — expire, never delete; no decay, no human gate `[vendor claim]` | hybrid retrieval + graph traversal, claimed sub-second with no LLM in the read path `[vendor claim]` | two time axes per fact, so "what was true then" and "what did we believe then" are different queries |
| **DIY: Markdown + git** | authorship via PRs; subagents summarise into files. No connectors, no events | plain files in the code repo; the path *is* the schema | human review inside PRs, nothing else. Session compaction prunes context, never the corpus | grep/glob inside a coding-agent session; citations are free (path + line) | knowledge inherits the software-correctness apparatus — review, blame, revert, CI |
| **Gorgias Cortex** (in-house) | scheduled pulls (Airbyte + custom) over Postgres/Notion/Gong/GitHub/Linear/HubSpot; transcripts chunked and embedded `[vendor claim]` | ~12k typed Markdown nodes in a GitHub repo, typed edges `[vendor claim]` | reads the agent's own traces for gaps, clusters them, emits PRs a human merges `[vendor claim]` | an agent walks typed edges from a skill entry point until it judges it has enough | the knowledge graph *is* a codebase; every fact change is a pull request |
| **The whitepaper vendor's product** (closed) | connector sync over "20+ sources"; humans and agents write through the same door `[vendor claim]` | documents with owner, permissions, verification tag, expiry window — "docs stay the store" | auto fact-check against connected data → side-by-side diffs in a triage queue; nothing lands without a human verdict `[vendor claim]` | cited answers, hybrid search, read+write MCP | refuse a machine-native representation entirely; put all the intelligence in trust and upkeep |

*(Their own two pages disagree: the diagram shows scheduled pulls and review-queues-only, the prose says "live-syncs" and drift detection.)*

**mem0** — the extractor is an unrecoverable choke point: what it misses at write time is stored nowhere and the transcript is gone, so recall failures are silent. Append-only plus rank-decay means the store only grows and a wrong fact is never removed.

**Zep / Graphiti** — a visible disagreement becomes an invisible verdict: a model adjudicates, expires the loser, returns the survivor, no trace an election happened. Invalidation fires only on explicit contradiction, so facts that went stale *in silence* look exactly as current as facts genuinely superseded.

**DIY** — silent unbounded rot with a bus factor of one; wrong and right files grep identically. Four thresholds in order: vocabulary, audience (the first non-engineer), concurrency (two sessions write contradicting files, the merge succeeds), attention (the week the maintainer gets busy).

**Cortex** — the review loop scales with the graph, not the team, so the shape does not survive copying without a dedicated AI function. Nothing expires, nothing reconciles a node against its source, and the gap signal is retrospective by construction: it finds only context the agent visibly failed to find.

**The vendor's product** — the review queue becomes a second unread inbox; stop draining it and you have the same staleness plus governance metadata *asserting* a freshness nobody checked. Expiry is doc-granular while rot is paragraph-granular, and documents-plus-hybrid-search cannot answer the relationship and history questions their own taxonomy assigns to graphs.

### Does a facade over these make sense?

Partly — the honest facade is thinner than it looks.

**Serve / retrieval — YES; the seam that earns its keep.** `search(query, *, k, scope) -> [ScoredRecord]` spans all five, given two non-negotiables. The returned *unit* differs (inferred assertion, passage, owned document, subgraph), so the record needs `kind` and `provenance`, not a uniform `.text`: flatten those and a caller cannot tell an LLM's guess from a sentence a human approved — which is what decides whether it can be cited. And backend-specific arguments (`as_of`, `include_invalidated`, `traverse_from`) belong behind a declared capability set, an unsupported temporal query **raising** rather than silently degrading. Silent degradation is the one failure this facade must never permit.

**Capture — YES, with two conditions.** `ingest(payload, *, source, occurred_at, scope, metadata) -> IngestReceipt`, the receipt reporting created / updated / skipped / deferred-for-review. `occurred_at` (caller-supplied validity time) belongs in the *shared* signature, not a backend escape hatch: backends ignoring it lose nothing, Zep loses its reason to exist without it — carry the **union** of the cheap arguments, not the intersection. And do **not** type capture as `store[key] = value`: mem0's `add()` is a *proposal* an LLM may legitimately answer by storing nothing, so a `MutableMapping` facade promises a put the system never performs and the caller learns weeks later, as a missing memory.

**Represent — NO.** You can abstract *which backend*, not *what a memory is*: a graph answers "how are these two related" and a fact-vector store cannot, so a uniform `Memory` type makes non-substitutable systems look substitutable. A facade should only **declare capability** — `unit=`, `supports_relations`, `supports_documents`, `supports_temporal`, `has_human_readable_tier` — and let callers branch. Documents-with-ACLs are the sharpest case: reduce `store[key]` to "the text" and you have discarded permissions, ownership and trust state — that product.

**Maintain — NO, and a `prune()` would be worse than no facade.** These are four theories of who owns truth, not four implementations of one operation. The same call is a no-op on mem0 (maintenance lives in the ranker), an async background rewrite elsewhere, and on a docs- or git-backed system *the opening of a human approval workflow that may resolve next Tuesday or never* — one signature, three semantics, latency differing by orders of magnitude, no guarantee the write lands, no way to tell which you got. The honest surfaces: **descriptive** (a policy object answering "what happens to a six-month-old unused fact here?"), **observability** (what changed, when, by whom), and a return *type* rather than a method — `Applied` vs `Proposed(ref=…)`.

**One cross-cutting trap.** mem0's `scope` is a *retrieval partition*; a documents brain's equivalent is an *access-control boundary*. A single `scope=` spanning both turns a permissions system into a filter — a security bug wearing an abstraction's clothes.

**Net for kc: three seams, not four.** Face capture and retrieval; face representation's *read* path with a documented escape hatch to native capability; model maintenance as a registry of independently-named policies that *report findings* — the shape this repo's own `align`/`upkeep` checks already take — not a method on a store. Then add the seam nobody in the whitepaper has: **retrieval telemetry as an input to curation**, Cortex's best idea and homeless in their model.

---

## Lines of our own

> A stale page costs a human an hour of doubt and an agent a decision already executed.

> Retrieval didn't just make documents easier to find. It gave bad ones a price.

> When a model merges two conflicting accounts it isn't summarising, it's voting — and nothing in the answer says an election was held.

> Every knowledge system ever shipped had an undocumented dependency on a colleague you could ask.

> Build the review gate with a hinge: everyone calls it temporary and nobody can say when it opens.

> A store that answers questions about the world but not about itself can only be maintained by humans.

---

## Hype to discard

- **Every number from the ~149-person survey.** Two headlines are manufactured arithmetic: an "expectation" statistic that is two unrelated *definition* options added together, and a "serves people not agents" statistic that is everything except the agents-only bucket, over half of it an "all of the above" option. A third contradicts the pie chart beneath it by switching denominators; two questions disagree about how many respondents have heard the term at all.
- **"80% of operational knowledge is tacit"** — an unsourced chestnut. Keep the qualitative claim (connectors cannot reach what never entered a system); drop the number. Same for "agent queries will outnumber human ones by orders of magnitude".
- **"Background agents cannot exist without a company brain."** Circular by construction, falsified by every unattended bot running today on narrow context. Defensible version: unattended operation needs bounded blast radius, verifiable output, and the ability to abstain — abstention being the one a knowledge layer can supply.
- **The category-creation theatre** — a five-moment "lineage" of which three moments are the same month, sourced to a VC essay, an accelerator's president and that accelerator's request-for-startups.
- **"Every system decomposes into these four components"** as a finding, and the 4×4 picker as 256 buildable systems — a chosen taxonomy over an unnamed sample, whose four boxes describe every data system ever built (write path / storage / compaction / read path).
- **A chapter titled "who got burned" naming no incident, date or cost** — a fear inventory, not a post-mortem. And "we have already solved the hardest problems in retrieval and maintenance", two pages from the admission that the field has no shared benchmark.

---

## Questions still open

The per-system checklists are answered with sources in `docs/ecosystem.md`, and most measurable-effects questions are taken up in `docs/research.md`. What follows is what neither settled.

1. Is stale context actually the dominant failure cause for unattended agents, versus tool errors, spec ambiguity, compounding-step failure? If not, a knowledge layer is a component, not the centre of the story.
2. Does staleness metadata improve **abstention calibration** over score-separability alone? Checkable against `ir`'s existing abstention work; nothing published answers it.
3. Write-time LLM distillation vs verbatim storage plus retrieval-time distillation — accuracy, cost, and where it crosses over. Sets kc's `extract` default; unmeasured at organisational corpus sizes.
4. Grep/lexical vs dense/hybrid recall on a realistic Markdown corpus (CLAUDE.md, runbooks, skills) — the number deciding whether kc's retrieval layer earns its cost. No public benchmark for organisational knowledge retrieval has been found at all, so it must be measured here and every retrieval choice stays a bet.
5. Does ACL-correct retrieval need per-principal index partitions, or is query-time filtering correct and performant — and what leaks via ranked-list side channels (a filtered-out doc still moving scores, counts, or a "no results" signal)?
6. Do any of the profiled systems revoke *derived* artifacts — embeddings, graph edges, cached answers — when a source ACL changes? If none do, that is a gap kc could occupy, designed in rather than added.
