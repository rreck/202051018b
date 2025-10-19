```json
{
  "id": "6ea5a3ef1e5d1a27",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291576,
  "host_pid": "9e6742732c60:1",
  "hash": "939171c8117e06e6aa8561027b66e3e5f840b18d077a736da6afe95a9dd4786a",
  "cid": "QmV1939171c8117e06e6aa8561027b66e3e5f840b18d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291576,
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
      "evaluated_at": 1760291576
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
  "sig": "9de1eb3c6aba4c98f3d38e7953b1eafe9f98885c603054a4283057cdedc4d659"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467602006
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 82596094, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285765, 'matching_hash': 'cc8ab13ff4b154cd'}}}