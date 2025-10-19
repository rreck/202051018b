```json
{
  "id": "02de429dc9be1f5d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292851,
  "host_pid": "9e6742732c60:1",
  "hash": "b28c0f5de2ad993a1366b96011bcd771411f7e0ddc1a3741e2e3104331b072bb",
  "cid": "QmV1b28c0f5de2ad993a1366b96011bcd771411f7e0d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292851,
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
      "evaluated_at": 1760292851
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
  "sig": "c79faeb4a68a8f73e359e42ca9f3b380e537f2e4ee0ef7289124327b87dd3963"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028366239
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 28041132, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285763, 'matching_hash': 'fc3cc28fddce4cc6'}}}