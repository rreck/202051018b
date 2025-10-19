```json
{
  "id": "5d664528914bec8e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291023,
  "host_pid": "9e6742732c60:1",
  "hash": "5230726572a6b7899bedf8945586183b45f8dc62a32a995d5b1f0aea614bef19",
  "cid": "QmV15230726572a6b7899bedf8945586183b45f8dc62",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291023,
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
      "evaluated_at": 1760291023
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
  "sig": "8f5893ac6f1cf8d75c9c08ceeabf1a292f1a4b187649dbc18d7fa6569dbbb1fd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026472141
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 165, 'threshold': 50, 'total_amount': 33991980, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 164, 'first_seen': 1760285764, 'matching_hash': 'c34da1cfbf75ff05'}}}