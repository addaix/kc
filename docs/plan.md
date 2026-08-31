# The plan: a visibility contract, landed in `ir`

## 1. The decision, and what changed

**This document previously specified kc as a new ~500-line distribution. It no longer does, because the panel that produced that verdict never heard the case against building anything.** A fourth proposal had been assigned to argue kc should not exist; it crashed, and the winner was chosen from three that agreed a package was owed and differed only in size. The missing argument has since been made and judged twice — once on architecture alone, once on whether the thing ships and survives a year — and both judgments went against the package. The **contract** survives almost verbatim. The **address** changes: it lands as a patch series against `i2mint/ir`, not as a distribution.

**The contract, unchanged.** A small reserved vocabulary of metadata fields bound into an index *at write time*, plus a wrapper at the retriever boundary composing them into a filter the caller cannot widen, forget or opt out of. Post-filtering is not access control with a latency penalty; it is a leak with a filter drawn over it, and the literature accepts one architecture: bind at ingest, filter inside the retrieval operator before any corpus statistic. Everything that follows is kept: the closure over **one** caller with no `principal=` to forget, refusal rather than degradation, an empty filter never returned on a failure path, deny-overrides as `$in` then `$nin` inside the filter, group *ids* bound and membership never expanded, and a leakage test asserting ids, float **scores** and result count.

**First: the decisive test measured coordination cost, not architectural fit.** The old §1 rested on *"a correct position for a new package requires no published package to change."* Applied consistently that can never return "improve what exists," because improving anything changes a published package. It is a generator of new distributions, not a test — and in a fleet whose own research names unstaffed maintenance as the dominant failure mechanism, that is the wrong instrument. The package it declined to change is `i2mint/ir`: same owner, same fleet, same machine. The cost it minimised is roughly one pull request.

**Second: the guarantee is borrowed from lines the wrapper cannot reach.** `ir/retrieve.py:427` narrows to `candidates` with the hard filter, and `_bm25_index_for` then builds the lexical index over the survivors only — that ordering is the whole contract, and `ir` maintains it for speed. The old §9 conceded as much by asking `ir` to pin the ordering as a test; if the *test* belongs in `ir`, so does the guarantee. Three further verified facts, each unreachable from outside:

- **The only unbypassable stamping point is inside `ir`.** `ir/index.py:182-183` passes `meta_extra` *into* `decompose(artifact_id, raw, meta_extra)`, and five of six shipped strategies splat `**meta` last into `filter_fields` — a convention, not a contract. A strategy ignoring its `metadata` argument drops the grant fields silently. (An unstamped record fails `$in`, so it fails **closed** — silent invisibility rather than a leak, but a corpus a caller half cannot see is its own failure.) Correct is to merge grants into `plan.filter_fields` *after* the strategy returns.
- **Surface metadata wins over filter fields.** `ir/index.py:211` is `{**plan.filter_fields, **dict(surface.metadata)}`, so a surface emitting a reserved key overrides a grant. Only fixable inside `ir`.
- **`guarded()` closes one door of at least four.** `ir.records_for_artifact` (`retrieve.py:636`) takes no filter and accepts a bare corpus *name*; `ir.expand` (`expand.py:201`) fetches every sibling through the ledger unchecked; `ir.traverse` (`traverse.py:105`) walks graph links with no `filter` parameter. All three are exported from `ir.__init__`. **The old §2 claim that "kc's own surface therefore has no unfiltered path" is retracted** — true of kc's surface, false of the corpus, and a wrapper closes only the doors it knows about while `ir` keeps growing read paths (D19).

**Third: there is no second principal, and the claimed day-one consumer does not exist** — §7 in full.

**Fourth, weakest but real: the distribution cannot ship.** PyPI `kc` is held by the owner's second publishing identity, published through 0.0.7 on 2026-08-29 meaning "Utils for filtering"; `thorwhalen/kc` returns 404; the checkout has no remote. Taking the name means editing a live fleet's publish ledger for a package with zero consumers, and landing in `ir` makes the question moot.

**The one condition that flips this back.** `ir` is offline-and-local-first by declared policy (`ir/policy.py:41`) and its owner could reasonably refuse an access-control vocabulary as scope creep. If that refusal is **in writing** (D13), the wrapper needs a home and a distribution is the honest answer. Ask before writing the code; it costs one issue, and `ir` already ships `select.disclose` and `test_retrieve_guards.py`, so a what-may-be-shown vocabulary is not foreign there.

