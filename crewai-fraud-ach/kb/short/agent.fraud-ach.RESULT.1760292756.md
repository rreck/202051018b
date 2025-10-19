```json
{
  "id": "60c8804c2ee523a7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292756,
  "host_pid": "9e6742732c60:1",
  "hash": "6afcbfd64cb3defc730621198b7ff80a871add80934a61f7f014a107d0f7e88d",
  "cid": "QmV16afcbfd64cb3defc730621198b7ff80a871add80",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292756,
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
      "evaluated_at": 1760292756
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
  "sig": "4ab0a33f8bc1bf592a4ff80563f9bc6f11d574b34c960e6a46d14b3a5e964ff3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279407211
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 44358780, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285764, 'matching_hash': 'efd9a787beb40cb2'}}}