```json
{
  "id": "79e58392fd2c606c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287412,
  "host_pid": "9e6742732c60:1",
  "hash": "8fd48e7546ae5ea1b78806ff3340efc3629aabc01e263db18c76502211a4224e",
  "cid": "QmV18fd48e7546ae5ea1b78806ff3340efc3629aabc0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287412,
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
      "evaluated_at": 1760287412
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "ebcdc5030b38ca428e74ba02b9028d0a5a21abdc5e3eadff84ce23793499abab"
}
```

Fraud detected: duplicate_transaction (score: 76)
Transaction: 044000038607326
Details: {'velocity': {'fraud_detected': True, 'risk_score': 68, 'details': {'transaction_count': 59, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 58, 'first_seen': 1760285763, 'matching_hash': '23e85c6499cf881c'}}}