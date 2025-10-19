```json
{
  "id": "8957d06ff884436c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292099,
  "host_pid": "9e6742732c60:1",
  "hash": "88540ec120d0d2fc2b7a97076ba737006bfe1eda331efbebf24015156e745508",
  "cid": "QmV188540ec120d0d2fc2b7a97076ba737006bfe1eda",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292099,
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
      "evaluated_at": 1760292099
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
  "sig": "c5d0b22e152965a76c581059695649a5a32d1903e39600c131d33dbd3e9e1f22"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270776467
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 190, 'threshold': 50, 'total_amount': 92889480, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 189, 'first_seen': 1760285763, 'matching_hash': 'a0c66d95a4fd4e21'}}}