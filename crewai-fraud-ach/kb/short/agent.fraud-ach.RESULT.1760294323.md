```json
{
  "id": "62700429dd93b1a2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294323,
  "host_pid": "9e6742732c60:1",
  "hash": "994d6b515d3050623832870ce5c0675438c63795f4778bc5dd3b1098ca444d98",
  "cid": "QmV1994d6b515d3050623832870ce5c0675438c63795",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294323,
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
      "evaluated_at": 1760294323
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_critical"
  ],
  "sig": "7833716f47d2dcef21cc0a9998f725cc21d5c36752e816e0cc01117575a18185"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 111000023922367
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 1405712524, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285763, 'matching_hash': '420dc08dc8ad4808'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 5956409}}}