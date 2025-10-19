```json
{
  "id": "8811017d8bdad197",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288737,
  "host_pid": "9e6742732c60:1",
  "hash": "dc4c04e88e72d5c0f5e712ff886ed408a8d10dfb98bf66b84e2d687124f58a95",
  "cid": "QmV1dc4c04e88e72d5c0f5e712ff886ed408a8d10dfb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288737,
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
      "evaluated_at": 1760288737
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
  "sig": "a7be6269f10bc6973425e1e3e0755b52b4420bcdf8ee822ad8bb90b97dc2b8a9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249334487
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 102, 'threshold': 50, 'total_amount': 21410208, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 101, 'first_seen': 1760285765, 'matching_hash': 'f464ac6512a738da'}}}