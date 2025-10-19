```json
{
  "id": "53d65db1c8b82bbd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293661,
  "host_pid": "9e6742732c60:1",
  "hash": "6a3b15c560e5467c2dcded155c9da7916350d3413f0d7ba317ca795731918b44",
  "cid": "QmV16a3b15c560e5467c2dcded155c9da7916350d341",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293661,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760293662
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_critical"
  ],
  "sig": "d94f299512a2655d7464a4855ae50d359ffe4839b0080048f1d23b10d16fd480"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 021000025025802
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 1788086475, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285764, 'matching_hash': 'd7be7bb127c676c6'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 81, 'details': {'zscore': 4.15, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8018325}}}