```json
{
  "id": "646673c65452ba19",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292762,
  "host_pid": "9e6742732c60:1",
  "hash": "ddd25803ba25314646bdf0d46ad9ebbc1e433a4f689ff77adc4bf1f28498a09a",
  "cid": "QmV1ddd25803ba25314646bdf0d46ad9ebbc1e433a4f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292762,
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
      "evaluated_at": 1760292762
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
  "sig": "439efa74a3598e255fe4000e47d42687777915c9472f94f06c1ff95630992c1e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466004729
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 58192428, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285765, 'matching_hash': '1e26fed2c08b1370'}}}