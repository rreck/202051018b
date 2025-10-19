```json
{
  "id": "1def1f52138a6fd1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291407,
  "host_pid": "9e6742732c60:1",
  "hash": "a6b2fd4738e6c83dc8194a2de565fbd85b3c48527509b6ac8990061281394d4c",
  "cid": "QmV1a6b2fd4738e6c83dc8194a2de565fbd85b3c4852",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291407,
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
      "evaluated_at": 1760291407
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
  "sig": "8b3705b6a1205dc53d4de9ba705844c18c9798681da8349d189466c651e29a2b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030330812
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 174, 'threshold': 50, 'total_amount': 35270148, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 173, 'first_seen': 1760285763, 'matching_hash': '72f4f50a1c3c0bfc'}}}}