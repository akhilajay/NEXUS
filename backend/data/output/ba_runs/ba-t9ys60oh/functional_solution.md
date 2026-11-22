# Functional solution

**Review draft**

## Source documents

- XATA_TODO_BRD.docx
- XATA_TODO_NFR.docx

## Functional requirements and business rules

- The platform shall allow XATA employees to create, manage, prioritize, track and complete personal and team TODO items. (`XATA_TODO_BRD.docx-002`)
- The solution shall provide a single, centralized web application as the common place to manage TODO items. (`XATA_TODO_BRD.docx-003`, `XATA_TODO_BRD.docx-004`)
- Users shall be able to quickly create and update TODO items. (`XATA_TODO_BRD.docx-004`)
- The solution shall provide visibility of open, completed and overdue TODO work. (`XATA_TODO_BRD.docx-004`)
- Team members shall be able to assign TODO items to one another. (`XATA_TODO_BRD.docx-004`)
- The solution shall provide basic priority and due-date management for TODO items. (`XATA_TODO_BRD.docx-004`)
- The solution shall provide a simple dashboard for work tracking. (`XATA_TODO_BRD.docx-004`)
- **BR-001** — System shall allow an authenticated user to create a TODO. (`XATA_TODO_BRD.docx-008`, `XATA_TODO_BRD.docx-005`)
- **BR-002** — A TODO shall contain title, description, status, priority and due date. Users shall be able to set priority and due date. (`XATA_TODO_BRD.docx-008`, `XATA_TODO_BRD.docx-005`)
- **BR-003** — Users shall be able to edit TODOs they own or are authorized to manage. (`XATA_TODO_BRD.docx-008`, `XATA_TODO_BRD.docx-005`)
- **BR-004** — Users shall be able to mark TODOs as completed. (`XATA_TODO_BRD.docx-008`, `XATA_TODO_BRD.docx-005`)
- **BR-005** — Users shall be able to assign a TODO to another authorized user. (`XATA_TODO_BRD.docx-008`, `XATA_TODO_BRD.docx-005`)
- **BR-006** — System shall support Open, In Progress and Completed statuses. (`XATA_TODO_BRD.docx-008`)
- **BR-007** — System shall support Low, Medium, High and Critical priorities. (`XATA_TODO_BRD.docx-008`)
- **BR-008** — Users shall filter TODOs by status, priority, assignee and due date. (`XATA_TODO_BRD.docx-008`, `XATA_TODO_BRD.docx-005`)
- **BR-009** — Users shall search TODOs by title or description. (`XATA_TODO_BRD.docx-008`, `XATA_TODO_BRD.docx-005`)
- Support user login and a basic user profile. (`XATA_TODO_BRD.docx-005`)
- Users shall be able to view and delete TODOs. (`XATA_TODO_BRD.docx-005`)
- TODOs shall support a description and optional notes. (`XATA_TODO_BRD.docx-005`)
- Provide a dashboard showing TODO status. (`XATA_TODO_BRD.docx-005`)
- Provide a basic team view for assigned TODOs. (`XATA_TODO_BRD.docx-005`)
- Maintain audit information such as created date and updated date for TODOs. (`XATA_TODO_BRD.docx-005`)
- Employee role: create and manage own TODOs, view assigned TODOs, and update status. (`XATA_TODO_BRD.docx-007`)
- Team Lead role: create and assign TODOs, view team TODOs, and monitor overdue work. (`XATA_TODO_BRD.docx-007`)
- Administrator role: manage users and basic platform configuration. (`XATA_TODO_BRD.docx-007`)
- **BR-010** — Dashboard shall show Open, In Progress, Completed and Overdue counts. Priority: Must. (`XATA_TODO_BRD.docx-009`)
- **BR-011** — Team Leads shall view TODOs assigned to their team members. Priority: Must. (`XATA_TODO_BRD.docx-009`)
- **BR-012** — System shall maintain created-by, created-date, updated-by and updated-date for each TODO. Priority: Must. (`XATA_TODO_BRD.docx-009`)
- **BR-013** — Users shall be able to delete TODOs where permitted. Priority: Should. (`XATA_TODO_BRD.docx-009`)
- **BR-014** — System shall prevent unauthorized modification of another user's TODO. Priority: Must. (`XATA_TODO_BRD.docx-009`)
- Create TODO: enter title; enter description; select priority; select due date; optionally assign to a user; save the TODO. (`XATA_TODO_BRD.docx-010`)
- Manage TODO: view details; edit information; change status; change priority or due date; reassign where authorized; delete where authorized. (`XATA_TODO_BRD.docx-011`)
- Dashboard: show total open TODOs, in-progress TODOs, completed TODOs, overdue TODOs, and high/critical priority TODOs. (`XATA_TODO_BRD.docx-012`)
- A TODO must have a title. (`XATA_TODO_BRD.docx-013`)
- A due date cannot be earlier than creation date unless explicitly permitted. (`XATA_TODO_BRD.docx-013`)
- Completed TODOs must have Completed status. (`XATA_TODO_BRD.docx-013`)
- Only authorized users can assign or modify TODOs. (`XATA_TODO_BRD.docx-013`)
- Overdue means due date has passed and status is not Completed. (`XATA_TODO_BRD.docx-013`)
- Deleting a TODO must not delete the user account or other TODOs. (`XATA_TODO_BRD.docx-013`)
- User can log in and create a TODO. (`XATA_TODO_BRD.docx-015`)
- TODO can be assigned, updated and completed. (`XATA_TODO_BRD.docx-015`)
- Dashboard counts correctly reflect TODO state. (`XATA_TODO_BRD.docx-015`)
- Users cannot modify TODOs outside their authorization. (`XATA_TODO_BRD.docx-015`)
- Filtering and search return correct results. (`XATA_TODO_BRD.docx-015`)
- XATA can complete the core TODO lifecycle without administrator assistance. (`XATA_TODO_BRD.docx-015`)

## Non-functional requirements

