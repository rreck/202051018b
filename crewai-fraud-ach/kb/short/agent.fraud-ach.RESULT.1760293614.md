```json
{
  "id": "14e072fd22b52d88",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293614,
  "host_pid": "9e6742732c60:1",
  "hash": "a593b59737c56ae5e3e8c0f0ef394c67109e40bc39c059615e361890cfa0294c",
  "cid": "QmV1a593b59737c56ae5e3e8c0f0ef394c67109e40bc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293614,
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
      "evaluated_at": 1760293614
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
  "sig": "30108c401e6f6e6d7b75e49c3e91199cc55caab65be903df922a7ee3ab646f5e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274960966
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 25920720, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285763, 'matching_hash': 'f5e3b3cd48fefc81'}}}