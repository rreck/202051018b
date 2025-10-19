```json
{
  "id": "b2027cfbc5323d87",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287272,
  "host_pid": "9e6742732c60:1",
  "hash": "9f3fef60561c4761180b24c40644c2dc2a73098c14c1605e293d405a88ec8cb8",
  "cid": "QmV19f3fef60561c4761180b24c40644c2dc2a73098c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287272,
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
      "evaluated_at": 1760287272
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
  "sig": "521c92d3de3455f103cedf06b6e32b516cea084fe4925869297edcc273524d64"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000020141329
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 54, 'threshold': 50, 'total_amount': 25512300, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 53, 'first_seen': 1760285764, 'matching_hash': '1e11ace6091d7a38'}}}