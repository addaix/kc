# Open decisions

Companion to [`docs/plan.md`](plan.md). The plan says what v1 builds; this says what it deliberately does not decide, and what would decide it.

Four parts per entry: **Question**, **Options**, **Settled by** — an experiment, a measurement, a document or a number, concrete enough to act on — and **Seam**, the one argument holding it open, or `none — inlined` where the decision was taken instead of deferred. An entry unresolved after two quarters is evidence the question was not load-bearing; close it as inlined.

**Revised after the panel's missing fourth argument was heard.** The plan no longer specifies a distribution: the contract lands in `i2mint/ir`. D1, D3, D4, D5 and D6 changed as a result; D13–D23 are new.

---

## Placement — the decision the exchange reopened

### D13. Does an access-control vocabulary belong inside `ir`

**Question.** `ir` is offline, local-first and single-user by declared policy (`ir/policy.py:41`). Landing `Grant`, the reserved fields and `guarded()` there is now the plan; only the owner can accept or refuse it.

**Options.** (i) Accept — ~200–300 lines against 9,655, no new dependency, turning a property `ir` maintains for speed into a tested security property. (ii) Refuse as scope creep.

**Settled by.** The owner, in writing, on one issue, **before any code**. `ir` already ships `select.disclose` and `test_retrieve_guards.py`, so a what-may-be-shown vocabulary is not foreign there. A written refusal is the single condition that revives kc as a distribution.

**Seam.** none — a routing decision, and the load-bearing one.

### D23. If `ir` refuses, where does the wrapper live

**Question.** A refusal under D13 leaves the contract homeless.

**Options.** (i) `priv`, beside `claude_transcripts` and `align` — zero-dependency, already home to the `Finding` shape the checks adopt and to the weekly channel that reads them. (ii) Its own distribution. (iii) `lacing` — struck: provenance vocabulary but no retrieval operator, and its Postgres store already answered the access question by binding `(owner_id, project_id)` at construction.

**Settled by.** How many repos consume the contract. One is a module; three with independent release cycles is a distribution. Today: zero, so (i) is the honest default.

**Seam.** none — contingent on D13.

---

## Blocked on the owner

### D1. Who publishes the distribution — moot unless D13 refuses

**Question.** Two corrections. PyPI `kc` belongs to the owner's **own second publishing identity**, so a transfer is self-service, not third-party-blocked — but that fleet is live (`kc` 0.0.7 shipped 2026-08-29, meaning "Utils for filtering"). `thorwhalen/kc` returns 404; the checkout has no remote.

**Options.** (i) Transfer repo and project. (ii) Publish from the second identity. (iii) A different name. (iv) Nothing — it lands in `ir`.

**Settled by.** D13. Under (iv) this entry retires unanswered, its most likely end. If a distribution survives, the credential work moves **ahead of the first commit** as a `manual-task` issue, not to first release.

**Seam.** none — a credential fact, contingent on D13.

### D21. If revived, the `kc` name or a new one

**Question.** Taking `kc` means removing a package from an active fleet's publish ledger and changing what `pip install kc` means for anyone who depended on it.

**Options.** (i) Take `kc`. (ii) A new name; leave 0.0.7 alone.

**Settled by.** Whether the published `kc` has downloads attributable to a real consumer. None → (i) is clean; any → (ii), since a semantic hijack is not worth a parked name. Deciding before a first release costs one command; after, a yank.

**Seam.** none — contingent on D13.

---

## Boundaries with packages that already exist

### D2. Where write and consolidation semantics live

**Question.** The capture path overlaps `raglab#6` (PurposeStore) — OPEN, ADR'd, specced, already claiming purpose-indexed writes, consolidation and a supersede ladder by name.

**Options.** (i) Stay read-side, owning no write verb. (ii) Take the write verb and close `raglab#6` in the same PR. (iii) Both ship.

**Settled by.** (iii) is struck on sight: two memory layers in one fleet is how they start disagreeing. Otherwise mechanical — if binding grants is a modified `metadata_of` plus a folded change signal with no second write path, (i) holds by construction, and `grants_of=` as a constructor keyword is not an ingest path.

**Seam.** none — inlined as (i).

### D3. Shared storage — and what `ir#28` actually is

**Question.** **Correction.** The old entry called `ir#28` "shared, multi-user storage". It is *"Evaluate unifying ir storage behind vd.Collection — DEFERRED"*, with no multi-user content at all.

