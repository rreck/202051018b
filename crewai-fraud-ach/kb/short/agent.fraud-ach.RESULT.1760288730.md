```json
{
  "id": "51b7996c2561adb5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288730,
  "host_pid": "9e6742732c60:1",
  "hash": "02c88ea2e446d2c0ee39def8aa8edf5105cd5a3a6e7226ede450db681163a401",
  "cid": "QmV102c88ea2e446d2c0ee39def8aa8edf5105cd5a3a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288730,
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
      "evaluated_at": 1760288730
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
  "sig": "e7b19ff7d50e5c11476e1bc23a70d2e574532af343278c8e60eef0edd60d184f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151102645
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 102, 'threshold': 50, 'total_amount': 41925468, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 101, 'first_seen': 1760285763, 'matching_hash': '9dd268c0fa996698'}}}