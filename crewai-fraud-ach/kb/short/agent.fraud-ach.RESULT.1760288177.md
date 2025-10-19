```json
{
  "id": "772766f05272a736",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288177,
  "host_pid": "9e6742732c60:1",
  "hash": "93ff34c53477481dc27677705f4b7395e732b895e8fb4abfa682a4af8120bb41",
  "cid": "QmV193ff34c53477481dc27677705f4b7395e732b895",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288177,
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
      "evaluated_at": 1760288177
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
  "sig": "1d1a9788d3fac12be686db5a1089d1439f3bc9f6bd104669e7e8f91dc2178276"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276997857
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 85, 'threshold': 50, 'total_amount': 40438495, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 84, 'first_seen': 1760285763, 'matching_hash': 'b73e9a6de72cc131'}}}