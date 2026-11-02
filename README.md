# Web Application Security Assessment Case Study

## 🎯 Project Overview
This repository contains a professional-grade security assessment report simulating a grey-box penetration test against a corporate web application infrastructure. The goal of this assessment was to identify, verify, and document critical security flaws following the **OWASP Top 10** framework.

---

## 🛠️ Toolkit Used
* **OS:** Kali Linux
* **Proxy & Interception:** Burp Suite Professional
* **Database Automation:** SQLmap
* **Custom Automation Scripting:** Python 3 (Requests library)

---

## 🔍 Key Findings Summary

### 1. SQL Injection (SQLi) — CVSS 9.8 (Critical)
* **Impact:** Bypassing authentication, reading sensitive database contents, and complete schema mapping.
* **Verification:** Automated exploitation using `sqlmap` confirmed a vulnerable backend database parameters layer.
* **Remediation:** Implementation of Parameterized Queries (Prepared Statements).

### 2. Stored Cross-Site Scripting (XSS) — CVSS 8.2 (High)
* **Impact:** Persistent execution of malicious JavaScript commands impacting arbitrary application users, exposing session hijacking vulnerabilities.
* **Verification:** Manual payload injection within client comments storage fields confirming browser alert reflection.
* **Remediation:** Strict input categorization and contextual HTML Output Encoding.

---

## 📄 Deliverables
The complete, detailed technical report containing full step-by-step Proof of Concepts (PoCs), target impact assessments, and source-code level mitigation guides can be found in the root directory above as `Web_Security_Assessment_Report.pdf`.
