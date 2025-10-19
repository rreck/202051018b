```json
{
  "id": "6ca3e2942900cc47",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292174,
  "host_pid": "9e6742732c60:1",
  "hash": "f8b7c4c2b00a3503416db9d9964fb350d14e0866683c5c0e6b350a8751ab58f1",
  "cid": "QmV1f8b7c4c2b00a3503416db9d9964fb350d14e0866",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292174,
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
      "evaluated_at": 1760292174
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
  "sig": "3e4d7cf1ded13dc00d9be42bd38739f6d861f391995199ed0dd0f9486e657384"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024544859
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 93065088, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285763, 'matching_hash': '21e0fdbcd06f2d49'}}}