```json
{
  "id": "4540f3cef39944c6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289509,
  "host_pid": "9e6742732c60:1",
  "hash": "9c716e53c2ec9cc83a36bb8cb66e4739e7a752f0efcb5531ab75c133ec600ef5",
  "cid": "QmV19c716e53c2ec9cc83a36bb8cb66e4739e7a752f0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289509,
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
      "evaluated_at": 1760289509
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
  "sig": "0a8d52e7056db7d9eee2abb0ac51ed90d02d55aa4df246d7d4b9e5d64255ee99"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597735648
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 125, 'threshold': 50, 'total_amount': 31481625, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 124, 'first_seen': 1760285763, 'matching_hash': '529f1dc61ac58982'}}}