**Options.** (i) Wait, and say so. (ii) Land the real shared-storage work upstream. (iii) A shared store of our own.

**Settled by.** (iii) is refused outright: a third indexing and invalidation core in a fleet that has two. Otherwise the number is how many distinct principals read one corpus (D20). `ecosystem.md`'s gap ranking (3) carries the same error and is owed the same correction.

**Seam.** `retriever` — a shared-store collection lands behind the same argument.

### D4. Whether a second consumer exists — the kill condition fired

**Question.** The old entry gave `reelee` one quarter and named its own kill condition: *"if that consumer lands enforcement inline instead… a reason to delete rather than argue."*

**Options.** (i) Wait to be adopted. (ii) Propose the wiring upstream.

**Settled by.** **Already, against the package.** `reelee/authz.py` (824 lines) and its 168-line MCP middleware shipped a per-caller capability chokepoint in production. Honest qualification: `reelee` solved a *different* problem — capability authz over projects at a tool boundary, never touching a ranker — so it does not refute the problem, only settles the *placement*.

**Seam.** none — the evidence arrived.

### D14. Who claims shared multi-reader storage

**Question.** With `ir#28` confirmed unrelated, the multi-principal precondition was deferred to an issue that will never deliver it. Nobody here claims shared, multi-reader corpus storage.

**Options.** (i) File the real issue against `ir`, scoped to a second reader. (ii) Record that none is planned.

**Settled by.** One reading of the roadmap. (ii) settles D5 and D20 by inspection and means only patch 1 lands — a legitimate outcome, not a failure.

**Seam.** none — bookkeeping with a consequence.

---

## The enforcement claim

### D5. Is this fleet actually multi-principal

**Question.** The contract is ceremony unless real queries resolve to more than one principal. **The old day-one answer does not survive verification:** `sessions` is absent from `~/.config/ir/corpora.json` and its directory is a 0-byte scaffold, so it would have had to be built in order to be guarded.

**Options.** (i) Two accounts on one machine. (ii) Client corpora beside personal ones. (iii) Neither, in practice.

**Settled by.** (i) fails: the split's own SSOT documents a **billing** boundary — "same person, same way of working" — whose failure mode is spending the wrong subscription. (ii) fails: separate indices, and an ACL cannot refuse an authorized caller. So (iii) holds today, and the ninety-day retrospective becomes a pre-condition (D20).

**Seam.** none — the kill criterion, now measured before the code rather than after.

### D20. Name the second principal, the corpus, and the reader

**Question.** Patches 2–3 are gated on three blanks: a second human or machine, one corpus both read, and a reader who is not the author.

**Options.** (i) A named engagement with a named second reader. (ii) An agent as a distinct principal (D15). (iii) No third answer.

**Settled by.** Writing the three names down. If they cannot be written, only patch 1 lands. It costs nothing and is the difference between a module and a deletion cycle.

**Seam.** none — a pre-condition, deliberately not a parameter.

### D15. Is an agent a principal distinct from the human who launched it

**Question.** A subagent handed a reduced principal set over `discover`'s corpus list is the one multi-principal story that survives verification: the human holds every grant, the agent need not.

**Options.** (i) Agents inherit the launcher's principals — then there is one principal. (ii) An agent is its own caller, making context hygiene an authorization question rather than a scoping one.

**Settled by.** Whether an agent ever receives a corpus list the human would not have typed. If yes, D20 has an answer nobody has written down.

**Seam.** `principals_of` — an agent id is just another caller key.

### D6. Whether the pre-filter guarantee stays true

**Question.** The central claim is borrowed: `ir` narrows to candidates with the hard filter and *then* builds the lexical index over those candidates only. Nothing in `ir`'s suite pins that ordering as a security property; it is there for speed.

**Options.** (i) Assert at construction and trust. (ii) Assert and pin with an external test. (iii) `ir` owns the guarantee.

**Settled by.** **(iii), taken.** The old entry called it "the long-run answer"; the exchange showed the long run had started. The leakage test lands in `ir`'s suite as patch 1, where a regression goes red in the repo that caused it — worth landing at zero principals, since under the old plan it would have died with the package at its own 90-day gate.

**Seam.** the `prefilters` assertion — a refusal, not a warning.

### D19. What closes the unfiltered read paths

**Question.** `guarded()` closes `search` and `discover`. Three other read paths take no caller and are exported from `ir.__init__`: `records_for_artifact` (accepts a bare corpus *name*), `expand` (every sibling, through the ledger), `traverse` (no `filter` parameter at all).

