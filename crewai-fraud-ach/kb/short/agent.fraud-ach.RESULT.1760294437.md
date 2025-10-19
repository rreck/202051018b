```json
{
  "id": "ee7323daa922cd90",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294437,
  "host_pid": "9e6742732c60:1",
  "hash": "b61cf7e5f57b6004526c50f545d02c5a174b411191e2ddf1a5bbcd1e7e748ed0",
  "cid": "QmV1b61cf7e5f57b6004526c50f545d02c5a174b4111",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294437,
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
      "evaluated_at": 1760294437
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
  "sig": "7abbea1060d6a99db2e374da42ac114cf2fb28414edb43bb2f07bba5b7f0b9d3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025362322
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 83451130, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285763, 'matching_hash': '755a8d21dcb7f46a'}}}