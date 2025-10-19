```json
{
  "id": "c0931dc8f9a4cd7d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290829,
  "host_pid": "9e6742732c60:1",
  "hash": "ed7c24434a6dfcca2fe86e7f2c090245229b9ba2f7ec69d6d5c80eaa8c004d0f",
  "cid": "QmV1ed7c24434a6dfcca2fe86e7f2c090245229b9ba2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290829,
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
      "evaluated_at": 1760290829
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
  "sig": "87610bf8476b5db346e8b0ab85c89251ee7e9a0cce6bb2096985138d865e7a18"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026132147
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 160, 'threshold': 50, 'total_amount': 29022880, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 159, 'first_seen': 1760285765, 'matching_hash': 'fe0c58008e192989'}}}