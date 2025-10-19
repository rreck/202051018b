```json
{
  "id": "1f029c746dd4d448",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293586,
  "host_pid": "9e6742732c60:1",
  "hash": "fc1a33dda76ce5418294f11694cb05d55d18284ceec8130a4fb458e36c6093ba",
  "cid": "QmV1fc1a33dda76ce5418294f11694cb05d55d18284c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293586,
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
      "evaluated_at": 1760293586
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
  "sig": "802f51875eca3244838d06620d4ca5c4f5107e2e16b4e3961f9332391ecf8e2c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599905929
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 85851870, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285765, 'matching_hash': 'da08c58383816f07'}}}