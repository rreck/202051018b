```json
{
  "id": "3a71af7ba1378bca",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286378,
  "host_pid": "9e6742732c60:1",
  "hash": "747b1243fbf649482ab8baf8e7f1c7ccecd9e1decfd36405b5e0c7f112a65df6",
  "cid": "QmV1747b1243fbf649482ab8baf8e7f1c7ccecd9e1de",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286378,
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
      "evaluated_at": 1760286378
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
  "sig": "438c4157e2d9916c1147c14b956682b5744e5bea16742c42276e42f66fcaa6fb"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000034020503
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 22, 'first_seen': 1760285765, 'matching_hash': '8db66b2beb557931'}}}