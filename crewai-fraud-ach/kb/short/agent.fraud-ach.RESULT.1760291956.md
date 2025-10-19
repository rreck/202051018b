```json
{
  "id": "b9234ad3bf78218f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291956,
  "host_pid": "9e6742732c60:1",
  "hash": "f479ab726ea391820cb64748e3351d4c5b686c387e8b6abf5fc858a808221e7e",
  "cid": "QmV1f479ab726ea391820cb64748e3351d4c5b686c38",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291956,
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
      "evaluated_at": 1760291957
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
  "sig": "17abe127a192493a482b3b397430f47472ebe56eb747d733ece231e7652c63e5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464999191
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 23754049, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285763, 'matching_hash': '0f07ea7feb264441'}}}