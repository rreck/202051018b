```json
{
  "id": "110971a484ee21d1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291892,
  "host_pid": "9e6742732c60:1",
  "hash": "5871b9c59e53ee4adc50aad5a6682fc67bda1c1ea5eb9d9fcd50d4b63bdda7a6",
  "cid": "QmV15871b9c59e53ee4adc50aad5a6682fc67bda1c1e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291892,
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
      "evaluated_at": 1760291892
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
  "sig": "814b30e30de31c5c0c836c70cad1da96ff842c572870d03baba318123515faa8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150658717
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 185, 'threshold': 50, 'total_amount': 61869180, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 184, 'first_seen': 1760285765, 'matching_hash': 'c0bd022b5af03ee8'}}}