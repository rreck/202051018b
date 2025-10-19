```json
{
  "id": "40fa835f4dc46d05",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288994,
  "host_pid": "9e6742732c60:1",
  "hash": "38e6e60ec8c9bb2d1981425d2c540d4ce51697a7796e5d5c19e2c466324e78b1",
  "cid": "QmV138e6e60ec8c9bb2d1981425d2c540d4ce51697a7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288994,
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
      "evaluated_at": 1760288994
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
  "sig": "fc3de9452c353875a53ed85829016987ea0af66945fb36982f42bddeec2cef69"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031029200
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 110, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 109, 'first_seen': 1760285763, 'matching_hash': '80e7fe619ff961e0'}}}