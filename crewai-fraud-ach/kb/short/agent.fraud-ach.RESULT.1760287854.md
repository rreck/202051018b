```json
{
  "id": "63d1fa0471f7086b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287854,
  "host_pid": "9e6742732c60:1",
  "hash": "2af3fecca7ae1db0b5575fc637e0a15ec62ccf95f024a0f8e390f71e8a3a4cf6",
  "cid": "QmV12af3fecca7ae1db0b5575fc637e0a15ec62ccf95",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287854,
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
      "evaluated_at": 1760287854
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
  "sig": "a91544c6d8d22ef03de64c7dbee800d50fa31b4c805e9061e0327c02c277bb01"
}
```

Fraud detected: duplicate_transaction (score: 91)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 98, 'details': {'transaction_count': 74, 'threshold': 50, 'total_amount': 23550352, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 73, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}