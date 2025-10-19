```json
{
  "id": "4efa0f5c2c890754",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290214,
  "host_pid": "9e6742732c60:1",
  "hash": "ff6dcfb61d084a2537ac2246cf376d4e42bacb85173699a939834de120cb6c48",
  "cid": "QmV1ff6dcfb61d084a2537ac2246cf376d4e42bacb85",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290214,
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
      "evaluated_at": 1760290214
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
  "sig": "cb0219f7bc40f0b5a4ce53ce0a3b78d5386c7379e9ff527e5ee6fe18e15a444e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249334487
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 144, 'threshold': 50, 'total_amount': 30226176, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 143, 'first_seen': 1760285765, 'matching_hash': 'f464ac6512a738da'}}}