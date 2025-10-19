```json
{
  "id": "b1a6bd5f1018fdd0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290431,
  "host_pid": "9e6742732c60:1",
  "hash": "e5be8ce0f33ccaf88624bdd6ef725b23c7d542a9bde75d0ba45a6ac0c79359f5",
  "cid": "QmV1e5be8ce0f33ccaf88624bdd6ef725b23c7d542a9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290431,
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
      "evaluated_at": 1760290431
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
  "sig": "afdb72bc27082f7ffe321add19f1f2b53fde6c4bc9596b8ff7a66a032a0a32d4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244291071
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 150, 'threshold': 50, 'total_amount': 18987150, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 149, 'first_seen': 1760285763, 'matching_hash': '1f8fb3dc368ee7c3'}}}