```json
{
  "id": "595cf6001342414e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289768,
  "host_pid": "9e6742732c60:1",
  "hash": "303c0dd506b158b7cf60efb9d5207cab796273d0e6b000d1c0a81ee9e39c140c",
  "cid": "QmV1303c0dd506b158b7cf60efb9d5207cab796273d0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289768,
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
      "evaluated_at": 1760289768
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
  "sig": "80db03b3e826e27aee409a476c54e31fa934820847f7bcd82cad874fcf17aecc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025198728
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 132, 'threshold': 50, 'total_amount': 12386616, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 131, 'first_seen': 1760285765, 'matching_hash': 'ff4b51392b1a88ca'}}}