- The first release shall be intentionally small and easy to use. (`XATA_TODO_BRD.docx-003`)
- The solution shall reduce dependency on spreadsheets, email and chat for TODO tracking. (`XATA_TODO_BRD.docx-004`)
- **BR-015** — System shall provide a web interface through supported browsers. Priority: Must. (`XATA_TODO_BRD.docx-009`)
- Application meets agreed NFRs. (`XATA_TODO_BRD.docx-015`)
- **NFR-PERF-001** — Normal page/API response time must be ≤ 2 seconds for 95% of requests under normal load. (`XATA_TODO_NFR.docx-003`)
- **NFR-PERF-002** — TODO create/update operations must complete in ≤ 2 seconds for 95% of requests. (`XATA_TODO_NFR.docx-003`)
- **NFR-PERF-003** — Dashboard loading must complete in ≤ 3 seconds for 95% of requests. (`XATA_TODO_NFR.docx-003`)
- **NFR-PERF-004** — Search/filter response must be ≤ 2 seconds for 95% of requests. (`XATA_TODO_NFR.docx-003`)
- **NFR-PERF-005** — The platform must support at least 500 concurrent active users. (`XATA_TODO_NFR.docx-003`)
- **NFR-AVL-001** — Monthly availability shall be ≥ 99.5%, excluding agreed maintenance windows. (`XATA_TODO_NFR.docx-004`)
- **NFR-AVL-002** — Planned maintenance shall be communicated at least 24 hours in advance. (`XATA_TODO_NFR.docx-004`)
- **NFR-AVL-003** — Service shall be restored within 30 minutes after an application failure. (`XATA_TODO_NFR.docx-004`)
- The solution shall support growth in users and TODO volume without major redesign. (`XATA_TODO_NFR.docx-005`)
- The solution shall support at least 100,000 TODO records initially. (`XATA_TODO_NFR.docx-005`)
- Application services should be horizontally scalable where practical. (`XATA_TODO_NFR.docx-005`)
- Database design shall support future growth beyond initial capacity. (`XATA_TODO_NFR.docx-005`)
- All users shall be authenticated before accessing protected functionality. (`XATA_TODO_NFR.docx-006`)
- Authorization shall be role-based. (`XATA_TODO_NFR.docx-006`)
- Users shall only access TODO data permitted by their role. (`XATA_TODO_NFR.docx-006`)
- Data shall be encrypted in transit using HTTPS/TLS. (`XATA_TODO_NFR.docx-006`)
- Sensitive credentials shall not be hard-coded. (`XATA_TODO_NFR.docx-006`)
- If passwords are locally managed, they shall use secure industry-standard hashing. (`XATA_TODO_NFR.docx-006`)
- The application shall protect against common web vulnerabilities, including injection, broken access control and XSS. (`XATA_TODO_NFR.docx-006`)
- Administrative actions should be auditable. (`XATA_TODO_NFR.docx-006`)
- TODO records shall have unique identifiers. (`XATA_TODO_NFR.docx-007`)
- Required fields shall be validated server-side. (`XATA_TODO_NFR.docx-007`)
- Updates shall not silently overwrite conflicting data. (`XATA_TODO_NFR.docx-007`)
- Created and updated timestamps shall be stored consistently. (`XATA_TODO_NFR.docx-007`)
- Referential integrity shall be maintained between TODOs and users. (`XATA_TODO_NFR.docx-007`)
- Deleted data handling shall follow XATA's retention policy. (`XATA_TODO_NFR.docx-007`)
- Core create/update/complete flow should require minimal steps. (`XATA_TODO_NFR.docx-008`)
- UI shall be responsive for standard desktop and tablet screens. (`XATA_TODO_NFR.docx-008`)
- Validation errors shall be understandable. (`XATA_TODO_NFR.docx-008`)
- Status, priority and overdue items shall be visually distinguishable. (`XATA_TODO_NFR.docx-008`)
- Common actions shall be discoverable without technical knowledge. (`XATA_TODO_NFR.docx-008`)
- Target WCAG 2.1 AA principles where practical. (`XATA_TODO_NFR.docx-009`)
- Keyboard navigation should support core workflows. (`XATA_TODO_NFR.docx-009`)
- Form controls should have meaningful labels. (`XATA_TODO_NFR.docx-009`)
- Text should have sufficient contrast and readable sizing. (`XATA_TODO_NFR.docx-009`)
- Solution shall use modular, maintainable code. (`XATA_TODO_NFR.docx-010`)
- Business logic shall be separated from presentation and persistence. (`XATA_TODO_NFR.docx-010`)
- APIs and major components shall be documented. (`XATA_TODO_NFR.docx-010`)
- Automated unit tests shall cover critical business logic. (`XATA_TODO_NFR.docx-010`)
- Configuration shall be externalized from source code. (`XATA_TODO_NFR.docx-010`)
- Logging shall support troubleshooting without exposing sensitive information. (`XATA_TODO_NFR.docx-010`)
- Application errors shall be logged with sufficient troubleshooting context. (`XATA_TODO_NFR.docx-011`)
- Health checks shall be available. (`XATA_TODO_NFR.docx-011`)
- Key metrics should include request failures and response latency. (`XATA_TODO_NFR.docx-011`)
- Logs should include correlation/request identifiers where appropriate. (`XATA_TODO_NFR.docx-011`)
- Operational alerts should be configurable for service failures. (`XATA_TODO_NFR.docx-011`)
- Production data shall be backed up according to an agreed schedule. (`XATA_TODO_NFR.docx-012`)
- Backups shall be protected from unauthorized access. (`XATA_TODO_NFR.docx-012`)
- Solution shall support restoration after major failure. (`XATA_TODO_NFR.docx-012`)
- Target RPO: 15 minutes unless XATA agrees otherwise. (`XATA_TODO_NFR.docx-012`)
- Target RTO: 30 minutes. (`XATA_TODO_NFR.docx-012`)
- Support current versions of major enterprise browsers such as Chrome and Edge. (`XATA_TODO_NFR.docx-013`)
- Avoid browser-specific functionality unless approved. (`XATA_TODO_NFR.docx-013`)
- APIs should use documented, versionable interfaces. (`XATA_TODO_NFR.docx-013`)
- Collect only data required for TODO management. (`XATA_TODO_NFR.docx-014`)
- Access to personal/team information shall follow XATA authorization rules. (`XATA_TODO_NFR.docx-014`)
- Sensitive information shall not be written to application logs. (`XATA_TODO_NFR.docx-014`)
- Data retention and deletion shall follow XATA policy. (`XATA_TODO_NFR.docx-014`)
- Critical application/database components shall have documented recovery procedures. (`XATA_TODO_NFR.docx-015`)
- Recovery procedures shall be tested periodically. (`XATA_TODO_NFR.docx-015`)
- XBS shall document dependencies required to restore the service. (`XATA_TODO_NFR.docx-015`)
- XBS shall demonstrate compliance with agreed NFRs through appropriate testing, evidence, configuration review and operational validation before production acceptance. (`XATA_TODO_NFR.docx-016`)
- Security NFR category has priority Must. (`XATA_TODO_NFR.docx-017`)
- Performance NFR category has priority Must. (`XATA_TODO_NFR.docx-017`)
- Availability NFR category has priority Must. (`XATA_TODO_NFR.docx-017`)
- Data Integrity NFR category has priority Must. (`XATA_TODO_NFR.docx-017`)
- Backup & Recovery NFR category has priority Must. (`XATA_TODO_NFR.docx-017`)
- Usability NFR category has priority Must. (`XATA_TODO_NFR.docx-017`)
- Maintainability NFR category has priority Must. (`XATA_TODO_NFR.docx-017`)
- Accessibility NFR category has priority Should. (`XATA_TODO_NFR.docx-017`)
- Advanced observability NFR category has priority Should. (`XATA_TODO_NFR.docx-017`)

## Clarifications and decisions

### Question 1

What does 'quickly' mean for creating and updating TODO items (for example, a target number of steps or time), and how will it be measured?

Response time is quantified: create/update operations must complete within 2 seconds for 95% of requests. 'Quickly' is otherwise only described as requiring minimal steps, with no step count or usability measure.

