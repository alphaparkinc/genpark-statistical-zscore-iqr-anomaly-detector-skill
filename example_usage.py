from client import StatisticalZscoreIqrAnomalyDetector
import json

def main():
    detector = StatisticalZscoreIqrAnomalyDetector()
    res = detector.run_benchmark_anomaly_detector()
    print("Anomaly Detector Benchmark Result:")
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    main()
