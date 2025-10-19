```json
{
  "id": "77971bdc0645461e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289795,
  "host_pid": "9e6742732c60:1",
  "hash": "83bd4e0b31d5939b276e442f2ab3f763ef950e9b9b312f912edd54e11d79e0fc",
  "cid": "QmV183bd4e0b31d5939b276e442f2ab3f763ef950e9b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289795,
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
      "evaluated_at": 1760289795
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
  "sig": "4b72827a5ffc1f9703ad442036af50cb892bf0d6cb9ae6041fbd274ff6b444f5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595235556
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 133, 'threshold': 50, 'total_amount': 23217278, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 132, 'first_seen': 1760285765, 'matching_hash': 'e45b9dbcffb11ba0'}}}