- `XATA_TODO_BRD.docx-004` — Allow users to quickly create and update TODOs.
- `XATA_TODO_NFR.docx-003` — TODO create/update operation | ≤ 2 seconds for 95% of requests
- `XATA_TODO_NFR.docx-008` — Core create/update/complete flow should require minimal steps.

**Decision pending** — What is the target number of steps or the usability measure for the create/update flow, and how will 'minimal steps' be tested and accepted?

**Provisional assumption** — 'Minimal steps' means creating a TODO requires only the BRD's section 7.1 fields and one save action, verified through usability testing with XATA users.
**Rationale** — This gives the team a concrete, testable basis for the usability requirement until XATA sets an explicit target.

### Question 2

What is the scope of 'basic' priority and due-date management (for example, priority levels, due-date rules, and overdue definition)?

Priority levels are Low, Medium, High and Critical. Overdue means the due date has passed and the status is not Completed. A due date cannot be earlier than the creation date unless explicitly permitted.

- `XATA_TODO_BRD.docx-008` — System shall support Low, Medium, High and Critical priorities.
- `XATA_TODO_BRD.docx-013` — Overdue means due date has passed and status is not Completed.
- `XATA_TODO_BRD.docx-013` — A due date cannot be earlier than creation date unless explicitly permitted.

**Decision pending** — Who can grant the explicit permission for a due date earlier than the creation date, and is a due date mandatory for every TODO?

**Provisional assumption** — A due date is optional, and only Team Leads and Administrators may permit a due date earlier than the creation date.
**Rationale** — This resolves the open exception rule with a sensible role-based default that can be confirmed with XATA.

### Question 3

What is the definition of a 'team' and how are team members grouped for TODO assignment and team-level TODO management?

The BRD does not define a team. It states that XATA will provide the team structure and that Team Leads view TODOs assigned to their team members.

- `XATA_TODO_BRD.docx-014` — XATA will provide the user list and team structure.
- `XATA_TODO_BRD.docx-007` — Team Lead | Team-level user | Create/assign TODOs; view team TODOs; monitor overdue work.
- `XATA_TODO_BRD.docx-009` — Team Leads shall view TODOs assigned to their team members.

**Decision pending** — What constitutes a team, how is membership recorded, and can a user belong to more than one team?

**Provisional assumption** — A team is a named group of users with one Team Lead, and each user belongs to exactly one team, based on the structure XATA provides.
**Rationale** — A single-team-per-user model is the simplest basis for team views and Team Lead permissions until XATA confirms the structure.

### Question 4

What content and metrics must the 'simple dashboard' include, and what does 'understand team workload' from the background require beyond the dashboard?

The dashboard must show Open, In Progress, Completed and Overdue counts (BR-010), plus High/Critical priority TODOs (section 7.3). The BRD does not define workload beyond the basic team view, and resource capacity planning is out of scope.

- `XATA_TODO_BRD.docx-009` — Dashboard shall show Open, In Progress, Completed and Overdue counts.
- `XATA_TODO_BRD.docx-012` — High/Critical priority TODOs.
- `XATA_TODO_BRD.docx-006` — Resource capacity planning.
- `XATA_TODO_BRD.docx-005` — Basic team view for assigned TODOs.

**Decision pending** — Does 'understand team workload' require per-assignee or per-team counts, and does 'Total open TODOs' include In Progress items?

**Provisional assumption** — Team workload means per-assignee counts of open, in-progress and overdue TODOs shown in the basic team view, with no capacity or effort measures.
**Rationale** — This uses existing in-scope team view and dashboard counts without adding out-of-scope capacity planning.

### Question 5

What measurable target defines success for 'reduce dependency on spreadsheets, email and chat', and what is the baseline?

- `XATA_TODO_BRD.docx-004` — Reduce dependency on spreadsheets, email and chat for TODO tracking.
- `XATA_TODO_BRD.docx-003` — XATA currently manages TODO items through a combination of email, spreadsheets, chat messages and personal notes.

**Decision pending** — What measurable target and baseline define success for reducing dependency on spreadsheets, email and chat? The BRD states the objective and the current practice qualitatively but gives no metric, target value, or measurement period.

**Provisional assumption** — Success is the share of in-scope team TODOs tracked in the platform, with the baseline set by a pre-launch measurement of current tracking practice.
**Rationale** — A proportion-based metric gives the objective a measurable form, and a pre-launch baseline gives it a reference point, though XATA must confirm both.

### Question 6

The supplied evidence contains no non-functional requirements (for example security, performance, availability, accessibility, or integration constraints). Are such requirements defined in another source, or are they out of scope for this BRD?

The non-functional requirements are defined in a separate document, XATA_TODO_NFR.docx, which XATA expects XBS to consider. They are not out of scope; the BRD assumptions also direct XBS to propose architecture based on both the BRD and NFR.

- `XATA_TODO_NFR.docx-002` — This document defines the non-functional requirements that XATA expects XBS to consider
- `XATA_TODO_BRD.docx-014` — XBS will propose the technical architecture based on the BRD and NFR.

### Question 7

BR-003 refers to TODOs users 'are authorized to manage', but the evidence does not define what authorization applies or which roles hold it.

Authorization is required to be role-based, and users may only access TODO data permitted by their role. Employees manage their own TODOs, and Team Leads create/assign TODOs and view team TODOs, but the BRD does not state which roles may edit TODOs owned by others.

- `XATA_TODO_NFR.docx-006` — Authorization shall be role-based.
- `XATA_TODO_BRD.docx-007` — Create/manage own TODOs; view assigned TODOs; update status.

**Decision pending** — Which roles hold the authority to edit TODOs they do not own, and under what conditions (for example, whether Team Leads may edit TODOs of their team members, or Administrators may edit any TODO)?

**Provisional assumption** — Employees may edit only their own TODOs, while Team Leads may also edit TODOs assigned to members of their team.
**Rationale** — This follows the stated role responsibilities and Team Lead visibility over team TODOs, giving a concrete starting rule for the design to confirm with XATA.

### Question 8

BR-005 allows assignment to 'another authorized user', but the evidence does not define who is authorized to receive assignments or how authorization is determined.

- `XATA_TODO_BRD.docx-008` — Users shall be able to assign a TODO to another authorized user.
- `XATA_TODO_BRD.docx-013` — Only authorized users can assign or modify TODOs.
- `XATA_TODO_BRD.docx-010` — Optionally assign to a user.

**Decision pending** — Who is eligible to receive a TODO assignment, and how is that eligibility determined (for example, all active users, only team members, or only users in a particular role)? The BRD says assignment is to 'another authorized user' but does not define authorization for receiving assignments.

**Provisional assumption** — Any active user in XATA's supplied user list may receive an assignment, while only users permitted to assign may create assignments to others.
**Rationale** — The BRD allows optional assignment to a user and only restricts who may assign, so treating all active users as assignable is the simplest starting point for XATA to confirm.

### Question 9