**One caveat for the front page.** Every published corpus-statistics attack targets BM25/TF-IDF; whether the channel exists in dense retrieval is unstudied in both directions. `ir`'s defaults are dense and hybrid, so the leakage test's score-equality assertion is strong for the lexical leg and unvalidated for the dense (D22).

## 2. Scope of v1 — three patches, in order

**Patch 1 — the ordering pin. This week, alone, gated on nothing.** `tests/test_leakage.py` in `ir`'s own suite: index a corpus, record principal A's ids, **float scores** and result count, add a document readable only by B, assert all three identical. Scores rather than ids is what detects a regression to post-filtering. It is worth writing **at zero principals**, because it protects a property `ir` already has against `ir`'s own future optimiser — and under the old plan it was scheduled to die with the package at its 90-day gate. Two index fixes ship alongside: merge grants into `plan.filter_fields` *after* `decompose` returns, and raise on a reserved key in `surface.metadata` rather than letting it win at `ir/index.py:211`.

**Patch 2 — vocabulary and binding. Gated on D5/D20 naming a second reader and a shared corpus.** `Grant(allow, deny)` — frozensets of opaque, stable principal ids stamped as `_ir_allow` / `_ir_deny` / `_ir_grants_version`. `Grant.empty()` is visible to nobody: fail-closed by default. Group *ids* are bound; membership is never expanded. Binding arrives as `grants_of=`, a keyword on the `CorpusSource` constructors rather than a wrapper, because `bind_grants` was `dataclasses.replace(source, metadata_of=…, change_signal=…)` over two fields `CorpusSource` already declares (`ir/sources.py:74-82`) — inside, a constructor keyword; outside, a wrapping copy plus re-stamp coordination for zero gain. The change signal folds in a grant fingerprint so the ledger re-stamps when **permissions** move, not only text; `on_empty='warn'` counts fail-closed artifacts, since a broken connector and a genuinely private corpus otherwise produce the same silence.

**Patch 3 — enforcement.** `ir/guard.py`: `guarded(retriever, caller, *, principals_of=…)` returns a closure over **one** caller taking a query and nothing else. The visibility fragment is set membership (`$in` allow, then `$nin` deny, so precedence survives native translation by a backend), never a disjunction of equalities. `guarded` **refuses** any retriever not declaring `prefilters=True`, and a caller-supplied `filter=` naming a reserved field raises. Failure semantics are types, because an empty filter is permit-all and **no failure path may return one**. `reconcile_grants(source, corpus)` is an id-only sweep recomputing grants without refetching bodies, restamping what differs, detecting deletions, returning a monotonic `grants_version` a caller can require.

**Alongside patch 3, three checks in `priv.align`'s `Finding` shape**: `reader-enforcement`, `unreadable-records` (grants resolving to nobody — written, invisible), and **`records-stamped`**, which is new and names a *cause* the other two see only as a symptom. Report never repair; `unavailable` is a separate list from `findings`; one entry in the weekly `priv.upkeep.UPKEEP_CHECKS`. Better still, `guarded()` should refuse at **bind** time rather than serve a corpus with unstamped records (D16). No new surface: `ir` has a CLI and an MCP server, and the guard adds arguments to them.

**Patch 1 is done when** a deliberate reversion to post-filtering in `ir/retrieve.py` turns the leakage test red. **Patches 2–3 are done when** a search as caller X returns rows that caller Y does not and the probe reports `leaked=False` — with D20 answered first, so the corpus exists and X and Y are not two invoices for one reader.

## 3. Explicitly out of scope

