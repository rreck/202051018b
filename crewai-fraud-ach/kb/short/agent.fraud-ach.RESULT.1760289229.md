```json
{
  "id": "fdfafe3b4d3cf776",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289229,
  "host_pid": "9e6742732c60:1",
  "hash": "235e0909a1a4e2c042fef809694b5ec726d1b1fc079f8f2417b9f7798d0a4b27",
  "cid": "QmV1235e0909a1a4e2c042fef809694b5ec726d1b1fc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289229,
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
      "evaluated_at": 1760289229
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "2a5d3d2fe79284825f6c4aa403df1bf8f98973072addaa1802fa103951b92536"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 676666911893287
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 117, 'threshold': 50, 'total_amount': 45625086, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 116, 'first_seen': 1760285763, 'matching_hash': '67218afda9e45d8d'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '676666915', 'validation_error': 'Invalid routing number checksum'}}}