The in-scope list includes deleting TODOs, but no business requirement or role responsibility states who may delete a TODO or under what conditions.

Deletion is limited to users where permitted or authorized, and deleting a TODO must not delete the user account or other TODOs. The BRD does not name which roles may delete or the conditions that apply.

- `XATA_TODO_BRD.docx-005` — Create, view, edit and delete TODOs.
- `XATA_TODO_BRD.docx-009` — Users shall be able to delete TODOs where permitted.
- `XATA_TODO_BRD.docx-011` — Delete where authorized.
- `XATA_TODO_BRD.docx-013` — Deleting a TODO must not delete the user account or other TODOs.

**Decision pending** — Which roles or ownership conditions allow a TODO to be deleted, and should deletion be limited to the creator, assignee, Team Lead or Administrator?

**Provisional assumption** — Only the TODO's creator or an Administrator may delete it, and deletion is a hard delete limited to that single TODO record.
**Rationale** — This gives a conservative default that matches the 'where permitted' wording and the rule that deletion must not affect other records, pending XATA confirmation.

### Question 10

The evidence does not define 'overdue' for the Team Lead's monitoring responsibility or what 'team' comprises.

Overdue is defined as a TODO whose due date has passed and whose status is not Completed. The documents do not define what the team comprises, but they state that XATA will provide the team structure.

- `XATA_TODO_BRD.docx-013` — Overdue means due date has passed and status is not Completed.
- `XATA_TODO_BRD.docx-009` — Team Leads shall view TODOs assigned to their team members.
- `XATA_TODO_BRD.docx-014` — XATA will provide the user list and team structure.

**Decision pending** — How is team membership determined for a Team Lead, such as direct reports, a configured team list, or a hierarchy, and what source will XATA supply?

**Provisional assumption** — A Team Lead's team is the set of users XATA assigns to that Team Lead in the team structure XATA provides.
**Rationale** — This links the team definition to the one input the BRD assigns to XATA, which lets the team view be built before the structure is confirmed.

### Question 11

The scope of 'basic platform configuration' for the Administrator role is not defined.

- `XATA_TODO_BRD.docx-007` — Manage users and basic platform configuration.
- `XATA_TODO_NFR.docx-010` — Configuration shall be externalized from source code.

**Decision pending** — What specific configuration activities fall under the Administrator's 'basic platform configuration' responsibility, and which of them are in scope for the first release?

**Provisional assumption** — Basic platform configuration is limited to user account and role administration until XATA defines a fuller list.
**Rationale** — The only related BRD text is 'Manage users', so limiting the term to user and role administration avoids inventing configuration scope.

### Question 12

The in-scope list includes optional notes, but BR-002 lists only title, description, status, priority and due date. It is unclear whether notes are a required, optional, or separate field.

The in-scope list describes notes as optional, while BR-002 names only title, description, status, priority and due date as the TODO's contents, so notes are not a required field.

- `XATA_TODO_BRD.docx-005` — Add description and optional notes.
- `XATA_TODO_BRD.docx-008` — A TODO shall contain title, description, status, priority and due date.

**Decision pending** — Is notes a separate optional free-text field on the TODO record, and should it be available at creation and during editing?

**Provisional assumption** — Notes is an optional free-text field on the TODO record that can be added or edited after creation.
**Rationale** — This follows the 'optional notes' wording and keeps notes out of the required-field validation set by BR-002.

### Question 13

The level of detail required for the dashboard showing TODO status and the basic team view is not defined.

The BRD defines the dashboard's minimum content: counts for Open, In Progress, Completed and Overdue TODOs (BR-010), plus Total open, In-progress, Completed, Overdue and High/Critical priority TODOs (section 7.3). It also defines the basic team view as showing TODOs assigned to team members for Team Leads (BR-011).

- `XATA_TODO_BRD.docx-009` — Dashboard shall show Open, In Progress, Completed and Overdue counts.
- `XATA_TODO_BRD.docx-005` — Basic team view for assigned TODOs.
- `XATA_TODO_BRD.docx-012` — High/Critical priority TODOs.

**Decision pending** — What layout, drill-down depth, filters, and per-member detail are required for the dashboard and the basic team view?

**Provisional assumption** — The dashboard shows only the counts listed in BR-010 and section 7.3, and the team view lists each team member's assigned TODOs with status, priority and due date.
**Rationale** — This keeps the first release to the minimum content the BRD already names, which avoids inventing UI detail that XATA has not requested.

### Question 14

The supplied evidence contains no non-functional requirements (such as performance, security, availability, or accessibility targets), so it is unclear whether none were specified or they were omitted from the BRD extract.

The BRD itself contains no NFRs, but the supplied separate XATA_TODO_NFR.docx defines them, including performance, availability, security, usability, accessibility, backup and recovery targets.

- `XATA_TODO_NFR.docx-001` — Non-Functional Requirements (NFR)
- `XATA_TODO_NFR.docx-003` — Normal page/API response time

### Question 15

Which browsers are 'supported browsers' for BR-015, and which versions are in scope?

The NFR names current versions of major enterprise browsers, given as examples Chrome and Edge, as the compatibility target. The BRD requires a web interface through supported browsers, but does not list them.

- `XATA_TODO_NFR.docx-013` — Support current versions of major enterprise browsers such as Chrome and Edge.
- `XATA_TODO_BRD.docx-009` — System shall provide a web interface through supported browsers.

**Decision pending** — Which browsers and minimum versions form the definitive supported list, given that 'such as' implies Chrome and Edge are examples only?

**Provisional assumption** — The supported browsers are the current stable versions of Google Chrome and Microsoft Edge.
**Rationale** — This gives the team a concrete, testable browser target based on the only browsers named in the NFR.

### Question 16

What rules define 'where permitted' for deletion (BR-013) and 'where authorized' for reassignment and deletion (section 7.2)? Authorization roles and criteria are not specified.

The BRD makes deletion and reassignment conditional on authorization but does not define the criteria. It requires that only authorized users can assign or modify TODOs, and the NFR requires role-based authorization so users access only the TODO data permitted by their role. Role descriptions give Employees control of their own TODOs and Team Leads control over team TODOs.

- `XATA_TODO_BRD.docx-009` — Users shall be able to delete TODOs where permitted.
- `XATA_TODO_BRD.docx-011` — Reassign where authorized.
- `XATA_TODO_BRD.docx-013` — Only authorized users can assign or modify TODOs.
- `XATA_TODO_NFR.docx-006` — Authorization shall be role-based.

**Decision pending** — Which roles and conditions (ownership, team membership, assignee status) permit deletion and reassignment of a TODO, and does an Administrator have any TODO-level rights?

**Provisional assumption** — A TODO owner may delete it, and a Team Lead may reassign or delete TODOs assigned to their team members, while Administrators have no TODO-level delete or reassign rights.
**Rationale** — This maps the existing role descriptions onto the delete and reassign actions so development can proceed, pending XATA confirmation.

### Question 17

