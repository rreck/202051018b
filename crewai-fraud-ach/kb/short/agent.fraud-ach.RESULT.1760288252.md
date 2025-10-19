```json
{
  "id": "61af226114bd1390",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288252,
  "host_pid": "9e6742732c60:1",
  "hash": "2d6cfba2eea365b01371e39c5d39e2ae6f118eec46b0cbc7b654eb899a68f0f4",
  "cid": "QmV12d6cfba2eea365b01371e39c5d39e2ae6f118eec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288252,
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
      "evaluated_at": 1760288252
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
  "sig": "acdec599d90cc149c57ac6c8da9795d6a86b2ac6d65ab7903267608901f2ed37"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022117413
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 87, 'threshold': 50, 'total_amount': 21414354, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 86, 'first_seen': 1760285765, 'matching_hash': 'c7f16f3a9aa8490f'}}}