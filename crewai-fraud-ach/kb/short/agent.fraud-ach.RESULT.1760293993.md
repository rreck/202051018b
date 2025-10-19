```json
{
  "id": "7479208990c5f9fb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293993,
  "host_pid": "9e6742732c60:1",
  "hash": "be7419a0114097a95ee9516c17e829e5a197e08b3bfe04cf6c12c98da95f73d9",
  "cid": "QmV1be7419a0114097a95ee9516c17e829e5a197e08b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293993,
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
      "evaluated_at": 1760293993
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
  "sig": "f2666506300a5fd69ce74981cda1e4bc7e12cca9518ce58a6e8b194b63fc82f3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022683015
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 56034010, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285765, 'matching_hash': 'a34aa564f21aebc1'}}}