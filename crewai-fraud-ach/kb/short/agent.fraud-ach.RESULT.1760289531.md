```json
{
  "id": "5a67c11054fc0fa7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289531,
  "host_pid": "9e6742732c60:1",
  "hash": "36523b454ad5db7fc53152e284da3045c14cac216901e139a2f89caf4e45ed5d",
  "cid": "QmV136523b454ad5db7fc53152e284da3045c14cac21",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289531,
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
      "evaluated_at": 1760289531
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
  "sig": "c350b8baeb5f50669783a651c73749bba23800f5443ce95df52f0738ff0abf0a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469479183
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 126, 'threshold': 50, 'total_amount': 16832340, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 125, 'first_seen': 1760285763, 'matching_hash': '2b83b0aed5f7590d'}}}