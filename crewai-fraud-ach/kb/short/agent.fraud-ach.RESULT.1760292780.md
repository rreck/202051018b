```json
{
  "id": "5769b30a80efca26",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292780,
  "host_pid": "9e6742732c60:1",
  "hash": "a83d8724ca72eafc9b470cc6a809972979684ed1c475489e74358e36568d407d",
  "cid": "QmV1a83d8724ca72eafc9b470cc6a809972979684ed1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292780,
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
      "evaluated_at": 1760292780
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
  "sig": "9d21d0efe9f9cfabffdc7b6dacc8c7f5089e1d40880d8ceaae14aa3b1c15b3c9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157097598
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 65579500, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285763, 'matching_hash': '62fa124f01b3075a'}}}