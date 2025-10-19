```json
{
  "id": "a331af7b04160ffa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291738,
  "host_pid": "9e6742732c60:1",
  "hash": "f49c901e157451cba5e56d428fa2078533496f8e42728fc0caba14aa795b9143",
  "cid": "QmV1f49c901e157451cba5e56d428fa2078533496f8e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291738,
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
      "evaluated_at": 1760291738
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
  "sig": "2d07f3d1d4417061838c72ece9975aaa02bebd708b06db0965f42c0cc5e26e98"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590642445
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50, 'total_amount': 17654364, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760285764, 'matching_hash': 'c07dd188e27cb1b7'}}}