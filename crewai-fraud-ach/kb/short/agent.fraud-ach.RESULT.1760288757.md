```json
{
  "id": "4541d2fe720ec081",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288757,
  "host_pid": "9e6742732c60:1",
  "hash": "c9600e6d240ee8e64268bff41ca7016070cd260e51fce58f2083805990d1ba96",
  "cid": "QmV1c9600e6d240ee8e64268bff41ca7016070cd260e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288757,
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
      "evaluated_at": 1760288757
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
  "sig": "994a6fe22cc7dfcd26d294505e8c808bc98994b25c9ad5116553e10c24aae564"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154261308
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 103, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 102, 'first_seen': 1760285763, 'matching_hash': 'f5aec8f7458ab0e7'}}}