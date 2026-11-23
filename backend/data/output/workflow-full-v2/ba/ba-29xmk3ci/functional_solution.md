# Functional solution

**Review draft**

## Source documents

- XATA_TODO_BRD.docx
- XATA_TODO_NFR.docx

## Functional requirements and business rules

- The platform shall allow XATA employees to create, manage, prioritize, track and complete personal and team TODO items. (`XATA_TODO_BRD.docx-002`)
- The platform shall provide a single system for managing TODO items. (`XATA_TODO_BRD.docx-004`)
- The platform shall allow users to quickly create and update TODOs. (`XATA_TODO_BRD.docx-004`)
- The platform shall provide visibility of open, completed and overdue work. (`XATA_TODO_BRD.docx-004`)
- The platform shall allow team members to assign TODOs to one another. (`XATA_TODO_BRD.docx-004`)
- The platform shall provide basic priority and due-date management for TODO items. (`XATA_TODO_BRD.docx-004`)
- The platform shall provide a simple dashboard for work tracking. (`XATA_TODO_BRD.docx-004`)
- **BR-001** — System shall allow an authenticated user to create a TODO. (Priority: Must) (`XATA_TODO_BRD.docx-008`)
- **BR-002** — A TODO shall contain title, description, status, priority and due date. (Priority: Must) (`XATA_TODO_BRD.docx-008`, `XATA_TODO_BRD.docx-005`)
- **BR-003** — Users shall be able to edit TODOs they own or are authorized to manage. (Priority: Must) (`XATA_TODO_BRD.docx-008`)
- **BR-004** — Users shall be able to mark TODOs as completed. (Priority: Must) (`XATA_TODO_BRD.docx-008`, `XATA_TODO_BRD.docx-005`)
- **BR-005** — Users shall be able to assign a TODO to another authorized user. (Priority: Must) (`XATA_TODO_BRD.docx-008`, `XATA_TODO_BRD.docx-005`)
- **BR-006** — System shall support Open, In Progress and Completed statuses. (Priority: Must) (`XATA_TODO_BRD.docx-008`)
- **BR-007** — System shall support Low, Medium, High and Critical priorities. (Priority: Must) (`XATA_TODO_BRD.docx-008`)
- **BR-008** — Users shall filter TODOs by status, priority, assignee and due date. (Priority: Must) (`XATA_TODO_BRD.docx-008`, `XATA_TODO_BRD.docx-005`)
- **BR-009** — Users shall search TODOs by title or description. (Priority: Should) (`XATA_TODO_BRD.docx-008`, `XATA_TODO_BRD.docx-005`)
- In scope: user login and basic user profile. (`XATA_TODO_BRD.docx-005`)
- In scope: view and delete TODOs (create and edit are covered by BR-001 and BR-003). (`XATA_TODO_BRD.docx-005`)
- In scope: add description and optional notes to a TODO. (`XATA_TODO_BRD.docx-005`)
- In scope: dashboard showing TODO status. (`XATA_TODO_BRD.docx-005`)
- In scope: basic team view for assigned TODOs. (`XATA_TODO_BRD.docx-005`)
- In scope: audit information such as created date and updated date for TODOs. (`XATA_TODO_BRD.docx-005`)
- Employee role responsibilities: create/manage own TODOs; view assigned TODOs; update status. (`XATA_TODO_BRD.docx-007`)
- Team Lead role responsibilities: create/assign TODOs; view team TODOs; monitor overdue work. (`XATA_TODO_BRD.docx-007`)
- Administrator role responsibilities: manage users and basic platform configuration. (`XATA_TODO_BRD.docx-007`)
- **BR-010** — Dashboard shall show Open, In Progress, Completed and Overdue counts. (Priority: Must) (`XATA_TODO_BRD.docx-009`)
- **BR-011** — Team Leads shall view TODOs assigned to their team members. (Priority: Must) (`XATA_TODO_BRD.docx-009`)
- **BR-012** — System shall maintain created-by, created-date, updated-by and updated-date. (Priority: Must) (`XATA_TODO_BRD.docx-009`)
- **BR-013** — Users shall be able to delete TODOs where permitted. (Priority: Should) (`XATA_TODO_BRD.docx-009`)
- **BR-014** — System shall prevent unauthorized modification of another user's TODO. (Priority: Must) (`XATA_TODO_BRD.docx-009`)
- Create TODO: user enters title and description, selects priority and due date, optionally assigns to a user, and saves the TODO. (`XATA_TODO_BRD.docx-010`)
- Manage TODO: user can view details, edit information, change status, change priority or due date, reassign where authorized, and delete where authorized. (`XATA_TODO_BRD.docx-011`)
- Dashboard shall show a count of High/Critical priority TODOs. (`XATA_TODO_BRD.docx-012`)
- A TODO must have a title. (`XATA_TODO_BRD.docx-013`)
- A due date cannot be earlier than the creation date unless explicitly permitted. (`XATA_TODO_BRD.docx-013`)
- Completed TODOs must have Completed status. (`XATA_TODO_BRD.docx-013`)
- Only authorized users can assign or modify TODOs, and users cannot modify TODOs outside their authorization. (`XATA_TODO_BRD.docx-013`, `XATA_TODO_BRD.docx-015`)
- Overdue means the due date has passed and the status is not Completed. (`XATA_TODO_BRD.docx-013`)
- Deleting a TODO must not delete the user account or other TODOs. (`XATA_TODO_BRD.docx-013`)
- A user can log in and create a TODO. (`XATA_TODO_BRD.docx-015`)
- A TODO can be assigned, updated, and completed. (`XATA_TODO_BRD.docx-015`)
- Dashboard counts correctly reflect TODO state. (`XATA_TODO_BRD.docx-015`)
- Filtering and search return correct results. (`XATA_TODO_BRD.docx-015`)
- All users shall be authenticated before protected functionality is accessed. (`XATA_TODO_NFR.docx-006`)
- Authorization shall be role-based. (`XATA_TODO_NFR.docx-006`)
- Users shall only access TODO data permitted by their role. (`XATA_TODO_NFR.docx-006`)
- TODO records shall have unique identifiers. (`XATA_TODO_NFR.docx-007`)
- Required fields shall be validated server-side. (`XATA_TODO_NFR.docx-007`)
- Updates shall not silently overwrite conflicting data. (`XATA_TODO_NFR.docx-007`)
- Created and updated timestamps shall be stored consistently. (`XATA_TODO_NFR.docx-007`)
- Referential integrity shall be maintained between TODOs and users. (`XATA_TODO_NFR.docx-007`)
- Deleted data handling shall follow XATA's retention policy. (`XATA_TODO_NFR.docx-007`)

## Non-functional requirements

