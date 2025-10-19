```json
{
  "id": "9c8f7b6530364497",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290365,
  "host_pid": "9e6742732c60:1",
  "hash": "173f5a6176e559a1a354e6abf835e88555be5e724da9c1f98c298b6ce1d6f85d",
  "cid": "QmV1173f5a6176e559a1a354e6abf835e88555be5e72",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290365,
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
      "evaluated_at": 1760290365
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
  "sig": "7aaa0ab997f6bf32c4b507da3b018f93c53a9da5aa2117b227bab54f41bb2e08"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029832912
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 67900772, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760285765, 'matching_hash': 'ede6214022caf300'}}}