Section 7.3 lists 'Total open TODOs' and 'High/Critical priority TODOs', which are not in BR-010. Is the dashboard required to show these counts, and how is 'Open' (BR-010) distinguished from 'Total open' (7.3)? Also, how is 'Overdue' defined?

'Overdue' is defined in the BRD as a due date that has passed while the status is not Completed. BR-010 requires Open, In Progress, Completed and Overdue counts, while section 7.3 separately lists 'Total open' and 'High/Critical' TODOs. The BRD does not distinguish 'Open' from 'Total open'.

- `XATA_TODO_BRD.docx-013` — Overdue means due date has passed and status is not Completed.
- `XATA_TODO_BRD.docx-009` — Dashboard shall show Open, In Progress, Completed and Overdue counts.
- `XATA_TODO_BRD.docx-012` — Total open TODOs.
- `XATA_TODO_BRD.docx-012` — High/Critical priority TODOs.

**Decision pending** — Is the dashboard required to show 'Total open' and 'High/Critical priority' counts in addition to BR-010, and how do 'Open' (BR-010) and 'Total open' (7.3) differ?

**Provisional assumption** — 'Total open' means the combined count of Open and In Progress TODOs, and the High/Critical count is an additional dashboard tile.
**Rationale** — This reading reconciles the two lists without dropping any required count, but XATA must confirm it.

### Question 18

How are a Team Lead's team members defined and maintained for the team-view requirement in BR-011?

The BRD says XATA will provide the user list and team structure, and the Administrator role manages users. It does not define how team membership is represented or who maintains it over time.

- `XATA_TODO_BRD.docx-014` — XATA will provide the user list and team structure.
- `XATA_TODO_BRD.docx-007` — Manage users and basic platform configuration.
- `XATA_TODO_BRD.docx-007` — Team-level user

**Decision pending** — How is team membership recorded (for example, a manager attribute or team assignment), and who maintains it after go-live: Administrators or XATA?

**Provisional assumption** — Administrators maintain team membership using the team structure XATA supplies.
**Rationale** — The Administrator role already manages users, so this gives a clear owner, though XATA must confirm it.

### Question 19

Who is permitted to approve a due date earlier than the creation date, and under what conditions is this 'explicit permission' given?

- `XATA_TODO_BRD.docx-013` — A due date cannot be earlier than creation date unless explicitly permitted.

**Decision pending** — Who may approve a due date earlier than the creation date, and what conditions must be met for that explicit permission to be granted?

**Provisional assumption** — Only Administrators may grant explicit permission for a due date earlier than the creation date.
**Rationale** — Administrators hold platform configuration responsibility, which makes them the most likely approver, but the BRD does not say so.

### Question 20

How are 'authorized users' defined, and what authorization model governs who can assign, modify, or update TODOs?

The NFR requires role-based authorization, and users may access only the TODO data their role permits. The BRD says only authorized users can assign or modify TODOs and that users cannot modify TODOs outside their authorization. The BRD does not define 'authorized users' explicitly.

- `XATA_TODO_NFR.docx-006` — Authorization shall be role-based.
- `XATA_TODO_NFR.docx-006` — Users shall only access TODO data permitted by their role.
- `XATA_TODO_BRD.docx-013` — Only authorized users can assign or modify TODOs.
- `XATA_TODO_BRD.docx-015` — Users cannot modify TODOs outside their authorization.

**Decision pending** — Which roles (Employee, Team Lead, Administrator) may assign or modify TODOs owned by others, and what precisely makes a user 'authorized'?

**Provisional assumption** — Employees may modify only their own TODOs, Team Leads may assign and modify TODOs for their team members, and Administrators manage users and configuration only.
**Rationale** — This maps the BRD role descriptions onto the role-based model the NFR requires, but the exact permission matrix must be confirmed by XATA.

### Question 21

What are the 'agreed NFRs'? The NFR evidence is referenced but not included in the supplied evidence, so the non-functional acceptance threshold cannot be determined.

The supplied NFR document (XATA_TODO_NFR.docx v1.0) is present and sets specific targets in sections 2 to 14, so the premise that the NFR evidence is missing does not hold. The document does not say which NFRs are 'agreed'. Section 15 refers to 'agreed NFRs' without listing them, and the Section 16 priority table marks Accessibility and Advanced observability as Should.

- `XATA_TODO_NFR.docx-016` — XBS shall demonstrate compliance with agreed NFRs through appropriate testing
- `XATA_TODO_BRD.docx-015` — Application meets agreed NFRs.
- `XATA_TODO_NFR.docx-017` — Accessibility | Should

**Decision pending** — Has XATA formally agreed the full NFR v1.0 target set, and do the Should-priority categories (Accessibility, Advanced observability) form part of the acceptance threshold?

**Provisional assumption** — All NFR-* targets in XATA_TODO_NFR.docx v1.0 are the agreed NFR set, with Must-priority categories treated as mandatory for acceptance.
**Rationale** — It gives the reviewer a concrete, testable acceptance baseline from the supplied NFR document while the agreement status is confirmed.

### Question 22

What fields, criteria, and scope are covered by 'filtering and search', and what defines a 'correct' result?

Filtering is required by status, priority, assignee and due date (BR-008, Must). Search is required by title or description (BR-009, Should). The source does not define what makes a result 'correct'.

- `XATA_TODO_BRD.docx-008` — Users shall filter TODOs by status, priority, assignee and due date.
- `XATA_TODO_BRD.docx-008` — Users shall search TODOs by title or description.
- `XATA_TODO_BRD.docx-015` — Filtering and search return correct results.

**Decision pending** — What defines a correct result: match semantics (exact or partial, case sensitivity), combined filter logic (AND/OR), and the visibility scope the results are drawn from?

**Provisional assumption** — A correct result is one that returns exactly the TODOs matching all selected filter criteria and search text, limited to TODOs the user is authorized to view.
**Rationale** — This gives a testable pass/fail rule for acceptance that aligns with the authorization rules in the BRD.

### Question 23

What counts are required on the dashboard, and how is each count defined in terms of TODO state (for example, how overdue TODOs are counted)?

BR-010 requires the dashboard to show Open, In Progress, Completed and Overdue counts. Section 7.3 also lists 'Total open', and High/Critical priority TODOs. Overdue is defined as due date passed and status not Completed. The source does not define whether 'Open' includes In Progress, or how the High/Critical count is defined.

- `XATA_TODO_BRD.docx-009` — Dashboard shall show Open, In Progress, Completed and Overdue counts.
- `XATA_TODO_BRD.docx-012` — Total open TODOs.
- `XATA_TODO_BRD.docx-013` — Overdue means due date has passed and status is not Completed.

**Decision pending** — Does the 'Open' or 'Total open' count include In Progress TODOs, does the Overdue count overlap with the Open and In Progress counts, and is the High/Critical priority count required on the dashboard?

**Provisional assumption** — The Open count includes only Open-status TODOs, In Progress is shown separately, Overdue counts Open and In Progress TODOs past due, and High/Critical is an additional count.
**Rationale** — The BRD names Open and In Progress as separate statuses, so this reading keeps each count mutually clear while using the stated overdue rule.

