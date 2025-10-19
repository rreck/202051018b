```json
{
  "id": "4bfb1b6905d25ed4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289170,
  "host_pid": "9e6742732c60:1",
  "hash": "d21777ba1dba32c9c2acbac1ac875decfeffc0cd5d788264c6a7ed77913e12e0",
  "cid": "QmV1d21777ba1dba32c9c2acbac1ac875decfeffc0cd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289170,
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
      "evaluated_at": 1760289170
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
  "sig": "3d3aa8533ddb78a6cd67a358197c8b612cf9194f686853d685eec7d20caa2265"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241265060
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 115, 'threshold': 50, 'total_amount': 52480365, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 114, 'first_seen': 1760285765, 'matching_hash': '7bee400a4c5e15b1'}}}