- XATA wants a simple centralized web application that provides a common place to manage TODOs, with the first release intentionally kept small and easy to use. (`XATA_TODO_BRD.docx-003`)
- **BR-015** — System shall provide a web interface through supported browsers. (Priority: Must) (`XATA_TODO_BRD.docx-009`)
- The initial release is web-based. (`XATA_TODO_BRD.docx-014`)
- The first release uses a single enterprise environment. (`XATA_TODO_BRD.docx-014`)
- The application meets the agreed NFRs. (`XATA_TODO_BRD.docx-015`)
- XATA can complete the core TODO lifecycle without administrator assistance. (`XATA_TODO_BRD.docx-015`)
- **NFR-PERF-001** — Normal page/API response time must be ≤ 2 seconds for 95% of requests under normal load. (`XATA_TODO_NFR.docx-003`)
- **NFR-PERF-002** — TODO create/update operation must complete in ≤ 2 seconds for 95% of requests. (`XATA_TODO_NFR.docx-003`)
- **NFR-PERF-003** — Dashboard loading must complete in ≤ 3 seconds for 95% of requests. (`XATA_TODO_NFR.docx-003`)
- **NFR-PERF-004** — Search/filter response must be ≤ 2 seconds for 95% of requests. (`XATA_TODO_NFR.docx-003`)
- **NFR-PERF-005** — The platform must support at least 500 concurrent active users. (`XATA_TODO_NFR.docx-003`)
- **NFR-AVL-001** — Monthly availability shall be ≥ 99.5%, excluding agreed maintenance windows. (`XATA_TODO_NFR.docx-004`)
- **NFR-AVL-002** — Planned maintenance shall be communicated at least 24 hours in advance. (`XATA_TODO_NFR.docx-004`)
- **NFR-AVL-003** — After an application failure, service shall be restored within 30 minutes. (`XATA_TODO_NFR.docx-004`)
- The solution shall support growth in users and TODO volume without major redesign. (`XATA_TODO_NFR.docx-005`)
- The solution shall support at least 100,000 TODO records initially. (`XATA_TODO_NFR.docx-005`)
- Application services should be horizontally scalable where practical. (`XATA_TODO_NFR.docx-005`)
- Database design shall support future growth beyond initial capacity. (`XATA_TODO_NFR.docx-005`)
- Data shall be encrypted in transit using HTTPS/TLS. (`XATA_TODO_NFR.docx-006`)
- Sensitive credentials shall not be hard-coded. (`XATA_TODO_NFR.docx-006`)
- If passwords are locally managed, they shall use secure industry-standard hashing. (`XATA_TODO_NFR.docx-006`)
- The application shall protect against common web vulnerabilities, including injection, broken access control and XSS. (`XATA_TODO_NFR.docx-006`)
- Administrative actions should be auditable. (`XATA_TODO_NFR.docx-006`)
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
- Target RPO is 15 minutes unless XATA agrees otherwise. (`XATA_TODO_NFR.docx-012`)
- Target RTO is 30 minutes. (`XATA_TODO_NFR.docx-012`)
- Solution shall support current versions of major enterprise browsers such as Chrome and Edge. (`XATA_TODO_NFR.docx-013`)
- Browser-specific functionality shall be avoided unless approved. (`XATA_TODO_NFR.docx-013`)
- APIs should use documented, versionable interfaces. (`XATA_TODO_NFR.docx-013`)
- Solution shall collect only data required for TODO management. (`XATA_TODO_NFR.docx-014`)
- Access to personal/team information shall follow XATA authorization rules. (`XATA_TODO_NFR.docx-014`)
- Sensitive information shall not be written to application logs. (`XATA_TODO_NFR.docx-014`)
- Data retention and deletion shall follow XATA policy. (`XATA_TODO_NFR.docx-014`)
- Critical application/database components shall have documented recovery procedures. (`XATA_TODO_NFR.docx-015`)
- Recovery procedures shall be tested periodically. (`XATA_TODO_NFR.docx-015`)
- XBS shall document dependencies required to restore the service. (`XATA_TODO_NFR.docx-015`)
- XBS shall demonstrate compliance with agreed NFRs through appropriate testing, evidence, configuration review and operational validation before production acceptance. (`XATA_TODO_NFR.docx-016`)
- The Security NFR category has priority Must. (`XATA_TODO_NFR.docx-017`)
- The Performance NFR category has priority Must. (`XATA_TODO_NFR.docx-017`)
- The Availability NFR category has priority Must. (`XATA_TODO_NFR.docx-017`)
- The Data Integrity NFR category has priority Must. (`XATA_TODO_NFR.docx-017`)
- The Backup & Recovery NFR category has priority Must. (`XATA_TODO_NFR.docx-017`)
- The Usability NFR category has priority Must. (`XATA_TODO_NFR.docx-017`)
- The Maintainability NFR category has priority Must. (`XATA_TODO_NFR.docx-017`)
- The Accessibility NFR category has priority Should. (`XATA_TODO_NFR.docx-017`)
- The Advanced observability NFR category has priority Should. (`XATA_TODO_NFR.docx-017`)

## Clarifications and decisions

### Question 1

What response time or effort threshold does 'quickly create and update TODOs' imply? The term is not measurable as written.

The response-time part is answered by NFR-PERF-002, which sets a target of 2 seconds for 95% of TODO create/update requests. No measurable effort threshold is defined; the NFR only asks that the core flow 'require minimal steps'.

- `XATA_TODO_NFR.docx-003` — TODO create/update operation | ≤ 2 seconds for 95% of requests
- `XATA_TODO_NFR.docx-008` — Core create/update/complete flow should require minimal steps.

**Decision pending** — What measurable effort target (for example, maximum number of steps or clicks to create or update a TODO) should replace 'minimal steps'?

**Provisional assumption** — Treat 'quickly' as the NFR-PERF-002 target of 2 seconds for 95% of create/update requests until XATA sets a step-count target.
**Rationale** — This gives the term a testable time threshold now, while the effort dimension is still pending XATA input.

### Question 2

How is 'overdue' defined, and which priority levels are included in 'basic priority' management?

Overdue means a TODO whose due date has passed and whose status is not Completed. The basic priority levels are Low, Medium, High and Critical.

- `XATA_TODO_BRD.docx-013` — Overdue means due date has passed and status is not Completed.
- `XATA_TODO_BRD.docx-008` — System shall support Low, Medium, High and Critical priorities.

### Question 3

Who may assign TODOs to whom, and how are 'team' and 'team members' defined (for example, membership, scope, or permissions)?

The BRD gives the Team Lead role the ability to 'Create/assign TODOs' and requires that users can assign a TODO to 'another authorized user'. Team membership and assignment scope are not defined; XATA is to provide the team structure.

- `XATA_TODO_BRD.docx-007` — Create/assign TODOs; view team TODOs; monitor overdue work.
- `XATA_TODO_BRD.docx-013` — Only authorized users can assign or modify TODOs.
- `XATA_TODO_BRD.docx-014` — XATA will provide the user list and team structure.

