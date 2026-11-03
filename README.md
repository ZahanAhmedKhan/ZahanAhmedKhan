<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:7dd3fc&height=230&section=header&text=Zahan%20Khan&fontSize=60&fontColor=ffffff&fontAlignY=36&desc=Data%20Engineering%20Student&descSize=24&descAlignY=58&animation=twinkling" width="100%" alt="header" />

<a href="https://github.com/ZahanAhmedKhan">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=22&pause=1200&color=7dd3fc&center=true&vCenter=true&width=700&lines=Data+Engineering+student+at+Sheridan+College;Building+streaming+and+batch+data+pipelines;Kafka+%E2%80%A2+Spark+%E2%80%A2+dbt+%E2%80%A2+Airflow+%E2%80%A2+Snowflake+%E2%80%A2+AWS;Looking+for+a+co-op+for+summer+2027" alt="Typing SVG" />
</a>

<br/><br/>

<img src="https://img.shields.io/badge/OPEN_TO_WORK-7dd3fc?style=for-the-badge&logo=github&logoColor=0f172a" alt="Open to work" />

<br/>

<img src="https://komarev.com/ghpvc/?username=ZahanAhmedKhan&color=7dd3fc&style=flat-square&label=Profile+Views" alt="Profile views" />
<img src="https://img.shields.io/github/followers/ZahanAhmedKhan?color=7dd3fc&labelColor=0f172a&style=flat-square&logo=github" alt="Followers" />

</div>

---

## 👤 Who I Am

```typescript
const zahan = {
  title: "Data Engineering Student @ Sheridan College",
  focus: ["Streaming pipelines", "Lakehouses", "Data modeling", "Data quality"],
  stack: ["Python", "SQL", "Kafka", "Spark", "dbt", "Airflow", "Dagster"],
  cloud: ["AWS", "Snowflake", "Terraform", "Docker"],
  status: "Third-year student building end-to-end data engineering projects",
  openTo: ["Co-op (Summer 2027)", "Data engineering roles"],
};
```

---

## 🚀 Featured Projects

### 📡 Bluesky Live Trend Radar
A real-time streaming pipeline that reads every public Bluesky post as it's published, streams it through Kafka and Spark Structured Streaming, and detects trending hashtags and sudden spikes within about a minute, shown on a live Grafana dashboard.

| Layer | Technology |
|-------|------------|
| Ingestion | Python (async WebSocket) → Apache Kafka |
| Processing | Spark Structured Streaming (event-time windows, watermarks) |
| Storage | PostgreSQL (idempotent upserts) |
| Dashboard | Grafana |
| Infra / CI | Docker Compose, GitHub Actions |

