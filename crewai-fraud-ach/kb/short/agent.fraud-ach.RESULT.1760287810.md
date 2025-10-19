```json
{
  "id": "26652e3bbb4d8bec",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287810,
  "host_pid": "9e6742732c60:1",
  "hash": "2fc9d7875449ff48a0fda8823ef159a487d6fdb3156e089b762ff5081b8c360c",
  "cid": "QmV12fc9d7875449ff48a0fda8823ef159a487d6fdb3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287810,
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
      "evaluated_at": 1760287810
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
  "sig": "1dfe28df9fa86cfe0197273b960711f63eb1e9ff0c8086499646a98b6e275572"
}
```

Fraud detected: duplicate_transaction (score: 90)
Transaction: 063100274546383
Details: {'velocity': {'fraud_detected': True, 'risk_score': 96, 'details': {'transaction_count': 73, 'threshold': 50, 'total_amount': 19314340, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 72, 'first_seen': 1760285763, 'matching_hash': '76da04c5629ac502'}}}