**Decision pending** — Who counts as 'authorized' to assign TODOs, and what defines a team and its members (membership source, scope, and whether Employees can assign to peers or only Team Leads can)?

**Provisional assumption** — Team Leads may assign TODOs to members of the team structure XATA provides, and Employees may assign only to themselves.
**Rationale** — This maps the stated roles to a concrete assignment scope while XATA supplies the team structure and the authorization rules.

### Question 4

What content, metrics, and views must the 'simple dashboard for work tracking' include?

The dashboard must show Open, In Progress, Completed and Overdue counts, and must also show total open, in-progress, completed, overdue and High/Critical priority TODOs. A basic team view for assigned TODOs is in scope, and the dashboard must load within 3 seconds for 95% of requests.

- `XATA_TODO_BRD.docx-009` — Dashboard shall show Open, In Progress, Completed and Overdue counts.
- `XATA_TODO_BRD.docx-012` — Total open TODOs.
- `XATA_TODO_BRD.docx-005` — Basic team view for assigned TODOs.

**Decision pending** — Which views and layouts are required, and does 'Total open' differ from the 'Open' status count?

**Provisional assumption** — The dashboard shows the four BR-010 counts plus the High/Critical count, scoped to the user's own TODOs, with Team Leads also seeing a team view.
**Rationale** — This combines the listed metrics with the stated role scope so the dashboard can be designed before XATA confirms layout details.

### Question 5

What defines 'simple' and 'intentionally small' for the first release, and which capabilities are explicitly out of scope?

The BRD defines the first-release boundary through explicit In Scope and Out of Scope lists, but it does not define 'simple' or 'intentionally small' with measurable criteria. Out of scope items include advanced project management, Gantt charts, time tracking, chat or collaboration features, file management, AI-generated TODOs, native mobile apps, complex workflow approvals and external customer access.

- `XATA_TODO_BRD.docx-003` — keeping the first release intentionally small and easy to use
- `XATA_TODO_BRD.docx-005` — Basic team view for assigned TODOs.
- `XATA_TODO_BRD.docx-006` — Chat or collaboration features.

**Decision pending** — Does XATA accept the In Scope list as the complete first-release capability set, and are any measurable criteria needed to define 'simple' or 'intentionally small'?

**Provisional assumption** — Treat the BRD's In Scope list as the complete first-release capability set, with everything not listed treated as out of scope.
**Rationale** — This gives the team a workable scope boundary for design and estimation until XATA confirms the scope and any measurable simplicity criteria.

### Question 6

The objective to 'reduce dependency on spreadsheets, email and chat' has no measurable target or baseline. Is it a success measure or a requirement, and if measurable, what is the target?

The objective is listed under Business Objectives, not under the numbered Business Requirements (BR-001 to BR-015), so it is an objective rather than a testable requirement. The BRD gives no baseline or measurable target for it.

- `XATA_TODO_BRD.docx-004` — Reduce dependency on spreadsheets, email and chat for TODO tracking.

**Decision pending** — What measurable target and baseline should XATA set for reducing dependency on spreadsheets, email and chat, and should it be tracked as a success measure?

**Provisional assumption** — Treat this objective as a qualitative success measure with no numeric target until XATA supplies a baseline.
**Rationale** — This keeps the objective in the success criteria without inventing a target that XATA has not agreed.

### Question 7

The supplied evidence contains no NFR content (for example performance, security, availability, accessibility, or supported platforms). Are NFR sources available that should be included?

NFR content is available: the supplied XATA_TODO_NFR.docx covers performance, availability, scalability, security, data integrity, usability, accessibility, maintainability, observability, backup and recovery, compatibility, privacy and disaster recovery. The BRD also states that XBS will propose the architecture based on the BRD and NFR, so the NFR document should be included.

- `XATA_TODO_NFR.docx-003` — NFR-PERF-001 | Normal page/API response time
- `XATA_TODO_NFR.docx-006` — Authorization shall be role-based.
- `XATA_TODO_BRD.docx-014` — XBS will propose the technical architecture based on the BRD and NFR.

### Question 8

What defines a user as 'authorized to manage' or an 'authorized user' for editing (BR-003) and assignment (BR-005)? No authorization rules or role mapping are specified.

Authorization must be role-based (NFR), and the BRD defines three roles. Employees create and manage their own TODOs, Team Leads create and assign TODOs and view team TODOs, and Administrators manage users and platform configuration. The BRD does not map these roles to specific edit or assign permissions for 'authorized to manage'.

- `XATA_TODO_BRD.docx-007` — Create/assign TODOs; view team TODOs; monitor overdue work.
- `XATA_TODO_BRD.docx-013` — Only authorized users can assign or modify TODOs.
- `XATA_TODO_NFR.docx-006` — Authorization shall be role-based.

**Decision pending** — Which roles, and under what ownership or team conditions, may edit or assign another user's TODO, and what does 'authorized to manage' mean?

**Provisional assumption** — Employees may edit only TODOs they own or are assigned, Team Leads may edit and assign TODOs for their team members, and Administrators may manage users and configuration without editing individual TODOs unless XATA says otherwise.
**Rationale** — This maps the stated role responsibilities to the edit and assign rules so design can proceed, and XATA can confirm or correct the mapping.

### Question 9

What defines a 'team' for the Team Lead team view and the basic team view for assigned TODOs? Team membership and structure are not described.

- `XATA_TODO_BRD.docx-009` — Team Leads shall view TODOs assigned to their team members.
- `XATA_TODO_BRD.docx-007` — view team TODOs; monitor overdue work
- `XATA_TODO_BRD.docx-014` — XATA will provide the user list and team structure.

**Decision pending** — Which users make up a team, and how is team membership assigned and maintained (for example, by manager reporting line, a team roster, or a user attribute)? The documents say XATA will provide the team structure but do not define it.

**Provisional assumption** — A team is the set of users who report to a given Team Lead, as listed in the team structure XATA provides.
**Rationale** — This gives the Team Lead view a concrete membership rule to build against until XATA confirms the actual team structure.

### Question 10

How is 'overdue' determined and how is monitoring of overdue work expected to be performed (e.g., views, alerts)? No overdue criteria or monitoring mechanism is specified.

Overdue is defined as a TODO whose due date has passed and whose status is not Completed. The dashboard must show an Overdue count, and Team Leads are expected to monitor overdue work.

- `XATA_TODO_BRD.docx-013` — Overdue means due date has passed and status is not Completed.
- `XATA_TODO_BRD.docx-009` — Dashboard shall show Open, In Progress, Completed and Overdue counts.
- `XATA_TODO_BRD.docx-007` — monitor overdue work

**Decision pending** — What monitoring mechanism is expected for overdue work beyond the dashboard count, such as a dedicated overdue view, filter, or alerts/notifications, and who sees it?

**Provisional assumption** — Overdue work is monitored through the dashboard Overdue count and a filter on due date and status, with no automated alerts in the first release.
**Rationale** — This uses the existing dashboard and filter requirements to give a workable monitoring approach while the alerting need is unconfirmed.

