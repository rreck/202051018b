```json
{
  "id": "861c9f145190103a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293853,
  "host_pid": "9e6742732c60:1",
  "hash": "47632e316d11d949f4fe5f12cb2a27a5a79d3f9bae642b19f0e6211c12f9b6f0",
  "cid": "QmV147632e316d11d949f4fe5f12cb2a27a5a79d3f9b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293853,
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
      "evaluated_at": 1760293853
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
  "sig": "58cfbb7747cf1e8b1a719702cbc23ea146e0a54f7349c72a14f5ce60f4e5f106"
}
```

Fraud detected: amount_anomaly (score: 90)
Transaction: 121000241645883
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 1980790196, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285763, 'matching_hash': '8711cb2fb2144ae4'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 85, 'details': {'zscore': 4.56, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8725948}}}