```json
{
  "id": "7332b9ead48f634d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287879,
  "host_pid": "9e6742732c60:1",
  "hash": "6610feeb4c4be81b9b6adbfcd8f49fb2f0c6294daac29c8cd0a048c65c914a40",
  "cid": "QmV16610feeb4c4be81b9b6adbfcd8f49fb2f0c6294d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287879,
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
      "evaluated_at": 1760287879
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
  "sig": "e7cca69bf9fde2dc59692e96142426c947db495af8cd9a680675dc2a64c63f03"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247499118
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 75, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 74, 'first_seen': 1760285765, 'matching_hash': 'f65a723d753f6ade'}}}