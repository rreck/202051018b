```json
{
  "id": "e0f320ed271691bc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292744,
  "host_pid": "9e6742732c60:1",
  "hash": "f09a3b3282e22ba6316076af2c1f6ee175bf348bd1fd17366496646204a9f0b8",
  "cid": "QmV1f09a3b3282e22ba6316076af2c1f6ee175bf348b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292744,
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
      "evaluated_at": 1760292744
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
  "sig": "1d15c58b115e6c02967c3435b029676e863f8ee860c2aaaf12b72f9850acc1fe"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157192911
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 54761556, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285764, 'matching_hash': 'e4f1eedb707bab1f'}}}