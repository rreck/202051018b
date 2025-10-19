```json
{
  "id": "64eb17e29e0c8e60",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292243,
  "host_pid": "9e6742732c60:1",
  "hash": "4aecca20fdbc47a5f4bac8bdf7b106f4db116de281ac588f31e2c3d7bc98bbc4",
  "cid": "QmV14aecca20fdbc47a5f4bac8bdf7b106f4db116de2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292243,
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
      "evaluated_at": 1760292243
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
  "sig": "0a983e6fc3885c0919e9eadd37f5ac0ad27a239033fbc07f98d556d76bb29f55"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593870321
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 15879075, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285763, 'matching_hash': 'ac61827ecd1197f0'}}}