#### Pricing, Experimentation \& Churn Impact System

##### Overview

This project builds a decision-first pricing analysis and experimentation system for a SaaS product.

The goal is not to predict churn at a user level, but to:

* Understand how pricing structures influence churn
* Design safe, guardrail-aware pricing experiments
* Quantify how much churn pressure each pricing decision adds or removes

The system is built to support real product and pricing decisions, not academic modeling.

##### Problem Statement

Pricing decisions often fail in three ways:

* Teams focus on revenue uplift without measuring churn risk
* Experiments are run without guardrails
* Churn models are hard to interpret for decision-makers

This project addresses those gaps by:

* Breaking pricing into decision surfaces
* Translating metrics into clear actions
* Using modeling for strategy, not prediction

###### Data \& Scope

The analysis is scoped to pricing-related dimensions only:

* Trial vs Non-Trial entry
* Billing frequency (Monthly / Annual)
* Plan structure (Basic / Pro / Enterprise)
* Seat size buckets

The system intentionally stops at pricing behavior and does not mix:

* Feature usage modeling
* Support interactions
* Marketing attribution

This keeps insights actionable for pricing teams.

###### 

##### Pricing System Analysis

###### 1\. Trial vs Non-Trial

Why this split matters:

Entry strategy affects onboarding quality, early intent, and value perception.

What I did:

* Compared churn, upgrade behavior, and subscription age
* Assigned performance labels and guardrail status

Outcome:

Trial users showed different churn dynamics than direct purchasers, indicating entry strategy affects downstream pricing outcomes.

###### 2\. Billing Frequency (Monthly vs Annual)

Why this split matters:

Billing cadence reflects commitment depth and value confidence.

What I did:

* Measured churn and upgrade behavior for each billing type
* Evaluated whether either group passed churn guardrails

Outcome:

Both billing types showed value misalignment, indicating pricing issues are structural rather than cadence-driven.

###### 3\. Plan × Seat Structure

Why this split matters:

Pricing risk changes with customer scale.

What I did:

* Bucketed customers by seat size
* Evaluated churn and upgrade behavior within each plan × seat segment

Flagged segments as:

* Rollout-safe
* Monitor
* Do not apply

Outcome:

Some large-seat segments were safe to expand, while mid and small segments showed high churn risk despite healthy upgrades.

##### Experimentation Framework

Rather than running one large experiment, I designed micro-experiments.

Why micro-experiments:

* Limits blast radius
* Allows guardrail enforcement
* Produces clearer learnings

What I did:

* Simulated expected impact for each plan × seat segment
* Compared baseline vs expected churn and upgrade rates

Assigned:

* Net effect label
* Guardrail status
* Recommended action

Each experiment answers:

“Should we even test this pricing change?”

##### Pricing → Churn Impact Model

This project includes an interpretable pricing impact model.

What this model is NOT:

❌ Not a churn prediction model
❌ Not a black-box ML system

What this model DOES:

Quantifies how much each pricing decision:

* Increases churn pressure
* Reduces churn pressure

Outputs: Percentage churn impact

Risk buckets (High Risk / Moderate / Neutral / Protective)

###### Why this matters

This allows teams to:

* Block risky pricing ideas early
* Identify protective pricing signals
* Design experiments with quantified guardrails

###### Dashboard Design Philosophy

The dashboard is designed as a branching decision system, not a static report.

###### Users explore pricing as branches:

Pricing system → experiments → churn impact

###### 

###### Each page includes:

* How-to-read guidance
* Decision summaries
* Expandable details

The goal is clarity over complexity.

###### Key Takeaways

* Pricing risk is structural, not isolated
* Upgrade signals alone are not sufficient
* Churn guardrails must exist before experimentation
* Interpretable models are more useful than predictive ones for pricing strategy


###### Why This Project Matters

This project demonstrates:

* Decision-first analytics
* Guardrail-aware experimentation design
* Practical modeling for strategy teams

It reflects how pricing and analytics work in real SaaS environments, not just notebooks.


###### Tools Used

* Python (pandas, scikit-learn)
* Streamlit
* Custom analytics utilities (Prepstack)
* GitHub for versioning


###### Author

Ridhisha Tyagi



