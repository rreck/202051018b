```json
{
  "id": "69d16100543030cf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293473,
  "host_pid": "9e6742732c60:1",
  "hash": "9a3d1b0ba5b59d7c52b987852f7e92cf15f33c078b8537cd9e7177fb15c7efe5",
  "cid": "QmV19a3d1b0ba5b59d7c52b987852f7e92cf15f33c07",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293473,
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
      "evaluated_at": 1760293473
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
  "sig": "9d131fd33135a6220a14fd09894d6a265a86c907c12aff9b067f94524de43196"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271976362
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 88461108, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285764, 'matching_hash': 'fe2a7bcd9137a402'}}}