### Question 11

What is included in the 'basic user profile' and in 'basic platform configuration' administered by the Administrator? Neither scope is defined.

- `XATA_TODO_BRD.docx-005` — User login and basic user profile.
- `XATA_TODO_BRD.docx-007` — Manage users and basic platform configuration.
- `XATA_TODO_NFR.docx-014` — Collect only data required for TODO management.

**Decision pending** — What data fields make up the basic user profile, and which configurable settings are included in basic platform configuration that the Administrator manages?

**Provisional assumption** — The basic user profile contains only the identity, role, and team attributes needed for login, assignment, and authorization, and basic platform configuration covers only user and role administration.
**Rationale** — Limiting both scopes to what login, assignment and authorization need matches the privacy rule and gives the team a minimal starting point to confirm.

### Question 12

Is the list of audit information fields complete? The source says 'such as created date and updated date', which implies additional fields may be expected but none are named.

BR-012 requires the system to maintain created-by, created-date, updated-by and updated-date as Must requirements. The 4.1 wording 'such as' is illustrative and does not add fields beyond these four.

- `XATA_TODO_BRD.docx-009` — System shall maintain created-by, created-date, updated-by and updated-date.
- `XATA_TODO_BRD.docx-005` — Audit information such as created date and updated date.
- `XATA_TODO_NFR.docx-006` — Administrative actions should be auditable.

**Decision pending** — Are any further audit fields required, such as audit records for administrative actions, which the NFR says should be auditable?

**Provisional assumption** — The four BR-012 fields are the complete TODO audit set for the first release, with administrative action auditing handled as a separate log.
**Rationale** — BR-012 is the only explicit, prioritized list of audit fields, so treating it as complete gives the design a firm baseline.

### Question 13

What content and behavior is expected for the dashboard showing TODO status? No metrics, filters, or audience are specified.

The BRD specifies the dashboard metrics: counts of Open, In Progress, Completed and Overdue TODOs, plus High/Critical priority TODOs. It does not specify dashboard filters, the target audience, or display and drill-down behavior.

- `XATA_TODO_BRD.docx-009` — Dashboard shall show Open, In Progress, Completed and Overdue counts.
- `XATA_TODO_BRD.docx-012` — High/Critical priority TODOs.
- `XATA_TODO_NFR.docx-003` — Dashboard loading

**Decision pending** — What filters, audience, scope (personal, team or all TODOs), and drill-down or refresh behavior should the dashboard have, and should High/Critical priority be shown as a count or a list?

**Provisional assumption** — The dashboard shows the four status counts and the High/Critical count scoped to the signed-in user's own and assigned TODOs, visible to all authenticated users.
**Rationale** — This gives a concrete default for scope and audience that XATA can confirm or change, without inventing filters the BRD does not mention.

### Question 14

Is a due date mandatory when creating a TODO? BR-002 lists due date as a TODO attribute but does not state whether it is required or optional, and the format is not specified.

- `XATA_TODO_BRD.docx-008` — A TODO shall contain title, description, status, priority and due date.
- `XATA_TODO_BRD.docx-010` — Select due date.
- `XATA_TODO_BRD.docx-013` — A TODO must have a title.
- `XATA_TODO_BRD.docx-013` — A due date cannot be earlier than creation date unless explicitly permitted.

**Decision pending** — Is due date required when a TODO is created, and what date format should be used? BR-002 says a TODO shall contain a due date, but the business rules say only the title must be present, and the format is not specified.

**Provisional assumption** — Due date is required at creation and is entered as a calendar date (no time component), pending XATA confirmation.
**Rationale** — BR-002 is a Must requirement that includes due date, so requiring it is the closest reading of the BRD, and a date-only format is the simplest default for a due date.

### Question 15

Which status changes may Employees make? The Employee role is said to 'update status', but BR-006 and BR-004 define only Open, In Progress, Completed and marking as completed; the permitted transitions are not defined.

The Employee role may 'update status', and the BRD defines three statuses (Open, In Progress, Completed) plus a requirement that users can mark TODOs as completed. The BRD does not define which status transitions Employees may make.

- `XATA_TODO_BRD.docx-007` — Create/manage own TODOs; view assigned TODOs; update status.
- `XATA_TODO_BRD.docx-008` — System shall support Open, In Progress and Completed statuses.
- `XATA_TODO_BRD.docx-008` — Users shall be able to mark TODOs as completed.
- `XATA_TODO_BRD.docx-013` — Completed TODOs must have Completed status.

**Decision pending** — Which specific status transitions (for example, Open to In Progress, In Progress back to Open, or reopening a Completed TODO) may Employees perform, and on which TODOs?

**Provisional assumption** — Employees may change status freely among Open, In Progress and Completed, but only on TODOs they own or are assigned to.
**Rationale** — This matches the Employee responsibilities and the authorization rules, and it gives the team a workable default until the transition rules are confirmed.

### Question 16

Is the priority of BR-009 (search, 'Should') consistent with the in-scope list, which includes search without a priority? Confirm whether search is required for initial release.

Search is in the initial-release in-scope list, so it is part of the first release. BR-009 is labelled 'Should', which is lower than the 'Must' used for most requirements, so the BRD does not explicitly reconcile the two.

- `XATA_TODO_BRD.docx-005` — Filter and search TODOs.
- `XATA_TODO_BRD.docx-008` — Users shall search TODOs by title or description. | Should

**Decision pending** — Is search (BR-009) mandatory for the initial release despite its 'Should' priority, or can it be deferred?

**Provisional assumption** — Treat search by title or description as required for the initial release because it is listed in scope.
**Rationale** — The in-scope list is the more specific statement of release content, so this avoids silently dropping an in-scope feature.

### Question 17

What criteria define 'where permitted' for deleting TODOs (BR-013)? The roles, ownership rules, and conditions are not specified.

BR-013 makes deletion conditional on 'where permitted,' and the BRD sets two boundaries: deletion must not remove the user account or other TODOs, and the NFR requires role-based authorization. The specific roles or ownership conditions that make deletion permitted are not defined.

- `XATA_TODO_BRD.docx-009` — Users shall be able to delete TODOs where permitted.
- `XATA_TODO_BRD.docx-013` — Deleting a TODO must not delete the user account or other TODOs.
- `XATA_TODO_NFR.docx-006` — Authorization shall be role-based.

**Decision pending** — Which roles or ownership conditions (for example, creator only, Team Lead, or Administrator) permit deleting a TODO?

**Provisional assumption** — Only the TODO's creator and Administrators may delete a TODO.
**Rationale** — A creator-plus-Administrator rule is a common default that matches the Employee and Administrator roles, giving the reviewer a concrete option to accept or reject.

### Question 18

What criteria define 'where authorized' for reassigning and deleting TODOs (section 7.2)? Authorization rules are not specified.

