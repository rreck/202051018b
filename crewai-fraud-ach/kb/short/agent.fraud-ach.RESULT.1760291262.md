```json
{
  "id": "60a80808df1c3d16",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291262,
  "host_pid": "9e6742732c60:1",
  "hash": "6faf8be22f8f33f3e83e5bf287a5d918cea8f9557d7cc361c8553a5a96d27b31",
  "cid": "QmV16faf8be22f8f33f3e83e5bf287a5d918cea8f955",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291262,
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
      "evaluated_at": 1760291262
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
  "sig": "d581b28becf4a8c1c388d01062bc6e5a572317d3f426eee2275396dae34999eb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460208894
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 171, 'threshold': 50, 'total_amount': 82222785, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 170, 'first_seen': 1760285763, 'matching_hash': '36d88bd4e0ec214b'}}}