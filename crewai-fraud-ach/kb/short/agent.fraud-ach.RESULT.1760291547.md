```json
{
  "id": "682eec42d09fb3fc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291547,
  "host_pid": "9e6742732c60:1",
  "hash": "a2b8bb68f1bac730ec445df50ceed7685038b408aed1b7de1b2c66db9aedafa9",
  "cid": "QmV1a2b8bb68f1bac730ec445df50ceed7685038b408",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291547,
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
      "evaluated_at": 1760291547
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
  "sig": "580944d7ac8fbd8ab781ce3f68d0cb29d459e304ba24d29dd4574af746143c7b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592654855
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 177, 'threshold': 50, 'total_amount': 53443911, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 176, 'first_seen': 1760285765, 'matching_hash': '0ed93ea6dd0046b6'}}}