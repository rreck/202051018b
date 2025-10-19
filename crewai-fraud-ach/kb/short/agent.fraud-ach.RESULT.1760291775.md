```json
{
  "id": "e0ca62d552240931",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291775,
  "host_pid": "9e6742732c60:1",
  "hash": "d9f86a5db098f420850c005d53280a5ba082e67d133e8c8756398117dd90d725",
  "cid": "QmV1d9f86a5db098f420850c005d53280a5ba082e67d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291775,
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
      "evaluated_at": 1760291775
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
  "sig": "ffd2d2ccbba1792a684f01a041d5381d2596eabb33a419bd1ad886aba91a5a3d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031517905
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 183, 'threshold': 50, 'total_amount': 81535833, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 182, 'first_seen': 1760285763, 'matching_hash': 'e8f76fb2eb784ea5'}}}