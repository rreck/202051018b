```json
{
  "id": "123bc8df84a69c6a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291356,
  "host_pid": "9e6742732c60:1",
  "hash": "e8d504a07765cdd42ffe46bb3fc1dd3efb8763b98887a8eb73d3dd399bc007b4",
  "cid": "QmV1e8d504a07765cdd42ffe46bb3fc1dd3efb8763b9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291356,
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
      "evaluated_at": 1760291356
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
  "sig": "6cd38f0eca5e4de79123b7493c8b374b532ba2746f20e208c5e3db89cb1b9709"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026531578
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 173, 'threshold': 50, 'total_amount': 79410114, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 172, 'first_seen': 1760285763, 'matching_hash': 'f6751e9d8f5fd136'}}}