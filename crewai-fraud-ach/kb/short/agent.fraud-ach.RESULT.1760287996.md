```json
{
  "id": "cfe9a17dbeea1623",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287996,
  "host_pid": "9e6742732c60:1",
  "hash": "b8f65b565dd757101ff6608a0245c337d1756568fcd2e2ae1e37153c8300a99f",
  "cid": "QmV1b8f65b565dd757101ff6608a0245c337d1756568",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287996,
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
      "evaluated_at": 1760287996
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
  "sig": "48ee0f988b3a20fdf0fe397bb7161bdda013239b6098d9cbbdd370cee7e24654"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022841229
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 79, 'threshold': 50, 'total_amount': 14075035, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 78, 'first_seen': 1760285763, 'matching_hash': '5d206cfe266207b6'}}}