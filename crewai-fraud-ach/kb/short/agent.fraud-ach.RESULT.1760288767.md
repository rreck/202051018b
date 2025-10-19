```json
{
  "id": "68a0aacbdcebab12",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288767,
  "host_pid": "9e6742732c60:1",
  "hash": "3657a134e9a49a6d3fd6376f7731c4288e78d731f0e96a160ac6a8f454b79417",
  "cid": "QmV13657a134e9a49a6d3fd6376f7731c4288e78d731",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288767,
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
      "evaluated_at": 1760288767
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
  "sig": "e416209df1b4496462140384847dfd5fe1d3f35ce66d78310880c45e7a9685bc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249867755
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 103, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 102, 'first_seen': 1760285765, 'matching_hash': '3e6b26eb59ce898a'}}}