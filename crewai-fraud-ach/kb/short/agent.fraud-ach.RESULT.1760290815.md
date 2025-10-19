```json
{
  "id": "00500dfca999a2a8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290815,
  "host_pid": "9e6742732c60:1",
  "hash": "17f02f5fbf130248a4692b43c718816d36c0a7bd863318a11080dceaf88cb38c",
  "cid": "QmV117f02f5fbf130248a4692b43c718816d36c0a7bd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290815,
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
      "evaluated_at": 1760290815
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
  "sig": "8ffada33af670c5346128257bfdfe4f1276920c2d67471b5277e9f88ab01fe06"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033621272
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 160, 'threshold': 50, 'total_amount': 23862720, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 159, 'first_seen': 1760285763, 'matching_hash': 'd5b1a20ced8a5769'}}}