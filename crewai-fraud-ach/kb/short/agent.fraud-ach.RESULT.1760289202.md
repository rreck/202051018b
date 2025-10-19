```json
{
  "id": "f6f19a91e9149ca1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289202,
  "host_pid": "9e6742732c60:1",
  "hash": "78cd671e47ba7866ec2acf95fcc070a281e3a61dea21757e590263396707e5c4",
  "cid": "QmV178cd671e47ba7866ec2acf95fcc070a281e3a61d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289202,
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
      "evaluated_at": 1760289202
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
  "sig": "f42dc08096a05abe0191adb760cc82a34059ca63bce6236248a8612a6df7e880"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467007138
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 116, 'threshold': 50, 'total_amount': 48684504, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 115, 'first_seen': 1760285765, 'matching_hash': '0c635cab5f5b8acd'}}}