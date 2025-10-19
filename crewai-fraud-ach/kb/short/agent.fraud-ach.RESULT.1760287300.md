```json
{
  "id": "60de936b61eed3da",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287300,
  "host_pid": "9e6742732c60:1",
  "hash": "20338e0ba7e49bb97bb8fe7b3ae7640ac5cf32d9eeec62de3aed0b96f26c22ba",
  "cid": "QmV120338e0ba7e49bb97bb8fe7b3ae7640ac5cf32d9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287300,
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
      "evaluated_at": 1760287300
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "a5fd5516001843b0f999352ca8c2bec87a702557f574e74a93a9a8a921ccfb78"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201467874144
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 55, 'threshold': 50, 'total_amount': 13705065, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 54, 'first_seen': 1760285764, 'matching_hash': '428cbf79813503ca'}}}