```json
{
  "id": "34d930067b5f02ff",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287698,
  "host_pid": "9e6742732c60:1",
  "hash": "d30b1fadef2d65ec2dd68b75bb47e26ba8babeaa268cd6ba5c9ebb0904b2f73a",
  "cid": "QmV1d30b1fadef2d65ec2dd68b75bb47e26ba8babeaa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287698,
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
      "evaluated_at": 1760287698
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
  "sig": "b79b447aeaf7bd17b827a9970e96b9d365d34b32036e8a94236b8ef43518dc74"
}
```

Fraud detected: duplicate_transaction (score: 86)
Transaction: 121000243187094
Details: {'velocity': {'fraud_detected': True, 'risk_score': 88, 'details': {'transaction_count': 69, 'threshold': 50, 'total_amount': 30939255, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 68, 'first_seen': 1760285764, 'matching_hash': '46900333a68fa7ba'}}}