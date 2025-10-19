```json
{
  "id": "0fb322d5f5789cfd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292908,
  "host_pid": "9e6742732c60:1",
  "hash": "1f246d4534e63dc3b5f0f69ac53db03d6ffb52fc14472fd41c5e2bebbdd70deb",
  "cid": "QmV11f246d4534e63dc3b5f0f69ac53db03d6ffb52fc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292908,
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
      "evaluated_at": 1760292908
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
  "sig": "6e602babfc869b1b8eb099f5bc704b77163ec01aa284897d53e17b98c4f09b3e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 65877336, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}