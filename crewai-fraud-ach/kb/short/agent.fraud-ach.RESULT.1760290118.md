```json
{
  "id": "d124951d94b77b19",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290118,
  "host_pid": "9e6742732c60:1",
  "hash": "04ebfaeab417b85037c4b13886a4f6c1086ac6ec8a38e2adc2d9f46211a83620",
  "cid": "QmV104ebfaeab417b85037c4b13886a4f6c1086ac6ec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290118,
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
      "evaluated_at": 1760290118
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
  "sig": "2cf0ce5616a10e1a2a3bedfc0d5a6e4d383d7686ee3d3f40c6e2fc2d1bb38624"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461662622
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 142, 'threshold': 50, 'total_amount': 27280472, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 141, 'first_seen': 1760285763, 'matching_hash': '96e0bea374e50243'}}}