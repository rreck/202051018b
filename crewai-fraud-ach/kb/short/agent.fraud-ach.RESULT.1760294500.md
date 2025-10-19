```json
{
  "id": "d66e6a5091144b9b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294500,
  "host_pid": "9e6742732c60:1",
  "hash": "4d3f7f5cb823ae1093c65736881c84d6537cac69ccc7596441d8ad4dc355d997",
  "cid": "QmV14d3f7f5cb823ae1093c65736881c84d6537cac69",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294500,
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
      "evaluated_at": 1760294500
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
  "sig": "e0f4fde461f7c81c3b45e5010fa04fdf5d6332773f9cd37ac018d6fc0465674e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594957329
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 118972766, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285763, 'matching_hash': '2b2bf7f9f831f062'}}}