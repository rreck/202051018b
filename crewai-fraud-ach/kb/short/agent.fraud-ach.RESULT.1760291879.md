```json
{
  "id": "747cd03c159d3d3b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291879,
  "host_pid": "9e6742732c60:1",
  "hash": "30f757a26fc1bbca67493be7f880c1258aa5ed0e519ea23d01a20f19994b369a",
  "cid": "QmV130f757a26fc1bbca67493be7f880c1258aa5ed0e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291879,
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
      "evaluated_at": 1760291879
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
  "sig": "2c5051f543f994e232e3ae3189010b8bf43d11dcc01d96e1b61efd434243fe09"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596849873
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 185, 'threshold': 50, 'total_amount': 52802515, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 184, 'first_seen': 1760285763, 'matching_hash': 'd03c8a9dd75ef277'}}}