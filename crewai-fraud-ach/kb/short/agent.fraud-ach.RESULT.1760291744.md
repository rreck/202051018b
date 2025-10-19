```json
{
  "id": "aa3552ad8911d9e0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291744,
  "host_pid": "9e6742732c60:1",
  "hash": "49fea3044804a17b8ee461aa6aea13fb915b2f98b667f014b1232189e5c26b8b",
  "cid": "QmV149fea3044804a17b8ee461aa6aea13fb915b2f98",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291744,
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
      "evaluated_at": 1760291744
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
  "sig": "e3c20115902d911774a2cbaa36e74002a0a29e9ddca5709d39a55251660a5998"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279745557
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50, 'total_amount': 17039932, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760285765, 'matching_hash': '46b84f4cf2bc4bde'}}}