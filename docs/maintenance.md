# Maintenance

## Files

`data/papers.json` is the editable catalog. Its `bibtex` field retains the original entry type and verified bibliographic fields. `data/paper_resources.json` stores recorded direct PDF links separately from the publication record. `scripts/render.py` generates both homepages and category README files, as well as the year index and export files. The script needs Python 3.10 or newer and uses only the standard library.

```sh
python scripts/render.py
python scripts/validate.py
python scripts/render.py --check
```

`validate.py` checks record identity and required fields. It also checks local Markdown links and confirms that generated files match the data. This is a structural check, not a verification of the cited papers' scientific claims.

## Add a paper

Use the paper's primary publication page. Check old under-review manuscripts for a later formal record using exact title, authors and paper identifiers. Do not promote a submission to an accepted paper. New candidates without an established formal publication can be omitted. The existing LlamaGen preprint is explicitly retained as foundational background. Confirm its title and author order. Keep preprint status distinct from accepted or published status. Supply the original BibTeX entry without invented pagination.

Assign the paper to the relevant collection and an existing subsection, or explain why a subsection is needed. A paper can have multiple section assignments. Background papers must remain identifiable.

Record a Code link only after matching the repository to the paper through author names, the paper identifier or an author-controlled page. Leave it empty when the association has not been checked. Update the code-check date only after checking the actual association.

Regenerate the lists. Both homepages and category counts update from the catalog. Do not manually replace generated paper lists. Add a short entry to `CHANGELOG.md`.

## Links

To check HTTP reachability explicitly:

```sh
python scripts/check_links.py --output link_report.json
```

A timeout or access restriction is not proof that a citation is incorrect. Inspect non-success responses before changing a link. HTTP success alone does not establish that the page matches the paper.

## Before publication

Review the repository name and license choices. Add a public survey URL only after one exists. Do not upload private manuscript drafts or third-party paper PDFs with the catalog. The repository does not need a fictional DOI, venue or citation badge to be useful.

## Coverage records

Update `publication_status` and `publication_evidence_url` alongside bibliographic fields. Keep metadata verification distinct from reading status. Record access failures as unresolved access, not evidence that a paper was never published. Keep conference year, first online date and proceedings imprint year distinct when they differ. See [coverage and limits](coverage.md).

The current venue policy admits formally published CCF-venue papers and explicitly allows TMLR. Do not label TMLR as CCF to implement this exception. Workshop-only publications stay excluded. Findings and other tracks remain separate until their eligibility is established. The current 232-record inventory includes 141 core, 68 background and 23 pending records. Do not advertise the full inventory size as a core-accelerator count.

The 69-entry retrospective scope review has separate source-reading and relevance fields. Reclassifying navigation does not alter original publication metadata. Preserve the source of each decision when updating these fields.


## Paper-level review fields

Every `screening` record must state the generated output, the concrete intervention and the original-source basis. Supply the cost boundary and exact source location. Record the actual reading extent. A selected-passage check must not become a claim that the complete proof was checked. Pending records need an explicit unresolved item.

The root README starts with the author-locked survey title and `Coming soon...`. It then presents the taxonomy overview and the full core-paper list. Each category has its own `papers/<category>/README.md`. Keep paper names in full and make their titles link to the recorded PDF when one is known. The official publication link remains available beside the title. Record alternate author versions in `data/paper_resources.json`, without changing formal publication metadata. A temporary publisher access failure does not establish that the paper or URL is invalid.

The renderer regenerates `scope_decisions.csv`, `full_review_186.csv` and `followup_visual_20261031.csv` from the JSON. It also generates the three admission lists and the core-only BibTeX. Keep the original 186 cohort fixed. New papers belong to the follow-up cohort. Historical 69-entry exports are not current admission sources.

Do not place background or pending papers in a core mechanism list. Memory reduction and model-call budgets require their own boundary labels. Archive unresolved search candidates outside the master count until identity and eligibility can be established. Keep third-party PDFs and local research paths outside the public repository.

## Directory-screening status

Retain all directory entries, not only keyword matches. The 31 October directory export records actual individual reading separately from retrieval. Semantic ordering does not establish relevance or irrelevance. Do not remove unread records or claim a venue has no eligible paper because a search returned no candidate. New paper-level admissions require original-source grounds.
