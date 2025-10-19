```json
{
  "id": "c9d1b95a0a16feb1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293322,
  "host_pid": "9e6742732c60:1",
  "hash": "4896033d8aa75ba31dac5614d1cc264cd1fcbe359f9572b0f2b51fe9f11c7420",
  "cid": "QmV14896033d8aa75ba31dac5614d1cc264cd1fcbe35",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293322,
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
      "evaluated_at": 1760293322
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
  "sig": "676a1a770ccb38e376fb6272d888cb6540d1262dd94fee31ed36ca8d55b97dbe"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277305476
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 88139880, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285763, 'matching_hash': 'e8a0d4fc67d0b61c'}}}