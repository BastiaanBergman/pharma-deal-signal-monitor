# Query Library

Expanded bank of `search_press_releases` query variants for the Pharmaceutic
Index MCP. Use in addition to or instead of the seven standard sweep queries
when the user requests a more targeted scan.

The tool is semantic — write queries as natural language descriptions of what
you are looking for, not keyword strings.

---

## Table of Contents
1. Standard signal sweep (baseline — always run these)
2. By modality
3. By therapeutic area
4. By geography
5. By deal type
6. By company stage
7. Combination / compound signal queries

---

## 1. Standard signal sweep

Run all seven for every general scan. These are the baseline.

| Signal category | Query |
|---|---|
| Positive clinical readout | `"Phase 2 or Phase 3 positive clinical trial results without partnership announcement"` |
| Regulatory milestone | `"FDA Breakthrough Therapy Fast Track or Orphan Drug designation granted"` |
| Collaboration termination | `"collaboration agreement terminated or partnership discontinued asset returned"` |
| BD leadership hire | `"Chief Business Officer or VP Business Development executive appointment hired"` |
| Capital raise | `"Series B Series C financing raise proceeds advance clinical pipeline"` |
| IND / trial initiation | `"IND filed or Phase 1 initiated first patient dosed"` |
| Explicit partnering language | `"exploring strategic alternatives seeking licensing partner out-licensing"` |

---

## 2. By modality

Use when the user specifies a technology class. Run alongside the standard sweep,
or as a standalone if the user wants modality-specific coverage only.

**Antibody-drug conjugates (ADC)**
- `"antibody-drug conjugate ADC clinical results payload linker"`
- `"ADC license partnership deal out-licensing antibody conjugate"`
- `"ADC toxicity tolerability safety data differentiated linker"`

**Bispecific antibodies**
- `"bispecific antibody T cell engager clinical data phase results"`
- `"bispecific antibody platform licensing deal partner"`

**Cell therapy (CAR-T, TCR, TIL)**
- `"CAR-T cell therapy clinical results response rate durable"`
- `"autologous allogeneic cell therapy IND Phase 1 initiated"`
- `"cell therapy manufacturing scale partnership CMO"`

**Gene therapy / gene editing**
- `"gene therapy AAV CRISPR clinical data IND filing"`
- `"gene editing platform license collaboration deal"`
- `"gene therapy rare disease durability long-term follow-up"`

**mRNA / nucleic acid therapeutics**
- `"mRNA LNP lipid nanoparticle delivery platform license"`
- `"siRNA antisense oligonucleotide ASO clinical results"`
- `"nucleic acid therapeutic IND first patient dosed"`

**Protein degradation (PROTAC, molecular glue)**
- `"PROTAC molecular glue targeted protein degradation clinical"`
- `"protein degradation platform collaboration deal license"`

**Radiopharmaceuticals**
- `"radiopharmaceutical theranostic PSMA FAPi clinical trial results"`
- `"radiopharmaceutical license deal partnership out-licensing"`

**Small molecule**
- `"small molecule oral inhibitor Phase 2 results primary endpoint"`
- `"best-in-class small molecule differentiated mechanism license"`

**Oligonucleotide / RNA interference**
- `"RNAi siRNA hepatic delivery clinical results liver"`
- `"oligonucleotide splice switching exon skipping Phase results"`

---

## 3. By therapeutic area

Use when the user specifies an indication or disease area.

**Oncology (general)**
- `"solid tumour overall survival progression-free survival Phase 2 results"`
- `"oncology combination therapy clinical data checkpoint inhibitor"`
- `"tumour mutational burden biomarker-selected oncology trial results"`

**Haematologic malignancies**
- `"AML MDS lymphoma leukaemia myeloma clinical trial Phase results"`
- `"blood cancer complete response minimal residual disease data"`

**Rare disease / orphan**
- `"rare disease orphan drug designation ultra-rare Phase 1 IND"`
- `"ultra-rare paediatric genetic disease clinical trial first patient"`
- `"lysosomal storage disorder enzyme replacement gene therapy results"`

**Neurology / CNS**
- `"Alzheimer Parkinson ALS multiple sclerosis Phase 2 clinical results"`
- `"CNS neurodegeneration blood-brain barrier delivery clinical data"`
- `"rare neurological disease IND clearance Phase 1 initiated"`

**Immunology / inflammation**
- `"autoimmune inflammatory disease Phase 2 results remission endpoint"`
- `"JAK inhibitor IL pathway biologic autoimmune clinical data"`
- `"atopic dermatitis rheumatoid arthritis IBD Crohn lupus trial results"`

**Cardiometabolic**
- `"cardiovascular heart failure MACE endpoint Phase 3 results"`
- `"obesity GLP-1 metabolic disease weight loss clinical data"`
- `"NASH MASH fibrosis liver metabolic Phase 2 results"`

