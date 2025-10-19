```json
{
  "id": "49f8d0798124f1b5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293481,
  "host_pid": "9e6742732c60:1",
  "hash": "7cbaa5e196eaeb0f78f1bc96a631d4944983d5b0a39d2ebefe5786d639faf19a",
  "cid": "QmV17cbaa5e196eaeb0f78f1bc96a631d4944983d5b0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293481,
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
      "evaluated_at": 1760293481
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
  "sig": "ad0eca38fb65978ca24ffaa361f694ecbb6b717bc9a8679d39b7a2e4e759b0c9"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 026009597367941
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 2038037214, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285764, 'matching_hash': '5430161f1ba10767'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 88, 'details': {'zscore': 4.89, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9306106}}}