### Question 24

NFR-PERF-001 applies only "under normal load", but the source does not define normal load (for example, the number of concurrent users or request volume). What load profile should the response-time target be measured against?

The NFR document gives no definition of 'normal load'. The only load figure is NFR-PERF-005, which requires at least 500 concurrent active users. Scalability section 4 sets a volume target of at least 100,000 TODO records initially, but no request volume is defined.

- `XATA_TODO_NFR.docx-003` — Concurrent active users | At least 500
- `XATA_TODO_NFR.docx-005` — Support at least 100,000 TODO records initially.

**Decision pending** — What concurrent user count, request rate and TODO data volume define 'normal load' for measuring the NFR-PERF-001 response-time target?

**Provisional assumption** — Normal load is 500 concurrent active users (the NFR-PERF-005 figure) against a dataset of 100,000 TODO records.
**Rationale** — Using the documented concurrency and data-volume figures gives a concrete load profile for performance testing until XATA defines normal load.

### Question 25

NFR-PERF-005 requires at least 500 concurrent active users but does not state whether the performance targets in NFR-PERF-001 to NFR-PERF-004 must be met at that concurrency level. Is the 500-user requirement expected to be tested against those response-time targets?

- `XATA_TODO_NFR.docx-003` — Concurrent active users | At least 500
- `XATA_TODO_NFR.docx-003` — ≤ 2 seconds for 95% of requests under normal load

**Decision pending** — Must the NFR-PERF-001 to NFR-PERF-004 response-time targets be met while 500 concurrent active users are active, and should the 500-user requirement be load-tested against them?

**Provisional assumption** — Test the 500-concurrent-user requirement against the same NFR-PERF-001 to NFR-PERF-004 response-time targets.
**Rationale** — Applying the existing targets at 500 users gives a single, testable pass/fail criterion until XATA confirms the intent.

### Question 26

The 95% response-time targets (NFR-PERF-001 to NFR-PERF-004) do not specify the measurement window or sampling method (for example, per day, per hour, or per test run). How should compliance with the 95% threshold be measured?

- `XATA_TODO_NFR.docx-003` — ≤ 2 seconds for 95% of requests under normal load
- `XATA_TODO_NFR.docx-016` — XBS shall demonstrate compliance with agreed NFRs through appropriate testing, evidence, configuration review and operational validation before production acceptance.

**Decision pending** — What measurement window (per day, per hour, or per test run) and sampling method should be used to determine whether 95% of requests meet the NFR-PERF-001 to NFR-PERF-004 targets?

**Provisional assumption** — Measure the 95% threshold over each formal load-test run under normal load, using all requests sampled during that run.
**Rationale** — A per-test-run measure is concrete and fits the NFR acceptance approach of testing before production, so it gives a usable criterion until XATA specifies otherwise.

### Question 27

Which maintenance windows are agreed and excluded from the 99.5% monthly availability target, and how is availability measured?

- `XATA_TODO_NFR.docx-004` — ≥ 99.5%, excluding agreed maintenance windows

**Decision pending** — Which specific maintenance windows has XATA agreed to exclude from the 99.5% monthly availability target, and what measurement method (monitoring source, calculation basis and reporting period) defines availability?

**Provisional assumption** — Calculate monthly availability as uptime divided by total calendar-month minutes minus only maintenance windows that XATA has approved in writing and that were communicated under NFR-AVL-002.
**Rationale** — Tying exclusions to written approval and advance notice gives a verifiable basis for the availability calculation until XATA lists the agreed windows.

### Question 28

Who must receive the 24-hour advance communication of planned maintenance, and through which channel?

- `XATA_TODO_NFR.docx-004` — Communicated ≥24 hours in advance
- `XATA_TODO_BRD.docx-016` — XATA IT | Technical / Operational Stakeholders

**Decision pending** — Who specifically must receive the 24-hour advance notice of planned maintenance (for example, XATA IT, end users, or Team Leads), and through which channel (email, banner, status page, or other)?

**Provisional assumption** — Send planned-maintenance notice at least 24 hours in advance to XATA IT by email, with a copy to the business owner.
**Rationale** — XATA IT is named as the technical and operational stakeholder in the BRD, so it is a reasonable default recipient until XATA confirms the audience and channel.

### Question 29

When does the 30-minute service restoration clock start and stop, and what constitutes restored service?

- `XATA_TODO_NFR.docx-004` — Service restored within 30 minutes

**Decision pending** — The NFR states the recovery target but does not define when the 30-minute clock starts or stops, or what counts as restored service. Who must confirm the start event, stop event, and restored-service criteria?

**Provisional assumption** — The clock starts when the application failure is detected and stops when the platform's health checks pass for the core TODO create, view, and update flows.
**Rationale** — Tying the start and stop points to detection and health checks gives the team a measurable, testable definition to confirm with XATA.

### Question 30

What time horizon or volume target applies to 'initially' in the 100,000 TODO record requirement, and what defines 'without major redesign'?

The volume target is at least 100,000 TODO records. The source gives no time horizon for 'initially', and it does not define 'without major redesign'.

- `XATA_TODO_NFR.docx-005` — Support at least 100,000 TODO records initially.
- `XATA_TODO_NFR.docx-005` — Support growth in users and TODO volume without major redesign.

**Decision pending** — What time horizon does 'initially' cover, and what changes count as a major redesign?

**Provisional assumption** — Treat 'initially' as the first production release and treat a major redesign as any change to the data model or core architecture.
**Rationale** — Linking 'initially' to the first release and redesign to data model or architecture changes gives a concrete basis for scoping the 100,000-record target.

### Question 31

Where horizontal scalability is required 'where practical,' what criteria determine when it is not practical?

- `XATA_TODO_NFR.docx-005` — Application services should be horizontally scalable where practical.

**Decision pending** — The NFR requires horizontal scalability 'where practical' but does not state the criteria for when it is not practical. Who will define those criteria, and on what basis?

**Provisional assumption** — Horizontal scaling is treated as impractical only where XBS documents a specific technical or cost constraint that XATA accepts in the architecture proposal.
**Rationale** — Requiring a documented, accepted constraint gives a clear exception process without inventing criteria that the source does not contain.

### Question 32

Is the locally managed password requirement applicable, given that the source does not state whether passwords are locally managed?

- `XATA_TODO_NFR.docx-006` — Passwords, if locally managed, shall use secure industry-standard hashing.
- `XATA_TODO_BRD.docx-005` — User login and basic user profile.
- `XATA_TODO_BRD.docx-014` — XBS will propose the technical architecture based on the BRD and NFR.

**Decision pending** — The NFR applies the hashing requirement only if passwords are locally managed, but no source states whether XATA's login will manage passwords locally or use another identity mechanism. Which authentication model will XATA and XBS adopt?

**Provisional assumption** — The hashing requirement applies only if XBS's approved authentication design stores passwords within the platform; otherwise it is delegated to the external identity provider.
**Rationale** — Making the requirement conditional on the approved authentication design lets the team apply it once the login model is confirmed.

### Question 33

