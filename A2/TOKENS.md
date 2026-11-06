# TOKENS: how a model would cut Kestrel's documents

**A2 · Part 1** · Source text: [`KESTREL_REFUND_POLICY.md`](KESTREL_REFUND_POLICY.md), Kestrel's hostel deposit refund policy (KIT/ACC/POL-07, about one and a half pages). Kestrel Institute of Technology is the fictional college from A1.

All counts come from Qwen2.5's tokenizer in my NB2 run: the last cell ("Your own documents") and the ranking cell I added after it, which ranks the words by how many tokens each one becomes.

## 1. Cut it

| Text | Characters | Words | Qwen tokens | Characters per token |
|---|---|---|---|---|
| Kestrel refund policy (KIT/ACC/POL-07) | 4,073 | 692 | 1,100 | 3.70 |
| Northbridge user manual (NB2 §2, my run) | 32,468 | — | 8,175 | 3.97 |

Kestrel's policy needs about 7% more tokens for the same amount of text (3.97 ÷ 3.70 ≈ 1.07). The manual is mostly plain English instructions. Kestrel's page is short, but it is dense with things the tokenizer has no single token for: document and request codes, rupee amounts, numbered clauses (1.1, 2.3, 5.4 …), a rate-card table and a title line in Hindi. Each of those is cut into small pieces, which pulls the average down. A long policy in plain English would come closer to the manual's 3.97.

## 2. What gets split

The ten words and codes cut into the most tokens. They are counted the way NB2 counts them: with a space in front, as they appear inside a sentence, and with surrounding punctuation removed. Ties are listed in the ranking cell's order.

| # | Word or code | Tokens | Pieces | Kind |
|---|---|---|---|---|
| 1 | `22CSE0417` | 9 | `' '` `2` `2` `C` `SE` `0` `4` `1` `7` | code (enrollment number) |
| 2 | `KIT/ACC/POL-04` | 9 | `' K'` `IT` `/` `ACC` `/P` `OL` `-` `0` `4` | code (document number) |
| 3 | `KIT/ACC/POL-07` | 9 | `' K'` `IT` `/` `ACC` `/P` `OL` `-` `0` `7` | code (document number) |
| 4 | `REQ-25-0917` | 9 | `' REQ'` `-` `2` `5` `-` `0` `9` `1` `7` | code (request number) |
| 5 | `छात्रावास` (hostel) | 9 | 9 pieces, most of them not whole letters (byte fragments) | another language (Hindi) |
| 6 | `2024-25` | 8 | `' '` `2` `0` `2` `4` `-` `2` `5` | number (academic year) |
| 7 | `Rs.15,000` | 8 | `' Rs'` `.` `1` `5` `,` `0` `0` `0` | amount |
| 8 | `refunds@kit-kestrel.edu.in` | 8 | `' refunds'` `@` `kit` `-` `kest` `rel` `.edu` `.in` | name inside an address |
| 9 | `FC-24/03` | 7 | `' FC'` `-` `2` `4` `/` `0` `3` | code (committee meeting) |
| 10 | `HSL-VAC-02` | 7 | `' H'` `SL` `-V` `AC` `-` `0` `2` | code (form number) |

Just below them: `सुरक्षा` (security, 7 tokens), then six at 6 tokens each: `1,200`, `1,800`, `H3-214`, `REQ-YY-NNNN`, `RV-YY-NNNN` and `वापसी` (refund). Every Hindi word of the title takes 4 to 9 tokens, and even a clause number like `1.1` takes 4: `' '` `1` `.` `1`.

**By kind**

- **Codes** (`REQ-25-0917`, `KIT/ACC/POL-07`, `H3-214`, `22CSE0417`). Qwen gives every digit its own token, and letters are cut wherever the vocabulary happens to have a piece (`/P`, `OL`, `-V`). So a code is never read as one thing. It is a row of 6 to 9 pieces that the model must keep in the right order. `REQ-25-0917` and `REQ-25-0971` match in 7 of their 9 positions; only the last two digits swap places. A model that writes a code back one digit at a time, each digit chosen from the next-token probabilities, can swap or change a digit and still sound fully confident. Copying a code that is in the input is easy, because attention can point straight at it. Producing one from memory is guessing.
- **Numbers and amounts** (`Rs.15,000`, `1,200`, `2024-25`). These are read digit by digit, just as 5,400 was in NB2. The model never sees "fifteen thousand" as one quantity. It sees `1` `5` `,` `0` `0` `0`. That is why a model can write amounts that look right (the right number of digits, a comma in the right place) without having done any arithmetic. Kestrel's refund is Rs.15,000 − Rs.500 − Rs.40 = Rs.14,460. A model that writes such a figure produces it one digit piece at a time, so the result can look right without the sum being right, and any rupee figure it writes needs checking.
- **Names** (`Kestrel` → `' K'` `est` `rel`; `KESTREL` → `' K'` `EST` `REL`; the e-mail address). Kestrel is rare, so it has no token of its own. Even the capitalised form is cut into *different* pieces, so the model starts from two different token sequences for the same college and has to learn that they mean one thing. Splitting also shows how little the model knows: it has no vector for "Kestrel Institute of Technology", only for fragments like `est`. Whatever it says about Kestrel's rules can only come from what colleges in general do.
- **Another language** (the Hindi title line). The six Hindi words take 35 tokens for 37 characters. The document's English title on the next line ("Hostel Security Deposit: No-Dues and Refund Policy") takes 12 tokens for 50 characters. Per character, the Hindi line costs about four times as much (0.95 against 0.24 tokens a character). Many of the Hindi pieces are not even whole letters: Devanagari characters are stored as several bytes, and the tokenizer falls back to byte pieces for combinations it rarely saw. That costs more, and it leaves the model less to work with: meaning spread over byte fragments is harder to recognise than a common English word. This is the same effect NB2 showed for Greek and Japanese.
- **Jargon and formats** (`Supersedes` → 3, `No-Dues` → 3, `end-semester` → 3, the table rule `|---|---|` → 5). Policy words and markup that are rare in general text are cut into several pieces (3 for these words, 5 for the table rule). They cost little each, but they add up across a long policy.

