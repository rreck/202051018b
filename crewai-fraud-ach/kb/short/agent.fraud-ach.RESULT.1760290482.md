```json
{
  "id": "fa196e8fb38c3a16",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290482,
  "host_pid": "9e6742732c60:1",
  "hash": "fbefd0850d4995b305289d1ef2197b83b5bfabfd438a89658e2784a620ebc4eb",
  "cid": "QmV1fbefd0850d4995b305289d1ef2197b83b5bfabfd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290482,
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
      "evaluated_at": 1760290482
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
  "sig": "8f062915982be3f6a1455b12cca17b15b43f7d5445e87848bc087e2765b0f573"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463448865
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 151, 'threshold': 50, 'total_amount': 25949803, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 150, 'first_seen': 1760285765, 'matching_hash': '5a565595f8571aef'}}}