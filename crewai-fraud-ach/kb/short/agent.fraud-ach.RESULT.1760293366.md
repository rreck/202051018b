```json
{
  "id": "b3b2d03ae94a76b3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293366,
  "host_pid": "9e6742732c60:1",
  "hash": "1d1dd294d3da8fc7db1fb25e6e290f9f0ac30a9f9284e0732da67a9e660443e5",
  "cid": "QmV11d1dd294d3da8fc7db1fb25e6e290f9f0ac30a9f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293366,
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
      "evaluated_at": 1760293366
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
  "sig": "b097bac3483431aeeed97f0abcacb1e2d181091c5f5a39818ab79a0b79e4a0dc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593654177
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 71270178, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285764, 'matching_hash': '5fbc310f1a1fe9dc'}}}