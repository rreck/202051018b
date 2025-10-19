```json
{
  "id": "cc4f6c93a928a122",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287357,
  "host_pid": "9e6742732c60:1",
  "hash": "bddc83a4cb60b56fa26f5e8ec232f4a7af86319a5f49a06bb2399683a0c46ea0",
  "cid": "QmV1bddc83a4cb60b56fa26f5e8ec232f4a7af86319a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287357,
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
      "evaluated_at": 1760287357
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
  "sig": "a9ef569d0a7926ca2185571c566d9c831398825c06b5e3718bd40404f5067f3c"
}
```

Fraud detected: duplicate_transaction (score: 74)
Transaction: 026009596502557
Details: {'velocity': {'fraud_detected': True, 'risk_score': 64, 'details': {'transaction_count': 57, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 56, 'first_seen': 1760285764, 'matching_hash': 'c368684e8d9c7f24'}}}