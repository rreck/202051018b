```json
{
  "id": "269c96e905c71e48",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294081,
  "host_pid": "9e6742732c60:1",
  "hash": "1b76be5560091e5afa235f234ee0cb2244fbb2cd08b606536d21f394c6cfc538",
  "cid": "QmV11b76be5560091e5afa235f234ee0cb2244fbb2cd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294081,
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
      "evaluated_at": 1760294081
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
  "sig": "9e1c686ba5f92a5836294665bd8f48d2eda658151712283ab3375bc842bec051"
}
```

Fraud detected: amount_anomaly (score: 85)
Transaction: 044000032598305
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 1416342543, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285763, 'matching_hash': '2af7a4570c2b815d'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 70, 'details': {'zscore': 3.08, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6131353}}}