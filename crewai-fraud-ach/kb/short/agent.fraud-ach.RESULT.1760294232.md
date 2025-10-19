```json
{
  "id": "57a1e946064dae22",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294232,
  "host_pid": "9e6742732c60:1",
  "hash": "e1e013de9ac7dae5950ec32e79143ed219d1f8c8f0f9f92baf6ea4b35cec37f1",
  "cid": "QmV1e1e013de9ac7dae5950ec32e79143ed219d1f8c8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294232,
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
      "evaluated_at": 1760294232
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "0f5a2852d9c4190ad8b540453704180ddf3a9ec9d6c93c5726da55cdac9339b9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590136300
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 115929918, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285764, 'matching_hash': '2d6fc2065b3c1287'}}}nt_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}