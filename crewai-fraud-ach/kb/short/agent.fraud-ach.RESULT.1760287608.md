```json
{
  "id": "fd7546efe60bd19a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287608,
  "host_pid": "9e6742732c60:1",
  "hash": "819324e8be7e6650069aa592226591b02400dff5b610b8ad47918a4271784a76",
  "cid": "QmV1819324e8be7e6650069aa592226591b02400dff5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287608,
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
      "evaluated_at": 1760287608
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
  "sig": "0ae4ac2054f4613a00b30d8d729c0afe734a4a04a70e0a6659419d282f5ccc85"
}
```

Fraud detected: duplicate_transaction (score: 83)
Transaction: 122105157447901
Details: {'velocity': {'fraud_detected': True, 'risk_score': 82, 'details': {'transaction_count': 66, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 65, 'first_seen': 1760285765, 'matching_hash': '08b33f5611b85fcf'}}}