🔗 [Code](https://github.com/ZahanAhmedKhan/bluesky-trend-radar)

### 🎮 Steam Game Market Lakehouse
A serverless AWS lakehouse that collects player counts, prices and discounts for thousands of Steam games every hour, then answers questions like *do sales actually bring players back?* and *how fast do new games lose their players?*

| Layer | Technology |
|-------|------------|
| Ingestion | AWS Lambda + EventBridge Scheduler → S3 |
| Lakehouse | Apache Iceberg, Glue Data Catalog, Athena |
| Transformation | dbt (bronze → silver → gold, SCD Type 2) |
| Orchestration | Apache Airflow |
| Infrastructure | Terraform |
| Dashboard | Streamlit |

🔗 [Code](https://github.com/ZahanAhmedKhan/steam-market-lakehouse)

### ⚽ Soccer Scouting Warehouse
A cloud data warehouse that turns millions of StatsBomb match events into a scouting tool: per-90 stats, percentiles by position, similar-player search and an underrated-players list.

| Layer | Technology |
|-------|------------|
| Orchestration | Dagster (partitioned assets) |
| Warehouse | Snowflake (DuckDB for local runs and CI) |
| Modeling | dbt (star schema, data tests, docs) |
| App | Streamlit |

🔗 [Code](https://github.com/ZahanAhmedKhan/soccer-scouting-warehouse)

---

## 🧩 Other Projects

| Project | What it is | Tech |
|---------|------------|------|
| 🚆 [GTA Transit Reliability Tracker](https://github.com/ZahanAhmedKhan/transit-tracker) | Loads the GO Transit schedule into PostgreSQL and analyzes it with SQL and a dashboard | Python, PostgreSQL, Docker, Streamlit |
| 🍛 [MacroLens](https://github.com/ZahanAhmedKhan/macrolens) | AI nutrition tracker: photograph food for calories and macros, with support for South Asian dishes | Python, Flask, Supabase, Groq |
| 🤖 [J.A.R.V.I.S.](https://github.com/ZahanAhmedKhan/jarvis) | Voice assistant with wake-word detection, system controls and Spotify integration | Python, OpenWakeWord, Spotify API |

---

## 🛠️ Technical Skills

<div align="center">

<img src="https://img.shields.io/badge/Python-0f172a?style=for-the-badge&logo=python&logoColor=7dd3fc" alt="Python" />
<img src="https://img.shields.io/badge/SQL-0f172a?style=for-the-badge&logo=postgresql&logoColor=7dd3fc" alt="SQL" />
<img src="https://img.shields.io/badge/Apache_Kafka-0f172a?style=for-the-badge&logo=apachekafka&logoColor=7dd3fc" alt="Kafka" />
<img src="https://img.shields.io/badge/Apache_Spark-0f172a?style=for-the-badge&logo=apachespark&logoColor=7dd3fc" alt="Spark" />
<img src="https://img.shields.io/badge/dbt-0f172a?style=for-the-badge&logo=dbt&logoColor=7dd3fc" alt="dbt" />
<img src="https://img.shields.io/badge/Airflow-0f172a?style=for-the-badge&logo=apacheairflow&logoColor=7dd3fc" alt="Airflow" />
<img src="https://img.shields.io/badge/Snowflake-0f172a?style=for-the-badge&logo=snowflake&logoColor=7dd3fc" alt="Snowflake" />
<img src="https://img.shields.io/badge/AWS-0f172a?style=for-the-badge&logo=amazonwebservices&logoColor=7dd3fc" alt="AWS" />
<img src="https://img.shields.io/badge/Terraform-0f172a?style=for-the-badge&logo=terraform&logoColor=7dd3fc" alt="Terraform" />
<img src="https://img.shields.io/badge/Docker-0f172a?style=for-the-badge&logo=docker&logoColor=7dd3fc" alt="Docker" />

</div>

- **Languages:** Python, SQL, JavaScript, HTML/CSS
- **Data Engineering:** Streaming & batch pipelines, ETL/ELT, medallion architecture, star schema, SCD Type 2, data quality testing
- **Streaming & Processing:** Apache Kafka, Spark Structured Streaming
- **Orchestration & Transformation:** Apache Airflow, Dagster, dbt
- **Cloud & Infrastructure:** AWS (S3, Lambda, Athena, Glue, EventBridge, IAM), Terraform, Docker Compose, GitHub Actions
- **Databases & Warehouses:** PostgreSQL, Snowflake, DuckDB, Apache Iceberg, Supabase
- **Dashboards:** Grafana, Streamlit
- **Other:** Flask, REST APIs, Groq & Gemini APIs, Git

---

## 📊 GitHub Stats

<div align="center">

<img height="180" src="https://github-readme-stats.vercel.app/api?username=ZahanAhmedKhan&show_icons=true&theme=nord&border_color=7dd3fc&title_color=7dd3fc&icon_color=7dd3fc&text_color=d8dee9&bg_color=0f172a" alt="GitHub stats" />
<img height="180" src="https://github-readme-stats.vercel.app/api/top-langs/?username=ZahanAhmedKhan&layout=compact&theme=nord&border_color=7dd3fc&title_color=7dd3fc&text_color=d8dee9&bg_color=0f172a" alt="Top languages" />

<br/>

<img src="https://streak-stats.demolab.com/?user=ZahanAhmedKhan&theme=nord&background=0f172a&border=7dd3fc&ring=7dd3fc&fire=7dd3fc&currStreakLabel=7dd3fc&sideLabels=d8dee9&currStreakNum=d8dee9&sideNums=d8dee9&dates=d8dee9" alt="GitHub streak" />

<br/>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=ZahanAhmedKhan&bg_color=0f172a&color=7dd3fc&line=7dd3fc&point=ffffff&area=true&area_color=7dd3fc&hide_border=true" alt="Contribution graph" />

</div>

---

## 🤝 Connect

<div align="center">

<a href="https://github.com/ZahanAhmedKhan"><img src="https://img.shields.io/badge/GitHub-ZahanAhmedKhan-0f172a?style=for-the-badge&logo=github&logoColor=7dd3fc" alt="GitHub" /></a>
<a href="https://linkedin.com/in/zahan-ahmed-khan-a51a50251"><img src="https://img.shields.io/badge/LinkedIn-Connect-0f172a?style=for-the-badge&logo=linkedin&logoColor=7dd3fc" alt="LinkedIn" /></a>

<br/><br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:7dd3fc,100:0f172a&height=140&section=footer&animation=twinkling" width="100%" alt="footer" />

</div>
