```json
{
  "id": "c8bf585eabf7a3e9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290890,
  "host_pid": "9e6742732c60:1",
  "hash": "e4482f1aee666bec716bd7370cafa36e6ae0d4fd69fb6d26cfa8e1d7eb67381b",
  "cid": "QmV1e4482f1aee666bec716bd7370cafa36e6ae0d4fd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290890,
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
      "evaluated_at": 1760290890
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
  "sig": "9d3538378915931012f0b451b6a26081793a6459c786dc97224e59cb1fd40442"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024544859
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 162, 'threshold': 50, 'total_amount': 78523668, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 161, 'first_seen': 1760285763, 'matching_hash': '21e0fdbcd06f2d49'}}}