BR-003 allows edits to TODOs a user owns or is authorized to manage, and the BRD states that only authorized users can assign or modify TODOs. The Team Lead role is described as able to create and assign TODOs. The criteria for 'authorized' are not defined for reassignment or deletion.

- `XATA_TODO_BRD.docx-011` — Reassign where authorized.
- `XATA_TODO_BRD.docx-013` — Only authorized users can assign or modify TODOs.
- `XATA_TODO_BRD.docx-008` — Users shall be able to edit TODOs they own or are authorized to manage.
- `XATA_TODO_BRD.docx-007` — Create/assign TODOs; view team TODOs; monitor overdue work.

**Decision pending** — What criteria define 'authorized' for reassigning and deleting TODOs, including whether a TODO's owner, assignee or Team Lead may reassign or delete it?

**Provisional assumption** — The TODO owner and the user's Team Lead may reassign TODOs, and only the owner may delete them.
**Rationale** — Splitting reassignment and deletion rights this way follows the existing Employee and Team Lead role descriptions and gives the reviewer a specific rule to confirm.

### Question 19

Which browsers are 'supported' for the web interface (BR-015)? No browser list or versions are given.

The NFR requires support for current versions of major enterprise browsers, naming Chrome and Edge as examples. It does not provide a closed list of supported browsers or specific version numbers.

- `XATA_TODO_NFR.docx-013` — Support current versions of major enterprise browsers such as Chrome and Edge.
- `XATA_TODO_BRD.docx-009` — System shall provide a web interface through supported browsers.

**Decision pending** — Is the supported browser list limited to current Chrome and Edge, or does it include other browsers, and which versions are required?

**Provisional assumption** — For the first release, supported browsers are the current stable versions of Chrome and Edge.
**Rationale** — Limiting support to the two named browsers gives the delivery team a testable baseline until XATA confirms the complete list.

### Question 20

What are the allowed priority values (for example, whether Critical and High are distinct from other levels), and how is 'Overdue' determined from the due date?

The allowed priority values are Low, Medium, High and Critical, so High and Critical are distinct levels. 'Overdue' means the due date has passed and the status is not Completed.

- `XATA_TODO_BRD.docx-008` — System shall support Low, Medium, High and Critical priorities.
- `XATA_TODO_BRD.docx-013` — Overdue means due date has passed and status is not Completed.

### Question 21

Who is authorized to permit a due date earlier than the creation date, and under what conditions is that exception granted?

- `XATA_TODO_BRD.docx-013` — A due date cannot be earlier than creation date unless explicitly permitted.

**Decision pending** — Which role or person may approve a due date earlier than the creation date, and what conditions must be met? The BRD only states the exception exists.

**Provisional assumption** — Only an Administrator or the Team Lead of the TODO's assignee may approve an earlier due date, and the approval is recorded in the audit fields.
**Rationale** — This gives the reviewer a concrete candidate approver and audit trail to confirm, using roles and audit requirements already in the BRD and NFR.

### Question 22

What roles and permissions define 'authorized users' for assigning and modifying TODOs?

The BRD defines three roles: Employee, Team Lead and Administrator. Only Team Leads are described as able to create and assign TODOs, and the BRD says only authorized users can assign or modify TODOs. The exact authorization boundary for each role is not defined.

- `XATA_TODO_BRD.docx-007` — Create/assign TODOs; view team TODOs; monitor overdue work.
- `XATA_TODO_BRD.docx-013` — Only authorized users can assign or modify TODOs.

**Decision pending** — What exact rules determine whether a user is authorized to assign or modify a given TODO, including whether an Employee can assign TODOs and whether a Team Lead can modify TODOs outside their team?

**Provisional assumption** — An Employee may modify only TODOs they own or are assigned to, a Team Lead may assign and modify TODOs for their team members, and an Administrator may manage all TODOs.
**Rationale** — This maps the stated role responsibilities to the ownership and team-scope requirements, giving the reviewer a concrete draft matrix to confirm.

### Question 23

Which NFRs are the 'agreed NFRs' referenced in the acceptance criteria, and where are they documented? No NFR content is included in the supplied evidence.

The NFR document supplied is XATA_TODO_NFR.docx (Version 1.0), which lists the non-functional requirements by category. The NFR acceptance section refers to 'agreed NFRs' but does not state that this document is the agreed baseline.

- `XATA_TODO_NFR.docx-001` — Version 1.0
- `XATA_TODO_NFR.docx-016` — XBS shall demonstrate compliance with agreed NFRs

**Decision pending** — Is XATA_TODO_NFR.docx Version 1.0 the agreed NFR baseline, and has any target been changed or agreed separately?

**Provisional assumption** — XATA_TODO_NFR.docx Version 1.0 is treated as the agreed NFR baseline until XATA confirms otherwise.
**Rationale** — The NFR document is the only NFR source supplied and its version label gives a clear reference point for the reviewer to confirm.

### Question 24

Beyond 'Completed', which TODO status values exist, and what transitions between them are permitted?

The BRD requires three statuses: Open, In Progress and Completed. Overdue is a derived condition (due date passed and status not Completed), not a separate status value.

- `XATA_TODO_BRD.docx-008` — System shall support Open, In Progress and Completed statuses.
- `XATA_TODO_BRD.docx-013` — Completed TODOs must have Completed status.

**Decision pending** — Which status transitions are permitted, for example whether a Completed TODO can be reopened to Open or In Progress, and who may trigger each transition?

**Provisional assumption** — Status moves forward from Open to In Progress to Completed, and a Completed TODO may be reopened to In Progress by its owner or Team Lead.
**Rationale** — This gives a simple default lifecycle that matches the three statuses and the completion rule, which the reviewer can accept or change.

### Question 25

NFR-PERF-001 refers to 'normal load' without defining it. What user volume, request rate, or operating conditions constitute normal load for the response-time target?

- `XATA_TODO_NFR.docx-003` — under normal load

**Decision pending** — What user volume, request rate, or operating conditions does XATA define as 'normal load' for the NFR-PERF-001 response-time target?

**Provisional assumption** — Treat normal load as up to 500 concurrent active users, the NFR-PERF-005 figure, in the single enterprise environment.
**Rationale** — It gives the team a testable load baseline drawn from the NFR itself until XATA confirms the definition.

### Question 26

NFR-PERF-005 requires 'at least 500' concurrent active users but does not define 'active' or the measurement window. Must the 500 users be supported at peak, sustained, or at a specific response-time target, and what counts as an active user?

- `XATA_TODO_NFR.docx-003` — At least 500

**Decision pending** — What counts as an 'active' user, over what measurement window, and must the 500 users be supported at peak, sustained load, or at a specific response-time target?

**Provisional assumption** — Treat an active user as an authenticated user who makes at least one request within a 5-minute window, with the 500 users supported at sustained load while meeting the NFR-PERF-001 to NFR-PERF-004 targets.
**Rationale** — A defined session-based activity rule and a sustained-load condition make the concurrency target measurable for test design.

