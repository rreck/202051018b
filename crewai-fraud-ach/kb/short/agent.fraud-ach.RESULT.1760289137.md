```json
{
  "id": "b5269b938dc21db5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289137,
  "host_pid": "9e6742732c60:1",
  "hash": "c8c147fba3622ed0694ddcdbd6c1f0cdc3e2fcdffdefe3ac0818c5c2b5437b1d",
  "cid": "QmV1c8c147fba3622ed0694ddcdbd6c1f0cdc3e2fcdf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289137,
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
      "evaluated_at": 1760289137
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
  "sig": "af0ed05d1502d5d7a3fe9a32ea0cdce2164cdb723237bc958df0aa2bca9e21f9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462765128
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 114, 'threshold': 50, 'total_amount': 34381602, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 113, 'first_seen': 1760285765, 'matching_hash': 'e332841741f2145e'}}}