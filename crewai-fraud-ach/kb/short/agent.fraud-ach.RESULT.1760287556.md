```json
{
  "id": "17d1e294b62b323c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287556,
  "host_pid": "9e6742732c60:1",
  "hash": "908ac535b55e8334886fe8242cbc346d1d9709f4a03a0bba2b6bcae5c77e3f13",
  "cid": "QmV1908ac535b55e8334886fe8242cbc346d1d9709f4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287556,
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
      "evaluated_at": 1760287556
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
  "sig": "c7c4204c950ff11b7402d482ea1c84a0d5e273c3e57588c782ad4bc3cdb8edcc"
}
```

Fraud detected: duplicate_transaction (score: 81)
Transaction: 121000242075877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 78, 'details': {'transaction_count': 64, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 63, 'first_seen': 1760285765, 'matching_hash': '7e39a816a4a44fcc'}}}