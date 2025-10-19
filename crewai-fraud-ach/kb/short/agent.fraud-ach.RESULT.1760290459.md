```json
{
  "id": "a1020b078f7b87c0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290459,
  "host_pid": "9e6742732c60:1",
  "hash": "b73dc4fa03609a957f26c58bf29cde5b10827de7e7ee5ba7d86dfb85acc823ef",
  "cid": "QmV1b73dc4fa03609a957f26c58bf29cde5b10827de7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290459,
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
      "evaluated_at": 1760290459
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
  "sig": "71f4131d418d270810a526e153bb92a82ca3dfb8450e6b81fcc08bb8ab680351"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029536226
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 151, 'threshold': 50, 'total_amount': 10995216, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 150, 'first_seen': 1760285763, 'matching_hash': 'ee8686fc8d545b2d'}}}