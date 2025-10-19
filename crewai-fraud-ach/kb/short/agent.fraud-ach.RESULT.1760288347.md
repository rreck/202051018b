```json
{
  "id": "9d0e751081884d11",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288347,
  "host_pid": "9e6742732c60:1",
  "hash": "bdd1bdf412d714096450a3b6c24121931bfa4d32878166f997c00537be05971a",
  "cid": "QmV1bdd1bdf412d714096450a3b6c24121931bfa4d32",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288347,
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
      "evaluated_at": 1760288347
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
  "sig": "4083a25e3a85c850a0bbe8aa842c41eb2e8b82fb857658fb0f07905ac72ea35b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029386599
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 90, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 89, 'first_seen': 1760285765, 'matching_hash': 'b64c8fcbcd38380f'}}}