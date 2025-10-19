```json
{
  "id": "4f30a89a2dcff4e4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291973,
  "host_pid": "9e6742732c60:1",
  "hash": "b9a1a3af950affd31ad0720fab0b82320ad695b65e6271531b2cd2a3105ee6bc",
  "cid": "QmV1b9a1a3af950affd31ad0720fab0b82320ad695b6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291973,
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
      "evaluated_at": 1760291973
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
  "sig": "eb5776cfa2630e1aa401a39c0fc9a47d969aee119232eff1f30f414f45679654"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000020703113
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 53770541, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285763, 'matching_hash': '6c2ac9b0cec56c2f'}}}