### Question 27

The NFR-PERF-001 to NFR-PERF-004 targets state '95% of requests' without specifying the measurement period or the load conditions under which the percentile is measured. Over what period and under what load should compliance be measured?

- `XATA_TODO_NFR.docx-003` — 95% of requests

**Decision pending** — Over what measurement period and under what load conditions should the '95% of requests' percentile targets in NFR-PERF-001 to NFR-PERF-004 be measured?

**Provisional assumption** — Measure the 95th percentile over a calendar month under the normal-load definition resolved for NFR-PERF-001.
**Rationale** — A monthly window aligns with the monthly availability measure in NFR-AVL-001 and gives a single consistent compliance period.

### Question 28

Which maintenance windows are 'agreed', who agrees them, and how are they documented? NFR-AVL-001 excludes them from the availability measure without defining them.

- `XATA_TODO_NFR.docx-004` — excluding agreed maintenance windows
- `XATA_TODO_NFR.docx-004` — Communicated ≥24 hours in advance

**Decision pending** — Which maintenance windows are agreed, who agrees them, and how are they documented so they can be excluded from the NFR-AVL-001 availability measure?

**Provisional assumption** — Treat agreed maintenance windows as those approved in writing by XATA IT and recorded in the operations runbook.
**Rationale** — XATA IT is named as the technical and operational stakeholder, so it is a reasonable approver and the runbook gives an auditable record.

### Question 29

How is monthly availability measured (calendar month definition, measurement point, and how partial outages are counted)?

Monthly availability is targeted at ≥ 99.5%, with agreed maintenance windows excluded. The source does not define the calendar month, the measurement point, or how partial outages are counted.

- `XATA_TODO_NFR.docx-004` — ≥ 99.5%, excluding agreed maintenance windows

**Decision pending** — What is the calendar month definition (including time zone), where is availability measured, and how are partial outages counted (for example, by minutes or as full-period downtime)?

**Provisional assumption** — Availability is measured per calendar month in XATA local time at the user-facing entry point, and partial outages are counted pro rata by minutes of unavailability.
**Rationale** — A concrete default lets XBS design monitoring and SLA reporting now, and XATA can confirm or change it during NFR acceptance.

### Question 30

How is 'restored' defined for the 30-minute recovery target in NFR-AVL-003, and is the target measured from failure detection or from failure onset?

- `XATA_TODO_NFR.docx-004` — Service restored within 30 minutes
- `XATA_TODO_NFR.docx-012` — Target RTO: 30 minutes.

**Decision pending** — How is 'restored' defined (for example, the health check passes, or core user flows work), and does the 30-minute clock start at failure detection or at failure onset?

**Provisional assumption** — 'Restored' means the health check passes and core create, view and complete flows succeed, and the 30-minute clock starts at failure detection by monitoring.
**Rationale** — Failure detection is measurable through monitoring alerts, whereas failure onset is usually unknown, so this default makes the target testable.

### Question 31

What growth targets (users, TODO volume, time horizon) apply beyond the initial 100,000 TODO records, and what counts as 'major redesign'?

- `XATA_TODO_NFR.docx-005` — Support at least 100,000 TODO records initially.
- `XATA_TODO_NFR.docx-005` — Database design shall support future growth beyond initial capacity.
- `XATA_TODO_NFR.docx-005` — Support growth in users and TODO volume without major redesign.

**Decision pending** — What user count, TODO volume and time horizon beyond the initial 100,000 TODO records should be planned for, and what specific change would count as a 'major redesign'?

### Question 32

Under what conditions is horizontal scalability considered 'practical', and is it required or only preferred?

Horizontal scalability is a preferred ('should') requirement, not a mandatory one, and applies to application services only.

- `XATA_TODO_NFR.docx-005` — Application services should be horizontally scalable where practical.

**Decision pending** — Which specific conditions make horizontal scaling 'practical' (for example, load thresholds, cost limits, or hosting constraints), and what should XBS do if those conditions are not met?

**Provisional assumption** — Horizontal scaling is a design preference that XBS must address in the architecture proposal, with any deviation justified in writing.
**Rationale** — This keeps the preferred status while giving XBS a clear obligation to document its decision without requiring an undefined 'practical' threshold.

### Question 33

Which user roles exist and which TODO data each role may access? The role model is not defined in the supplied evidence.

The BRD defines three roles: Employee, Team Lead and Administrator, each with key responsibilities. The NFR requires role-based authorization and says users may access only the TODO data their role permits. No per-role data-access matrix is supplied.

- `XATA_TODO_BRD.docx-007` — Create/manage own TODOs; view assigned TODOs; update status.
- `XATA_TODO_BRD.docx-007` — Create/assign TODOs; view team TODOs; monitor overdue work.
- `XATA_TODO_NFR.docx-006` — Users shall only access TODO data permitted by their role.

**Decision pending** — What exact TODO data may each role (Employee, Team Lead, Administrator) view, edit, assign or delete, including whether Employees can see TODOs assigned to others and what Administrators may see of TODO content?

**Provisional assumption** — Use the BRD responsibilities list as the working access baseline for Employee, Team Lead and Administrator until XATA agrees a full access matrix.
**Rationale** — It gives the design team a documented starting point for authorization without inventing permissions the evidence does not state.

### Question 34

Which passwords are 'locally managed' versus externally managed, and what hashing standard is intended?

Where passwords are locally managed, the NFR requires secure industry-standard hashing. The evidence does not name a specific algorithm or identify which passwords are locally managed versus externally managed.

- `XATA_TODO_NFR.docx-006` — Passwords, if locally managed, shall use secure industry-standard hashing.

**Decision pending** — Which user accounts or credentials are locally managed and which are handled by an external identity provider, and which specific hashing algorithm and parameters XATA requires?

**Provisional assumption** — Assume no passwords are locally managed until XATA confirms its authentication source, so local hashing requirements apply only if that changes.
**Rationale** — It avoids designing a local password store that XATA may not need, while keeping the hashing requirement in place if local passwords are later confirmed.

### Question 35

Which administrative actions must be auditable, and what audit records and retention are required? The 'should' obligation strength is not clarified.

The NFR states that administrative actions should be auditable. The BRD requires record-level created-by, created-date, updated-by and updated-date fields for TODOs. The evidence does not list which administrative actions must be audited or specify audit record content or retention.

- `XATA_TODO_NFR.docx-006` — Administrative actions should be auditable.
- `XATA_TODO_BRD.docx-009` — System shall maintain created-by, created-date, updated-by and updated-date.

**Decision pending** — Which specific administrative actions must be audited, what fields each audit record must hold, how long audit records must be retained, and whether the 'should' obligation is to be treated as mandatory.

### Question 36

What is XATA's retention policy referenced for deleted data, and where is it documented? The policy content is not supplied.

