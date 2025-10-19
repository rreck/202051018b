```json
{
  "id": "99cb0b864bb1387b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291206,
  "host_pid": "9e6742732c60:1",
  "hash": "f70645f7260856a84c0c6af578b1aa04682321d5574f9c9c968a6d57063713af",
  "cid": "QmV1f70645f7260856a84c0c6af578b1aa04682321d5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291206,
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
      "evaluated_at": 1760291206
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
  "sig": "81e92d5b2af018f2e0f855aa2a3c42787cb98be9d1a3975634de7c35c7535ed6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463448865
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 169, 'threshold': 50, 'total_amount': 29043157, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 168, 'first_seen': 1760285765, 'matching_hash': '5a565595f8571aef'}}}