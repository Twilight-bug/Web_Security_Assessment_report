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


---

# Project 2: REST API Penetration Testing (OWASP Juice Shop)

**Target System:** Modern Node.js / Angular E-Commerce Application  
**Vulnerability Type:** Insecure Direct Object Reference (IDOR / BOLA)  
**Severity:** 🔴 High (CVSS 8.5)  

### 🔍 Vulnerability Overview
Modern web applications rely heavily on backend REST APIs to fetch database records dynamically. During an API security audit of the target platform, it was discovered that the `/rest/basket/` endpoint fails to perform structural object-level authorization checks. 

### 🛠️ Proof of Concept (PoC)
1. Monitored active application requests within Burp Suite HTTP History and isolated the user cart parameter fetching string: `GET /rest/basket/6`.
2. Transferred the raw HTTP header structures into **Burp Suite Repeater**.
3. Manually manipulated the direct numerical identifier resource index from user group `6` down to user group `5`.
4. The server incorrectly validated the request and returned an `HTTP/1.1 200 OK` payload exposing the alternate user's private shopping data, confirming complete parameter tampering data leakage.

### 💡 Remediation Strategy
Implement a strict server-side **Access Control Layer** that maps incoming active session tokens (like JWTs) explicitly to the numerical database resource being requested. Never rely solely on user-supplied numbers to deliver secure database paths.
