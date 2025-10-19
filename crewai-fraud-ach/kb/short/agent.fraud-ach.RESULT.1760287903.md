```json
{
  "id": "fb62f0e90912679d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287903,
  "host_pid": "9e6742732c60:1",
  "hash": "246111bd6f6532673718839e68b12bec52ad4fd39acfd8de7eb0a8d1f5be9d8c",
  "cid": "QmV1246111bd6f6532673718839e68b12bec52ad4fd3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287903,
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
      "evaluated_at": 1760287903
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
  "sig": "2b71533b86409515449b97ab6696ed967315bc056fe4594bfcd3b5148eaec0f3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155364313
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 76, 'threshold': 50, 'total_amount': 29359940, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 75, 'first_seen': 1760285763, 'matching_hash': 'ab592f5d42fe5ec0'}}}