- `XATA_TODO_NFR.docx-007` — Deleted data handling shall follow XATA's retention policy.

**Decision pending** — XATA must supply or identify its retention policy for deleted TODO and user data, including retention periods, deletion method and the document that holds the policy.

### Question 37

Which fields are 'required' for TODO records, and how should conflicting updates be detected and resolved?

The BRD lists the TODO content fields (title, description, status, priority, due date), and the business rules make title mandatory. The NFR requires server-side validation of required fields and says updates must not silently overwrite conflicting data, but it does not define a conflict detection or resolution method.

- `XATA_TODO_BRD.docx-008` — A TODO shall contain title, description, status, priority and due date.
- `XATA_TODO_BRD.docx-013` — A TODO must have a title.
- `XATA_TODO_NFR.docx-007` — Required fields shall be validated server-side.
- `XATA_TODO_NFR.docx-007` — Updates shall not silently overwrite conflicting data.

**Decision pending** — Which fields other than title are mandatory for save, and how should conflicting updates be detected and resolved (for example, version checks, timestamp checks, or user merge prompts)?

**Provisional assumption** — Title is the only mandatory field, and concurrent edits are detected with an updated-date or version check that rejects a stale save and asks the user to reload.
**Rationale** — This gives the team a workable baseline for validation and conflict handling while the BRD and NFR leave both points open.

### Question 38

What scope and success criteria apply to 'where practical' for targeting WCAG 2.1 AA principles, and which specific WCAG success criteria are required?

- `XATA_TODO_NFR.docx-009` — Target WCAG 2.1 AA principles where practical.

**Decision pending** — What parts of the application are in scope for WCAG 2.1 AA, what does 'where practical' mean in measurable terms, and which specific WCAG 2.1 success criteria must be met and verified?

### Question 39

What is the measurable meaning of 'minimal steps' for the core create/update/complete flow, and what are the defined 'standard desktop and tablet screens' (sizes, resolutions, or devices)? Are mobile phone screens in scope?

The NFR requires the UI to be responsive for standard desktop and tablet screens, and the BRD places mobile native applications out of scope. The NFR does not define 'minimal steps' in measurable terms or specify screen sizes, resolutions, or devices.

- `XATA_TODO_NFR.docx-008` — UI shall be responsive for standard desktop and tablet screens.
- `XATA_TODO_NFR.docx-008` — Core create/update/complete flow should require minimal steps.
- `XATA_TODO_BRD.docx-006` — Mobile native applications.

**Decision pending** — What is the measurable step-count target for create, update and complete, which standard desktop and tablet screen sizes or devices must be supported, and are mobile phone browser layouts in scope?

**Provisional assumption** — Mobile phone browser layouts are out of scope for the first release, and desktop and tablet are tested at common widths of 768 px and 1280 px or wider.
**Rationale** — This gives the testers concrete viewports and a clear boundary while XATA confirms the screen definitions.

### Question 40

Which business logic is considered 'critical' for the automated unit test coverage requirement, and is there a minimum coverage target?

- `XATA_TODO_NFR.docx-010` — Automated unit tests shall cover critical business logic.

**Decision pending** — Which business logic is classified as critical for unit testing, and what minimum unit test coverage percentage, if any, is required?

**Provisional assumption** — The business rules in BRD section 8 and the create, edit, status, priority, overdue and authorization logic are treated as critical until XATA confirms the list and a numeric coverage target.
**Rationale** — This gives developers a concrete starting scope for unit tests without inventing a coverage percentage the documents do not state.

### Question 41

In which cases are correlation/request identifiers considered 'appropriate' for logs, and what is the expected handling of sensitive information in logs?

Sensitive information must not be written to application logs, and logging should support troubleshooting without exposing it. Correlation/request identifiers should be included in logs where appropriate, but the documents do not define when that applies.

- `XATA_TODO_NFR.docx-011` — Logs should include correlation/request identifiers where appropriate.
- `XATA_TODO_NFR.docx-014` — Sensitive information shall not be written to application logs.
- `XATA_TODO_NFR.docx-010` — Logging shall support troubleshooting without exposing sensitive information.

**Decision pending** — In which specific log events or cases are correlation/request identifiers required, and what counts as sensitive information for logging purposes?

**Provisional assumption** — Include a correlation/request identifier in all application error logs and in request-scoped logs, and treat credentials, passwords, tokens and personal data as sensitive.
**Rationale** — This gives the reviewer a concrete default for the undefined 'where appropriate' condition and the sensitive-data scope, which can be confirmed with XATA.

### Question 42

What is the agreed backup schedule for production data, and who agrees it?

- `XATA_TODO_NFR.docx-012` — Production data shall be backed up according to an agreed schedule.
- `XATA_TODO_BRD.docx-017` — Detailed technical design and implementation decisions are to be proposed by XBS and agreed with XATA.

**Decision pending** — What is the production data backup schedule (frequency and retention), and which party (XATA or XBS) must agree to it?

**Provisional assumption** — XBS proposes the production backup schedule and XATA approves it before production acceptance.
**Rationale** — The BRD states that technical design decisions are proposed by XBS and agreed with XATA, so this follows the stated operating model.

### Question 43

How will XATA agree to a different RPO than 15 minutes, and what process or approval applies?

- `XATA_TODO_NFR.docx-012` — Target RPO: 15 minutes unless XATA agrees otherwise.

**Decision pending** — What process, approver and documentation are required for XATA to agree to an RPO other than 15 minutes?

**Provisional assumption** — A non-default RPO is approved by XATA's designated business owner in writing and recorded in the NFR acceptance evidence.
**Rationale** — The NFR allows an alternative RPO only if XATA agrees but names no approver or method, so a written sign-off gives a traceable default.

### Question 44

Is the 15-minute RPO and 30-minute RTO a hard requirement or a target, and what scope (which data, components, or service) do they apply to?

The 15-minute RPO and 30-minute RTO are stated as targets, not hard requirements, and the RPO can be changed if XATA agrees. The documents do not state which data, components or service they apply to.

- `XATA_TODO_NFR.docx-012` — Target RPO: 15 minutes unless XATA agrees otherwise.
- `XATA_TODO_NFR.docx-012` — Target RTO: 30 minutes.

**Decision pending** — Which data, components or service do the 15-minute RPO and 30-minute RTO apply to, and are they binding for production acceptance?

**Provisional assumption** — The RPO and RTO apply to the production TODO application database and its backups, and are treated as acceptance targets verified during NFR acceptance.
**Rationale** — This narrows the undefined scope to the core production data store, which holds the TODO records that the backup requirement names.

### Question 45

What constitutes a 'major failure' for the restoration requirement, and what restoration time or success criteria apply?

The NFR sets a restoration target but does not define 'major failure'. The stated targets are RTO of 30 minutes and RPO of 15 minutes, and application-failure recovery is to restore service within 30 minutes.