| Excluded | Why | Owned instead by |
|---|---|---|
| Ranking, fusion, abstention, disclosure, traversal, federation | the guard never scores; it composes a `filter=` | `ir`, in modules this series does not touch |
| Vector storage, backend adapters, the filter dialect | plain dicts in vd's dialect; no new import | `vd` |
| Embedding, chunking, segmentation, reranking, embedding caches | a third indexing/invalidation core is the predictable failure | `ef` |
| Write/consolidation semantics, purpose-scoped stores, bi-temporal SUPERSEDE | claimed, OPEN, ADR'd, specced | `raglab#6` |
| Shared / multi-user corpus storage | **correction:** `ir#28` is *"Evaluate unifying ir storage behind vd.Collection — DEFERRED"* and holds no multi-user content, so the old row and `ecosystem.md`'s gap ranking (3) were wrong on both halves | nobody — file the real issue or record that none is planned (D14) |
| Provenance vocabulary, artifact catalog, blob store | its docstring asks for a wrapping permission facade; that facade is now `ir/guard.py` and still does not move in | `lacing` |
| Connectors and source acquisition | a to-do list of ~40-line `CorpusSource` classmethods, not architecture | `contaix`, `hubcap`, `dn` |
| Fetch provenance (ETag, `fetched_at`, content-type) | a local copy covers only what came through here | `graze` (upstream) |
| A uniform `Memory` type, or adapters over mem0 / Zep-Graphiti / Letta | they do not agree what a memory is; each bundles an embedder, a store and an extractor — each is an application | nobody, deliberately |
| `prune()` or any maintenance verb | one signature over three incompatible semantics, with no way to tell which you got | the findings registry |
| A registry of systems, a chooser, a drift verifier | the fields that actually rot are the ones a verifier cannot probe | `docs/detail/ecosystem-full.md` |
| Conflict adjudication, bi-temporality, supersession | bi-temporal modelling cannot hold live disagreement, and no study shows a conflict-preserving store beating latest-wins | measure the base rate first |
| Controlled vocabulary, entity resolution, knowledge graph | concept-only indexing measured far worse than plain text; graph indexing costs ~40–60× with no consistent return | nobody |
| Retrieval telemetry / query logging | a mechanism every search must feed, and a query log is itself sensitive | not built |
| `check_age` / `check_disuse` curation checks | discipline-dependent maintenance, the dominant documented failure mechanism | not built |
| Encryption, ORAM, existence hiding, count suppression, identifier hashing | refuted at internet scale; if *existence* is the secret, the answer is a separate corpus | not built |
| Prompt-injection defence, output filtering | probabilistic; not a boundary | not built |
| Any benchmark or comparative retrieval claim | no dataset pairs a corpus with per-principal ACLs and relevance judgements | not built |

## 4. The seams

Two. Both are one keyword argument, both default to something needing no new dependency, and both name replacements that exist today.

| Seam | Default (no new dependency) | Two concrete replacements | Question it defers |
|---|---|---|---|
| `principals_of` on `guarded()` — caller → the principal ids bound in the index | `static_principals(mapping)`: a `caller → principals` `Mapping` (a dict, a JSON file, any `dol` store), `unknown='raise'` so an unrecognised caller is never silently resolved to nobody | SpiceDB via `authzed`; OpenFGA via `openfga-sdk` (both Apache-2.0) — **subject-side only**, never `LookupResources` / `ListObjects` | Where group membership lives and who operates it — a deployment decision |
| `retriever` on `guarded()`, carrying `prefilters: bool` | the in-process `ir.discover` retriever, asserting `prefilters=True` on verified source behaviour | a `vd.Collection` retriever (several backends would declare `False` — which is the point); `toolery.Catalog(search_backend=...)` | Whether the corpus stays in-process. A remote index that ranks globally and trims must declare `False` and be **refused**, not quietly become a leak |

**NOT seams**, written directly on purpose: the metadata key names, the grant dataclass shape, the vd filter dialect, the combining algorithm, the CLI argument parsing, the report rendering, the check registry.

## 5. Deferred, not abstracted

