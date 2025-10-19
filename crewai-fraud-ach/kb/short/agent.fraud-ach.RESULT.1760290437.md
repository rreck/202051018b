```json
{
  "id": "6f6ea2a58546959e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290437,
  "host_pid": "9e6742732c60:1",
  "hash": "1d355f31eb16d6da64cf9e2382b62bc571f717f2624dd27b6fe59132f02d23a6",
  "cid": "QmV11d355f31eb16d6da64cf9e2382b62bc571f717f2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290437,
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
      "evaluated_at": 1760290437
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
  "sig": "0d7c6b82425fedb8cc5a9968c5f198b1dc6a816a112d908c1cc99eda13c5b8d2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242987850
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 150, 'threshold': 50, 'total_amount': 17554350, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 149, 'first_seen': 1760285764, 'matching_hash': 'ac2312cc15fe4af9'}}}