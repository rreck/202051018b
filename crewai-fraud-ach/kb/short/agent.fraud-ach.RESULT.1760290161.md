```json
{
  "id": "e8e02f78f330ac73",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290161,
  "host_pid": "9e6742732c60:1",
  "hash": "6b51184e2b572b997e80e37d29d3b48f65f942e29ae76200d3a6eec2b254ffc9",
  "cid": "QmV16b51184e2b572b997e80e37d29d3b48f65f942e2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290161,
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
      "evaluated_at": 1760290161
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
  "sig": "7e4aec925036600388868ed34d6f4d14ff30a66519d0aaf34142c9aa9a9b3ebb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248452995
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 143, 'threshold': 50, 'total_amount': 27546805, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 142, 'first_seen': 1760285763, 'matching_hash': '319e0dd4a1544393'}}}