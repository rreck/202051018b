```json
{
  "id": "6fd7bafcbf32d751",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291189,
  "host_pid": "9e6742732c60:1",
  "hash": "3548fffba149ed2d9b2fc2f43ad64669e54924d2fd4fa1f2ebb0f0fdb3e63a10",
  "cid": "QmV13548fffba149ed2d9b2fc2f43ad64669e54924d2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291189,
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
      "evaluated_at": 1760291189
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
  "sig": "8b05bde1b2514b8fc59b438326af6a5083ef2265d9936eae660109d6078d2bbc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155063461
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 169, 'threshold': 50, 'total_amount': 53243112, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 168, 'first_seen': 1760285764, 'matching_hash': '55217e698cd3f78f'}}}