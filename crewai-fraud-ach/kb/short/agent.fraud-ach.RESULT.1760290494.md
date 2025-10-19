```json
{
  "id": "9cf93dabca3f1f8b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290494,
  "host_pid": "9e6742732c60:1",
  "hash": "8ee9591d5e23b820b12ed3ab7ab83c7494b464b65175e682936e71bec1627cff",
  "cid": "QmV18ee9591d5e23b820b12ed3ab7ab83c7494b464b6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290494,
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
      "evaluated_at": 1760290494
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
  "sig": "eef7401474337c8cf95c5ca0f080203b03248208c8e4ed474565dd552a44f297"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599280040
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 152, 'threshold': 50, 'total_amount': 73991472, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 151, 'first_seen': 1760285763, 'matching_hash': '3242f38050bfb93d'}}}