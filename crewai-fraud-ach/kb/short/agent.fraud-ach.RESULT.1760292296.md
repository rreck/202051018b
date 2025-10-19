```json
{
  "id": "a3b2c1065b8f5384",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292296,
  "host_pid": "9e6742732c60:1",
  "hash": "68109d3712bd9dc54af5e4c6ea131a241dc8371cc3bf45b8a24e9ba2e2370263",
  "cid": "QmV168109d3712bd9dc54af5e4c6ea131a241dc8371c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292296,
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
      "evaluated_at": 1760292296
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
  "sig": "adb772e7759f4d537d39906239ea715e4fda07b721bdb66fd768d669dc659256"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039404283
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50, 'total_amount': 64869138, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285765, 'matching_hash': '11fbcf742e15d2b0'}}}