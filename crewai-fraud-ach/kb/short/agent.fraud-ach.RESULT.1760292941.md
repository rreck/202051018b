```json
{
  "id": "912aa52fd321d44b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292941,
  "host_pid": "9e6742732c60:1",
  "hash": "6bbc09c1c90f21df10d848f91cb2c66597ea8f2f3fdde48fb463bb631c286fe7",
  "cid": "QmV16bbc09c1c90f21df10d848f91cb2c66597ea8f2f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292941,
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
      "evaluated_at": 1760292941
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
  "sig": "8bc3651efe0957147d58e024122ceadabe6e3a8b15a804a956f77daebeb12c72"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024587821
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 89776128, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285765, 'matching_hash': 'e3fd1743fc412dec'}}}