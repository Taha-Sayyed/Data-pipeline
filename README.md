# 🎧 Spotify Data Pipeline (ETL) 

> A comprehensive data engineering project that builds an automated ETL pipeline for Spotify music data using AWS cloud services, transforming raw JSON data into actionable insights through SQL analytics.

## 🚀 Project Overview

This project creates a fully automated **Extract, Transform, Load (ETL)** pipeline that processes Spotify playlist data and generates meaningful music analytics. The pipeline extracts data from Spotify's API, transforms it into structured datasets, and enables powerful SQL-based analysis of music trends and patterns.

**Key Achievement**: Automated daily data processing with zero manual intervention, transforming complex JSON structures into clean, queryable datasets for music analytics.

## 🎯 Problem Statement

Music enthusiasts and data analysts often struggle to:
- Access structured data from streaming platforms for analysis
- Automate the collection and processing of music metadata
- Generate insights about artist popularity, song trends, and album performance
- Scale data processing without manual intervention

This pipeline solves these challenges by creating an end-to-end automated system for Spotify data processing and analysis.

## 🏗️ Architecture
   ![Image](https://github.com/user-attachments/assets/a38dc4ef-50b0-429d-8f25-867bd54f0ec9)
 
## 🛠️ Technologies Used

### Core Technologies
- **Python 3.8+** - Primary programming language for data processing
- **Pandas** - Data manipulation and analysis
- **Boto3** - AWS SDK for Python integration

### AWS Services
- **AWS Lambda** - Serverless compute for extraction and transformation
- **Amazon S3** - Scalable object storage for raw and processed data
- **Amazon CloudWatch** - Automated scheduling and monitoring
- **AWS Glue** - Data catalog and schema management
- **Amazon Athena** - Interactive SQL query engine
- **AWS Glue Crawler** - Automatic schema discovery

### APIs & External Services
- **Spotify Web API** - Music data extraction source

## ✨ Features

### 🔄 Automated Data Pipeline
- **Daily automated extraction** of playlist data from Spotify API
- **Event-driven transformation** triggered by new data arrivals
- **Zero-downtime processing** with serverless architecture

### 📊 Data Processing Capabilities
- **Multi-format data handling**: JSON to structured CSV transformation
- **Data segmentation**: Automatic splitting into albums, artists, and songs datasets
- **Data quality assurance**: Built-in cleaning and validation processes

### 🔍 Analytics Ready
- **SQL-queryable datasets** through Amazon Athena
- **Automated schema inference** via AWS Glue Crawler
- **Scalable query performance** for large datasets

## 📁 Data Structure

The pipeline organizes data into three main categories:

![Image](https://github.com/user-attachments/assets/e142cbaa-083a-48bb-a8ba-7bf3068be380)


## 📈 Available Analytics

The pipeline enables comprehensive music analysis through various SQL queries:

### 🎵 Song Analytics
- Track popularity rankings and trends
- Song duration analysis and patterns
- Recently added songs tracking
- Zero vs. high popularity song identification

### 🎤 Artist Analytics
- Artist popularity scoring based on song performance
- Song count per artist analysis
- Artists with extensive catalogs (5+ songs)
- Top performing artists identification

### 💿 Album Analytics
- Most frequent albums in playlists
- Songs per album distribution
- Album popularity metrics
- Complete album-artist-song relationships

### 📊 Sample Query Results
- **Top 10 Most Popular Songs** with artist information
- **Longest Songs** with complete metadata
- **Average Song Duration** across different artists
- **Songs Added in Last 30 Days** for trend analysis

![Image](https://github.com/user-attachments/assets/7cadbf85-c91c-423d-8bd3-335533c92070)

## 🚀 Getting Started

### Prerequisites
- AWS Account with appropriate permissions
- Spotify Developer Account
- Python 3.8 or higher
- Basic understanding of AWS services

### Setup Instructions

1. **Spotify API Setup**
   ```bash
   # Register your application at https://developer.spotify.com/
   # Obtain your CLIENT_ID and CLIENT_SECRET
   ```

2. **AWS Configuration**
   ```bash
   # Configure AWS credentials
   aws configure
   ```

3. **Lambda Function Deployment**
   - Deploy extraction Lambda with Spotify API integration
   - Deploy transformation Lambda with data processing logic
   - Configure appropriate IAM roles and permissions

4. **S3 Bucket Configuration**
   - Create bucket with organized folder structure
   - Set up appropriate access policies
   - Configure event notifications for Lambda triggers

5. **CloudWatch Scheduling**
   - Set up daily triggers for data extraction
   - Configure monitoring and alerting

## 💡 Use Cases

### 🎵 Music Enthusiasts
Perfect for music lovers who want to:
- Track their favorite artists' song releases
- Analyze music trends and popularity patterns
- Discover insights about their preferred playlists

### 🎤 Arijit Singh Fans
Specifically designed for fans who want to:
- Stay updated with Arijit Singh's top performing songs
- Analyze the popularity trends of his music catalog
- Get automated updates about his latest releases

### 📊 Data Analysts & Students
Ideal for professionals and learners wanting to:
- Practice real-world ETL pipeline development
- Learn AWS cloud services integration
- Understand data engineering best practices

## 🔮 Future Enhancements

- **Multi-Artist Support**: Extend beyond single artist playlists
- **Real-time Processing**: Implement streaming data processing
- **Advanced Analytics**: Machine learning for music recommendation
- **Dashboard Integration**: Web-based visualization interface
- **API Development**: RESTful API for external data access


## 🙏 Acknowledgments

- **Spotify** for providing comprehensive music data through their API
- **AWS** for robust cloud infrastructure services
- **Arijit Singh** for inspiring this project with amazing music

## 📧 Contact

If you have any questions, suggestions, or would like to discuss this project further, please feel free to reach out!

---

⭐ **If you found this project helpful, please consider giving it a star!** ⭐

*Built with ❤️ for music and data engineering*
