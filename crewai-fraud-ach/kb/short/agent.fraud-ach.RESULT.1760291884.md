```json
{
  "id": "2c9d7f338c07fbeb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291884,
  "host_pid": "9e6742732c60:1",
  "hash": "ee2364a07689ae1218a64a7beb4a3580e1b5781b63689f92c214a6811e6ad89e",
  "cid": "QmV1ee2364a07689ae1218a64a7beb4a3580e1b5781b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291884,
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
      "evaluated_at": 1760291884
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
  "sig": "16d849aeed13e7dc702616b28d7d56f407c6ec0c3fbb24b3177948580cac6e60"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023360084
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 185, 'threshold': 50, 'total_amount': 33093540, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 184, 'first_seen': 1760285763, 'matching_hash': 'bfec758d4b349e38'}}}