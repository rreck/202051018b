```json
{
  "id": "6bf85cc4e27bee7d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290047,
  "host_pid": "9e6742732c60:1",
  "hash": "e06efaa77d5409bd13feaccb7c1b9a3e741c6c52c1c5daa9101a90965fe57919",
  "cid": "QmV1e06efaa77d5409bd13feaccb7c1b9a3e741c6c52",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290047,
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
      "evaluated_at": 1760290047
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
  "sig": "4b13a4924aa8ec580185fd67a565368b4c00635392ad1bae89250fa7e7a71816"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468629827
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 140, 'threshold': 50, 'total_amount': 12376280, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 139, 'first_seen': 1760285763, 'matching_hash': 'f998250ed7d87b2f'}}}