Which administrative actions must be auditable, and what is the required audit retention? The 'should' obligation strength is not resolved.

The NFR states that administrative actions should be auditable, which makes this a 'should' obligation. The BRD defines audit fields only for TODO records (created-by, created-date, updated-by, updated-date), and no audit retention period is stated.

- `XATA_TODO_NFR.docx-006` — Administrative actions should be auditable.
- `XATA_TODO_BRD.docx-009` — System shall maintain created-by, created-date, updated-by and updated-date.

**Decision pending** — Which specific administrative actions (for example, user management or role changes, configuration changes) must be audited, and what is the required audit-record retention period?

**Provisional assumption** — Treat user account creation, deactivation, role changes and platform configuration changes as the auditable administrative actions, with audit records retained for the same period as the application's log/retention policy once XATA confirms it.
**Rationale** — It gives XBS a concrete, testable scope for the 'should' requirement while the specific actions and retention period remain unconfirmed.

### Question 34

What is XATA's retention policy referenced for deleted data, and where is it defined?

- `XATA_TODO_NFR.docx-007` — Deleted data handling shall follow XATA's retention policy.
- `XATA_TODO_NFR.docx-014` — Data retention and deletion shall follow XATA policy.

**Decision pending** — XATA must provide its data retention policy, including the retention period for deleted TODOs and any related user or audit data, and confirm where that policy is defined.

**Provisional assumption** — Until XATA provides its policy, XBS should design deletion as a configurable behaviour with no fixed retention period hard-coded.
**Rationale** — This avoids locking in a retention rule that XATA has not yet defined while still allowing the design to comply once the policy is supplied.

### Question 35

The scope of 'where practical' for WCAG 2.1 AA conformance is undefined. Which success criteria or conformance level must be met, and which exceptions apply?

The NFR targets WCAG 2.1 AA principles, applied only where practical, and accessibility is classed as a 'Should' priority. The NFR does not list specific success criteria or define the exceptions.

- `XATA_TODO_NFR.docx-009` — Target WCAG 2.1 AA principles where practical.
- `XATA_TODO_NFR.docx-017` — Accessibility | Should

**Decision pending** — Which WCAG 2.1 AA success criteria must be met, and what conditions qualify as 'not practical' exceptions that XATA would accept?

**Provisional assumption** — Treat all WCAG 2.1 AA success criteria as the target, with any exception recorded and agreed with XATA case by case.
**Rationale** — This gives a testable baseline for conformance and a clear route for documenting exceptions without redefining the 'where practical' wording.

### Question 36

'Standard desktop and tablet screens' and 'minimal steps' are not quantified. What screen sizes, resolutions, and maximum step counts are expected?

The NFR requires the UI to be responsive for standard desktop and tablet screens and says the core create/update/complete flow should require minimal steps. Mobile native applications are out of scope. No screen sizes, resolutions or maximum step counts are specified.

- `XATA_TODO_NFR.docx-008` — UI shall be responsive for standard desktop and tablet screens.
- `XATA_TODO_NFR.docx-008` — Core create/update/complete flow should require minimal steps.
- `XATA_TODO_BRD.docx-006` — Mobile native applications.

**Decision pending** — What specific desktop and tablet screen sizes and resolutions must be supported, and what is the maximum number of steps for the core create, update and complete flows?

**Provisional assumption** — Assume responsive support for common desktop widths (1280px and above) and tablet widths (approximately 768px to 1024px), with the core flow limited to a step count agreed in the design review.
**Rationale** — Stating working viewport ranges gives the design and test teams a concrete starting baseline until XATA confirms the target devices and step limits.

### Question 37

'Critical business logic' for automated unit test coverage is not defined. Which modules or rules are in scope, and is a coverage threshold required?

- `XATA_TODO_NFR.docx-010` — Automated unit tests shall cover critical business logic.
- `XATA_TODO_BRD.docx-013` — Overdue means due date has passed and status is not Completed.

**Decision pending** — Which modules or business rules count as 'critical business logic' for automated unit test coverage, and is a numeric coverage threshold required?

**Provisional assumption** — Treat the BRD Section 8 business rules as the critical business logic in scope for unit tests, with no numeric coverage threshold until XATA sets one.
**Rationale** — The BRD's business rules are the only explicit rule set in the evidence, so they give reviewers a concrete starting scope.

### Question 38

The set of 'key metrics' beyond request failures and response latency is not specified, and no alert thresholds are given for 'service failures'. Which metrics and thresholds are required?

The NFR names request failures and response latency as the key metrics, and says operational alerts should be configurable for service failures, but it sets no alert thresholds.

- `XATA_TODO_NFR.docx-011` — Key metrics should include request failures and response latency.
- `XATA_TODO_NFR.docx-011` — Operational alerts should be configurable for service failures.

**Decision pending** — Which metrics beyond request failures and response latency are required, and what alert thresholds apply to request failures, latency and service failures?

**Provisional assumption** — Use the NFR-PERF-001 target of 2 seconds at the 95th percentile as the response latency alert threshold.
**Rationale** — It reuses an existing NFR target so the latency alert has a measurable starting value until XATA confirms thresholds.

### Question 39

No BRD evidence was supplied, and the NFR evidence contains no requirement IDs or functional requirements. Are there BRD functional requirements and IDs that must be included in this inventory?

The BRD is in the evidence and defines functional requirements BR-001 through BR-015, each with an ID and a Must or Should priority.

- `XATA_TODO_BRD.docx-008` — BR-001 | System shall allow an authenticated user to create a TODO. | Must

**Decision pending** — Must all BR-001 to BR-015 requirements be included in this inventory, or only the Must-priority ones?

**Provisional assumption** — Include all BR-001 to BR-015 requirements in the inventory, with their Must or Should priority carried over.
**Rationale** — Including every BRD requirement with its original priority avoids dropping in-scope functionality before XATA confirms the scope.

### Question 40

Who agrees the backup schedule, and what is its frequency and retention period? The source says only 'an agreed schedule'.

- `XATA_TODO_NFR.docx-012` — Production data shall be backed up according to an agreed schedule.
- `XATA_TODO_NFR.docx-012` — Target RPO: 15 minutes unless XATA agrees otherwise.

**Decision pending** — Who agrees the production backup schedule, and what backup frequency and retention period does it set?

**Provisional assumption** — Set the backup frequency to no longer than 15 minutes so that the stated RPO target can be met, pending XATA agreement.
**Rationale** — The RPO target of 15 minutes is the only quantified backup constraint in the evidence, so it provides a provisional frequency limit.

### Question 41

What constitutes a 'major failure', and what is the restoration time or success criterion after one? The source does not define either.

The NFR gives a 30-minute recovery target: 'Target RTO: 30 minutes' and, for application failure, 'Service restored within 30 minutes'. It does not define 'major failure' or tie the 30-minute target to it.

- `XATA_TODO_NFR.docx-012` — Solution shall support restoration after major failure.
- `XATA_TODO_NFR.docx-012` — Target RTO: 30 minutes.
- `XATA_TODO_NFR.docx-004` — Service restored within 30 minutes

