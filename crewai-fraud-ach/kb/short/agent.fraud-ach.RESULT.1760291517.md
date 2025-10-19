```json
{
  "id": "48d8ec7267bb9800",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291517,
  "host_pid": "9e6742732c60:1",
  "hash": "b391aaf90a31756b2124e2b78f6a6421579b3408e484c3ab259227b171f8ae3a",
  "cid": "QmV1b391aaf90a31756b2124e2b78f6a6421579b3408",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291517,
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
      "evaluated_at": 1760291517
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
  "sig": "9620712d9a9fcb5b1b2fa103e5ea5d1dd08bcba2d8fc9e579888d95112f923bc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599553408
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 177, 'threshold': 50, 'total_amount': 21124242, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 176, 'first_seen': 1760285763, 'matching_hash': '67e91645ed6012ef'}}}