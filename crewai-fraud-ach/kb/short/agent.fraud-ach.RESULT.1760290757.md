```json
{
  "id": "497cf637edc0ad18",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290757,
  "host_pid": "9e6742732c60:1",
  "hash": "926db944a3598617070eee27008e8770f5a9869c3e2e96d204bfa6f1b331afda",
  "cid": "QmV1926db944a3598617070eee27008e8770f5a9869c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290757,
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
      "evaluated_at": 1760290757
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
  "sig": "1805355cf49f8b789cf85f04a783243e60b51c349452a88034e5e1aa637cd230"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022683015
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 158, 'threshold': 50, 'total_amount': 38661020, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 157, 'first_seen': 1760285765, 'matching_hash': 'a34aa564f21aebc1'}}}