```json
{
  "id": "29d0e222167062d6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293889,
  "host_pid": "9e6742732c60:1",
  "hash": "7dfebe6511c40fc1e538706936ed149da5d9fc2faeca0564d695ba96e2cc7c4b",
  "cid": "QmV17dfebe6511c40fc1e538706936ed149da5d9fc2f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293889,
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
      "evaluated_at": 1760293889
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
  "sig": "f584c8119038d9d6b9d543202ed2f077dfb145cf22eb10cedd1c9dc85fec8930"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022307864
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 106869557, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285765, 'matching_hash': '183a325d3d521c29'}}}