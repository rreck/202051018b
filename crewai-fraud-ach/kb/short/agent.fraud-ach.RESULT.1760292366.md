```json
{
  "id": "19105c4cf684649b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292366,
  "host_pid": "9e6742732c60:1",
  "hash": "4af883c096606a5533c657b2338257a68f5434c3ac2f4cf5291d646e4fd811a8",
  "cid": "QmV14af883c096606a5533c657b2338257a68f5434c3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292366,
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
      "evaluated_at": 1760292366
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
  "sig": "11309fef5ce39047fcde969e23d78434f91558267c7eecb31d8930d12b096a92"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272276410
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 34966792, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285764, 'matching_hash': '97f823784b1b19f6'}}}