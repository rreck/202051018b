```json
{
  "id": "f345656d2b935e94",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293838,
  "host_pid": "9e6742732c60:1",
  "hash": "72737bea483aeb27661e71486a2db65b8b0ea5c9ecd0b5b24fe740731a71c814",
  "cid": "QmV172737bea483aeb27661e71486a2db65b8b0ea5c9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293838,
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
      "evaluated_at": 1760293838
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
  "sig": "52d4db77150c13d12e2135fdf0f7e103c340400e7f33f94d81eb7493ab5a0d05"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038480332
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 16979606, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285765, 'matching_hash': '8289eea4583ef54f'}}}