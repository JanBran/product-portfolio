-- ============================================
-- USAGE DATA QUERIES
-- ============================================
-- This file contains reusable queries for common data pulls.
-- Adjust table names and schemas to match your data warehouse.
-- ============================================

-- --------------------------------------------
-- DAILY ACTIVE USERS (DAU)
-- --------------------------------------------
-- Description: Count of unique users with any activity per day
-- Use case: Daily health check, trend analysis

SELECT
    DATE(event_timestamp) AS date,
    COUNT(DISTINCT user_id) AS dau
FROM events
WHERE event_timestamp >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY date
ORDER BY date DESC;


-- --------------------------------------------
-- WEEKLY ACTIVE USERS (WAU)
-- --------------------------------------------
-- Description: Rolling 7-day unique active users

SELECT
    DATE(event_timestamp) AS date,
    COUNT(DISTINCT user_id) OVER (
        ORDER BY DATE(event_timestamp)
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS wau_rolling
FROM events
WHERE event_timestamp >= DATE_SUB(CURRENT_DATE(), INTERVAL 60 DAY)
GROUP BY date
ORDER BY date DESC;


-- --------------------------------------------
-- FEATURE ADOPTION
-- --------------------------------------------
-- Description: Percentage of users who have used a feature
-- Parameters: Replace 'feature_name' with actual feature

SELECT
    feature_name,
    COUNT(DISTINCT user_id) AS users_who_used,
    COUNT(DISTINCT user_id) * 100.0 / (SELECT COUNT(DISTINCT user_id) FROM users WHERE is_active = true) AS adoption_rate
FROM events
WHERE event_name = 'feature_used'
    AND event_timestamp >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY feature_name
ORDER BY users_who_used DESC;


-- --------------------------------------------
-- RETENTION COHORT
-- --------------------------------------------
-- Description: Cohort retention analysis by signup week

WITH user_cohorts AS (
    SELECT
        user_id,
        DATE_TRUNC(signup_date, WEEK) AS cohort_week
    FROM users
),
user_activity AS (
    SELECT
        user_id,
        DATE_TRUNC(event_timestamp, WEEK) AS activity_week
    FROM events
    GROUP BY user_id, activity_week
)
SELECT
    c.cohort_week,
    DATE_DIFF(a.activity_week, c.cohort_week, WEEK) AS weeks_since_signup,
    COUNT(DISTINCT a.user_id) AS active_users,
    COUNT(DISTINCT a.user_id) * 100.0 / COUNT(DISTINCT c.user_id) AS retention_rate
FROM user_cohorts c
LEFT JOIN user_activity a ON c.user_id = a.user_id
GROUP BY cohort_week, weeks_since_signup
ORDER BY cohort_week, weeks_since_signup;


-- --------------------------------------------
-- FUNNEL CONVERSION
-- --------------------------------------------
-- Description: Step-by-step funnel conversion
-- Customize steps for your funnel

WITH funnel_steps AS (
    SELECT
        user_id,
        MAX(CASE WHEN event_name = 'signup_started' THEN 1 ELSE 0 END) AS step_1_started,
        MAX(CASE WHEN event_name = 'signup_completed' THEN 1 ELSE 0 END) AS step_2_completed,
        MAX(CASE WHEN event_name = 'first_action' THEN 1 ELSE 0 END) AS step_3_activated,
        MAX(CASE WHEN event_name = 'converted' THEN 1 ELSE 0 END) AS step_4_converted
    FROM events
    WHERE event_timestamp >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
    GROUP BY user_id
)
SELECT
    SUM(step_1_started) AS started,
    SUM(step_2_completed) AS completed,
    SUM(step_3_activated) AS activated,
    SUM(step_4_converted) AS converted,
    SUM(step_2_completed) * 100.0 / NULLIF(SUM(step_1_started), 0) AS start_to_complete_rate,
    SUM(step_3_activated) * 100.0 / NULLIF(SUM(step_2_completed), 0) AS complete_to_activate_rate,
    SUM(step_4_converted) * 100.0 / NULLIF(SUM(step_3_activated), 0) AS activate_to_convert_rate
FROM funnel_steps;


-- --------------------------------------------
-- POWER USERS
-- --------------------------------------------
-- Description: Identify highly engaged users

SELECT
    user_id,
    COUNT(*) AS total_events,
    COUNT(DISTINCT DATE(event_timestamp)) AS active_days,
    COUNT(DISTINCT feature_name) AS features_used
FROM events
WHERE event_timestamp >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY user_id
HAVING active_days >= 20  -- Active 20+ days in last 30
ORDER BY total_events DESC
LIMIT 100;


-- --------------------------------------------
-- SESSION ANALYSIS
-- --------------------------------------------
-- Description: Average session duration and pages per session

SELECT
    DATE(session_start) AS date,
    COUNT(DISTINCT session_id) AS total_sessions,
    AVG(session_duration_seconds) AS avg_duration_seconds,
    AVG(events_in_session) AS avg_events_per_session
FROM sessions
WHERE session_start >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY date
ORDER BY date DESC;


-- ============================================
-- ADD YOUR CUSTOM QUERIES BELOW
-- ============================================
