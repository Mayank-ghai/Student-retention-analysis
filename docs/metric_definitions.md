# Metric Definitions

All data is synthetic. Snapshot (analysis) date: 30 Sep 2026.

## Unit of analysis
We count **enrollments** (one student in one course), not students.

**Rationale:** a student can take two courses and finish only one. Counting
students would force us to call that person either a completer or a
non-completer, which hides what happened. Counting enrollments measures
each course separately. Any student-level number is labelled clearly.

## Core definitions
| Term | Definition | Rationale |
|---|---|---|
| Started | At least 1 activity record within 14 days of enrollment | Someone who first studies on day 40 never really "started" the course as planned |
| Completed | At least 90% of the course's modules marked complete | The business defined completion as 90%; modules are what our data tracks |
| Mature enrollment | Enrolled at least (duration_weeks × 7 + 30) days before the snapshot date | Students who enrolled recently haven't had time to finish; including them makes completion look falsely low |
| Inactive | No activity for 14+ consecutive days (a rule to TEST, not assume) | 14 days is a starting guess; on Day 11 we check whether students really stop returning after this |
| Dropped out | No activity for 30+ days and not completed | Longer than "inactive" so a short break isn't counted as quitting |
| Refunded | payment_status = 'Refunded' | Uses the payment record, which is the source of truth for money |
| Early engagement | Total minutes watched in the first 14 days after enrollment | Measured early, so it can predict completion instead of being a result of it |

## KPIs
| KPI | Formula | Population | Rationale |
|---|---|---|---|
| Completion rate | completed ÷ enrollments | Mature enrollments only | Everyone included has had time to finish |
| Course-start rate | started ÷ enrollments | Enrolled at least 14 days ago | Newer students haven't had the full 14 days to start |
| Week-3 active rate | enrollments with activity on days 15–21 ÷ enrollments | Enrolled at least 21 days ago | Newer students haven't reached week 3 yet |
| Module drop-off rate (module N) | enrollments whose last module is N ÷ enrollments that reached N | Mature, not completed | Shows where people stop, relative to how many got there |
| Assessment pass rate | first-attempt passes (score ≥ 60) ÷ first attempts | All first attempts | First attempts show how hard a quiz really is; retakes inflate the rate |
| Refund rate | refunded ÷ paid enrollments | Enrolled at least 30 days ago | Most refunds happen in the first weeks; newer enrollments haven't had the chance |
| Revenue lost to refunds | sum of refunded amount_inr | Same as refund rate | Puts a money value on the problem |

## Edge cases
| Situation | Rule | Rationale |
|---|---|---|
| Duplicate enrollment (same student, course, date) | Keep the lowest enrollment_id | Otherwise one student is counted twice |
| Activity dated before enrollment date | Exclude | Impossible in reality, so it's a data error |
| minutes_watched is 0 or negative | Exclude | Not real studying |
| Duplicate activity events | Count once | Otherwise minutes are inflated |
| Refunded enrollment | Counts as not completed | The student left the course |
| A group has fewer than 100 enrollments | Don't report it separately | Small groups give unreliable percentages |
