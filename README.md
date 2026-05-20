# Python SQL Monitoring Platform

A Python-based SQL Server monitoring framework designed to collect operational metrics from multiple SQL Server instances and store them in a centralized repository for historical analysis and reporting.

This project was built as part of a DBA automation and Python learning initiative focused on improving operational visibility, reducing manual monitoring efforts, and creating reusable monitoring components for SQL Server environments.

---

# Current Features

## Inventory-Driven Execution
- Supports multiple SQL Server instances through CSV-based inventory management.

## Authentication Support
- Windows Authentication
- SQL Server Authentication

## Monitoring Collectors
Currently implemented collectors:

1. Long Running Queries
2. Fragmentation Details

## Historical Repository Storage
Collected metrics are stored in centralized SQL Server tables for historical tracking and future reporting.

## Centralized Logging
- Execution logging
- Collector logging
- Error logging
- Authentication visibility

## Modular Architecture
The framework is designed using reusable modules for:
- Connections
- Collectors
- Repository operations
- Logging

---

# Project Architecture

```text
Inventory
    ↓
Connection Module
    ↓
Collectors
    ↓
DataFrames
    ↓
Repository Layer
    ↓
Historical SQL Tables
```

---

# Project Structure

```text
project/
│
├── main.py
│
├── inventory/
│
├── collectors/
│     ├── fragmentation.py
│     └── long_running_queries.py
│
├── queries/
│     ├── fragmentation.sql
│     └── long_running_queries.sql
│
├── common/
│     ├── db_connection.py
│     ├── logger.py
│     └── repository.py
│
├── logs/
│
├── README.md
│
└── table_creation_scripts.sql
```

---

# Technologies Used

- Python
- pandas
- pyodbc
- SQL Server
- Git
- GitHub

---

# Repository Tables

Current historical tables:

1. FragmentationHistory
2. LongRunningQueriesHistory

---

# How To Run

## 1. Install Python Libraries

```bash
pip install pandas pyodbc
```

---

## 2. Configure Inventory

Create:

```text
inventory/instances.csv
```

Example:

```csv
InstanceName,AuthenticationType,Username,Password
SERVER1,WINDOWS,,
SERVER2,SQL,sa,password
```

---

## 3. Execute Framework

```bash
python main.py
```

---

# Logging

Execution logs are generated inside:

```text
logs/monitoring.log
```

---

# Future Enhancements

Planned improvements:

- Backup monitoring
- Always On Availability Group monitoring
- Database growth tracking
- Blocking and deadlock monitoring
- Parallel collector execution
- Scheduling and automation
- Dashboard/reporting layer
- Email alerting
- Config-driven execution

---

# Learning Objectives

This project focuses on:
- SQL Server automation
- Python modular programming
- Monitoring framework design
- Historical metric collection
- Operational logging
- Repository architecture
- Git and GitHub workflow

---

# Author

Jameel Ahmed Qureshi

SQL Server DBA | Automation Learner | Python for DBAs
