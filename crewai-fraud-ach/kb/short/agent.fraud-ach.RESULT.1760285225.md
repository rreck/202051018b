```json
{
  "id": "1a03a6ded3d80e54",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285225,
  "host_pid": "9e6742732c60:1",
  "hash": "9ed8102c2bff73d863f9d95a34cfbf1cdbaaf3b687d5f999a5889ab12d60e87f",
  "cid": "QmV19ed8102c2bff73d863f9d95a34cfbf1cdbaaf3b6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285225,
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
      "evaluated_at": 1760285225
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
  "sig": "8cfa53b91be82564086fd3c428ceca2fdbb1b1c3c62fd0c512046c36c0d4d835"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201464924143
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10159625, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 24, 'first_seen': 1760284979, 'matching_hash': '7b94effc1b7c4489'}}}