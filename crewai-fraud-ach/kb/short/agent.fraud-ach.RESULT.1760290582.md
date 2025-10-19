```json
{
  "id": "2d8ef786dd90350b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290582,
  "host_pid": "9e6742732c60:1",
  "hash": "9cb679caf1efd4bb90084bdee4c6b64cc391ec35946acbe0a0acf9103d46f792",
  "cid": "QmV19cb679caf1efd4bb90084bdee4c6b64cc391ec35",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290582,
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
      "evaluated_at": 1760290582
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
  "sig": "d8cd8b908f35c2265c27734b60041bd14a90aba94654d231b90d970f61bd154e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460526260
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 154, 'threshold': 50, 'total_amount': 55031900, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 153, 'first_seen': 1760285763, 'matching_hash': '4d7dea8b6c0fe79e'}}}