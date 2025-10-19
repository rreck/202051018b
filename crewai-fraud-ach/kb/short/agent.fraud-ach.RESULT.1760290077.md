```json
{
  "id": "4951ea5afd484fcf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290077,
  "host_pid": "9e6742732c60:1",
  "hash": "a9986d558b2015127a7341c9936d4495a0fad34491a10186eac65eb1468e682f",
  "cid": "QmV1a9986d558b2015127a7341c9936d4495a0fad344",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290077,
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
      "evaluated_at": 1760290077
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
  "sig": "e738f0ceb5df14510e30bf4b3e6f324a8b279349bb83a79eeef5be45395fc2c5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150128981
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 141, 'threshold': 50, 'total_amount': 26967660, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 140, 'first_seen': 1760285763, 'matching_hash': '59c56ba6c2207f9a'}}}aly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5956409}}}