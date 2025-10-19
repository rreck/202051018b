```json
{
  "id": "33374c8c1bcb96f4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287705,
  "host_pid": "9e6742732c60:1",
  "hash": "40187e27fa9138a35f47965f0646919720ce31b9096a135f7f73fd488268bd92",
  "cid": "QmV140187e27fa9138a35f47965f0646919720ce31b9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287705,
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
      "evaluated_at": 1760287705
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
  "sig": "036f442d5a877568d535918d7a4449f315ca80c8e8e0d761abf2f74edbbd7734"
}
```

Fraud detected: duplicate_transaction (score: 86)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 88, 'details': {'transaction_count': 69, 'threshold': 50, 'total_amount': 21959112, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 68, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}