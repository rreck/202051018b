```json
{
  "id": "bbb7d62081952ab1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293335,
  "host_pid": "9e6742732c60:1",
  "hash": "d88b31cb2745e311c4e967b65f6d386a06a4674e5dc2e38e0bd52cf8bdae0acf",
  "cid": "QmV1d88b31cb2745e311c4e967b65f6d386a06a4674e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293335,
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
      "evaluated_at": 1760293335
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
  "sig": "0b9520f5aa38ebcafb21649c7ca86fcef8fcaeb05acede7ac4a7afd2bc8ceb75"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467874144
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 53823528, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285764, 'matching_hash': '428cbf79813503ca'}}}