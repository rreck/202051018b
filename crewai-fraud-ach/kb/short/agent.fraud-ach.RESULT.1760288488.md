```json
{
  "id": "22094df65bc41799",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288488,
  "host_pid": "9e6742732c60:1",
  "hash": "1d20f5060c5122a9f7325dd42d552135130d5afab2811899f0cb91b67edebbc7",
  "cid": "QmV11d20f5060c5122a9f7325dd42d552135130d5afa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288488,
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
      "evaluated_at": 1760288488
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
  "sig": "150db584f3247ce66361a9d877ed03c27c3aa67743fe2963730e2f3dcd82a103"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150128981
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 95, 'threshold': 50, 'total_amount': 18169700, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 94, 'first_seen': 1760285763, 'matching_hash': '59c56ba6c2207f9a'}}}