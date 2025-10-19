```json
{
  "id": "3a613139798600db",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292319,
  "host_pid": "9e6742732c60:1",
  "hash": "5c65839464d1ad8819d7a118277b2e12664a9634bf5f89ca532c5fb45c7e878a",
  "cid": "QmV15c65839464d1ad8819d7a118277b2e12664a9634",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292319,
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
      "evaluated_at": 1760292319
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
  "sig": "8292c84b7dab9aab1e7113a57d0c606e5c4198dd1e34ca98a3e12fe676c06382"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032147418
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 72357090, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285764, 'matching_hash': '7eb9a0fe320f28ac'}}}