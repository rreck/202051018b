```json
{
  "id": "c38db1538c4fa855",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288119,
  "host_pid": "9e6742732c60:1",
  "hash": "08c4c702ed0267a33bdef5be701344938b2babbc6c05b945a23ed347e9bf9740",
  "cid": "QmV108c4c702ed0267a33bdef5be701344938b2babbc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288119,
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
      "evaluated_at": 1760288119
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
  "sig": "ebd20b46e099dc342f272d8f1e16e8960a40e0a2fcfe2344c1771b48c9a3d8a0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037423947
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 83, 'threshold': 50, 'total_amount': 16575183, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 82, 'first_seen': 1760285763, 'matching_hash': '5528b0ca47a44e30'}}}