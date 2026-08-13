# Chapter 1: Why AI Engineering, Why Now

## The Story

I was twelve or thirteen the first time I opened a broken device with no idea what I was doing. Nobody around me knew this stuff either. There was no mentor, no course, no plan. Just curiosity and a screwdriver. Sometimes the thing worked again. Sometimes it didn't. And almost every time, when I closed it back up, there'd be a few screws left over that I could never place. The device still worked anyway. It still did what it was built to do, missing screws and all.

I didn't think much of it at the time. Looking back now, I think it was the first version of something I've relearned in a dozen different forms since: things don't need to be perfect to work and to provide the value they're meant to provide. Chasing perfection is very often just a way of avoiding moving forward, or avoiding exposing yourself.

That curiosity turned into a technical university education, where I started on the hardware side and drifted, unevenly, toward software. But even then it was never really about the code. I was never trying to become "a developer" in the standard sense. What pulled me in was solving problems: the tools I picked up along the way, hardware or software, were always just whatever got the problem solved. That distinction matters more than it sounds like it should: it means every move I've made since has been driven by the problem, not by loyalty to a particular stack or title.

The clearest early example of that is the decision that took me out of Portugal entirely. I didn't feel like I fit the standard path available to me there: finish the degree, take a junior role at a big company, spend years slowly climbing. That's not how I wanted to move through life, and I didn't see room to do it differently where I was. So I left, as an Erasmus student, for Vienna. I didn't speak German. Most of the coursework was in German. I had no money to spare, no community waiting for me, and no real plan, just a belief that there was more room somewhere else to build my own path. On paper it made no sense. On intuition, it was obvious.

My professional path started as a software tester, which, at the time, felt like exactly the right fit: close enough to technology to see how things actually worked, far enough from "developer" that I could watch real products meet real people and pay attention to how they actually used them. I moved into test automation from there, and eventually hit a ceiling, no clear next step from where I stood. That's when I found Scrum Master and agile coaching work: a way to shape *how* technology gets built, without writing the code or owning the product decisions myself. Shaping the conditions that let other people contribute their knowledge toward something more meaningful. Another step in the same direction: always chasing a closer relationship to real impact, never chasing the title.

Over the last ten years I worked across B2B, B2C, and B2B2C, pure software and software built for hardware, picking up product design and product development along the way, always with one eye on business strategy. I was motivated, constantly learning, always trying to provide more value. I grew a lot. I also learned, the hard way, that this specific mode (the all-in, always-more version of myself) wasn't sustainable. I gave too much of my energy and my commitment, and it led to burnout.

There are different ways I could have chosen to explain the reasons that led to my burnout: "the system being broken", or "me not knowing my own limits". I'm not interested in assigning blame either way. What matters more is what I choose to do with it, and I choose to see it as something that had to happen, so that I could stop, realign, and actually define my own direction instead of drifting further along someone else's.

The burnout taught me to follow my gut and actually listen to my body. During this "break", I figured out what I actually wanted to do and what kind of value I wanted to put into the world, and it was never about getting rich or famous. It was about helping people. My first real plan afterward was to become a burnout-prevention coach for IT companies, bringing my own experience back into the field to help them reshape how they work. After nearly a year of planning and learning, organizing, etc, two big walls stopped me. First, Austria's bureaucracy: to legally offer something like that, I'd essentially need to become a therapist. Second, and harder: for a company to pay for that kind of work, the people inside it have to actually want to change how they work from the inside. That's rare. It's genuinely difficult to make happen.

While I was running into those walls, AI was growing exponentially around me. And because the constant in my story was never "developer" or "coach", it was always "find a problem, find whatever tool solves it", turning toward AI wasn't a trend I jumped on. It was the same pattern, redirected.

Here's the part that actually matters, though: AI today is accessible to almost everyone, often for free or close to it. But accessibility isn't the same as benefit. Most of the businesses I care about (small, non-technical, deeply important to the people around them, and going to keep existing no matter how much the technology shifts) don't have the technical understanding to actually benefit from any of it. That gap is exactly why AskDila exists: to let small businesses focus on what they're actually good at, by using AI to take the repeatable work off their plate: the work that was never their passion in the first place.

Building AskDila is what showed me this gap firsthand: having an application running is not the same thing as having a *production-ready* application, reliable, safe, able to scale. That gap between "it runs" and "it's ready" is the entire reason this book and this roadmap exist. It's the difference between a demo and a real AI engineer's work.

A disclaimer, if you're a solo founder like me: even if a product is genuinely production-ready, that doesn't mean the business is ready. Building the product is only part of it, usually a small part of it. That's an entire book of its own, and not this one.

Why now? Honestly, why not now. Burnout gave me the space to stop and actually reflect. The work I did on myself in that space is what gave me the courage to pivot and go after what I actually want to build, instead of what was simply next in line.

