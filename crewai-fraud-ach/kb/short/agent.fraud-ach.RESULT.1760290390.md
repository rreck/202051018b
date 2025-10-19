```json
{
  "id": "e6d1ed5adec2eb14",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290390,
  "host_pid": "9e6742732c60:1",
  "hash": "7ba44b437c67f73a3458bf468a424fe3b5ecb0bec18814fe715b900bb6f460ab",
  "cid": "QmV17ba44b437c67f73a3458bf468a424fe3b5ecb0be",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290390,
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
      "evaluated_at": 1760290390
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "12335abcd13052144cdb834dd7075023afebad0824e38a2a27275648f8b0b921"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 111000023166202
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 149, 'threshold': 50, 'total_amount': 149000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 148, 'first_seen': 1760285763, 'matching_hash': 'ab99b3da8ccd3a17'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}