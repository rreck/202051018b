```json
{
  "id": "761634ee97402535",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290659,
  "host_pid": "9e6742732c60:1",
  "hash": "16c6603273c8e0a9568be628a334b8a946b184046a15eb5fdd714042af365890",
  "cid": "QmV116c6603273c8e0a9568be628a334b8a946b18404",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290659,
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
      "evaluated_at": 1760290659
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
  "sig": "b0965323c57ae7da28e3f8578d1f6de352c45257aae28170e9c7dcc9b2309e0a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270910087
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 156, 'threshold': 50, 'total_amount': 63043032, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 155, 'first_seen': 1760285763, 'matching_hash': '020bc3c8298f3eb9'}}}