- **`changes=` on `reconcile_grants`** — inlined as the id-only sweep. SpiceDB `WatchService` and OpenFGA `ReadChanges` stream *relationship* changes, not computed permission changes, and the fan-out is unbuilt everywhere, so neither implements the seam. Add the argument when one working fan-out exists.
- **`visibility_of` (a policy engine compiling a rule into a filter)** — Cerbos `PlanResources` and OPA Compile/UCAST are real and permissive, but this nests a second seam inside the first for one question. Inlined as `principal_filter`; a content-derived predicate is refused at construction, naming both, because a filter that silently drops a condition over-grants.
- **Rule-combining algorithm** — inlined as deny-overrides, `$in` then `$nin` inside the filter. **Field- and passage-level visibility** — the record is the unit; no shape in the evidence and no second implementation to point at.
- **Per-principal index partitioning** — a corpus-layout change, not a parameter, and the shape the evidence actually recommends. The fleet is *already* there: every `ir` corpus is a separate directory with its own BM25 and its own dense matrix. Per-record set membership is the weaker fallback for corpora that cannot be partitioned, and adopting it must not move this fleet from the recommended shape to the fallback one (D17).
- **A materialised permission view** — the scalable answer past ~10³–10⁴ accessible objects per principal, and **no permissive implementation exists anywhere**. **Embedding-inversion mitigations** belong in `ef`/`vd`; the architectural rule is documented instead — the index must sit inside the same permission boundary as the documents.
- **Async** — a decision: `guarded()` returns whatever the wrapped retriever returns; `ir` and `ef` are sync throughout.

## 6. The API surface

```python
# ir/base.py — vocabulary and errors, beside the corpus vocabulary already here.
ALLOW_FIELD, DENY_FIELD, GRANTS_VERSION_FIELD = '_ir_allow', '_ir_deny', '_ir_grants_version'
RESERVED_FIELDS = frozenset({ALLOW_FIELD, DENY_FIELD, GRANTS_VERSION_FIELD})
PUBLIC = '*'                      # a value, not a magic string
DFLT_MAX_PRINCIPALS = 1000
PrincipalId = CallerId = str      # opaque, stable, resolved OUTSIDE the index

class VisibilityError(Exception): ...
#  PrincipalsUnavailable (raised, never an empty list), PrincipalSetTooLarge (raised,
#  never truncated), UnenforceableRetriever, ReservedFieldError, GrantsStale,
#  UnexpressiblePolicy — all subclasses; no failure path returns a permit-all filter.

@dataclass(frozen=True)
class Grant:
    allow: frozenset[PrincipalId] = frozenset()
    deny: frozenset[PrincipalId] = frozenset()
    @classmethod
    def empty(cls) -> 'Grant': ...          # visible to nobody — the fail-closed default
    def as_metadata(self) -> dict[str, list[PrincipalId]]: ...   # sorted, JSON-able, stable
    def fingerprint(self) -> str: ...       # folded into the corpus change signal

@runtime_checkable
class Retriever(Protocol):
    prefilters: bool                        # a claim about the operator, not a hint
    def __call__(self, query: str, *, filter: Mapping | None = None, **kw) -> Any: ...

# ir/sources.py — one new dataclass field beside metadata_of and change_signal.
GrantsOf = Callable[[str, Any], Grant]      # + grants_from_field / grants_from_path helpers
@dataclass
class CorpusSource:
    ...
    grants_of: GrantsOf | None = None       # composes metadata_of + change_signal internally

# ir/index.py — grants merged AFTER decompose returns; a reserved key in surface
# metadata RAISES rather than winning the {**plan.filter_fields, **surface.metadata} merge.

# ir/guard.py — a retriever you cannot ask an unfiltered question.
PrincipalsOf = Callable[[CallerId], frozenset[PrincipalId]]
def static_principals(mapping, *, unknown: str = 'raise') -> PrincipalsOf: ...
def principal_filter(caller, *, principals_of, max_principals=DFLT_MAX_PRINCIPALS) -> dict:
    """{'$and': [{allow: {'$in': [...principals, PUBLIC]}}, {deny: {'$nin': [...]}}]}"""
def guarded(retriever: Retriever, caller: CallerId, *, principals_of: PrincipalsOf,
            max_principals: int = DFLT_MAX_PRINCIPALS,
            require_grants_after: str | None = None) -> Callable[..., Any]: ...

# ir/reconcile.py, ir/probe.py + the findings registry
def reconcile_grants(source, corpus, *, grants_of=None) -> ReconcileReport: ...
def leakage_probe(build, queries, *, caller, decoys, retriever_of) -> ProbeReport: ...
CHECKS = (check_reader_enforcement, check_unreadable_records, check_records_stamped)
```

## 7. First consumer — honestly, there is not one yet

