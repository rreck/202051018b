```json
{
  "id": "50dce0dc4100265b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294185,
  "host_pid": "9e6742732c60:1",
  "hash": "5255149f8e72b23959096c4a4cc1134ebfa6783fe6fc06d7d473a7394594e685",
  "cid": "QmV15255149f8e72b23959096c4a4cc1134ebfa6783f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294185,
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
      "evaluated_at": 1760294185
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
  "sig": "1b5cb5ee827b5e040856da13abd82f0a75938d86d6d28c8eb2a8ebe822e19ec3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248019681
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 107173476, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285763, 'matching_hash': 'd399d5f74d941af5'}}}