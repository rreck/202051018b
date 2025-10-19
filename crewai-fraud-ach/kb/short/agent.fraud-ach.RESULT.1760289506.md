```json
{
  "id": "5782657f993ccc8b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289506,
  "host_pid": "9e6742732c60:1",
  "hash": "21ef15a848a42440a1e0900e4d7ed6b8b3b6f8f61fd54263795753800bd7e968",
  "cid": "QmV121ef15a848a42440a1e0900e4d7ed6b8b3b6f8f6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289506,
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
      "evaluated_at": 1760289506
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
  "sig": "c9903acd81a5d82efe5ca2d24b2381fe75d869fdd87b787115a9fdf3a0ce6c57"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244291071
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 125, 'threshold': 50, 'total_amount': 15822625, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 124, 'first_seen': 1760285763, 'matching_hash': '1f8fb3dc368ee7c3'}}}