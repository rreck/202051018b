```json
{
  "id": "e9adbede3e9731d1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294622,
  "host_pid": "9e6742732c60:1",
  "hash": "4b85ba04f828c47bb8a855afc0e7dd55dd3516c810b24117feef35d59d5f6569",
  "cid": "QmV14b85ba04f828c47bb8a855afc0e7dd55dd3516c8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294622,
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
      "evaluated_at": 1760294622
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
  "sig": "df54dd9992ae055cc9af0017a6c02d97cbb795b1e23521ff3ca6e8923f5dfc90"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038907358
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 52122275, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285764, 'matching_hash': '4f1b5532b664e41d'}}}