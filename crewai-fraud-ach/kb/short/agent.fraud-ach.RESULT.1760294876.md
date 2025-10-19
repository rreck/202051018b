```json
{
  "id": "bb2a3e4cf618bc22",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294876,
  "host_pid": "9e6742732c60:1",
  "hash": "c47f9f5c471e4eafc3511b177ae6480ef504e28b86c39030d7f15e049a5bd708",
  "cid": "QmV1c47f9f5c471e4eafc3511b177ae6480ef504e28b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294876,
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
      "evaluated_at": 1760294876
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
  "sig": "d3b2af2b0140209afa8113efe671e5f2c44cc56f0f452361eca1ef997d3fcc20"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155324238
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 115855422, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285764, 'matching_hash': '6027d2fe89c09f43'}}}