# PerfProbe - Distributed Performance \& Stress Analyzer

Project Objective:

Design and implement a modular performance analysis framework that can:

1. Generate load against APIs or services (HTTP endpoints)
2. Collect metrics like latency, throughput, error rates
3. Visualize results (CLI + Web Dashboard)
4. Support scalable concurrent testing using async/multithreading

# Running the App

1. Write default configurations in config/default.yaml
2. Run "python cli.py" for using the configurations in default.yaml
3. If you dont wanna use default configurations and use some other configuration then Run "python cli.py --url https://example.com --users 20 --rps 10 --duration 30"
4. If you wanna add another configuration add the configuration.yaml file in config folder like prod.yaml or dev.yaml and then run "python cli.py --config "prod" "

# Current Pipeline

cli -> Runner -> Metrics -> Reporter

