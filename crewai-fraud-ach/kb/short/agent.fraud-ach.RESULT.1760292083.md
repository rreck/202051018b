```json
{
  "id": "fb04d0f691fd9275",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292083,
  "host_pid": "9e6742732c60:1",
  "hash": "2d3fe33439e914897412df3cc5dae2011e1b725e7115d89a168ed06db055e3cd",
  "cid": "QmV12d3fe33439e914897412df3cc5dae2011e1b725e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292083,
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
      "evaluated_at": 1760292083
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
  "sig": "b7f0947a66fe54759e2a582cdd194feae030064191f851d090a4e4431782ab2d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037990803
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 190, 'threshold': 50, 'total_amount': 44222500, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 189, 'first_seen': 1760285763, 'matching_hash': 'be616144f18eac0b'}}}