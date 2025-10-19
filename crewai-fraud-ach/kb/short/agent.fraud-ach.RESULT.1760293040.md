```json
{
  "id": "9759bebe1197c6b6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293040,
  "host_pid": "9e6742732c60:1",
  "hash": "9415f3f9504824315944e44f58c51bea6d6ab4f058a49e58a1084e7aa5da9cf2",
  "cid": "QmV19415f3f9504824315944e44f58c51bea6d6ab4f0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293040,
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
      "evaluated_at": 1760293040
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
  "sig": "49e932e357131f1e33031e10b5aa89824c31a1c127a90e3931af4ca53cf23497"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466969713
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 65329740, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285763, 'matching_hash': '1e9180284a8352f5'}}}