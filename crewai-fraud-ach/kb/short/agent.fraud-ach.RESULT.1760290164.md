```json
{
  "id": "362017c44e30f8ac",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290164,
  "host_pid": "9e6742732c60:1",
  "hash": "a986f3fd46235145a4ee269ba401e312bff205aaecffa5a58e23149952f4855d",
  "cid": "QmV1a986f3fd46235145a4ee269ba401e312bff205aa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290164,
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
      "evaluated_at": 1760290164
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
  "sig": "208d2cb48c64b1fc6f5dafa7dbb09a6013c936c91edb1c4bb7ec61dbe2bfa300"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030595065
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 143, 'threshold': 50, 'total_amount': 43453553, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 142, 'first_seen': 1760285763, 'matching_hash': '3889a0f66c8870f8'}}}