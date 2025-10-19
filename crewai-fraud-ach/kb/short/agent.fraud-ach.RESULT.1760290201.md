```json
{
  "id": "511d3518346cf210",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290201,
  "host_pid": "9e6742732c60:1",
  "hash": "9a18a36978ca37d39603743577840422ab31b52f61f90d7230d4958052fd0c7a",
  "cid": "QmV19a18a36978ca37d39603743577840422ab31b52f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290201,
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
      "evaluated_at": 1760290201
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
  "sig": "2b976849ca904f270ba4b7eb9328346bdd4c1425d2947f2fe277c6a6a900e06c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028850671
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 144, 'threshold': 50, 'total_amount': 13688352, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 143, 'first_seen': 1760285763, 'matching_hash': '07a264c4d7b66912'}}}