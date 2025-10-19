```json
{
  "id": "37af57d7a9b9d7fb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293776,
  "host_pid": "9e6742732c60:1",
  "hash": "46433a788499ea4000cbaad5e17b9b9caf678079db0c5869f340da7783da6bab",
  "cid": "QmV146433a788499ea4000cbaad5e17b9b9caf678079",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293776,
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
      "evaluated_at": 1760293776
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
  "sig": "d718b1f6f92ddb44ef34aa8765340d3b51d460a4bbfaf55dedc8e9bf8d8756d3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158912506
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 34618725, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285765, 'matching_hash': 'bcd6f6796bd6b696'}}}