```json
{
  "id": "334fd4582abea727",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288461,
  "host_pid": "9e6742732c60:1",
  "hash": "353b31702baa657b39e2875a1ebb2d8e8886ee444e3468a3200a41da3b3a1be7",
  "cid": "QmV1353b31702baa657b39e2875a1ebb2d8e8886ee44",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288461,
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
      "evaluated_at": 1760288461
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
  "sig": "1f4331d20e490077a44a317b1da2aa7eed1c85a6ed6b19ce62827f152488278f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029068175
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 94, 'threshold': 50, 'total_amount': 32812674, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 93, 'first_seen': 1760285763, 'matching_hash': 'd04fb7e5778b56f7'}}}