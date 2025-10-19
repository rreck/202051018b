```json
{
  "id": "193bdd93b15f5b6b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294864,
  "host_pid": "9e6742732c60:1",
  "hash": "4fab6688a8183f97326c067dc94e6968f5fa73754d2770daa7bf59ee5172614a",
  "cid": "QmV14fab6688a8183f97326c067dc94e6968f5fa7375",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294864,
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
      "evaluated_at": 1760294864
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
  "sig": "de0f4d354dc42a5d0896ed90037f2ce332266c493ecb34d6c2fe8917d57fe71d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022956374
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 40944978, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285763, 'matching_hash': '4e30c52d3b71935d'}}}