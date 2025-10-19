```json
{
  "id": "e6dd972579008699",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294871,
  "host_pid": "9e6742732c60:1",
  "hash": "74d99402cf25cda2bf6c281d0c5cf688fd393b671f24e84585527ff68442eb41",
  "cid": "QmV174d99402cf25cda2bf6c281d0c5cf688fd393b67",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294871,
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
      "evaluated_at": 1760294871
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
  "sig": "29859db84c489dc6afd5f062817cd8f08cc9ebf38c2e1427422587fbf427f865"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023973780
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 21588960, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285763, 'matching_hash': 'a6cf7acef53d66c2'}}}}