**Options.** (i) Carry the caller through every read path. (ii) Narrow the claim to the guarded surface and list what stays open. (iii) Enforce beneath all of them, at the store read boundary.

**Settled by.** Whether `expand` sits on a consumer's path — it does, via `select` / `disclose`. That points at (iii), the only option that does not go stale as `ir` grows read paths.

**Seam.** `retriever` — but (iii) sits below it, which is the argument for taking it seriously.

### D16. Should `guarded()` refuse a corpus with unstamped records

**Question.** A record missing the allow field fails `$in` and so fails **closed** — the right direction. But a corpus the caller silently half cannot see is indistinguishable from a genuinely private one.

**Options.** (i) Serve it and report via `records-stamped`. (ii) Refuse at **bind** time.

**Settled by.** Whether a partially-stamped corpus is ever legitimate. If not, (ii): fail at bind, where someone is watching, rather than at query, where nobody is.

**Seam.** none — a constructor-time check, cheap either way.

### D7. What an ACL change costs

**Question.** Folding a grant fingerprint into the change signal re-runs the whole indexing strategy for every artifact whose permissions moved, not just its metadata.

**Options.** (i) Accept it; the content-hash embedding cache makes the re-embed nearly free. (ii) A metadata-only restamp path.

**Settled by.** Time one reconcile pass after moving grants on 10% of a real corpus. Seconds → (i); a minute → (ii), now D18 and worth asking for regardless.

**Seam.** none — inlined as (i), with the measurement as trigger.

---

## Cost and measurement

### D17. Is the per-principal lexical index the binding constraint

**Question.** `_candidate_key(surfaces, filter)` (`ir/retrieve.py:136-146`) puts the serialised filter in the BM25 cache key, so every distinct principal set builds its own index over its own candidates.

**Options.** (i) Per-record set membership over one index. (ii) Permission-homogeneous collections — what the evidence names as standard practice, and what this fleet **already has**: every corpus a separate directory with its own BM25 and dense matrix.

**Settled by.** Measure now, on the real `skills` and `packages` corpora with two synthetic principal sets, rather than waiting for kill criterion #4 to fire. If (i) is the memory constraint it looks like, adopting it moves this fleet from the recommended shape to the documented fallback — an argument against the per-record design, not a tuning note.

**Seam.** none — a corpus-layout change, not a parameter.

### D18. Should the metadata-only restamp land regardless

**Question.** A restamp path skipping the indexing strategy serves any metadata change, not only a permissions change.

**Options.** (i) Land it with the grant vocabulary. (ii) Land it independently, now.

**Settled by.** It is the cheaper of the two things the old plan asked `ir` for and has a consumer whether or not D13 is accepted. (ii), unless D7's measurement says the cost is already seconds.

**Seam.** none — an upstream improvement with its own justification.

### D22. Does the corpus-statistics channel exist in dense retrieval

**Question.** Every published attack targets BM25/TF-IDF. Whether a shared ANN graph leaks through traversal behaviour or the k-th neighbour distance is unstudied **in both directions** — the research records this as one of three claims traceable to no primary source.

**Options.** (i) State it as a known limit in the test's docstring and the README. (ii) Measure it on the existing `skills` corpus.

**Settled by.** `ir`'s defaults are dense and hybrid, so the test's score-equality assertion is strong for the lexical leg and unvalidated for the dense. (i) is owed immediately and costs one paragraph; (ii) is a research project, worth naming as unbuilt rather than implying it is done.

**Seam.** none — a documented limit.

---

## Authorization

### D8. Where principals come from

**Question.** A caller resolves to the principal ids bound in the index; the default is a committed `caller → principals` mapping.

**Options.** (i) The static mapping. (ii) A relationship store queried subject-side (SpiceDB, OpenFGA). (iii) A policy engine compiling a rule into a filter (Cerbos `PlanResources`, OPA Compile to UCAST) — all Apache-2.0, and (iii) already emits the fragment.

**Settled by.** Principals-per-caller, with the documented ceiling sitting where we never go. Object-side listing is what breaks: `ListObjects` returns whatever it found inside a 3 s deadline up to 1000 results, with no cursor and no truncation flag — silently dropping documents the user *is* entitled to see. Subject-side, the ceiling is only how many ids fit one predicate; v1 raises past its cap rather than truncating, and the first raise is the evidence that (ii) or (iii) is owed.

