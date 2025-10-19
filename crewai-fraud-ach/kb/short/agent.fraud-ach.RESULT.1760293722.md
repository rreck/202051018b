```json
{
  "id": "a194cf3ff09dc86f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293722,
  "host_pid": "9e6742732c60:1",
  "hash": "b20363915e1e9eb3c64ae0d0a3eef56f8a3464292e353071c6ddcfa1a3d1aae9",
  "cid": "QmV1b20363915e1e9eb3c64ae0d0a3eef56f8a346429",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293722,
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
      "evaluated_at": 1760293722
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
  "sig": "e47886a0a277e6410aa4b7b972065812cacded0c1ca5bd0f9a46122e4cea61f2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029769834
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 86140320, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285764, 'matching_hash': '4022d05a51a758f8'}}}