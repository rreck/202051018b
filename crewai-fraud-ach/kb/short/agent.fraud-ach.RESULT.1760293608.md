```json
{
  "id": "7bd447745ebac16b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293608,
  "host_pid": "9e6742732c60:1",
  "hash": "712714b682c3f14b562aa73798bdc32f88bfa706043d955f46cfee36f3507fa4",
  "cid": "QmV1712714b682c3f14b562aa73798bdc32f88bfa706",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293608,
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
      "evaluated_at": 1760293608
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
  "sig": "3da1fc0ca67fe83cdca1bf4a142bad9a9e0ec761bb12fe1bd6191ab03d3055d4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022300374
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 30909504, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285763, 'matching_hash': '0c9c3ceb4a82225f'}}}