## 3. Words versus tokens

Three real examples from the Kestrel policy that a fixed word vocabulary would never contain:

1. **`H3-214`**, a room code. Every room has a different one, and new hostels add new codes.
2. **`22CSE0417`**, an enrollment number (policy 3.2). Every student has a different one, and a new batch is added every year.
3. **`HSL-VAC-02`**, a form code (policy 2.1). Forms are renamed and renumbered as rules change, and each college has its own.

A word vocabulary maps each whole word to one id. A word it has never seen has no id at all, and the model can do nothing with it. NB2 showed that a third of the words in two new Northbridge documents were unknown to a vocabulary built from Northbridge's own text. A token vocabulary never fails like that. When a word has no token of its own, BPE falls back to smaller pieces that it does have (`H3-214` → `' H'` `3` `-` `2` `1` `4`, `HSL-VAC-02` → `' H'` `SL` `-V` `AC` `-` `0` `2`), and in the worst case to single bytes. Anything can be written down, so nothing is "unknown".

It has two costs. First, **length**: a code that would be one word becomes 6 to 9 tokens, so the same text costs more to send and fills more of the context. Second, **meaning**: the model has no single vector for `H3-214` or for Kestrel. It has to build the meaning from pieces whose vectors were learnt from other uses (`est`, `rel`, `3`), so it is easier to confuse two codes or two numbers that share most of their pieces.

## 4. What it costs

**The question:** a student asks Ask Kestrel Q2 from Part 2, "I lost my room key. How much will be deducted from my deposit?" The answer is a written rule (Annexure A), so the assistant sends the whole refund policy with it. I ran my four timed runs on Q1, not Q2, so I use Q1's measured output as a stand-in for the reply and the thinking. (A live question like Q1 would instead need tool calls to EduDesk and the ERP, which add tokens not counted here.)

| Part | Tokens | Source of the number |
|---|---|---|
| System prompt + question | 100 | measured: AI Studio's token count for my Part 2 prompt with Q1 (Q2 is a few tokens shorter, so I keep 100) |
| The refund policy sent with it | 1,100 | **estimate**: Qwen's count from NB2; Gemini's tokenizer differs, so its count will be somewhat different |
| **Input total** | **about 1,200** | |
| Visible reply | about 74 | **estimate**: my four Part 2 replies counted with Qwen's tokenizer (72, 85, 69, 68) |
| Thinking | about 635 | **estimate**, see the assumptions below |
| **Output total (reply + thinking)** | **about 709** | thinking is billed as output |

How the thinking figure was worked out, and what it assumes:
- AI Studio showed a total for each of my four runs: 754, 928, 834 and 719 tokens. I **assume** that total is input + thinking + reply. I could not check this in AI Studio, but it is how the API reports usage in NB2 (cell 21: prompt 90 + reply 43 + thinking 390 = total 523).
- On that assumption, each run's output (thinking + reply) is the total minus the 100 input tokens: 654, 828, 734 and 619, about 709 on average.
- Thinking is then 709 minus the reply (about 74), so about 635. This mixes Gemini's counts with Qwen's counts for the reply, so it is approximate.
- These runs had about 100 input tokens. I **assume** thinking stays about the same when the policy is added, but my own data says it varies a lot. Across the four runs thinking was about 551 to 743 tokens. In my Part 3 fact test it was only about 273 (504 total − 159 input − 72 reply). NB2 exercise 3 had 390 for a 43-token reply. So thinking is the least certain number here: from 273 to 743 thinking tokens, the cost runs from about $0.0016 to $0.0031 a question, or about $600 to $1,110 a year.

Prices (NB2, `gemini-3.8-flash`, US dollars per million tokens): input $0.50 / M, output $3.00 / M.

**Working:**

```
one question  = 1,200 × 0.50 / 1,000,000  +  709 × 3.00 / 1,000,000
              = 0.000600 + 0.002127
              = $0.002727

a year        = $0.002727 × 1,000 questions a day × 365 days  =  about $995
```

For comparison: with the reply only and no thinking, the year would cost about $300 ((600 + 74 × 3) ÷ 1,000,000 × 365,000). Without the policy in the input but with thinking, it would cost about $795 ((100 × 0.50 + 709 × 3) ÷ 1,000,000 × 365,000).

**Where the money goes:** thinking is about 70% of the cost, even though nobody reads it, because it is about nine times the length of the reply and output costs six times as much as input. The policy itself is about 20% (the whole input, including the prompt and question, is about 22%). The biggest saving would come from less thinking (a lower thinking level for simple rule questions like this one). The next would come from sending only the relevant clauses of the policy instead of all of it, which is what Lecture 3's retrieval does. A real check: Kestrel handles about 600 refunds a year (A1), so 1,000 questions a day is far more than this one process would ever see. At realistic volumes the cost is small. What matters more is whether the answers are right, which is Part 2.
