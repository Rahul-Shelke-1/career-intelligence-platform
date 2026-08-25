# Vision with Scraper

### 1. Notebook does:

```
config
  ↓
parse repositories
  ↓
GitHub API
  ↓
raw GitHub data
  ↓
basic normalization
  ↓
save raw JSON
  ↓
save tabular representation
```

Don't modularize heavily yet.

**Get the ugly notebook working first.**

---

### 2. What data should we actually collect?

For your eventual agent, I'd structure the acquisition around opportunity signals, not just GitHub objects.

#### Repository

```
repo
├── name
├── owner
├── description
├── language
├── stars
├── forks
├── watchers
├── created_at
├── updated_at
└── topics
```

#### Issues

This is probably your highest-value initial dataset.

```
issue
├── repo
├── issue_id
├── title
├── body
├── author
├── labels
├── state
├── created_at
├── updated_at
├── closed_at
├── comments
├── reactions
└── url
```

But **don't stop at the issue itself**.

The comments are extremely valuable because they contain things like:

> "We need someone to implement X."

> "This is currently blocked because..."

> "I started working on this but..."

> "Would someone be interested in..."

That's opportunity data.

---

### Pull requests

```
pull_request
├── repo
├── pr_id
├── title
├── body
├── author
├── state
├── created_at
├── merged_at
├── closed_at
├── labels
├── reviewers
├── comments
├── review_comments
├── commits
├── files_changed
└── url
```

PRs give you another very important signal:

**What are people actually building?**

Issues tell you what people **want**.

PRs tell you what people **are implementing**.

---

#### Discussions

If the repository has GitHub Discussions:

```
discussion
├── repo
├── discussion_id
├── title
├── body
├── category
├── author
├── comments
├── reactions
├── created_at
└── url
```

This is potentially even more interesting for your future agent because discussions expose:

- pain points
- feature requests
- community sentiment
- architectural debates
- unanswered questions
- emerging needs

---

## 3. Then your agent can reason over it

Eventually the pipeline becomes:

```
                  GitHub
                    │
                    ▼
             ┌─────────────┐
             │   Scraper   │
             └──────┬──────┘
                    │
                    ▼
              Raw MongoDB
                    │
                    ▼
            Transformation
                    │
                    ▼
          Opportunity Dataset
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
       Issues      PRs    Discussions
          │         │         │
          └─────────┼─────────┘
                    ▼
              AI Researcher
                    │
                    ▼
          Opportunity Signals
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
       "Fix X"   "Build Y"   "Learn Z"
                    │
                    ▼
             User Opportunity
                    │
                    ▼
              Engagement
                    │
                    ▼
              Contribution
                    │
                    ▼
               Reputation
                    │
                    ▼
               Job Offer
```

That last chain is the actual product thesis.

You're not trying to tell someone:

> "Here are 500 GitHub issues."

You're trying to tell them:

> **"Here are 3 opportunities that you have a realistic chance of converting into career value."**

That's a much more interesting problem.

---

## 4. Opportunity detection becomes the interesting part

Suppose the scraper finds:

```
Issue #1823

Title:
Add GPU support for X

Created:
8 months ago

Comments:
17

Status:
OPEN

Labels:
enhancement
help wanted

Last activity:
12 days ago
```

The future agent could calculate:

```
Opportunity Score

Need                HIGH
Age                 HIGH
Activity            MEDIUM
Difficulty          MEDIUM
Competition         LOW
User skill match    HIGH
Maintainer activity HIGH
Contribution value  HIGH

=> STRONG OPPORTUNITY
```

Then tell the user:
>
> **Potential opportunity**
>
> The project has had an open GPU-support request for 8 months, with recent discussion and no active implementation. Your Python/CUDA/ML background makes this potentially suitable.
>
>Suggested action:
>
> 1. Read maintainer discussion.
> 2. Reproduce the current limitation.
> 3. Comment with a proposed implementation.
> 4. Create a PR if maintainers agree.

Now you're getting into **career intelligence**, rather than scraping.

---

## 5. Rival/company monitoring makes the system much more powerful

Your other idea is important too.

Suppose the user is targeting:

```
Company A
Company B
Company C
```

The system watches their:

- GitHub repositories
- engineering discussions
- open issues
- PRs
- releases
- technologies
- contributors
- job postings
- technical announcements

Then it can detect:

```
Company A
    │
    ├── migrating to Kubernetes
    ├── building RAG infrastructure
    ├── hiring ML Platform Engineers
    └── repeatedly discussing observability
```

The agent can infer:

> **Company A appears to be investing heavily in ML infrastructure and observability.**

Then compare that with the user's profile.

```
User skills
    │
    ├── Kubernetes       ✓
    ├── Docker           ✓
    ├── MLflow           ✓
    ├── AWS              ✓
    └── Observability    partial
```

And produce:

```
Career Opportunity

Company A
Role: ML Platform Engineer

Fit: 78%

Gap:
Observability with OpenTelemetry

Suggested project:
Build OpenTelemetry instrumentation
for an ML inference pipeline.

Then:
→ contribute to relevant OSS project
→ demonstrate work publicly
→ apply to Company A
```

**That is the convergence loop you're describing.**