**Decision pending** — What qualifies as a 'major failure', and does the 30-minute RTO apply to it?

**Provisional assumption** — Treat a major failure as an unplanned outage that requires restoration from backup, and apply the 30-minute RTO to it.
**Rationale** — This gives the reviewer a working definition and a measurable restoration target until XATA confirms the scope.

### Question 42

Who may agree to a different RPO, and what is the process for that agreement? The source says only 'unless XATA agrees otherwise'.

XATA is the party whose agreement can change the default RPO of 15 minutes. The source does not say who within XATA may agree or how that agreement is made.

- `XATA_TODO_NFR.docx-012` — Target RPO: 15 minutes unless XATA agrees otherwise.

**Decision pending** — Which XATA role may approve a different RPO, and what process (for example, a formal change request) must be followed?

**Provisional assumption** — The XATA business owner approves any RPO change in writing before it takes effect.
**Rationale** — The BRD names XATA as the Business Owner / Client, which gives a reasonable default approver until XATA confirms.

### Question 43

Which browsers and versions are in scope beyond Chrome and Edge? 'Major enterprise browsers' and 'current versions' are not defined.

Chrome and Edge are named only as examples ('such as'), so the list is not exhaustive. The source does not identify other browsers or which versions are in scope.

- `XATA_TODO_NFR.docx-013` — Support current versions of major enterprise browsers such as Chrome and Edge.
- `XATA_TODO_BRD.docx-009` — System shall provide a web interface through supported browsers.

**Decision pending** — Which enterprise browsers and versions must be supported beyond Chrome and Edge, and what does 'current' mean?

**Provisional assumption** — In-scope browsers are the latest two major versions of Chrome, Edge, Firefox and Safari.
**Rationale** — This gives the design team a concrete test matrix while XATA confirms the official browser list.

### Question 44

Who approves browser-specific functionality, and what approval criteria apply?

The NFR requires that browser-specific functionality be avoided unless approved. It does not name an approver or set approval criteria.

- `XATA_TODO_NFR.docx-013` — Avoid browser-specific functionality unless approved.
- `XATA_TODO_BRD.docx-016` — XATA IT | Technical / Operational Stakeholders

**Decision pending** — Who approves browser-specific functionality, and what criteria must be met for approval?

**Provisional assumption** — XATA IT approves browser-specific functionality against the compatibility and maintainability requirements.
**Rationale** — The BRD lists XATA IT as the technical and operational stakeholder, which makes it the most plausible approver until XATA decides.

### Question 45

Which XATA authorization rules and XATA data retention/deletion policies apply? They are referenced but not supplied in the evidence.

- `XATA_TODO_NFR.docx-014` — Access to personal/team information shall follow XATA authorization rules.
- `XATA_TODO_NFR.docx-014` — Data retention and deletion shall follow XATA policy.

**Decision pending** — Which XATA authorization rules and which XATA data retention and deletion policy apply? Neither document is supplied, so XATA must provide them.

**Provisional assumption** — Use the BRD role matrix (Employee, Team Lead, Administrator) and business rules as the interim authorization baseline until XATA supplies its formal rules.
**Rationale** — It gives the team a documented starting point for access design while the formal XATA rules are outstanding.

### Question 46

How often must recovery procedures be tested? 'Periodically' is not quantified.

- `XATA_TODO_NFR.docx-015` — Recovery procedures shall be tested periodically.

**Decision pending** — How often must recovery procedures be tested (for example, a fixed frequency such as annually), and who sets that frequency?

**Provisional assumption** — Recovery procedures are tested at least annually and before production acceptance.
**Rationale** — A fixed annual minimum plus a pre-go-live test gives a measurable cadence for XBS to confirm with XATA.

### Question 47

What does 'XBS' refer to, and what is the scope of the dependency documentation required to restore the service?

XBS is the delivery and implementation partner that designs and builds the platform for XATA. The NFR requires XBS to document the dependencies needed to restore the service.

- `XATA_TODO_BRD.docx-001` — Delivery Partner: XBS
- `XATA_TODO_NFR.docx-015` — XBS shall document dependencies required to restore the service.

**Decision pending** — What exactly must the restore-dependency documentation cover (for example, infrastructure, data stores, third-party services, credentials, and runbooks), and in what format and by when?

**Provisional assumption** — The dependency documentation covers infrastructure, databases, external services, configuration, and credentials needed to restore the service.
**Rationale** — Listing these categories gives XBS a concrete minimum scope to confirm with XATA.

### Question 48

The supplied evidence does not contain the agreed NFR statements, measurable thresholds, units, or time periods for the priority categories; what are the specific agreed NFRs and their acceptance criteria?

The NFR document does contain measurable targets, not just placeholders. Examples include response times of ≤ 2 seconds for 95% of requests, 500 concurrent users, 99.5% monthly availability, and 30-minute recovery time. Priorities are set by category, and compliance is to be shown through testing, evidence, configuration review and operational validation. It is not stated in the evidence that these targets are formally agreed with XATA.

- `XATA_TODO_NFR.docx-003` — ≤ 2 seconds for 95% of requests under normal load
- `XATA_TODO_NFR.docx-004` — ≥ 99.5%, excluding agreed maintenance windows
- `XATA_TODO_NFR.docx-012` — Target RPO: 15 minutes unless XATA agrees otherwise.
- `XATA_TODO_NFR.docx-016` — XBS shall demonstrate compliance with agreed NFRs through appropriate testing, evidence, configuration review and operational validation before production acceptance.
- `XATA_TODO_NFR.docx-017` — Advanced observability | Should

**Decision pending** — Has XATA formally agreed the listed targets and their priorities, and what is the specific acceptance test or threshold for each category, especially the Should categories (Accessibility and Advanced observability) and the qualitative categories (Usability, Maintainability, Security)?

**Provisional assumption** — The targets in NFR sections 2 to 4 and 11 are treated as the agreed baseline unless XATA revises them.
**Rationale** — This lets design and testing start from the documented measurable targets while formal agreement is confirmed.

### Question 49

The priority table uses Must and Should without defining how Should-priority categories (Accessibility, Advanced observability) differ in acceptance obligation from Must-priority categories; is a Should item required for production acceptance?

- `XATA_TODO_NFR.docx-016` — XBS shall demonstrate compliance with agreed NFRs through appropriate testing, evidence, configuration review and operational validation before production acceptance.
- `XATA_TODO_NFR.docx-017` — Accessibility | Should
- `XATA_TODO_NFR.docx-017` — Advanced observability | Should

**Decision pending** — Does XATA treat Should-priority NFR categories (Accessibility and Advanced observability) as required for production acceptance, or as non-gating backlog items? The NFR marks them Should but does not define their acceptance obligation.

**Provisional assumption** — Should-priority NFR categories are non-gating for production acceptance and are tracked as follow-up items unless XATA states otherwise in writing.
**Rationale** — This gives the reviewer a working default that matches the Must/Should distinction without blocking go-live on items the NFR describes as "where practical" or "should".
