```json
{
  "id": "10399a4b532d461e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286609,
  "host_pid": "9e6742732c60:1",
  "hash": "1596e88b64e6b4fe490370403ca085a9c0176083ca627ead77705096913f6904",
  "cid": "QmV11596e88b64e6b4fe490370403ca085a9c0176083",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286609,
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
      "evaluated_at": 1760286609
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "529bf917e88fa9905919849c4ed0c35f38dd44b92f6f344e67351e2cab7834bf"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000029068175
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10821201, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 30, 'first_seen': 1760285763, 'matching_hash': 'd04fb7e5778b56f7'}}}g number checksum'}}}