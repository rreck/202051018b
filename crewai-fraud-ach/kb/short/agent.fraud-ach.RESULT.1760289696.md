```json
{
  "id": "aa9a93db8d03bb1a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289696,
  "host_pid": "9e6742732c60:1",
  "hash": "909ff875b3ffbd65671bbff0f9f40cec5ecda10b8af889c00a0906bdfcd7d2a1",
  "cid": "QmV1909ff875b3ffbd65671bbff0f9f40cec5ecda10b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289696,
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
      "evaluated_at": 1760289696
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
  "sig": "e3cfd0ead42f929301b97d9c276b21ee75c9e1eca40f1991ac4c3b4e73be21a1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270650471
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 130, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 129, 'first_seen': 1760285765, 'matching_hash': '471e898b7e147a60'}}}