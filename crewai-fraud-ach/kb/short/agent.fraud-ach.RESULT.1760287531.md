```json
{
  "id": "cc4578a726a0aa14",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287531,
  "host_pid": "9e6742732c60:1",
  "hash": "17554d42aeca14a0955e95558e2b2f265940e5ff55085634d2f9a2621c6ff042",
  "cid": "QmV117554d42aeca14a0955e95558e2b2f265940e5ff",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287531,
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
      "evaluated_at": 1760287531
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
  "sig": "82979bdcd7e0bc16ef2a1a8cb91cbb687c1372ad4f0678cbb6ba1784db2a49fe"
}
```

Fraud detected: duplicate_transaction (score: 80)
Transaction: 121000249334487
Details: {'velocity': {'fraud_detected': True, 'risk_score': 76, 'details': {'transaction_count': 63, 'threshold': 50, 'total_amount': 13223952, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 62, 'first_seen': 1760285765, 'matching_hash': 'f464ac6512a738da'}}}