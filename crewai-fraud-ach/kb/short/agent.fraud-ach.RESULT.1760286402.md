```json
{
  "id": "0e011125aaeed02b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286402,
  "host_pid": "9e6742732c60:1",
  "hash": "62cc2e4e4e43798b13385bb071acbf7653999079e0107e2e760a7b02e0f70f78",
  "cid": "QmV162cc2e4e4e43798b13385bb071acbf7653999079",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286402,
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
      "evaluated_at": 1760286402
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "7ccc0d24105a6fa92a2d99d2ab0feb765ac3dc86a0eb1596696c5efad77fb5ee"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105155322765
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10314888, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 23, 'first_seen': 1760285763, 'matching_hash': '7a27d1bb592c5069'}}}