**Seam.** `principals_of` — one argument, two named permissive replacements.

### D9. How permission moves are learned

**Question.** Reconciliation needs to know whose grants changed.

**Options.** (i) An id-only sweep recomputing grants without refetching bodies — cheap, and it detects deletions. (ii) A relationship change feed.

**Settled by.** (ii) is not yet a real option and must not be a seam: both candidate feeds stream *relationship* changes, and the fan-out to "these grants changed" is unbuilt everywhere. A seam's replacement must already exist; this is raw material.

**Seam.** none — inlined as (i), both feeds named so the later addition is an ADD at an existing boundary.

---

## Representation

### D10. Conflict: claims-with-rank or latest-wins

**Question.** When two versions of one unit disagree, does the store hold both as ranked claims, or does the newest win with an audit trail?

**Options.** (i) Latest-wins per `(source, unit)`, every version retained and provenanced. (ii) N claims per property with per-claim provenance and a three-valued rank.

**Settled by.** The base rate of contradiction on the real corpus, counted mechanically before any schema is frozen. A handful → (ii) is machinery for a problem this corpus does not have. No study shows a conflict-preserving store beating latest-wins downstream, so (ii) needs the base rate *and* a downstream win.

**Seam.** none — inlined as (i), with the count exposed as a report.

### D11. Retrieval configuration

**Question.** Dense, lexical or hybrid; what *k*; rerank or not.

**Options.** All of them — the retrieval layer implements each, and the guard scores nothing.

**Settled by.** Nothing the guard can produce, which is the point: no public dataset pairs a corpus with per-principal ACLs and relevance judgements. What may honestly be reported is corpus-specific — recall@k against the *authorised* ground truth, never the global one.

**Seam.** `retriever` — configuration belongs to the wrapped thing.

### D12. Whether existence is part of the secret

**Question.** A filter over a shared index hides content, not presence.

**Options.** (i) Accept it and say so. (ii) Suppress counts or hash identifiers. (iii) A separate corpus per confidentiality boundary.

**Settled by.** (ii) is refuted, not merely unattractive — count suppression was broken in 1979, identifier hashing abandoned at internet scale. So the question is per-deployment and answerable in one sentence: *is the existence of this document itself confidential?* Yes → (iii); no → (i). Equally architectural: the index must sit inside the same permission boundary as the documents, because embedding inversion recovers 50–70% of input words as a bag of words.

**Seam.** none — inlined as (i), stated in the README.

---

## Taken and logged

Decided rather than deferred; recorded so nobody re-opens them without new evidence.

| Decision | Taken as | Why not a seam |
|---|---|---|
| **Placement** | Inside `ir`, as three patches, gated on D13. | The guarantee depends on `ir`'s pre-filter ordering, stamping point and merge order — a security property depending on another distribution's undocumented optimisation is a promise that stops holding silently. |
| **Reserved field prefix** | `_ir_allow` / `_ir_deny` / `_ir_grants_version`. | A corpus-format decision outlives whichever module writes it; a `_kc_` prefix stamped into every index would permanently cite a package the plan scheduled for possible deletion. |
| **Async** | Synchronous throughout. | Retrieval and embedding are sync end to end; an async layer would be the only one in a sync stack. Revisit when an HTTP surface with concurrent callers exists. |
| **Rule combining** | Deny-overrides, as set membership then set exclusion *inside* the filter. | An (allow-set, deny-set) grant has one defensible precedence, and expressing it inside the filter keeps it through native translation. |
| **Content-derived predicates** | Refused at construction, naming the two policy engines that replace them. | The replacement half of the `principals_of` seam. Silently reducing a predicate to a set over-grants; raising does not. |
| **Field- and passage-level visibility** | The record is the unit. | No shape in the evidence and no second implementation to point at. |
| **Maintenance checks** | Three security assertions — pre-score enforcement still asserted, grants resolving to nobody, every record stamped. Report-only, weekly. | Age and disuse are curation, and curation that requires discipline starves. A query log is itself sensitive: it records what each principal asked. |

---

*Evidence for every claim is in [`docs/detail/`](detail/): permissions and the pre-filter argument in `research-permissions.md`, conflict in `research-conflict.md`, retrieval evaluation in `research-retrieval.md`, failure mechanisms in `research-failure.md`, licence verdicts in `ecosystem-full.md`.*