## The Concept

"AI Engineer" is a genuinely new discipline, not a rebrand of an old one, and that distinction is worth being precise about, because the job market treats it as precise. A data scientist builds and evaluates models. An ML engineer trains and deploys them at scale. An AI engineer, in the way the market is actually hiring for it in 2026, builds *production systems around* large language models (retrieval pipelines, agents, evaluation harnesses, observability, cost control) for real products that real people depend on. (Chapter 3 goes deep on how these three roles actually differ day to day; this chapter only needs the broad strokes.)

The reason this discipline exists at all is the exact gap I ran into with AskDila: it has never been easier to get an LLM to *do something impressive in a demo*. It has stayed hard to make that same thing reliable, safe, and affordable enough to put in front of a real customer, every day, without surprises. That gap, running vs. production-ready, is where AI engineers actually get paid, and it's the thesis this entire book is organized around.

I didn't want to take that claim on faith, mine or anyone else's, so before writing a line of this book I went and checked it against the current market directly: real AI Engineer postings, targeting the kind of remote-EU and Zurich-tier roles that clear €100k+. A few things came back that didn't match my assumptions going in. Fine-tuning and LoRA, which I expected to be a broad differentiator, turned out to show up almost exclusively in one outlier, PhD-level, $200k+ research role. It's a narrow specialization, not a general requirement. On the other hand, full-stack product ability, the kind I've built over years shipping real client work through B-Software and am now applying to AskDila, showed up as a real, named differentiator in nearly a third of postings, and nothing in my original roadmap had credited that at all. And the postings that clearly cleared the €100k+ bar consistently had one thing in common: they named specific evaluation and observability tooling, not just "experience with LLM APIs." That's the gap between a generalist and a senior hire.

That's the market's version of "running vs. production-ready." The rest of this book is me closing that gap in public, one chapter at a time.

## The Build

The hands-on work for this chapter had two parts: writing the personal "why" you just read, and grounding it against real evidence from the job market: not vibes, not last year's blog posts.

**Steps I actually followed:**

1. Wrote the personal "why" first, in raw form, before touching any market data, captured as it came out, across several sessions, in `00_meta/STORY_BANK.md`. Some of it will get reused later in the book, some of it won't; none of it got discarded.
2. Searched for current (2026) AI Engineer job postings matching my actual target: remote-EU or Zurich-tier, €100k+/$150k+ base, roles that fit an experienced full-stack founder adding AI depth, not entry-level, not pure-research.
3. Pulled full content from every posting I could actually access (LinkedIn, Wellfound, Ashby, Dice, aggregators) and skipped the ones that 403'd or redirected rather than guessing at their contents.
4. For each posting, logged: company, role, comp if listed, location/remote policy, and every specific technical requirement named (tools, frameworks, years of experience, seniority language).
5. Aggregated across postings into a ranked skill-frequency list, and compared it directly against the skill tiers this book's roadmap had assumed going in.
6. Filled in `07_career_prep/SKILL_GAP_MATRIX.md` with the result: required-in-market vs. my own current self-rated level, so every later chapter has a concrete target to close, not a guess.
7. Logged the decisions that changed as a result of this research, and the reasoning behind them, in `planning_journal/`, so the "why" behind each pivot survives even after the roadmap itself moves on.

**Where to find the actual output:** `07_career_prep/SKILL_GAP_MATRIX.md` for the filled skill matrix, `planning_journal/2026-08-13-job-market-skill-research.md` for the full research writeup and reasoning, and `02_exercises/part0/ch01_exercise.md` for the reproducible version of this exercise if you're following along.

## The Debrief

**What broke / what surprised me:** the roadmap I started with was a reasonable first draft, and it was still wrong in places. I'd overweighted fine-tuning as a broad differentiator when the evidence says it's a narrow specialist track. I'd completely undercounted my own existing full-stack ability as market-relevant, when it's actually one of the more distinctive things I bring to this. Neither of those would have surfaced if I'd just followed the original plan without checking it against anything real.

**The honest gap:** the definition of done for this chapter called for 10 annotated job postings. I got full content from 9, the tenth one 403'd, and I decided not to fake the tenth by guessing at a posting I couldn't actually read. That's a leftover screw. The chapter still works without it.

**What this connects to:** every skill-level gap logged in `SKILL_GAP_MATRIX.md` this week is now a concrete target tied to a real salary band, not an assumption, starting with the biggest one: RAG, currently at 0/5 against the single most in-demand skill in the postings I read. That's where the next real chapters are headed.

## Status
- [x] Story drafted
- [x] Concept researched and verified
- [x] Build completed and tested
- [x] Debrief written
- [ ] Chapter reviewed
