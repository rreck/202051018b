```json
{
  "id": "37bc9df7eb841b8b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288503,
  "host_pid": "9e6742732c60:1",
  "hash": "4ebe0c57d367c7f306985a805e053d3493efd5dad764e73a1e1cc4f64f876a79",
  "cid": "QmV14ebe0c57d367c7f306985a805e053d3493efd5da",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288503,
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
      "evaluated_at": 1760288503
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
  "sig": "7b19c7dd460d610c1c4981fa26825a09dd55ced244084ae8c7312ca9c708007d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464170386
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 95, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 94, 'first_seen': 1760285764, 'matching_hash': 'cc3f2cd033134006'}}}