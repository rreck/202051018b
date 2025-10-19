```json
{
  "id": "678ba7349e99f8a4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286652,
  "host_pid": "9e6742732c60:1",
  "hash": "e1587327ffdd3ed7ca1786942acf58af4811b85ebca7edb80a4f859ff08d24ae",
  "cid": "QmV1e1587327ffdd3ed7ca1786942acf58af4811b85e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286652,
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
      "evaluated_at": 1760286652
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
  "sig": "b1e2e5c7d5dba8fba30e0e11270161ad60e7c2db001646feeb27034f04ad844f"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10183936, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 31, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}