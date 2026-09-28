---
prompts:
  - prompt: |
      Save the post below as content/blog/en/stop-confirming-bookings-by-phone.md, then write the LinkedIn ads runbook for it. We have 2,000 EUR a month, we sell to clinic and studio owners in Germany and Poland, and I will post the organic companion myself.

      ---
      title: Stop confirming bookings by phone
      date: 2026-09-01
      author: Head of Product
      ---

      Most small clinics and studios still confirm every appointment by phone the day before. A receptionist works down a list, leaves voicemails, and marks the ones who answered. It feels like care. It is mostly lost time. [Try automatic confirmations free for 14 days](/signup).

      ## Where the first hour goes

      We looked at how front desks using our booking software spend the first hour of the day. The confirmation calls were the largest single block, larger than check-ins and larger than rescheduling. The calls also reached the fewest people: a client who books online rarely answers an unknown number at work.

      ## What we changed

      So we replaced the call with a message the client can answer in one tap. Two days before the visit they get a text and an email with three buttons: keep, move, or cancel. Keep does nothing. Move opens the calendar at the same service and the same staff member. Cancel frees the slot at once, and the waiting list gets the offer within a minute.

      Three things changed for the clinics that switched. The front desk got its first hour back. Cancellations arrived two days out instead of at the door, which is early enough to fill the slot. And the clients who never answered calls started answering, because a button is easier than a conversation.

      ## What it does not fix

      A client who has decided not to come will not tell you, whatever the channel. A deposit or a cancellation fee is the tool for that, and we do not think a reminder should pretend otherwise. If most of your no-shows come from new clients booking free first visits, start there.

      Setting it up takes about ten minutes. You choose when the message goes out, write the text in your own words, and decide whether a cancellation opens the slot to the waiting list or to everyone. Nothing changes for clients who prefer to call: the phone still works, it just stops being the only way.

      If your desk still starts the day with a call list, try it for two weeks and compare the first hours. [Start the free trial](/signup).
    stack: No data store
  - prompt: "Write LinkedIn ads for our latest blog post. We can spend about 1,500 EUR a month."
    stack: No data store
  - prompt: |
      Here is a short post of ours; save it as content/blog/en/new-calendar-view.md and give me the LinkedIn ad copy and the Campaign Manager steps to promote it on 600 EUR a month.

      ---
      title: A new calendar view
      date: 2026-09-15
      ---

      The calendar now has a week view for each staff member. Drag an appointment to move it, and the client gets a message with the new time. [See it in the demo](/demo).
    stack: No data store
---

# Prompts

What an operator types after installing this skill, in their own words. An agent eval installs the skill
into an empty Next.js app, gives the agent one of these prompts and no further help, then type-checks, builds
and tests the result; the first prompt runs before every release. This skill writes a runbook rather than
code, so each prompt carries the post it works on, and the checks only confirm the agent left the app intact:
what a run shows is in its notes, scored against the hard rules. The first prompt is a post that should get
a runbook, the second names no post and the third names one too short to promote, so the last two score
whether the agent stops and asks. The results are the other files in this folder. Section 10 of
[STANDARD.md](https://github.com/timerise-ai/skills/blob/main/STANDARD.md) says how a run is made. The
prompts and the newest runs are on [the skill's page](https://timerise.ai/skills/ad-campaign-runbook) on
timerise.ai.
