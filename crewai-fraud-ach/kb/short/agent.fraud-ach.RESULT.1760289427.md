```json
{
  "id": "f1eaa6c4c19c8390",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289427,
  "host_pid": "9e6742732c60:1",
  "hash": "8f2eeb933ae5d33ffd0f064f6090989a3b4bbb4f075addfb1bcc009079cdd70f",
  "cid": "QmV18f2eeb933ae5d33ffd0f064f6090989a3b4bbb4f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289427,
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
      "evaluated_at": 1760289427
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
  "sig": "fb0ed97bffcced27e3afddd0e3f34ead46e30595987f295d325890a5e6bf4bc1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274851410
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 123, 'threshold': 50, 'total_amount': 15224694, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 122, 'first_seen': 1760285763, 'matching_hash': '05e1730ec720465d'}}}