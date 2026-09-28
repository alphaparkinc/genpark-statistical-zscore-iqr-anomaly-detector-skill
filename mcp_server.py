import sys, json
from client import StatisticalZscoreIqrAnomalyDetector

def main():
    detector = StatisticalZscoreIqrAnomalyDetector()
    for line in sys.stdin:
        line = line.strip()
        if not line: continue
        try:
            req = json.loads(line)
            method = req.get("method")
            rid = req.get("id")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "tools": [
                        {"name": "detect_anomalies", "description": "Detect anomalies.", "inputSchema": {"type": "object", "properties": {"values": {"type": "array"}}, "required": ["values"]}},
                        {"name": "run_benchmark_anomaly_detector", "description": "Run self-test.", "inputSchema": {"type": "object"}}
                    ]
                }
            elif method == "tools/call":
                tname = params.get("name")
                args = params.get("arguments", {})
                if tname == "detect_anomalies":
                    out = detector.detect_anomalies(args.get("values", []))
                elif tname == "run_benchmark_anomaly_detector":
                    out = detector.run_benchmark_anomaly_detector()
                else:
                    out = {"error": f"Unknown tool {tname}"}
                res = {"content": [{"type": "text", "text": json.dumps(out)}]}
            else:
                res = {"error": "Unsupported method"}
            print(json.dumps({"jsonrpc": "2.0", "id": rid, "result": res}), flush=True)
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "error": {"code": -32603, "message": str(e)}}), flush=True)

if __name__ == "__main__":
    main()
