```json
{
  "id": "7e5f7b23f4be991f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292977,
  "host_pid": "9e6742732c60:1",
  "hash": "ca6a473f7d474ee6a440bf82f4d3eb4860a7be152c4c2cccc932283c7dc3ab22",
  "cid": "QmV1ca6a473f7d474ee6a440bf82f4d3eb4860a7be15",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292977,
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
      "evaluated_at": 1760292977
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
  "sig": "059f8d4a0069cab3f286331e113eb79f9c5d4c3a1b2d1267987c3330f56d03b2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025657387
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 66460328, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285763, 'matching_hash': '1be88e7372567f08'}}}