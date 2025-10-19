```json
{
  "id": "a5e8784eac52866f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291566,
  "host_pid": "9e6742732c60:1",
  "hash": "2f12047e023ed7c937d4ee6bc4f299919275c6cd0e3b0ca02eec82ef8e847e39",
  "cid": "QmV12f12047e023ed7c937d4ee6bc4f299919275c6cd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291566,
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
      "evaluated_at": 1760291566
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
  "sig": "46e4737cd20b0cc1fb00f4d3f3f8d00614224a52bd5c6f0582604517655058a9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025853793
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 48400336, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285763, 'matching_hash': 'ff3a3f7dec7a702a'}}}