**Infectious disease / vaccines**
- `"infectious disease antiviral vaccine Phase results efficacy"`
- `"RSV influenza HIV antiviral clinical trial data"`

**Ophthalmology**
- `"retinal disease AMD geographic atrophy ophthalmology Phase results"`
- `"gene therapy eye rare retinal disease IND clinical"`

**Rare respiratory**
- `"pulmonary fibrosis IPF cystic fibrosis lung disease Phase results"`

---

## 4. By geography

Use when the user wants to focus on companies from a specific region or deals
involving specific territory rights.

**Chinese biotech (out-licensing to West)**
- `"Chinese biotech company license out-licensing global rights US Europe"`
- `"China innovative drug company partnership US rights deal"`
- `"NMPA approval Chinese company seeking global partner rights"`
- `"Greater China rights licensed asset available US EU development"`

**Chinese biotech (in-licensing from West)**
- `"Greater China rights licensed deal Chinese company in-license"`
- `"Asia Pacific APAC rights license Chinese partner deal signed"`

**Japanese biotech / pharma**
- `"Japanese company out-licensing global rights ex-Japan asset"`
- `"Japan biotech Phase results seeking partner US EU commercialise"`

**Korean biotech**
- `"Korean biotech company Phase results global license partner"`
- `"Korea out-licensing deal rights US Europe partnership"`

**European biotech**
- `"European biotech company seeking US partner license deal"`
- `"EU ex-US rights licensed European company asset"`

**Israeli biotech**
- `"Israeli biotech company license deal partnership Phase results"`

---

## 5. By deal type

Use when the user is interested in a specific transaction structure.

**Out-licensing / asset available**
- `"company out-licensing asset seeking partner license deal"`
- `"rights available license seeking buyer pharma biotech"`
- `"non-core asset divest out-license available strategic review"`

**In-licensing / acquisition targets**
- `"Phase 2 results unpartnered no deal announced seeking acquirer"`
- `"biotech positive data undisclosed partnership available"`

**Platform deals**
- `"platform technology discovery collaboration research agreement signed"`
- `"platform license deal multiple programmes option rights"`

**M&A signals**
- `"exploring strategic alternatives acquisition merger shareholder value"`
- `"buyout offer received strategic review board of directors"`
- `"takeover bid acquisition premium shareholder value"`

**Terminations / reversions (asset freed up)**
- `"licence agreement terminated mutual consent asset returned"`
- `"collaboration ended discontinued wind down rights reverted"`
- `"partner exercised termination right asset back licensor"`

**Option exercises (deal confirmed)**
- `"exercised option license agreement full development rights"`
- `"option exercised IND Phase milestone triggered license"`

---

## 6. By company stage

Use when the user wants to filter by company maturity or type.

**Early-stage / preclinical**
- `"preclinical IND enabling studies first-in-class mechanism seeking partner"`
- `"discovery platform Series A preclinical proof of concept"`

**Clinical-stage biotech**
- `"Phase 1 2 clinical biotech unpartnered seeking collaborator license"`

**Late-stage / near-commercial**
- `"Phase 3 NDA BLA submission seeking commercial partner US launch"`
- `"PDUFA date approaching seeking co-commercialisation partner"`

**Virtual / capital-constrained**
- `"virtual biotech lean team Phase results capital raise runway"`
- `"financing bridge round extend runway Phase readout approaching"`

**SPAC / recently public**
- `"SPAC reverse merger recently public biotech pipeline assets"`

---

## 7. Combination / compound signal queries

Use to explicitly hunt for companies showing multiple signals at once — the
highest-priority BD leads.

- `"Phase 2 results positive AND capital raise financing same company"`
- `"Breakthrough Therapy designation AND IND filed same programme"`
- `"collaboration terminated AND new financing raised company"`
- `"Phase 2 readout AND Chief Business Officer hired same company"`
- `"orphan drug designation AND Phase 1 results AND seeking partner"`
- `"positive data AND strategic alternatives AND no deal announced"`

Note: the MCP performs semantic search, so these combined queries may not
surface results with perfect logical AND behaviour. If a combined query returns
weak results, break it into two separate queries and manually check for
company overlap in the results.

---

## Query writing tips

**Be descriptive, not keyword-heavy.** The tool is semantic. "A small biotech
company that just got positive Phase 2 data and hasn't announced a deal yet"
will often outperform "Phase 2 results unpartnered."

**Vary phrasing across runs.** If a query returns 0–1 results, try rephrasing
before concluding there is nothing in the corpus. Different companies use
different terminology for the same concept.

**Negative space queries work.** Queries like "positive clinical results without
a partnership announcement" help surface the in-between moment the skill is
designed to catch.

**Specificity improves precision.** Adding indication, modality, or phase
narrows results to what the user actually needs. Generic queries return generic
results.
