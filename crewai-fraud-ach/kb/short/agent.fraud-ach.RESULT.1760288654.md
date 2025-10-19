```json
{
  "id": "9622f86236da22f6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288654,
  "host_pid": "9e6742732c60:1",
  "hash": "2751c12b2bf20af01edf58d8eb5cafa73506237ce891cdba67cc93ae3f13e0a0",
  "cid": "QmV12751c12b2bf20af01edf58d8eb5cafa73506237c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288654,
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
      "evaluated_at": 1760288654
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
  "sig": "b4870e712743e7f7817d8702e0fdfa0759fb3e8e4731d8334fd450cf76d5753a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278849424
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 100, 'threshold': 50, 'total_amount': 28647900, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 99, 'first_seen': 1760285763, 'matching_hash': '586e1ac2088494e1'}}}