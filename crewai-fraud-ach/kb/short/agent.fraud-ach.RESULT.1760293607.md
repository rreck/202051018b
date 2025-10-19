```json
{
  "id": "29265eb16337cea3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293607,
  "host_pid": "9e6742732c60:1",
  "hash": "f30e40d8ce0f6e58a1ebe74fd04e127be53ec64039a63aabc5ea7eee070ac76d",
  "cid": "QmV1f30e40d8ce0f6e58a1ebe74fd04e127be53ec640",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293607,
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
      "evaluated_at": 1760293607
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
  "sig": "589ecf10ea1a70b8104b249229cfc9bd1fb42b5e57e10bc0f0a50aa422c5cc43"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271403003
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 55500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285763, 'matching_hash': 'a8be718158b742cd'}}}