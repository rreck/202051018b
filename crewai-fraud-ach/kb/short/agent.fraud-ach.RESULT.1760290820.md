```json
{
  "id": "d81e43ce91de285d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290820,
  "host_pid": "9e6742732c60:1",
  "hash": "3b646d6430d749219d185f5dac6ec724fe295be1979ecf9497e6b070f91af12d",
  "cid": "QmV13b646d6430d749219d185f5dac6ec724fe295be1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290820,
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
      "evaluated_at": 1760290820
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
  "sig": "6a02453afb9deedd8a91618bf79627f3f19d6eb4d4d8b2799a6710cf4ffcb2eb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596556765
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 160, 'threshold': 50, 'total_amount': 29383040, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 159, 'first_seen': 1760285763, 'matching_hash': '746e82f5d57aeb25'}}}