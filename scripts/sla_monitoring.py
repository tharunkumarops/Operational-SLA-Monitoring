import pandas as pd

# Load tasks dataset
tasks = pd.read_csv('../data/tasks.csv', parse_dates=['start_time','end_time'])

# Calculate duration in hours
tasks['duration_hours'] = (tasks['end_time'] - tasks['start_time']).dt.total_seconds()/3600

# Determine SLA status
tasks['status'] = tasks.apply(lambda x: 'On-Time' if x['duration_hours'] <= x['sla_hours'] else 'Overdue', axis=1)

# Save detailed report
tasks.to_csv('../data/sla_report.csv', index=False)

# Aggregate summary
sla_summary = tasks.groupby('task_type')['status'].value_counts().unstack(fill_value=0)
sla_summary['Total Tasks'] = sla_summary.sum(axis=1)
sla_summary['Compliance %'] = round((sla_summary.get('On-Time',0)/sla_summary['Total Tasks'])*100,2)

# Save summary
sla_summary.to_csv('../data/sla_summary.csv')

print("SLA monitoring report and summary generated successfully!")