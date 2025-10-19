```json
{
  "id": "3bd3d603584ecc3f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293974,
  "host_pid": "9e6742732c60:1",
  "hash": "c4a4333f2a295d200d395d745d852c62cd2d9faec63e9de1d0ff54ca182ad26c",
  "cid": "QmV1c4a4333f2a295d200d395d745d852c62cd2d9fae",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293974,
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
      "evaluated_at": 1760293974
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
  "sig": "fc45e724808a4784566eaf71462e32b555145816e9acad3d3d46d58d7349a8ac"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592473066
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 74908419, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285763, 'matching_hash': '48f07b8f6bc31034'}}}