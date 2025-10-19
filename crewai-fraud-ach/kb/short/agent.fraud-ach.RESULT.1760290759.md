```json
{
  "id": "becca91923911d0b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290759,
  "host_pid": "9e6742732c60:1",
  "hash": "8a0a251a76537ca7b324fbf2600489ea1412148789ff1d5838c9fe94f49ce031",
  "cid": "QmV18a0a251a76537ca7b324fbf2600489ea14121487",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290759,
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
      "evaluated_at": 1760290759
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
  "sig": "1e0551ef69899420f39d5a9d8182988115a6b6d72a101d6e8cea53605812b36d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 158, 'threshold': 50, 'total_amount': 50283184, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 157, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}