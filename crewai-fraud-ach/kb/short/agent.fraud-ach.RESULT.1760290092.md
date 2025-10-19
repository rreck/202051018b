```json
{
  "id": "53f0ee05796102f3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290092,
  "host_pid": "9e6742732c60:1",
  "hash": "ea8823d1dd1218f75a487246c0d5e953b32ef3eed68b0abd3472f4e98b56d8dc",
  "cid": "QmV1ea8823d1dd1218f75a487246c0d5e953b32ef3ee",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290092,
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
      "evaluated_at": 1760290092
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
  "sig": "01ba6d12947f49d7208cf63991ea290e270c4ed68a6c041f95802a5d95f77b86"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022148998
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 141, 'threshold': 50, 'total_amount': 39198846, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 140, 'first_seen': 1760285765, 'matching_hash': 'cc8f74c02d21ef44'}}}