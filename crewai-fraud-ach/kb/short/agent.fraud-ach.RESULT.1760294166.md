```json
{
  "id": "8f06dcacdfc8ec61",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294166,
  "host_pid": "9e6742732c60:1",
  "hash": "28430756ed0a3f1d3ca194f5c61c94449161b9d9d035580075924edd5e8d6fca",
  "cid": "QmV128430756ed0a3f1d3ca194f5c61c94449161b9d9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294166,
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
      "evaluated_at": 1760294166
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
  "sig": "0ae9c284d816cdae02252e03c2610ca0d1e238e3d6697632b135ea062d067632"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593402675
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 50776059, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285763, 'matching_hash': '1478dad6bc2a5e7e'}}}