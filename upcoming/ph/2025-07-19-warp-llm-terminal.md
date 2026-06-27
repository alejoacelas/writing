# Warp is a terminal you can talk to

*Source: https://wow.pjh.is/journal/warp-llm-terminal*  ·  *Published: 2025-07-19*

---

[Warp](https://www.warp.dev/) puts LLM magic into a terminal.

Simple example: if I start a development server and get an error, Warp understands the error and suggests a fix:

I press `CMD+Enter` to run the prompt it suggested:

I authorise a risky command, then it completes the full process:

Warp has a built-in coding agent, so it can handle much more complex "it not work, plz fix" situations. I've not yet used it much, but it aced the one real test I've given it: upgrade a complex codebase from Node 18 to Node 22:

```
✅ Successfully upgraded everything to Node.js 22

Key Changes Made:

1. Updated Node.js version requirement in package.json from ^18.16 to ^22.0.0
2. Updated critical dependencies for Node.js 22 compatibility:
•  TypeScript: ^4.9.3 → ^5.9.0
•  @vercel/node: ^2.15.5 → ^5.3.0
•  date-fns: ^2.29.1 → ^4.1.0
•  date-fns-tz: ^2.0.0 → ^3.2.0
•  axios: ^1.7.7 → ^1.11.0
•  dotenv: ^16.3.1 → ^17.2.0
•  And several other dependencies
3. Updated TypeScript configuration to target ES2020 for better compatibility with Node.js 22
4. Fixed API compatibility issues:
•  Updated date-fns-tz import from utcToZonedTime to toZonedTime
•  Fixed Supabase query builder type issues with strategic type assertions
•  Fixed process.cwd() usage in test files
5. Excluded unused cron jobs from TypeScript checking as requested
6. Updated Vercel CLI to the latest version (44.7.3) 

Results:
•  ✅ All TypeScript errors resolved (0 errors)
•  ✅ All tests passing (15/15 test suites, 145 passed tests)
•  ✅ Vercel dev server starts successfully
•  ✅ Build process completes without errors

The original deployment error was caused by version compatibility issues between the different Node.js versions and outdated dependencies. Now everything is aligned with Node.js 22 and should work smoothly!

You can now run your Vercel development server with confidence using yarn develop.

```

I've not used the agent enough to compare it to Claude Code.

Speaking of Claude Code: Warp is great for managing a [Git worktree workflow](https://docs.anthropic.com/en/docs/claude-code/common-workflows#run-parallel-claude-code-sessions-with-git-worktrees) so you can code with several Claude Code instances in parallel.

Finally: Warp clearly has a great design team. There are lots of lovely details, e.g. it's easy to set up launch configs with multiple windows, tabs and split panes on each tab.

```yaml
name: Local Development
active_window_index: 0
windows:
  - active_tab_index: 0
    tabs:
      - title: "hartreeworks.org"
        layout:
          split_direction: horizontal
          panes:
            - cwd: /Users/ph/Documents/www/HartreeWorks/hartreeworks.org
              commands:
                - exec: sh dev
            - cwd: /Users/ph/Documents/www/HartreeWorks/hartreeworks.org
              is_focused: true
      - title: "wow.pjh.is"
        layout:
          split_direction: horizontal
          panes:
            - cwd: /Users/ph/Documents/www/AI Wow/vercel-wow
              commands:
                - exec: sh dev
            - cwd: /Users/ph/Documents/www/AI Wow/vercel-wow
              is_focused: true

```

It's now my default terminal.
