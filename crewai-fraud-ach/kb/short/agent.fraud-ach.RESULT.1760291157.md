```json
{
  "id": "0aabef3b6dadac7e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291157,
  "host_pid": "9e6742732c60:1",
  "hash": "b5422b973d9b83afd3a9520b010c603a5983352ba8d3deb86cbe64a22c40daad",
  "cid": "QmV1b5422b973d9b83afd3a9520b010c603a5983352b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291157,
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
      "evaluated_at": 1760291157
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
  "sig": "820bc0bcefd1fd47896c4c93d9c3abd74d949b805e1deca566573a8ac874d083"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022841229
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 168, 'threshold': 50, 'total_amount': 29931720, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 167, 'first_seen': 1760285763, 'matching_hash': '5d206cfe266207b6'}}}