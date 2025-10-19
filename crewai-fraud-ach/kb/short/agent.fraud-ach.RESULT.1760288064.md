```json
{
  "id": "56f2d57bbbe520d5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288064,
  "host_pid": "9e6742732c60:1",
  "hash": "aafea863d23828491e1f14caffa8b25c654a6312b055b9302cfaa8a1bef5cc32",
  "cid": "QmV1aafea863d23828491e1f14caffa8b25c654a6312",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288064,
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
      "evaluated_at": 1760288064
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
  "sig": "5e927d74085867d1c13a2cfe05dd0834657ba7d1f9e48b969aa2c8c84e15065f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466322331
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 81, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 80, 'first_seen': 1760285765, 'matching_hash': '8006c6780242cc6a'}}}