```json
{
  "id": "042b9c4fb067b03f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290656,
  "host_pid": "9e6742732c60:1",
  "hash": "6be5b3640e263974fdf78cf5e2aac86be5b32ee986a88dd82f6432dc0cbc329d",
  "cid": "QmV16be5b3640e263974fdf78cf5e2aac86be5b32ee9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290656,
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
      "evaluated_at": 1760290656
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
  "sig": "88f860ef03c5e06cf215e92a35a8d107b35e5f5492a5d4ab27b406f3c6e5885d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596116036
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 156, 'threshold': 50, 'total_amount': 39000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 155, 'first_seen': 1760285763, 'matching_hash': 'e2bf4d89584c6445'}}}