**There is no day-one consumer, and claiming otherwise was this plan's worst error.** The old §7 named "the two Claude accounts on this machine, indexed into one corpus." That corpus is not registered — `~/.config/ir/corpora.json` holds exactly `skills`, `packages` and `reports` — and `~/.local/share/ir/corpora/sessions` is a 0-byte scaffold from 2026-08-06, so it would have had to be *built in order to be guarded*: the captive consumer D5 says defeats the weak test. And the boundary it would enforce is billing, not confidentiality: the split's own SSOT opens "same person, same way of working" and names its failure mode as spending the wrong subscription. There is one reader.

**The motivating hazard is real but an authorization filter does not close it.** `~/.local/share/ir/corpora/` holds `trufflepig_fmp` (4.0M) and `trufflepig_p2` (45M) beside the personal corpora, and `ir.discover` takes a *list* of corpus names, so a federated call naming one corpus too many returns client-confidential material into an unrelated context. But those are separate corpora with separate indices, the human who could type that name holds every grant, and an ACL cannot refuse an authorized caller. What closes it is scope hygiene. The one multi-principal story that survives scrutiny is absent from the plan entirely: an **agent** running `discover` over a corpus list is arguably not the same principal as the human who launched it (D15).

**`reelee` is precedent for placement, not a pending adopter.** Its 824-line `authz.py` and 168-line MCP middleware are a capability chokepoint over *projects* at a tool boundary, never touching a ranker or a corpus statistic — so not a refutation of this problem, but a demonstration of where the fleet puts this code when it meets it for real: inside the package that owns the domain, as `lacing/store/postgres.py` did by binding `(owner_id, project_id)` at construction. That fired D4's own kill condition before kc's first commit.

**This is why patch 1 ships alone.** Its value does not depend on a second reader; patches 2–3's value entirely does, and building enforcement with no reader to enforce against is the anticipatory-package failure the fleet's own cautionary precedent (`ayn`) embodies. Landing it inside `ir` removes the packaging overhead without making speculative code less speculative.

## 8. How we would know this was wrong

- **D20 cannot be answered — a second human or machine, and one shared corpus, named before code.** The old plan measured this ninety days *after* the first commit; making it a precondition costs nothing and is the difference between a module and a deletion cycle. If both blanks stay empty, only patch 1 lands.
- **`tests/test_leakage.py` cannot be made to pass against the default retriever.** Then the central promise is unavailable and the output is a bug report on `ir/retrieve.py`, not a release.
- **`ir` stops pre-filtering, or the `filter_fields` merge order changes.** Previously that silently broke a promise across a package boundary; it is now a red test in the same suite as the change.
- **The per-principal lexical-index cache blows memory.** `_candidate_key(surfaces, filter)` (`ir/retrieve.py:136-146`) puts the serialised filter in the BM25 cache key, so each distinct principal set builds its own index over its own candidate set. **Measure this now** against the real `skills` and `packages` corpora with two synthetic principal sets, rather than waiting for it to fire (D17).
- **`ir`'s owner declines the vocabulary in writing.** Then the wrapper needs a home and a distribution is the honest answer — the one condition that revives the package (D13, D23).
- **No second consumer within a quarter**, or `reader-enforcement` never fires. Two of the four mechanisms were then speculative and should be cut before anyone depends on them.


## 9. What this requires of `ir`

**It *is* `ir`.** Roughly 200–300 lines against a 9,655-line package at 0.1.29 — MIT, auto-publishing on merge, in daily use with ~430 tests. No new runtime dependency: plain dicts in vd's filter dialect, and a frozen dataclass over frozensets.

Three properties formerly borrowed across a package boundary become owned ones, each pinned by a test in the suite that can break them: the pre-filter-before-index ordering (`ir/retrieve.py:427`), `**meta`-last in every indexing strategy (five of six today — replaced by merging grants after `decompose` returns), and `filter_fields` losing to surface metadata (`ir/index.py:211` — replaced by a raise). **The old §9's answer to "what does this require of other packages" was "Nothing."** Two paragraphs later it filed two upstream issues, one asking `ir` to pin the ordering the whole guarantee rests on. The honest answer was always "three undocumented properties of `ir`, maintained for speed."

One request stands independently of the grant vocabulary: a **metadata-only restamp path**, so a metadata change re-stamps without re-running the indexing strategy. It serves any metadata change, not only a permissions one (D18).