- `XATA_TODO_NFR.docx-012` — Solution shall support restoration after major failure.
- `XATA_TODO_NFR.docx-012` — Target RTO: 30 minutes.
- `XATA_TODO_NFR.docx-004` — Service restored within 30 minutes

**Decision pending** — What events qualify as a 'major failure', and what success criteria (for example, data-loss tolerance or verification steps) define a successful restoration?

**Provisional assumption** — Treat any failure that requires restoring production data or services from backup as a major failure subject to the 30-minute RTO and 15-minute RPO.
**Rationale** — This gives the bidder a measurable baseline for restoration design and testing until XATA defines the term.

### Question 46

Which browsers and versions make up 'major enterprise browsers' beyond Chrome and Edge, and who approves browser-specific functionality?

Chrome and Edge are cited as examples of major enterprise browsers, and the list is not exhaustive. Browser-specific functionality requires approval, but the approver is not named.

- `XATA_TODO_NFR.docx-013` — Support current versions of major enterprise browsers such as Chrome and Edge.
- `XATA_TODO_NFR.docx-013` — Avoid browser-specific functionality unless approved.
- `XATA_TODO_BRD.docx-009` — System shall provide a web interface through supported browsers.

**Decision pending** — Which other browsers and versions must be supported, and who is authorized to approve browser-specific functionality?

**Provisional assumption** — Treat current versions of Chrome and Edge as the minimum supported browsers until XATA names any additional browsers.
**Rationale** — This gives the design a concrete baseline for browser testing while XATA confirms the full browser list and approver.

### Question 47

What is the required frequency for periodic recovery procedure testing?

- `XATA_TODO_NFR.docx-015` — Recovery procedures shall be tested periodically.

**Decision pending** — What frequency (for example, annually or per release) must XBS use for periodic testing of the recovery procedures, and who approves that schedule?

**Provisional assumption** — Require a full recovery test before production acceptance and then at least annually.
**Rationale** — The NFR requires periodic testing and production acceptance evidence, so a pre-go-live test plus an annual cadence gives a defensible default until XATA sets the frequency.

### Question 48

What are the XATA authorization rules and XATA data retention and deletion policies referenced by the privacy requirements, and are they provided to the bidder?

- `XATA_TODO_NFR.docx-014` — Access to personal/team information shall follow XATA authorization rules.
- `XATA_TODO_NFR.docx-014` — Data retention and deletion shall follow XATA policy.
- `XATA_TODO_BRD.docx-013` — Only authorized users can assign or modify TODOs.

**Decision pending** — Will XATA provide its authorization rules and its data retention and deletion policy to the bidder, and if so, when and in what form?

**Provisional assumption** — Use the BRD role descriptions and business rules as the interim authorization baseline until XATA supplies its formal authorization rules.
**Rationale** — The BRD defines roles and authorization-related rules, which gives design work a provisional basis while the formal XATA documents are outstanding.

### Question 49

What does 'XBS' refer to, and what is its role relative to the solution?

XBS is XATA's delivery partner and implementation partner. It is responsible for designing and implementing the TODO Management Platform, proposing the technical architecture based on the BRD and NFR, and documenting the dependencies needed to restore the service.

- `XATA_TODO_BRD.docx-001` — Delivery Partner: XBS
- `XATA_TODO_BRD.docx-016` — XBS | Implementation Partner
- `XATA_TODO_BRD.docx-014` — XBS will propose the technical architecture based on the BRD and NFR.
- `XATA_TODO_NFR.docx-015` — XBS shall document dependencies required to restore the service.

### Question 50

The priority table assigns Must or Should to NFR categories but does not state the underlying NFR statements, thresholds, units, or measurement criteria for each category. Which specific requirements sit under each category?

The priority table does not restate the requirements, but the NFR document contains them in sections that match the category names: Security (section 5), Performance (section 2, NFR-PERF-001 to 005), Availability (section 3, NFR-AVL-001 to 003), Data & Integrity (section 6), Backup & Recovery (section 11), Usability (section 7), Maintainability (section 9), Accessibility (section 8), and Observability & Operations (section 10, mapped to 'Advanced observability'). Thresholds and units exist for Performance, Availability and Backup & Recovery, for example RPO and RTO targets, but Security, Usability and Maintainability have qualitative statements with no measurement criteria.

- `XATA_TODO_NFR.docx-017` — Security | Must
- `XATA_TODO_NFR.docx-017` — Accessibility | Should
- `XATA_TODO_NFR.docx-003` — NFR-PERF-001 | Normal page/API response time | ≤ 2 seconds for 95% of requests under normal load
- `XATA_TODO_NFR.docx-004` — NFR-AVL-001 | Monthly availability | ≥ 99.5%, excluding agreed maintenance windows
- `XATA_TODO_NFR.docx-012` — Target RPO: 15 minutes unless XATA agrees otherwise.

**Decision pending** — Which priority applies to Scalability, Compatibility, Privacy, Disaster Recovery and NFR Acceptance, which have no row in the priority table? Also, what measurable criteria will be used to verify the qualitative Security, Usability, Maintainability and Accessibility requirements?

**Provisional assumption** — Treat Scalability, Compatibility, Privacy and Disaster Recovery as Must until XATA confirms otherwise.
**Rationale** — Section 15 requires XBS to demonstrate compliance with all agreed NFRs before production acceptance, so unlisted categories need a provisional priority to be testable.

### Question 51

The source does not define the obligation strength of 'Must' versus 'Should'. Is a 'Should' category excluded from the production acceptance demonstration required by the NFR acceptance section?

- `XATA_TODO_NFR.docx-016` — XBS shall demonstrate compliance with agreed NFRs
- `XATA_TODO_NFR.docx-017` — Accessibility | Should

**Decision pending** — Are the Should-priority NFR categories (Accessibility and Advanced observability) included in or excluded from the production acceptance demonstration, and what do Must and Should mean for acceptance?

**Provisional assumption** — Treat the Should-priority categories as included in the production acceptance evidence unless XATA explicitly agrees to exclude them.
**Rationale** — Section 15 names no priority-based exclusion, so including them is the conservative reading until XATA confirms otherwise.

### Question 52

The NFR acceptance section refers to 'agreed NFRs' but the supplied evidence does not identify what was agreed or where the agreed NFR baseline is recorded.

- `XATA_TODO_NFR.docx-016` — XBS shall demonstrate compliance with agreed NFRs
- `XATA_TODO_NFR.docx-002` — This document defines the non-functional requirements that XATA expects XBS to consider

**Decision pending** — What NFRs were formally agreed between XATA and XBS, and where is the agreed NFR baseline recorded?

**Provisional assumption** — Treat the NFR document (Version 1.0) as the working NFR baseline until a signed-off agreement or record is provided.
**Rationale** — The document is versioned and contains concrete targets, so it gives the acceptance section a usable reference point pending confirmation.
