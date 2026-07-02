# Superconductor, plain terminal, or an editor?

**Recommendation: on a Mac, use Superconductor. On Windows or Linux, use plain
terminal windows for now. Reach for a code editor's integration only if you're
already living in one.**

The question is how you *run* Claude Code — the engine is the same either way.
What differs is how easily you can run several agents at once and review their
work, which is where most of the productivity comes from.

## Superconductor (Mac)

A native Mac app from [super.engineering](https://super.engineering) built for
exactly this: many Claude Code sessions in parallel, each isolated so they don't
step on each other, with a clean view to review and ship what they change. For a
newcomer it hides the parts of running parallel agents that would otherwise mean
learning git branching by hand.

- **Cost:** free while in alpha; no paid tier published.
- **Needs:** Claude Code installed and your own Claude account — it drives Claude
  Code under the hood and never sees your credentials.
- **Catch:** Mac only (Apple Silicon), and still alpha. Windows and Linux are
  planned but not here yet.

*(Don't confuse it with superconductor.com — a different, cloud-based product.
The one we mean is super.engineering.)*

## Plain terminal (any OS)

Just open several terminal windows or tabs and run `claude` in each. It's what
Superconductor automates, done manually. Entirely fine — a little more juggling,
no extra software, works everywhere. **This is the answer for Windows and Linux
today.**

## A code editor (VS Code, etc.)

Claude Code integrates with editors like VS Code. Worth it *if you already work
in one* and want the diffs and file tree right there. If you don't, don't adopt
an editor just for this — it's a whole tool to learn for a benefit
Superconductor or a terminal already gives you.
